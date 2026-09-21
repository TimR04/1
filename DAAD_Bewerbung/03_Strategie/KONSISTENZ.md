# KONSISTENZ — Schlussprüfung der vier Dokumente

Agent Konsistenz, 21.09.2026. Grundlage: `KANON.md`, `03_DECKBLATT_VERIFIZIERT.md`,
`RED_TEAM.md`, `08_ENTSCHEIDUNGEN_21_09.md`.

Geprüft wurden:

| Datei | Rolle |
|---|---|
| `04_Dokumente/Lebenslauf_Tim_Roesch_DAAD.docx` | geprüft und korrigiert |
| `04_Dokumente/Motivationsschreiben_Tim_Roesch.docx` | geprüft und korrigiert |
| `04_Dokumente/Studienplan_Tim_Roesch.docx` | geprüft und korrigiert |
| `05_Gutachten/Empfehlungsschreiben_Freidinger_Entwurf.docx` | nur gelesen, nicht verändert |

Korrigiert wurde über die Quellskripte `cv.js`, `motivation.js`, `sp2.js`; die `.docx`-Dateien
sind daraus neu erzeugt. Sicherungskopien der Skripte liegen als `*.js.bak` daneben.

---

## 0 · Grenze dieser Prüfung

**LibreOffice steht in dieser Umgebung nicht zur Verfügung. Eine optische Prüfung des
Seitenumbruchs war unmöglich.** Alle Seitenzahlen unten sind Rechenschätzungen aus der
Dokument-XML (Zeichen pro Zeile bei Calibri, Zeilenhöhe, Absatz- und Tabellenabstände, Fotohöhe)
mit einer Unsicherheit von geschätzt ±8 Prozent. Geprüft ist maschinell: dass jede XML-Datei im
Paket parst, die Wortzahlen, die Gedankenstriche, die Schriftgrade, die Platzhalter, die
verbotenen Inhalte und die wortgleichen Überschneidungen zwischen Motivationsschreiben und
Studienplan. **Der Bewerber muss alle drei Dateien vor dem Absenden einmal in Word öffnen und den
Umbruch ansehen**, insbesondere beim Lebenslauf (Schätzung 1,86 von 2 zulässigen Seiten) und beim
Studienplan (Schätzung 4,81 von 5 zulässigen Seiten).

---

## 1 · Befunde

Schwere: **kritisch** = kostet die Bewerbung einen Beleg oder erzeugt einen sichtbaren
Widerspruch · **hoch** = Verstoß gegen Kanon oder DAAD-Vorgabe · **mittel** = Doppelung oder
Abweichung, die einem aufmerksamen Leser auffällt · **gering** = Schreibweise, Typografie.

### B1 · Die Zahlen 139 und 94 Prozent fehlten in allen vier Dokumenten
**Schwere:** kritisch
**Fundstelle:** Motivationsschreiben, Absatz 2 (Prüfverfahren); Zuteilungsmatrix weist das
KI-Prüfverfahren mit 139/94 % als **P** dem Motivationsschreiben zu.
**Ursache:** Der Motivationsschreiben-Agent hat die Zahlen in der Annahme weggelassen, der
Studienplan führe sie; der Studienplan-Agent hat sie gleichzeitig entfernt. Der härteste
Einzelbeleg der Bewerbung stand damit nirgends.
**Korrektur:** Im bestehenden Absatz eingebaut, ohne ihn aufzublähen (Satz geteilt, netto
+9 Wörter): „Ich habe das Verfahren an 139 Aussagen eines vollständigen Berichts gegengeprüft;
die Bewertungsgenauigkeit lag bei 94 Prozent. Damit habe ich drei Partner als Unterstützer
gewonnen …" Im Studienplan bleiben die Zahlen draußen (dort **S**, Regel: ohne Zahlen, die das
primäre Dokument führt).
**Status:** behoben

### B2 · „Als erster Student ausgewählt" fehlte im Lebenslauf
**Schwere:** hoch
**Fundstelle:** Lebenslauf, Berufserfahrung, 5. Rotation Singapur (Sep 2025 – Nov 2025).
**Bewertung:** Es ist eine Auswahlentscheidung Dritter, kein Eigenlob, und steht in derselben
Kategorie wie „Aufnahme unter den besten 10 % der Bewerber". Quelle:
`01_CURRENT_CV_EXTRACT.md` Zeile 19 („First-ever student selected for this placement"), bestätigt
im Kanon.
**Korrektur:** Als erste Zeile des Eintrags aufgenommen: „Als erster Student für dieses Expert
Placement ausgewählt".
**Status:** behoben

### B3 · Schriftgrad im Lebenslauf abweichend
**Schwere:** hoch
**Fundstelle:** Lebenslauf durchgehend: Fließtext 10,5 pt (size 21) statt der Kanon-Vorgabe 11 pt
(size 22). Der Studienplan verwendete bereits size 22, das Motivationsschreiben ebenfalls.
Nebenbefund: die Abschnittsabstände des Lebenslaufs (before 300 / after 130) wichen von denen des
Studienplans ab (before 260 / after 120), obwohl der Kanon identische Designtokens verlangt.
**Korrektur:** Lebenslauf auf die Kanon-Werte gezogen: Fließtext 22, Stationstitel 21 fett
schwarz, Datumsspalte 19 in 595959, Abschnittsüberschrift 23 fett 1F3864 mit Linie 0,75 pt
BFC7D5, Name 32 fett 1F3864; Dokument-Standardschriftgrad 21 → 22; Abschnittsabstände an den
Studienplan angeglichen. Der Schriftgrad wurde **nicht** gesenkt, um Platz zu sparen; inhaltlich
gekürzt werden musste ebenfalls nichts, weil die Schätzung bei 1,86 Seiten bleibt.
**Status:** behoben

### B4 · FNF-Praktikum Washington stand im Studienplan
**Schwere:** hoch
**Fundstelle:** Studienplan, Abschnitt 5, Machbarkeit: „… im Frühjahr folgt ein Praktikum im
Regionalbüro der Friedrich-Naumann-Stiftung in Washington, D.C."
**Bewertung:** Der Bewerber hat die Rückfrage zu diesem Praktikum nicht beantwortet
(`08_ENTSCHEIDUNGEN_21_09.md` enthält dazu keine Entscheidung), und die Anweisung an diese Phase
lautet ausdrücklich, es nicht aufzunehmen. Dazu kam ein Matrixverstoß in beide Richtungen: Im
Lebenslauf, wo die Tatsache **P** wäre, fehlte sie; im Studienplan, wo sie nur **S** ist, stand
sie. Eine unbestätigte Planangabe allein im Sekundärdokument ist der ungünstigste aller Zustände.
**Korrektur:** Satzteil aus dem Studienplan entfernt. Der Satz endet jetzt nach dem
BCG-Praktikum. Im Lebenslauf wurde die Station **nicht** ergänzt.
**Status:** behoben — **Entscheidung des Bewerbers nötig.** Bestätigt er das Praktikum, gehört es
als datierter künftiger Eintrag („Apr 2027 – Jun 2027") in den Lebenslauf und darf im Studienplan
mit einem Halbsatz wieder erwähnt werden.

### B5 · Verbotene Doppelung: das Karriere-Argument stand wortnah in beiden Dokumenten
**Schwere:** hoch
**Fundstelle:**
- Motivationsschreiben, letzter Absatz: „Die Verfahren, um die es geht, gibt es längst. Ihre
  Einführung scheitert nach meiner Erfahrung seltener an der Technik als daran, dass niemand im
  Raum sitzt, der sie fachlich beurteilen kann."
- Studienplan, Ausblick: „Der Bedarf ist absehbar: Die Verfahren sind vorhanden, aber ihre
  Einführung scheitert selten an der Technik und häufig daran, dass niemand beurteilen kann, ob
  ihren Ergebnissen zu trauen ist."

Dasselbe Argument, nahezu dieselbe Formulierung. Der DAAD verbietet ausdrücklich, Motivation und
Studienplan zusammenzufassen; zwei Dokumente, die denselben Satz zweimal bringen, lesen sich wie
ein geteiltes.
**Korrektur:** Das Karriereziel ist laut Matrix **P** im Motivationsschreiben und nur **S** im
Studienplan. Also bleibt das Argument im Motivationsschreiben unverändert stehen, und der
Ausblick des Studienplans wurde auf drei Sätze umgeschrieben, die die Perspektive aus dem
Studienplan heraus begründen und den Bogen zum Betriebsleiter aus Singapur schließen, statt das
Argument zu wiederholen (netto −25 Wörter).
**Status:** behoben

### B6 · Verbotene Doppelung: „Entscheidung zwischen technischer und betriebswirtschaftlicher Tiefe"
**Schwere:** mittel
**Fundstelle:** Motivationsschreiben Absatz 4 und Studienplan Abschnitt 2, letzter Satz —
wortgleiche Wendung. „Warum nicht Deutschland" ist **P** im Studienplan, **S** im
Motivationsschreiben.
**Korrektur:** Der Studienplan behält die Formulierung. Im Motivationsschreiben ersetzt durch:
„In Deutschland habe ich kein Programm gefunden, das mir beide Seiten in einem Jahr
zusammenbringt." Ein Satz, ohne Herleitung — regelkonform für **S**.
**Status:** behoben

### B7 · Verbotene Doppelung: Forschungsumfeld des Institute for Manufacturing
**Schwere:** mittel
**Fundstelle:** Motivationsschreiben Absatz 4 („die Lehre von Menschen getragen wird, die selbst
an verteilter Information und Automatisierung in der Produktion forschen") gegen Studienplan
Abschnitt 2 („die Gruppe Distributed Information and Automation etwa an verteilter Information
und Automatisierung in der Produktion. Dass die Lehre von Personen getragen wird, die auf diesen
Feldern forschen …"). Zusätzlich wiederholte das Motivationsschreiben mit „wann sich auf ein
maschinell erzeugtes Ergebnis ein Eingriff an einer laufenden Anlage stützen lässt" die Frage,
die der Studienplan in Abschnitt 1 und Abschnitt 4 zweimal führt — und die es selbst einen Absatz
vorher schon gestellt hatte.
**Korrektur:** Forschungsinteresse ist **P** im Studienplan, **S** im Motivationsschreiben. Beide
Sätze im Motivationsschreiben zu einem zusammengezogen, mit eigener Wendung und Rückbindung an
den eigenen Prüfverfahrens-Absatz statt an die Studienplan-Formulierung.
**Status:** behoben

### B8 · Bezeichnung der Bachelorarbeit uneinheitlich
**Schwere:** mittel
**Fundstelle:** Studienplan Abschnitt 1: „In meiner Abschlussarbeit habe ich ein KI-gestütztes
**Prüfverfahren** für Due-Diligence-Berichte entwickelt." Kanon, Lebenslauf und Gutachten nennen
die Arbeit „KI-gestütztes **Prüftool** für Due-Diligence-Berichte".
**Korrektur:** Studienplan auf „Prüftool" gezogen. Wo nicht die Arbeit, sondern das entstandene
Verfahren gemeint ist (Lebenslauf 6. Rotation, Motivationsschreiben Absatz 2), bleibt
„Prüfverfahren" — das ist die Sache, nicht der Titel.
**Status:** behoben

### B9 · Programmbezeichnung im Betreff uneinheitlich
**Schwere:** mittel
**Fundstelle:** Betreff des Motivationsschreibens nannte „… Institute for Manufacturing,
University of Cambridge"; Studienplan-Metazeile und Betreff des Gutachtens nennen beide
„… Institute for Manufacturing, Department of Engineering, University of Cambridge".
**Korrektur:** Betreff des Motivationsschreibens angeglichen. Im laufenden Text bleibt die kurze
Form, das ist keine Titelangabe.
**Status:** behoben

### B10 · „Digital and Tech" gegen „Digital & Tech"
**Schwere:** gering
**Fundstelle:** Studienplan Abschnitt 5 gegen Lebenslauf und Kanon.
**Korrektur:** Studienplan auf „Digital & Tech" gezogen.
**Status:** behoben

### B11 · Maschinentext: Häufung von Antithesen
**Schwere:** mittel
**Befund vor der Korrektur:** Motivationsschreiben 6 Antithesen der Form „nicht X, sondern Y" /
„statt" / „seltener … als" auf 7 Fließtextabsätze (0,86 je Absatz), davon drei allein im
Schlussabsatz. Studienplan 8 auf 31 Absätze, darunter die Figur „nicht nur wirtschaftlich /
nicht nur ihren wirtschaftlichen Nutzen" dreimal in zwei benachbarten Abschnitten.
**Korrektur:** Im Motivationsschreiben Schlussabsatz entschlackt („Der Zeitpunkt ist der richtige:
Ich stehe am Anfang dieses Wegs."); im Studienplan die dritte und die überzählige zweite
Wiederholung der Figur aufgelöst (Abschnitt 1 Ziel, Abschnitt 2 Absatz 1).
**Messung nachher:** Motivationsschreiben 4 auf 7 Absätze (0,57), Studienplan 5 auf 31 (0,16).
Das liegt im Bereich normaler deutscher Sachprosa.
**Status:** behoben

### B12 · Maschinentext: zwei Dreierfiguren in einem Absatz
**Schwere:** gering
**Fundstelle:** Motivationsschreiben Absatz 3 (Böblingen): die drei unbeantworteten Fragen und
unmittelbar danach „wie diese Systeme aufgebaut sind, was sie leisten und wo sie an Grenzen
stoßen".
**Korrektur:** Die zweite Figur auf ein Paar gekürzt. Die erste trägt Inhalt und bleibt.
**Status:** behoben

### B13 · Datum im Motivationsschreiben fest eingetragen
**Schwere:** gering
**Fundstelle:** Motivationsschreiben: „Stuttgart, 21. September 2026". Lebenslauf und Gutachten
führen an derselben Stelle den gelben Platzhalter `[Datum]`.
**Bewertung:** Kein Widerspruch — ein Brief trägt das Datum seiner Abfassung, ein Lebenslauf das
der Einreichung. Aber der Bewerber sollte es bewusst entscheiden. Frist ist Freitag, 25.09.2026.
**Status:** **Entscheidung des Bewerbers nötig.** Nicht geändert.

### B14 · Empfehlungsschreiben weicht von den Designtokens ab
**Schwere:** gering
**Fundstelle:** `Empfehlungsschreiben_Freidinger_Entwurf.docx` verwendet die Schriftgrade 15, 17,
18, 19 und 22; der Kanon kennt 18, 19, 21, 22, 23, 32. Außerdem schreibt es „Wirtschaftsinformatik
– International Management for Business & IT" mit Gedankenstrich, während der Lebenslauf die
Klammerform verwendet. Es ist das einzige der vier Dokumente mit einem Gedankenstrich im Text.
**Bewertung:** Teilweise sachlich begründet — der Brief hat einen Briefkopf mit kleiner
gesetzter Absender- und Fußzeile, die der Kanon nicht vorsieht. Das Schreiben geht ohnehin auf den
Briefbogen des Gutachters und wird von ihm gesetzt.
**Status:** **offen, bewusst nicht geändert** (Auftrag: nur lesen). Wenn der Bewerber den Entwurf
weitergibt, ist das unerheblich; der Gutachter überträgt ihn auf sein eigenes Papier.

### B15 · Offene gelbe Platzhalter
**Schwere:** hoch (Bewerbung unvollständig, solange sie stehen)
**Fundstellen:**
- Lebenslauf: `[Geburtsdatum]`, `[Geburtsort]`, `[Staatsangehörigkeit]`, `[Zeitraum]`
  (Angelverein), `[Zertifikat und Jahr]` (Englisch), `[Datum]`
- Motivationsschreiben: `[Straße und Hausnummer]`, `[Postleitzahl]`
- Studienplan: keine
- Gutachten: `[Hier eigenen Briefbogen bzw. Institutslogo einsetzen]`, `[Datum]`, `[Unterschrift]`

**Hinweis zum Englisch-Zertifikat:** Laut Kanon liegt **kein Zertifikat** vor. Der Platzhalter
`[Zertifikat und Jahr]` verleitet dazu, eines zu erfinden. Existiert keines, sollte die Zeile
schlicht „Verhandlungssicher" lauten; das Deckblatt weist die Einschätzung der Arbeitssprache
ausdrücklich dem Gutachter zu, und das Gutachten liefert sie bereits.
**Status:** **Entscheidung des Bewerbers nötig.**

### B16 · Bewusst belassene Wiederholung
**Schwere:** gering, kein Fehler
**Fundstelle:** „an der Schnittstelle von Operations und digitaler Technologie" steht wortgleich
im Motivationsschreiben (Schlussabsatz) und im Studienplan (Ausblick), je einmal.
**Bewertung:** Das ist Satz 8 des Kanon-Narrativs, also der rote Faden selbst, und je ein Satz
je Dokument — im Studienplan die für **S** zulässige Höchstmenge. Eine Variation um der Variation
willen würde die Bewerbung uneinheitlicher machen, nicht besser.
**Status:** belassen, dokumentiert.

---

## 2 · Prüfungen ohne Befund

| Prüfung | Ergebnis |
|---|---|
| Rotationsdaten Lebenslauf gegen Kanon | alle sechs stimmen: Mär–Mai 2026, Sep–Nov 2025, Mai–Aug 2025, Dez 2024 – Feb 2025, Jan–Aug 2024 |
| SG Kirchen-Hausen | überall 362 Mitglieder, Rolle Vorstand, seit Mär 2025 |
| Jugendclub Kirchen-Hausen | Lebenslauf 180 Mitglieder / 40.000 € (**P**); Motivationsschreiben nur „führe die Kasse", ohne Zahlen (**S**) — regelkonform |
| Angelverein | Lebenslauf **P** mit Zeitraum-Platzhalter, Motivationsschreiben ein Satz (**S**) |
| Gedankenstriche im Fließtext | **0** in allen drei Dokumenten. Die 13 Halbgeviertstriche im Lebenslauf stehen ausnahmslos in Datumsangaben („Okt 2023 – Sep 2026"), sind also Bis-Striche, keine Gedankenstriche |
| Noten oder Credits im Motivationsschreiben | keine |
| Noten oder Credits im Studienplan | keine. Der Abschnitt zu den Credit Points spricht nur über Cambridge und sagt ausdrücklich, dass keine ECTS ausgewiesen werden — keine erfundenen ECTS |
| DHBW-Modulnamen außerhalb des Gutachtens | keine |
| Cambridge-Prestige, Ranking, „weltweit führend" | keine Treffer in beiden Dokumenten |
| Rückkehr-nach-Deutschland-Formeln | keine Treffer |
| Kundenname aus dem Schifffahrtsprojekt | nicht genannt; der Studienplan schreibt „ein früheres Kundenprojekt" |
| Namentlich genannte Cambridge-Betreuer | keine; nur Forschungsgruppen |
| BCG als Argument | im Motivationsschreiben **0** Treffer; im Studienplan genau eine sachliche Erwähnung als Vorbereitungszeit (**S**) |
| Mercedes Böblingen, Robotik-Vortrag | nur im Motivationsschreiben (**P**), nicht im Studienplan — entspricht `08_ENTSCHEIDUNGEN_21_09.md` |
| Singapur-Workshop, Predictive Maintenance | ausführlich nur im Studienplan (**P**); im Motivationsschreiben je ein Satz ohne Zahlen (**S**) |
| Ankündigungsformeln („auf zwei Ebenen", „in zweifacher Hinsicht") | 0 Treffer |
| Satzlängenstreuung | Motivationsschreiben Ø 16,0 Wörter, Streuung 7,7, von 3 bis 45; Studienplan Ø 14,6, Streuung 7,8, von 2 bis 38. Kein gleichmäßiger Maschinenrhythmus |
| XML-Struktur | alle Teile aller vier Pakete parsen |

**Roter Faden.** Das Narrativ trägt und die drei Dokumente überschneiden sich nach den
Korrekturen nur noch in Eigennamen. Der Lebenslauf liefert die Belege, das Motivationsschreiben
führt die persönliche Linie vom Prüfverfahren über Böblingen zur Berufsabsicht, der Studienplan
führt die fachliche Linie von Singapur über das Curriculum zum Forschungsvorhaben. Beide enden
an derselben Frage, aber von verschiedenen Seiten: das Motivationsschreiben bei „niemand im Raum,
der es beurteilen kann", der Studienplan bei der Frage des Betriebsleiters. Eine maschinelle
Prüfung auf wortgleiche Sechs-Wort-Folgen zwischen Motivationsschreiben und Studienplan findet
nur noch den Programmnamen, den Universitätsnamen, den Hochschulnamen und die Narrativwendung
aus B16.

---

## 3 · Umfänge und Seitenschätzungen

| Dokument | Wörter | geschätzte Seiten | zulässig | Bewertung |
|---|---|---|---|---|
| Lebenslauf | 381 | **1,86** | 2 | knapp, vor dem Absenden ansehen |
| Motivationsschreiben | 794 | **1,57** | 2 | unkritisch |
| Studienplan | 2.034 | **4,81** | 5 | knapp, vor dem Absenden ansehen |
| Empfehlungsschreiben (nur gelesen) | 576 | 1,71 | — | — |

Wortzahlen einschließlich Tabelleninhalten und Kopfzeilen. Der Lebenslauf ist durch die Umstellung
auf 11 pt um etwa 0,07 Seiten gewachsen und durch die angeglichenen Abschnittsabstände um etwa
0,03 Seiten geschrumpft; die neue Singapur-Zeile kostet eine Zeile. Der Studienplan ist durch die
Streichung des Washington-Praktikums und den gekürzten Ausblick um 54 Wörter kürzer geworden.

**Wenn der Lebenslauf in Word doch über zwei Seiten läuft**, ist zuerst inhaltlich zu kürzen und
nicht der Schriftgrad zu senken. Die günstigsten Kandidaten, in dieser Reihenfolge: die Zeile
„Weitere Werkzeuge | Jira, PowerPoint" mit der Zeile darüber zusammenlegen; im Eintrag zur
3. Rotation die PMO-Zeile mit der Standortanalyse zu einer Zeile verbinden.

---

## 4 · Was der Bewerber noch entscheiden muss

1. **FNF-Praktikum Washington** (B4) — soll es in die Bewerbung? Wenn ja, gehört es in den
   Lebenslauf und darf im Studienplan wieder mit einem Halbsatz erwähnt werden.
2. **Englisch-Zertifikat** (B15) — existiert eines? Wenn nein, Platzhalter streichen statt füllen.
3. **Geburtsdatum, Geburtsort, Staatsangehörigkeit, Zeitraum Jugendwart** (B15) — nachtragen.
4. **Anschrift im Motivationsschreiben** (B15) — Straße und Postleitzahl nachtragen.
5. **Datum** (B13) — Lebenslauf und Gutachten tragen einen Platzhalter, das Motivationsschreiben
   den 21.09.2026. Vor dem Absenden angleichen oder bewusst so lassen.
6. **Optische Kontrolle** (Abschnitt 0) — alle drei Dateien einmal in Word öffnen.
