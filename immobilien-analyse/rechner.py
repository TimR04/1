#!/usr/bin/env python3
"""
Underwriting-Rechner für Kapitalanlage-Wohnimmobilien (Financial Underwriter, Agent 2).

Liest objekte.json, rechnet je Objekt drei Szenarien (A konservativ, B Base, C Upside)
und drei Finanzierungsvarianten, und schreibt Markdown-Tabellen nach stdout.

Alle Annahmen stehen in PARAM bzw. im Objekt-Datensatz und sind bewusst sichtbar,
damit sie mit verifizierten Exposé-Daten überschrieben werden können.

Aufruf:  python3 rechner.py [objekte.json] [--detail]
"""
import json
import math
import sys

# ---------------------------------------------------------------------------
# Finanzierung (Angaben des Nutzers)
# ---------------------------------------------------------------------------
KREDITRAHMEN = 215_000          # €
SOLLZINS = 0.0195               # p.a.
RATE_GENANNT = 1_454            # €/Monat, wie vom Kreditnehmer genannt
EK_MAX = 20_000                 # € verfügbares Eigenkapital

ANNUITAET_GENANNT = RATE_GENANNT * 12 / KREDITRAHMEN   # 8,115 % p.a.

FINANZIERUNG = {
    # Rate wie genannt, proportional auf die tatsächlich benötigte Darlehenssumme skaliert
    "F1": {"name": "Rate wie genannt (8,1 % Annuität)", "annuitaet": ANNUITAET_GENANNT},
    # hypothetisch – nur gültig, wenn der Darlehensgeber 2 % Anfangstilgung zulässt
    "F2": {"name": "hypothetisch 2 % Tilgung", "annuitaet": SOLLZINS + 0.02},
    # ökonomische Sicht: Tilgung ist Vermögensaufbau, nicht Aufwand
    "F0": {"name": "nur Zins (ökonomisch)", "annuitaet": SOLLZINS},
}

# ---------------------------------------------------------------------------
# Kaufnebenkosten Baden-Württemberg
# ---------------------------------------------------------------------------
GREST = 0.05                    # Grunderwerbsteuer BW
NOTAR_GRUNDBUCH = 0.018         # Kaufvertrag + Auflassung + Grundschuld (Annahme)
MAKLER_STANDARD = 0.0357        # Käuferanteil inkl. MwSt., falls nicht anders angegeben

# ---------------------------------------------------------------------------
# Kostenannahmen je Szenario
# ---------------------------------------------------------------------------
PARAM = {
    "A": {  # konservativ
        "leerstand": 0.05,          # Anteil der Kaltmiete
        "etw_inst_se_qm": 0.80,     # €/m²/Monat Instandhaltung Sondereigentum
        "etw_ruecklage_qm": 1.20,   # €/m²/Monat Erhaltungsrücklage, falls nicht bekannt
        "etw_verwaltung": 32,       # €/Monat WEG-Verwaltung, falls nicht bekannt
        "etw_sev": 25,              # €/Monat Sondereigentumsverwaltung
        "haus_inst_qm_jahr": 16.0,  # €/m²/Jahr Instandhaltung ganzes Haus
        "haus_verw_we": 30,         # €/WE/Monat Mietverwaltung
        "haus_sonst": 0.02,         # sonstige nicht umlagefähige Kosten (Anteil Kaltmiete)
    },
    "B": {  # Base Case
        "leerstand": 0.03,
        "etw_inst_se_qm": 0.55,
        "etw_ruecklage_qm": 1.00,
        "etw_verwaltung": 30,
        "etw_sev": 0,
        "haus_inst_qm_jahr": 13.0,
        "haus_verw_we": 20,
        "haus_sonst": 0.015,
    },
    "C": {  # Upside (nur mit konkreter Maßnahme)
        "leerstand": 0.025,
        "etw_inst_se_qm": 0.45,
        "etw_ruecklage_qm": 1.00,
        "etw_verwaltung": 30,
        "etw_sev": 0,
        "haus_inst_qm_jahr": 12.0,
        "haus_verw_we": 20,
        "haus_sonst": 0.015,
    },
}


def monatsrate(darlehen, annuitaet):
    return darlehen * annuitaet / 12


def kaufnebenkosten(preis, makler_pct):
    return preis * (GREST + NOTAR_GRUNDBUCH + makler_pct)


def kosten_monat(o, sz, miete):
    """Nicht umlagefähige Bewirtschaftungskosten pro Monat (ohne Finanzierung)."""
    p = PARAM[sz]
    wfl = o["wfl"]
    leer = miete * p["leerstand"]
    if o["typ"] == "ETW":
        if o.get("hausgeld_nu") is not None:   # bekannter nicht umlagef. Anteil inkl. Rücklage
            hg_nu = o["hausgeld_nu"]
        else:
            hg_nu = o.get("einheiten", 1) * p["etw_verwaltung"] + wfl * p["etw_ruecklage_qm"]
        inst = wfl * p["etw_inst_se_qm"]
        verw = o.get("einheiten", 1) * p["etw_sev"]
        sonst = 0
    else:
        hg_nu = 0
        inst = wfl * p["haus_inst_qm_jahr"] / 12
        verw = o.get("einheiten", 1) * p["haus_verw_we"]
        sonst = miete * p["haus_sonst"]
    return {"hausgeld_nu": hg_nu, "instandhaltung": inst, "verwaltung": verw,
            "leerstand": leer, "sonstiges": sonst,
            "summe": hg_nu + inst + verw + leer + sonst}


def miete_szenario(o, sz):
    """Kaltmiete pro Monat je Szenario aus den Objektdaten."""
    return o["miete"][sz]


def finanzierung(o, preis=None):
    preis = o["preis"] if preis is None else preis
    makler = o.get("makler_pct", MAKLER_STANDARD)
    nk = kaufnebenkosten(preis, makler)
    reno = o.get("reno", 0)
    darlehen = min(preis, KREDITRAHMEN)
    ek = nk + reno + max(0, preis - KREDITRAHMEN)
    return {"preis": preis, "nk": nk, "reno": reno, "darlehen": darlehen, "ek": ek,
            "ek_ok": ek <= EK_MAX, "gesamtinvest": preis + nk + reno}


def kennzahlen(o, sz, preis=None):
    f = finanzierung(o, preis)
    miete = miete_szenario(o, sz)
    k = kosten_monat(o, sz, miete)
    noi = miete - k["summe"]
    out = {"sz": sz, "miete": miete, "kosten": k, "noi": noi, **f,
           "brutto": miete * 12 / f["preis"], "faktor": f["preis"] / (miete * 12),
           "netto": noi * 12 / f["gesamtinvest"]}
    for key, fin in FINANZIERUNG.items():
        rate = monatsrate(f["darlehen"], fin["annuitaet"])
        cf = noi - rate
        out[key] = {"rate": rate, "cf": cf,
                    "dscr": noi / rate if rate else float("nan"),
                    "coc": cf * 12 / f["ek"] if f["ek"] > 0 else float("nan")}
    # Break-even-Kaltmiete (CF = 0) für F1/F2 bei gegebenen Kosten
    var = PARAM[sz]["leerstand"] + (PARAM[sz]["haus_sonst"] if o["typ"] != "ETW" else 0)
    fix = k["summe"] - k["leerstand"] - k["sonstiges"]
    for key in ("F1", "F2"):
        out[key]["break_even_miete"] = (out[key]["rate"] + fix) / (1 - var)
    return out


def max_kaufpreise(o, sz="B", ziel_cf=100):
    """Maximal vertretbare Kaufpreise aus tatsächlicher Miete und Kosten."""
    miete = miete_szenario(o, sz)
    jahresmiete = miete * 12
    noi = miete - kosten_monat(o, sz, miete)["summe"]
    res = {f"brutto_{int(y*100)}": jahresmiete / y for y in (0.06, 0.07, 0.08, 0.09)}
    for key in ("F1", "F2"):
        ann = FINANZIERUNG[key]["annuitaet"] / 12
        # Darlehen = Kaufpreis (bis Kreditrahmen); CF = NOI - P*ann
        res[f"cf0_{key}"] = min(noi / ann, KREDITRAHMEN) if noi > 0 else 0
        res[f"cf{ziel_cf}_{key}"] = min((noi - ziel_cf) / ann, KREDITRAHMEN) if noi > ziel_cf else 0
    # Eigenkapital-Grenze: Nebenkosten + Reno <= EK_MAX
    makler = o.get("makler_pct", MAKLER_STANDARD)
    res["ek_grenze"] = min((EK_MAX - o.get("reno", 0)) / (GREST + NOTAR_GRUNDBUCH + makler),
                           KREDITRAHMEN)
    return res


def verhandlung(o):
    """Inseratspreis vs. vertretbare Preise; CF-Tests im konservativen Szenario A, Renditen auf Base-Miete."""
    b = max_kaufpreise(o, "B")
    a = max_kaufpreise(o, "A")
    res = {
        "inserat": o["preis"],
        "p6": b["brutto_6"], "p7": b["brutto_7"], "p8": b["brutto_8"], "p9": b["brutto_9"],
        "cf0_F2_A": a["cf0_F2"], "cf100_F2_A": a["cf100_F2"], "cf0_F1_B": b["cf0_F1"],
        "ek_grenze": b["ek_grenze"],
    }
    res["interessant_ab"] = min(res["p6"], res["cf0_F2_A"], res["ek_grenze"])
    res["sehr_attraktiv_ab"] = min(res["p7"], res["cf100_F2_A"], res["ek_grenze"])
    return res


def fmt1(x):
    return f"{x:.1f}".replace(".", ",")


def eur(x, nd=0):
    if x is None or (isinstance(x, float) and math.isnan(x)):
        return "n.a."
    if abs(x) < 0.5:
        x = 0
    s = f"{x:,.{nd}f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return s + " €"


def pct(x, nd=1):
    return f"{x*100:.{nd}f} %".replace(".", ",")


def tabelle_objekt(o):
    rows = []
    hdr = "| Kennzahl | A konservativ | B Base | C Upside |\n|---|---:|---:|---:|"
    ks = {sz: kennzahlen(o, sz) for sz in ("A", "B", "C")}
    def row(label, fn):
        rows.append(f"| {label} | " + " | ".join(fn(ks[sz]) for sz in ("A", "B", "C")) + " |")
    row("Kaltmiete/Monat", lambda k: eur(k["miete"]))
    row("Bruttomietrendite", lambda k: pct(k["brutto"], 2))
    row("Faktor", lambda k: f"{k['faktor']:.1f}".replace(".", ","))
    row("nicht umlagef. Hausgeld", lambda k: eur(k["kosten"]["hausgeld_nu"]))
    row("Instandhaltung", lambda k: eur(k["kosten"]["instandhaltung"]))
    row("Verwaltung", lambda k: eur(k["kosten"]["verwaltung"]))
    row("Leerstand/Mietausfall", lambda k: eur(k["kosten"]["leerstand"]))
    row("Sonstiges", lambda k: eur(k["kosten"]["sonstiges"]))
    row("**Reinertrag (NOI)/Monat**", lambda k: "**" + eur(k["noi"]) + "**")
    row("Nettomietrendite (auf Gesamtinvest)", lambda k: pct(k["netto"], 2))
    for key in ("F1", "F2", "F0"):
        nm = FINANZIERUNG[key]["name"]
        row(f"Rate {key} ({nm})", lambda k, key=key: eur(k[key]["rate"]))
        row(f"**Cashflow {key}/Monat**", lambda k, key=key: "**" + eur(k[key]["cf"]) + "**")
    row("DSCR F1 / F2", lambda k: f"{k['F1']['dscr']:.2f} / {k['F2']['dscr']:.2f}".replace(".", ","))
    row("Cash-on-Cash F2", lambda k: pct(k["F2"]["coc"]))
    row("Break-even-Miete F1 / F2", lambda k: eur(k["F1"]["break_even_miete"]) + " / " + eur(k["F2"]["break_even_miete"]))
    return hdr + "\n" + "\n".join(rows), ks


def main():
    path = next((a for a in sys.argv[1:] if not a.startswith("--")), "objekte.json")
    detail = "--detail" in sys.argv
    with open(path, encoding="utf-8") as fh:
        objekte = json.load(fh)
    print("| ID | Objekt | Preis | Miete B | Brutto B | Faktor B | NOI B | CF F1 (A/B) | CF F2 (A/B) | EK nötig | EK ok |")
    print("|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|")
    for o in objekte:
        a, b = kennzahlen(o, "A"), kennzahlen(o, "B")
        print(f"| {o['id']} | {o['name']} | {eur(o['preis'])} | {eur(b['miete'])} | {pct(b['brutto'],2)} | "
              f"{fmt1(b['faktor'])} | {eur(b['noi'])} | {eur(a['F1']['cf'])} / {eur(b['F1']['cf'])} | "
              f"{eur(a['F2']['cf'])} / {eur(b['F2']['cf'])} | {eur(b['ek'])} | {'ja' if b['ek_ok'] else 'NEIN'} |")
    if "--verhandlung" in sys.argv:
        print("\n| ID | Inserat | 6 % brutto | 7 % | 8 % | 9 % | CF 0 bei F2 (Szen. A) | CF +100 bei F2 (A) | CF 0 bei F1 (B) | EK-Grenze | **Interessant ab** | **Sehr attraktiv ab** |")
        print("|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|")
        for o in objekte:
            v = verhandlung(o)
            r = lambda x: eur(round(x / 1000) * 1000)
            print(f"| {o['id']} | {eur(v['inserat'])} | {r(v['p6'])} | {r(v['p7'])} | {r(v['p8'])} | {r(v['p9'])} | "
                  f"{r(v['cf0_F2_A'])} | {r(v['cf100_F2_A'])} | {r(v['cf0_F1_B'])} | {r(v['ek_grenze'])} | "
                  f"**{r(v['interessant_ab'])}** | **{r(v['sehr_attraktiv_ab'])}** |")
    if detail:
        for o in objekte:
            print(f"\n### {o['id']} – {o['name']}\n")
            f = finanzierung(o)
            print(f"Kaufpreis {eur(f['preis'])} · Nebenkosten {eur(f['nk'])} "
                  f"(Makler {pct(o.get('makler_pct', MAKLER_STANDARD), 2)}) · Reno {eur(f['reno'])} · "
                  f"Darlehen {eur(f['darlehen'])} · Eigenkapital {eur(f['ek'])}\n")
            t, _ = tabelle_objekt(o)
            print(t)
            m = max_kaufpreise(o)
            print("\nMaximaler Kaufpreis (Base-Case-Miete): "
                  + " · ".join(f"{k}: {eur(v)}" for k, v in m.items()))


if __name__ == "__main__":
    main()
