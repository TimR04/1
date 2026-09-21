# Prompt: Erstellung der drei fehlenden DAAD-Bewerbungsdokumente

*(vollständig, zum Einfügen in eine neue Session)*

---

Du koordinierst die Fertigstellung einer DAAD-Stipendienbewerbung. **Frist: Freitag, 25.09.2026.**
Alle Dokumente auf Deutsch, alle als `.docx` über die `docx`-Bibliothek (Node).

**Arbeitsverzeichnis:** `/home/user/1/DAAD_Bewerbung/`

## Bewerbung

Tim Rösch, DAAD „Stipendien für ein Masterstudium im Ausland", Zielprogramm **MPhil in Industrial
Systems, Manufacture and Management**, Institute for Manufacturing, Department of Engineering,
University of Cambridge, Förderbeginn Oktober 2027.

## Was existiert, was fehlt

| Dokument | Stand |
|---|---|
| Empfehlungsschreiben | fertig, `05_Gutachten/` — **nicht anfassen**, nur als Abgleichsquelle lesen |
| Studienplan | Entwurf vorhanden, `04_Dokumente/Studienplan_Tim_Roesch.docx` — **überarbeiten, nicht neu schreiben** |
| **Lebenslauf (DAAD-Fassung)** | **fehlt** |
| **Motivationsschreiben** | **fehlt** |

## Pflichtlektüre vor jeder Aktion

Lies **vollständig**, bevor du irgendetwas schreibst:

- `01_Eingaben/00_APPLICANT_PROFILE.md` — Ausgangsprofil
- `01_Eingaben/05_CV_V3_AENDERUNGEN.md` — maßgebliche CV-Auswertung
- `01_Eingaben/03_DECKBLATT_VERIFIZIERT.md` — **wörtliche DAAD-Auswahlkriterien**
- `01_Eingaben/06_ISMM_OFFIZIELL_VERIFIZIERT.md` — **verifizierter Cambridge-Programmtext**
- `01_Eingaben/07_NOTEN_VERIFIZIERT.md` — Leistungsübersicht
- `01_Eingaben/08_ENTSCHEIDUNGEN_21_09.md` — verbindliche Festlegungen des Bewerbers
- `03_Strategie/DAAD_APPLICATION_BLUEPRINT.md` — Blueprint, besonders Abschnitte 3, 4, 6, 7
- `03_Strategie/RED_TEAM.md` — Schwachstellenanalyse
- `03_Strategie/04_CHECKLISTE.md`
- `04_Dokumente/Studienplan_Tim_Roesch.docx` und `05_Gutachten/Empfehlungsschreiben_Freidinger_Entwurf.docx`

`01_Eingaben/01_CURRENT_CV_EXTRACT.md` ist die **überholte** englische CV-Fassung. Nur zur
Historie, nicht als Faktenquelle.

---

## Phase 0 — Kanon (du selbst, bevor Agenten starten)

Schreibe `03_Strategie/KANON.md` mit vier Teilen. Er ist für alle Agenten bindend.

**1 · Faktenliste.** Jede belegte Tatsache mit Quelldatei. Schreibweisen, Datumsangaben, Titel und
Zahlen werden hier einmal festgelegt und später nirgends variiert.

**2 · Narrativ, maximal acht Sätze.** Die Linie: breit angelegtes duales Wirtschaftsinformatik-
Studium mit Praxis bei EY-Parthenon → eigenes Interesse verdichtet sich an der Schnittstelle von
Technologie und betrieblicher Entscheidung → Singapur als Wendepunkt → die erkannte Grenze:
wirtschaftlich beurteilen können, technisch und produktionsseitig nicht → ISMM schließt genau
diese Lücke → Spezialisierung Operations × Technologie.

**3 · Zuteilungsmatrix.** Pro Tatsache genau ein führendes Dokument. Mindestens diese Zeilen:
Noten und Abschlüsse · Bachelorarbeit · KI-Prüfverfahren · EY-Rotationen · Singapur-Workshop ·
Predictive-Maintenance-Anwendungsfall · Mercedes Böblingen · Robotik-Vortrag · BCG (geplant) ·
FNF Washington (geplant) · Cambridge-Module · Industrieprojekte · Werksbesuche · Studienreise ·
Forschungsinteresse · Warum nicht Deutschland · Warum nicht Management · SG Kirchen-Hausen ·
Jugendclub · Angelverein · FNF-Stipendium · e-fellows · Sprachkenntnisse · Karriereziel.
Kennzeichne je Dokument: PRIMÄR / SEKUNDÄR / NICHT.

**4 · Designtokens.** Verbindlich für alle drei Dokumente:

```
Schrift            Calibri durchgehend
Fließtext          11 pt, Zeilenabstand 1,15, Blocksatz
Name / Titelzeile  16 pt fett, Farbe 1F3864
Abschnitt          11,5 pt fett, Farbe 1F3864, dünne Linie darunter (0,75 pt, BFC7D5)
Unterabschnitt     11 pt fett, schwarz
Tabellen           9 pt; Kopfzeile Füllung EDF0F5 fett; Rahmen 0,5 pt BFC7D5
Metazeile          9,5 pt, Farbe 595959
Ränder             oben 2,0 · unten 1,8 · links 2,5 · rechts 2,0 cm
```

Keine weiteren Farben. Keine Fettung im Fließtext. Ruhig, aufgeräumt, viel Weißraum.

---

## Phase 1 — drei Agenten parallel, jeder mit dem Kanon

### Agent LEBENSLAUF → `04_Dokumente/Lebenslauf_Tim_Roesch_DAAD.docx`

Deutscher tabellarischer Lebenslauf, **zwei Seiten**, rückwärts-chronologisch.
Abschnittsfolge und Begründung: Blueprint Abschnitt 6.

- Kopf mit **Foto** (`01_Eingaben/Foto_Tim_Roesch.png`, rechts oben, ca. 3,5 × 4,5 cm)
- Persönliche Daten: Geburtsdatum und -ort, Staatsangehörigkeit — **Platzhalter gelb markieren**,
  falls unbekannt
- Akademische Ausbildung · Berufserfahrung · Stipendien und Auszeichnungen · Ehrenamtliches
  Engagement · Sprachkenntnisse · IT- und Methodenkenntnisse · Interessen · Ort und Datum
- **Kein** Profilabsatz, **kein** Key-Skills-Block, **keine** Consulting-Impact-Bullets
- Bachelorarbeit als eigener Eintrag unter der Ausbildung
- Ehrenamt: Verantwortungsumfang quantifizieren, nicht Wirkung. SG **362 Mitglieder**,
  Jugendclub 40.000 € / 180 Mitglieder, **Angelverein (Jugendwart) aufnehmen**
- **Programmierkenntnisse wieder aufnehmen** (Python, Java, SQL) — belegt durch die
  Programmiermodule, siehe `07_NOTEN_VERIFIZIERT.md`
- BCG als datierter künftiger Eintrag, klar als solcher gekennzeichnet
- Muss mit dem DAAD-Online-Formular bei Daten und Titeln **exakt** übereinstimmen

### Agent MOTIVATIONSSCHREIBEN → `04_Dokumente/Motivationsschreiben_Tim_Roesch.docx`

**Maximal zwei Seiten, rund 800 Wörter.** Struktur: Blueprint Abschnitt 7.

- Es ist der primäre Beleg für das Kriterium **Potenzial** (Motivation, Perspektiven,
  außerfachliches Engagement)
- **Das Schreiben argumentiert, der Studienplan belegt.** Fachliche Herleitung gehört dorthin,
  hier nur als Behauptung mit Verweis
- Hierher gehört die **persönliche Auslösergeschichte**: Werksrundgang bei Mercedes in Böblingen,
  rund 98 % Automatisierung, und der anschließende Vortrag über Robotik in der Produktion
- Engagement gehört hierher, nicht in den Studienplan
- **Cambridge-Prestige an keiner Stelle.** Substitutionstest: „TU München" einsetzen — überlebt der
  Satz, streichen
- Keine Noten, keine Modulnamen
- Klischees vermeiden: „neue Kulturen kennenlernen", „ich bin motiviert / ehrgeizig / wissbegierig",
  „eine der besten Universitäten der Welt"
- **Kein Rückkehr- oder Nutzen-für-Deutschland-Absatz**

### Agent STUDIENPLAN → bestehende Datei **überarbeiten**

`04_Dokumente/Studienplan_Tim_Roesch.docx`. **Unverändert bleiben:** der Singapur-Anker, die
Unterscheidung wirtschaftliche/physische Ebene, Abschnitt 2 zur Programmwahl, das
Forschungsinteresse an vorausschauender Instandhaltung.

Aufgaben: Abgleich mit dem Kanon · Designtokens anwenden · Überschneidungen mit dem
Motivationsschreiben entfernen · auf **vier bis viereinhalb Seiten** ausbauen, falls der Praxisteil
zu dünn wirkt (fünf Seiten sind das Maximum) · sicherstellen, dass die sieben DAAD-Pflichten
erfüllt bleiben (Ziel, Kursliste, Kurzinhalte, Credit-Angabe über Prüfungsformen, Einordnung
rückwärts und vorwärts, Begründung der Wahl, Forschungsteil).

---

## Phase 2 — Agent KONSISTENZ

Liest alle drei fertigen Dokumente **plus** das Empfehlungsschreiben und prüft:

1. Widersprüche bei Daten, Titeln, Zahlen, Schreibweisen
2. Verbotene Doppelungen, besonders Motivationsschreiben gegen Studienplan
3. Verstöße gegen die Zuteilungsmatrix
4. Abweichungen von den Designtokens
5. Seitenzahlen: Lebenslauf 2, Motivationsschreiben 2, Studienplan maximal 5
6. **Maschinentext-Marker**: Gedankenstriche, „nicht X, sondern Y", „auf zwei Ebenen",
   angehängte Bewertungsnebensätze, zu gleichmäßiger Satzrhythmus, Dreierfiguren
7. Ob jeder Absatz eines dieser fünf Kriterien bedient: Wahl der Gastinstitution begründet ·
   sinnvolle Einbindung in den Studienverlauf · Durchführbarkeit · Kenntnis der Lehr- und
   Forschungsmöglichkeiten · Qualität des wissenschaftlichen Vorhabens

Ergebnis: `03_Strategie/KONSISTENZ.md` mit konkreten, umsetzbaren Korrekturen. Setze sie
anschließend selbst um.

---

## Harte Regeln für alle Agenten

- **Keine erfundenen Tatsachen, Namen, Zahlen oder Cambridge-Details.** Nur was in `01_Eingaben/`
  belegt ist. Unbekanntes bleibt gelb markierter Platzhalter.
- **Keine Noten** in Motivationsschreiben und Studienplan. Die gehören in Lebenslauf und Transcript.
- **Keine eigenen DHBW-Modulnamen** in Motivationsschreiben und Studienplan.
- **BCG trägt kein Argument.** Erwähnung als geplant, mehr nicht.
- **Kein Kundenname** aus dem Schifffahrtsprojekt.
- **Kein einzelner Cambridge-Betreuer namentlich.** Forschungsgruppen dürfen genannt werden, sie
  sind belegt.
- **Keine erfundene ECTS-Zahl für Cambridge.** Prüfungsformen angeben.
- Leser sind **fachfremde deutsche Professoren**. Jeder Fachbegriff wird in einem Halbsatz
  eingeordnet.
- Jede Datei nach dem Schreiben **strukturell prüfen** (XML parst, Wortzahl, Tabellen) und das
  Ergebnis berichten. LibreOffice steht nicht zur Verfügung, eine optische Prüfung ist nicht
  möglich — das offen sagen.
- Nach jedem fertigen Dokument committen und pushen.
