# CV Research

**Agent:** 4 — CV Research
**Programme:** DAAD "Stipendien für ein Masterstudium im Ausland" ("Master im Ausland")
**Applicant:** German, DHBW B.Sc. Wirtschaftsinformatik (IMBIT), consulting (EY/EY-Parthenon), target MPhil ISMM Cambridge, start October 2027
**Date of research:** 2026-09-17

---

## 0. Research log

### 0.1 Tooling constraints (read this before trusting any "verbatim" below)

Two hard constraints shaped this research and must be disclosed:

1. **`WebFetch` was blocked for every domain tried.** The agent proxy returned `EGRESS_BLOCKED` for `www.daad.de`, `www2.daad.de`, `static.daad.de`, `www.daad.pl`, `www.ifm.eng.cam.ac.uk`, `www.mygermanuniversity.com`, `www.ipw.uni-hannover.de` and `gostralia-gomerica.de`. I could not open a single source page directly. Attempts to diagnose the proxy (`curl .../__agentproxy/status`, reading `/root/.ccr/README.md`) were denied by the permission classifier.
   **Consequence:** everything below is based on *search-engine-relayed page content* (`WebSearch` returns substantive summaries and quoted fragments of the indexed pages). Where I present German wording in quotation marks, it is wording **as relayed by the search tool from the indexed DAAD page/PDF** — not text I read on the page myself. I have marked every such item `[RELAYED]`. **Every `[RELAYED]` A-classification must be re-verified by opening the URL in a browser before the CV is finalised.** I have deliberately *not* invented any quotation.
2. **The session-wide web-search budget (200 calls, shared across the 9-agent team) was exhausted** after my 24th search. Questions I had not yet reached at that point are marked `[SEARCH BUDGET EXHAUSTED — NOT SEPARATELY VERIFIED]` and are classified conservatively (C or D), with the reasoning shown.

### 0.2 Searches performed (24; German and English)

| # | Language | Query |
|---|---|---|
| 1 | DE | DAAD Stipendien für ein Masterstudium im Ausland Lebenslauf Bewerbungsunterlagen |
| 2 | DE | DAAD Lebenslauf Stipendium tabellarisch Vorlage Hinweise |
| 3 | DE | DAAD Portal Bewerbungsportal Lebenslauf hochladen Anlagen Formular ausfüllen (domain-limited to daad.de) |
| 4 | DE | DAAD Checkliste Bewerbungsunterlagen tabellarischer Lebenslauf Muster |
| 5 | DE | "Stipendien für ein Masterstudium im Ausland" Bewerbungsvoraussetzungen Auswahlkriterien (domain-limited to daad.de) |
| 6 | DE | DAAD Lebenslauf "maximal 3 Seiten" tabellarisch lückenlos Stipendium |
| 7 | DE | DAAD "europass" Lebenslauf "bitte nutzen Sie hierfür ausschließlich das europass-Format" Ausschreibung |
| 8 | EN | DAAD scholarship CV "europass" required format curriculum vitae attachments |
| 9 | DE | DAAD "Master im Ausland" Ausschreibung 2027 Bewerbungsunterlagen Liste "Lebenslauf" Seiten Portal |
| 10 | DE | DAAD Bewerbungsportal Online-Bewerbungsformular Bildungsgang Werdegang Lebenslauf automatisch erzeugt PDF |
| 11 | DE | meindaad.de Bewerbungsformular ausfüllen Abschnitte Schul-/Hochschulbildung Berufstätigkeit Sprachkenntnisse |
| 12 | DE | DAAD Lebenslauf Foto ja oder nein Stipendienbewerbung Bewerbungsfoto |
| 13 | DE | DAAD Lebenslauf "ohne Foto" Anlage Bewerbung Stipendium Hinweis |
| 14 | DE | uni-bremen Bewerbungshilfe für Studierende DAAD Lebenslauf Motivationsschreiben Tipps PDF |
| 15 | EN | Cambridge postgraduate application CV resume requirement applicant portal (domain-limited to cam.ac.uk) |
| 16 | EN | UK CV conventions no photo no date of birth no marital status graduate application |
| 17 | EN | Cambridge "supporting documents" CV guidance postgraduate "your CV" two pages (domain-limited) |
| 18 | DE | Lebenslauf Stipendium Begabtenförderungswerk Aufbau chronologisch antichronologisch Abitur Noten angeben |
| 19 | DE | e-fellows.net Stipendien und Auszeichnungen im Lebenslauf wo angeben eigene Rubrik |
| 20 | DE | DHBW duales Studium im Lebenslauf darstellen Theoriephasen Praxisphasen erklären |
| 21 | EN | academic CV vs professional resume scholarship application differences thesis publications |
| 22 | DE | Bachelorarbeit Thema im Lebenslauf angeben Stipendium akademischer Lebenslauf Note |
| 23 | DE | DAAD Auswahlkriterien Stipendium fachliche Qualifikation gesellschaftliches Engagement Auswahlkommission |
| 24 | DE | DAAD Auswahlgespräch Vorbereitung Lebenslauf außerfachliches Engagement Ehrenamt Erfahrungsbericht |

Search 25 (`"Deine Chance DAAD" Bewerbungsleitfaden …`) was refused: budget exhausted.

### 0.3 Questions left open by the budget

Not separately searched, therefore conservatively classified below: hobbies/Interessen in a DAAD CV specifically; a dedicated source on presenting German grades (1,0–4,0 scale / ECTS grade) to a committee; a dedicated source on profile/summary paragraphs in German scholarship CVs; a dedicated source on consulting-CV bullet style vs. scholarship CV; the exact 2026/27 "Master im Ausland" attachment list read off the programme page itself.

---

## 1. Official DAAD requirements for the CV (classification A) — including whether the portal generates one

### 1.1 The document is named "Lebenslauf" and is an uploaded attachment, not a form

**A [RELAYED]** — Applications run exclusively through the DAAD Portal, and the listed application documents are uploaded in the portal section **"Anlagen"** (attachments). Relayed wording: *"Die aufgelisteten Bewerbungsdokumente werden im DAAD-Portal im Bereich ‚Anlagen' hochgeladen."*
Source: DAAD Stipendiendatenbank, "Stipendien für ein Masterstudium im Ausland" — https://www2.daad.de/ausland/studieren/stipendium/de/70-stipendien-finden-und-bewerben/?detail=57503584 ; DAAD, "Bewerbung um ein DAAD-Stipendium" — https://www.daad.de/de/im-ausland-studieren-forschen-lehren/stipendien-finanzierung/bewerbung/

**A [RELAYED]** — **Only PDF files can be uploaded to the portal.** Relayed wording: *"Bitte beachten Sie, dass Sie nur PDF-Dateien in das Portal hochladen können."*
Source: https://www.daad.de/de/im-ausland-studieren-forschen-lehren/stipendien-finanzierung/bewerbung/

**A [RELAYED]** — **Upload only the attachments that are actually listed** in the call. Extra documents are not wanted.
Source: same page.

**A [RELAYED]** — Incomplete applications are not considered; completeness is the applicant's responsibility (*"Unvollständige Bewerbungen werden vom DAAD nicht berücksichtigt. Die Verantwortung für die Vollständigkeit liegt bei Ihnen."*).
Source: https://www2.daad.de/ausland/studieren/stipendium/de/70-stipendien-finden-und-bewerben/?detail=57503584

### 1.2 The document set for this programme

**A [RELAYED]** — The attachment set for "Master im Ausland"-type study scholarships comprises: tabular CV; **Studienplan (max. 5 Seiten)** with a detailed description of the study plan and any master's-thesis research; **Motivationsschreiben (max. 2 Seiten)** setting out academic and personal motives; Abschlusszeugnis; Hochschulzugangsberechtigung; Zulassung/Nachweis der Gasthochschule; Sprachnachweis; Gutachten einer/eines Hochschullehrenden.
Sources: https://www2.daad.de/ausland/studieren/stipendium/de/70-stipendien-finden-und-bewerben/?detail=57503584 ; https://www.e-fellows.net/stipendien/daad-stipendium
*(The digital variant of the programme uses a 6-page Studienplan: https://www2.daad.de/ausland/studieren/stipendium/de/70-stipendien-finden-und-bewerben/?detail=57694370 — not the applicant's case.)*

**Load-bearing consequence for the CV:** the CV is **one of eight documents**, and it sits beside a transcript (Abschlusszeugnis), a language certificate and a 2-page motivation letter. Anything that those documents carry does not need to be carried again by the CV. This single structural fact drives most of the recommendations in §2 and §5.

### 1.3 Length

**B [RELAYED] — NOT confirmed on the programme page itself.** DAAD's standard formulation across scholarship-database entries is *"Der Lebenslauf muss lückenlos und tabellarisch aufgebaut sein und darf maximal 3 Seiten umfassen"* — "gapless, tabular, maximum 3 pages". The search result attached this wording to a cluster of DAAD Stipendiendatenbank pages (Promotionen in Deutschland, Cotutelle, Forschungsstipendien, Doktorandenstipendien) and reported that longer CVs are acceptable in several programmes, with **Studienstipendien – Masterstudium** and **ERP-Studienstipendien** explicitly accepting 3 pages.
Sources: https://www2.daad.de/deutschland/stipendium/datenbank/de/21148-stipendiendatenbank/?detail=50026200 (Studienstipendien – Masterstudium für alle wissenschaftlichen Fächer) ; https://www2.daad.de/deutschland/stipendium/datenbank/de/21148-stipendiendatenbank/?detail=57135739 ; https://www2.daad.de/deutschland/stipendium/datenbank/de/21148-stipendiendatenbank/?detail=57507783 ; https://www2.daad.de/deutschland/stipendium/datenbank/de/21148-stipendiendatenbank/?detail=57742121 ; https://www.mygermanuniversity.com/de/articles/CV-for-DAAD-Scholarship-Application
**I could not verify a page limit on the "Stipendien für ein Masterstudium im Ausland" page (detail=57503584) itself.** Treat "max. 3 pages" as a ceiling that certainly is not exceeded, not as a target. See §2.1 for the recommendation.

### 1.4 Format: tabular, gapless, typed

**A [RELAYED]** — DAAD's own application checklist: *"Der Lebenslauf sollte computergeschrieben, lückenlos und tabellarisch sein; mit Angabe des Studiengangs sowie Erwähnung persönlicher Eignung und außerfachlichen Engagements."* ("typed, gapless, tabular; stating the degree programme and mentioning personal aptitude and extracurricular engagement").
Source: DAAD, "Checkliste Bewerbungsunterlagen" — https://www2.daad.de/medien/ausland/dokumente/checkliste_bewerbungsunterlagen.pdf
This is the single most important official sentence for this document. It is a **content instruction, not only a format instruction**: DAAD explicitly names *persönliche Eignung* and *außerfachliches Engagement* as things the CV must show.

**A [RELAYED]** — Related DAAD checklists repeat "lückenlos tabellarisch": e.g. *"ein tabellarischer Lebenslauf inklusive außerfachlichem Engagement"* (Doktorandenstipendien), *"lückenloser tabellarischer Lebenslauf mit wissenschaftlichem Werdegang"* (Postdoc), *"lückenloser tabellarischer Lebenslauf … in Deutsch oder Englisch"* (Praktika).
Sources: https://www2.daad.de/medien/ausland/dokumente/checkliste_bewerbung_doktoranden_kurz_deutsche_de.pdf ; https://www2.daad.de/medien/ausland/ausschreibungen/postdoc_checkliste_fuer_bewerbungsunterlagen.pdf ; https://static.daad.de/media/daad_de/pdfs_nicht_barrierefrei/im-ausland-studieren-forschen-lehren/checkliste_bewerbung_proglinie_1.pdf

### 1.5 Does DAAD provide a form or template for the CV?

**A [RELAYED] — For this programme: no template, no form.** DAAD supplies forms for the *application form* (Bewerbungsformular) and the *Gutachten* (referee report), which are downloaded from the portal, filled in offline and re-uploaded. Relayed: *"nach der Anmeldung im DAAD-Portal finden Sie das Bewerbungsformular sowie den Vordruck für das Gutachten."* No equivalent CV Vordruck is provided for the study-scholarship line.
Source: https://www.daad.de/de/im-ausland-studieren-forschen-lehren/stipendien-finanzierung/bewerbung/ ; https://www.meindaad.de/de/help/wie-kann-ich-meine-bewerbung-einreichen-o/

**Exception worth knowing (A [RELAYED]):** some *other* DAAD programme lines do impose a CV form — the Kongressreisen / HAW.International Kongressreisen line requires a specific attachment **"K2 Lebenslauf (bitte ohne Foto)"**.
Sources: https://www2.daad.de/ausland/studieren/stipendium/de/70-stipendien-finden-und-bewerben/?detail=57369745 ; https://www2.daad.de/ausland/studieren/stipendium/de/70-stipendien-finden-und-bewerben/?detail=57479681
This matters only as proof that DAAD *does* say so explicitly when it wants a form or wants no photo — and it does not say so here.

### 1.6 Does the portal auto-generate a CV from the entered data?

**A [RELAYED] — No. The portal generates a "Bewerbungszusammenfassung", not a CV.** On submission the applicant receives, as an attachment to the submission confirmation, a PDF titled **"Bewerbungszusammenfassung"** containing the completed application form plus all submitted attachments.
Source: https://www.meindaad.de/de/help/wie-kann-ich-meine-bewerbung-einreichen-o/ ; https://www.daad.de/de/im-ausland-studieren-forschen-lehren/stipendien-finanzierung/bewerbung/

**B** — But the structured application form *does* capture biographical and career data independently of the uploaded CV (person, planned project, and — per the portal guide — education/career/language fields), and the funding programme and related fields are pre-filled when the applicant enters the portal from the scholarship database.
Sources: https://www.daad.de/de/im-ausland-studieren-forschen-lehren/stipendien-finanzierung/bewerbung/ ; DAAD portal guide, https://static.daad.de/media/daad_de/pdfs_nicht_barrierefrei/im-ausland-studieren-forschen-lehren/daad_kr_portal-bewerbung_erstellen_und_verwalten.pdf

**What this means, and it is the most practically useful finding in §1:**
- **B** The uploaded CV is **not** the committee's only route to the applicant's dates. The form already has them. So the CV's job is not to be a complete data dump — it is to be the *readable, weighted* version of the record. Do not pad it to 3 pages just because 3 pages are allowed.
- **A [RELAYED]** The CV and the form are read side by side, and completeness is the applicant's responsibility — so **the CV must not contradict the form**: identical dates, identical employer names, identical degree titles. Any mismatch is a self-inflicted credibility problem.
  Source: https://www2.daad.de/ausland/studieren/stipendium/de/70-stipendien-finden-und-bewerben/?detail=57503584

### 1.7 Deadlines / cycle (context only)

**A [RELAYED]** — For a start in 2027, deadlines are region-dependent: a December selection round for funding starting from September 2027, with regional application deadlines reported as 30 September 2026, 16 November 2026 and 1 December 2026, and other regions selecting in March. Applicants are advised to submit several days early.
Source: https://www2.daad.de/ausland/studieren/stipendium/de/70-stipendien-finden-und-bewerben/?detail=57503584
**Verify the exact deadline for the UK on the programme page** — this is Agent-1 territory but it bears on the CV because the CV's "current position" line has to be true as of submission, and an October-2027 start means the CV is written in autumn 2026.

### 1.8 Selection process — why the CV is read at all

**A [RELAYED]** — *"Nach einer ersten Vorauswahl auf Basis der eingereichten Unterlagen werden die erfolgreichen Bewerberinnen und Bewerber zu einer persönlichen Vorstellung vor der Auswahlkommission eingeladen."* — a first pre-selection on the documents alone, then interview.
Source: https://www2.daad.de/ausland/studieren/stipendium/de/70-stipendien-finden-und-bewerben/?detail=57503584

**A [RELAYED]** — The committee decides on **academic qualification and the quality of the study/research project *plus* non-academic criteria**, explicitly including extracurricular knowledge and abilities and **social engagement**, and it assesses the applicant's **development potential and ability to take responsibility (Verantwortungsübernahme)**. Committees are honorary and composed chiefly of German university teachers, plus former DAAD scholarship holders.
Sources: https://www.daad.de/de/in-deutschland-studieren/stipendien/hinweise-daad-stipendien/ ; https://www.daad.de/de/im-ausland-studieren-forschen-lehren/stipendien-finanzierung/wichtige-hinweise-zu-daad-stipendien/ ; https://www.daad.de/de/der-daad/wer-wir-sind/organisation/auswahlkommissionen/ ; https://www.studieren-weltweit.de/tipps-auswahlgespraech-stipendium/

**B** — Therefore the CV has exactly two jobs in the pre-selection: (i) make the academic record legible in seconds, and (ii) evidence *persönliche Eignung*, *außerfachliches Engagement* and *Verantwortungsübernahme* — the criteria DAAD names. Content that serves neither is space wasted.

---

## 2. Findings by question

### 2.1 Expected length — does DAAD state a limit?

- **B [RELAYED]** Ceiling: **max. 3 pages** is DAAD's standard CV formulation and is reported as explicitly applying to the Master-level study-scholarship lines. Not verified on the "Master im Ausland" page itself (§1.3). — https://www2.daad.de/deutschland/stipendium/datenbank/de/21148-stipendiendatenbank/?detail=50026200
- **C** Target: **2 pages.** German scholarship-CV guidance converges on a maximum of two A4 pages for the tabular form. — https://stipendiumscoach.de/lebenslauf-stipendium/ ; https://www.mystipendium.de/bewerbung-stipendium/lebenslauf-stipendium ; https://www.uni-bremen.de/fileadmin/user_upload/sites/international/Studieren_im_Ausland/Bewerbungshilfe_fuer_Studierende.pdf
- **B** Reasoning for this applicant: a 2027 Master applicant with one Bachelor's degree, roughly two to three years of practice-phase and internship experience and three club offices has a record that fits two pages honestly. A three-page CV built out of a Bachelor-only record signals padding to a committee of professors who read hundreds of these. Use page 3 only if publications/projects genuinely require it.
- **Recommendation: 2 pages, hard. 3 is the legal ceiling, not the goal.**

### 2.2 Does DAAD provide a form/template, or require a specific format? Does the portal auto-generate a CV?

- **A [RELAYED]** No CV template or form for this programme; CV is a free-form PDF uploaded under "Anlagen"; PDF only. — §1.5, §1.1
- **A [RELAYED]** The portal does **not** auto-generate a CV. It generates a "Bewerbungszusammenfassung" bundling the completed form and the attachments. — §1.6
- **B** Practical consequences: (a) name the file unambiguously (`Nachname_Vorname_Lebenslauf.pdf`); (b) keep it under the portal's general upload hygiene — the Cambridge portal's 2 MB/unencrypted rule is a useful discipline even though it is Cambridge's, not DAAD's (https://www.postgraduate.study.cam.ac.uk/apply/how/supporting-documents); (c) **mirror the form exactly** on dates, titles and employer names.

### 2.3 Europass — required or not? (the claim that must be checked)

- **A [RELAYED] — The blanket claim "DAAD requires Europass" is FALSE.** Europass is required in *specific* DAAD programme lines and not in others. The **EPOS** line (Entwicklungsbezogene Postgraduiertenstudiengänge) requires a gapless CV **using the Europass template**, hand-signed. The **Studienstipendien – Masterstudium für alle wissenschaftlichen Fächer** line does **not**. — https://www2.daad.de/deutschland/stipendium/datenbank/de/21148-stipendiendatenbank/?detail=50076777 ; https://www2.daad.de/medien/deutschland/stipendien/formulare/epos_faq_en.pdf ; https://www2.daad.de/deutschland/stipendium/datenbank/de/21148-stipendiendatenbank/?detail=50026200
- **C** The explicit secondary rule, consistent with the above: *if DAAD does not ask for Europass, do not use it.* — https://www.mygermanuniversity.com/articles/CV-for-DAAD-Scholarship-Application
- **Note on DAAD's dual role:** DAAD is itself the German National Agency issuing Europass Mobility in the higher-education sector and promotes Europass editorially. That is almost certainly the origin of the folk claim. It is an institutional role, not an application requirement. — https://eu.daad.de/infos-fuer-einzelpersonen/foerderung-fuer-studierende-und-graduierte/europass/de/46248-europass/ ; https://eu.daad.de/mit-erasmus-ins-ausland/foerderung-fuer-studierende-und-graduierte/der-europass/
- **DAAD SILENT** for "Master im Ausland" specifically — no Europass instruction found on the programme page.
- **Recommendation (B): do not use Europass.** It is verbose, template-locked, burns roughly a page on chrome, and cannot be weighted the way §5 requires. **Action item: re-read the "Master im Ausland" attachment list in the portal before submitting; if it names Europass, that overrides this recommendation immediately (A beats B).**

### 2.4 German vs international CV style — which dominates?

- **A [RELAYED]** DAAD prescribes the **German** genre by name: *tabellarischer Lebenslauf*, *lückenlos*, *computergeschrieben*. — https://www2.daad.de/medien/ausland/dokumente/checkliste_bewerbungsunterlagen.pdf
- **B** The reader is a German committee (chiefly German university teachers, plus DAAD alumni), applying German scholarship-selection criteria, reading German-language criteria. — https://www.daad.de/de/der-daad/wer-wir-sind/organisation/auswahlkommissionen/
- **Verdict: German tabular Lebenslauf dominates.** UK conventions do not govern this document. See §4 for the full argument and §2.16 for the one real tension.

### 2.5 Chronological (ascending) vs reverse chronological — resolve explicitly

This is the one point where credible German sources genuinely disagree, so state it carefully.

- **DAAD SILENT.** No DAAD source found specifies ordering. DAAD specifies *tabellarisch* and *lückenlos* only. — https://www2.daad.de/medien/ausland/dokumente/checkliste_bewerbungsunterlagen.pdf
- **C** German scholarship guidance: the **tabular** CV is **antichronologisch** (newest first), while the **ausformulierter Lebenslauf** (narrative, used by some Begabtenförderungswerke) is chronological ascending. Explicit: *"Der ausführliche Lebenslauf ist chronologisch, ein normaler CV antichronologisch."* — https://stipendiumscoach.de/lebenslauf-stipendium/ ; https://zety.de/blog/ausformulierter-lebenslauf ; https://de.indeed.com/karriere-guide/bewerbung/antichronologischer-lebenslauf
- **C** DAAD-facing advice explicitly names reverse-chronological ("American format") as the expected order for the DAAD CV, alongside the requirement that it be tabular, clearly structured and grouped by topic. — https://www.mygermanuniversity.com/de/articles/CV-for-DAAD-Scholarship-Application ; https://www.mygermanuniversity.com/articles/CV-for-DAAD-Scholarship-Application
- **C** The older German convention (ascending, school first) survives mainly in the narrative form and in formal/administrative Lebensläufe; it is no longer the default for a tabular CV.
- **Resolution (C, well-supported): reverse chronological within each section.** Reasons: (i) it is the modern German tabular default *and* the international default, so it costs nothing on either side; (ii) it is the only order that puts the most relevant item — the current/most recent position, and above all the completed B.Sc. and its AI thesis — in the committee's first eye-sweep; (iii) ascending order would open a Bachelor-level CV with the Abitur, which is the least decision-relevant item in the whole document.
- **A [RELAYED]** Whichever order is chosen, it must be **lückenlos**: apply it consistently and leave no unexplained gap. Gaps are the thing DAAD actually polices. — https://www2.daad.de/medien/ausland/dokumente/checkliste_bewerbungsunterlagen.pdf
- **One caveat (B):** ordering must be *consistent across all sections and across all four documents*. A reverse-chronological CV read next to a chronologically-narrated motivation letter is fine; a CV that is reverse-chronological in Education and ascending in Experience is not.

### 2.6 Photo — include or not?

Genuinely contested. Set out the evidence honestly.

- **DAAD SILENT for this programme.** No photo instruction found on the "Master im Ausland" page or in the general Checkliste Bewerbungsunterlagen.
- **A [RELAYED] — counter-evidence that DAAD speaks when it cares:** the Kongressreisen / HAW.International lines require the CV **"bitte ohne Foto"**. DAAD therefore *does* issue explicit no-photo instructions where it wants them — and has not done so here. — https://www2.daad.de/ausland/studieren/stipendium/de/70-stipendien-finden-und-bewerben/?detail=57369745 ; https://www2.daad.de/ausland/studieren/stipendium/de/70-stipendien-finden-und-bewerben/?detail=57479681
- **C** German-market and DAAD-facing advice: a photo is standard in a German Lebenslauf and is normally expected/accepted in a DAAD application; it should be a professional, LinkedIn-grade photograph. — https://www.mygermanuniversity.com/de/articles/CV-for-DAAD-Scholarship-Application ; https://www.mygermanuniversity.com/de/articles/CV-for-German-Universities ; https://cvlotse.de/ratgeber/lebenslauf-mit-oder-ohne-foto
- **C** German labour-market practice is drifting away from photos generally (AGG-driven), so a photo-free German CV is no longer unusual. — https://bewerbung.net/lebenslauf-foto ; https://www.workwise.io/karriereguide/bewerbung/bewerbungsfoto-ja-nein
- **C** UK/Cambridge practice is the opposite: **no photo**, on Equality Act 2010 grounds. — https://uk.indeed.com/career-advice/cvs-cover-letters/date-of-birth-cv
- **Recommendation (C): include a discreet, professional photo in the DAAD CV** — this is a German document for a German committee, DAAD explicitly bans photos where it wants them banned and does not here, and German convention treats the photo as neutral. Keep it small (top-right, passport proportions), current, plain background, business dress. It must never crowd content or push the CV onto a third page.
- **Firm corollary (B): do NOT reuse this photo version for Cambridge.** Maintain two files. See §4 and §6.6.
- **D (flagged as weak):** the secondary claim that "even if the DAAD programme does not require a photo, you must submit an application photo anyway" appears in one commercial guide and I could not corroborate it in any DAAD source. Treat as unverified; do not build on it. — https://www.mygermanuniversity.com/de/articles/CV-for-DAAD-Scholarship-Application

### 2.7 Date and place of birth

- **DAAD SILENT** in the CV instructions. **But B [RELAYED]:** the portal application form collects personal data (*"Sie vervollständigen Angaben zu Ihrer Person und Ihrem geplanten Vorhaben"*), so DAAD has these data regardless. — https://www.meindaad.de/de/help/wie-kann-ich-meine-bewerbung-einreichen-o/ ; https://www.meindaad.de/de/datenschutzhinweise-bewerbungsformular/
- **C** German convention: **Geburtsdatum und Geburtsort belong in the Persönliche Daten block** of a tabular Lebenslauf. — https://www.mystipendium.de/bewerbung-stipendium/lebenslauf-stipendium ; https://www.lebenslaufmuster.de/tabellarischer-lebenslauf/
- **C** UK convention: omit both. — https://uk.indeed.com/career-advice/cvs-cover-letters/date-of-birth-cv
- **Recommendation (C): include date of birth and place of birth in the DAAD CV.** They are German-convention neutral, they match the form, and their absence in a German scholarship CV reads as a small foreign-ness rather than as modernity. Omit both from the Cambridge CV.

### 2.8 Nationality

- **DAAD SILENT** in the CV instructions, **but B**: nationality is materially relevant to this programme — DAAD "Master im Ausland" funds German applicants (and equivalents), and the eligibility rule found (degree not more than five years old) sits in the same eligibility block. Nationality is a gate condition, not decoration. — https://www2.daad.de/ausland/studieren/stipendium/de/70-stipendien-finden-und-bewerben/?detail=57503584
- **C** German convention places **Staatsangehörigkeit** in the Persönliche Daten block. — https://www.mystipendium.de/bewerbung-stipendium/lebenslauf-stipendium
- **Recommendation (C): include nationality ("deutsch").** Omit from the Cambridge CV (where it is a protected characteristic); if Cambridge needs it, it goes in the portal fields, not the CV. — https://uk.indeed.com/career-advice/cvs-cover-letters/date-of-birth-cv

### 2.9 How much detail does professional experience need — and does consulting bullet style translate?

- **A [RELAYED]** The CV must be *lückenlos* and must state the degree programme and evidence *persönliche Eignung*. Professional experience is therefore mandatory content, but it is not what DAAD names as the criterion. — https://www2.daad.de/medien/ausland/dokumente/checkliste_bewerbungsunterlagen.pdf
- **A [RELAYED]** The committee's criteria are academic qualification, the quality of the study project, extracurricular ability and social engagement, development potential and readiness to take responsibility. Commercial impact is not on the list. — https://www.daad.de/de/in-deutschland-studieren/stipendien/hinweise-daad-stipendien/
- **B** Therefore: **every professional entry needs a date range, employer, role and location — and at most one to two short lines of substance.** The substance should establish *domain* (manufacturing, operations, digital transformation, AI/analytics) and *responsibility level*, because those are what make the ISMM plan credible, not what makes a hire attractive.
- **C / D — consulting bullet style does NOT translate cleanly.** [SEARCH BUDGET EXHAUSTED — NOT SEPARATELY VERIFIED; classified conservatively.] What survives and what dies:
  - **Dies:** action-verb-plus-outcome bullets whose payload is client value ("drove EUR Xm EBITDA uplift", "identified EUR Xm synergies"), stacked 3–4 per role, superlatives, firm-internal jargon (workstream, deep-dive, PMI, CDD/VDD), and client names the applicant is under NDA for. A German professorial committee reads this as a job application filed at the wrong address — and, worse, as an applicant whose orientation is commercial rather than academic, which directly undercuts the "why an MPhil rather than a promotion" question the whole application has to answer.
  - **Survives, reframed:** *scope and subject matter*. "Transaction and operations projects for industrial clients; commercial due diligence and post-merger operations; analytics/AI workstreams" is exactly the kind of line that makes an industrial-systems MPhil look like a continuation rather than a detour.
  - **Survives unchanged:** dates, employer, role title, location, and international placements.
- **Recommendation (B): 1–2 lines per role, topic-led not result-led; use the space saved on §2.11 and §2.13.** The motivation letter, not the CV, is where the professional work is argued into a rationale (Agent-2's territory — do not duplicate it here).

### 2.10 How should academic achievements be shown?

- **A [RELAYED]** The CV must name the **Studiengang** explicitly. — https://www2.daad.de/medien/ausland/dokumente/checkliste_bewerbungsunterlagen.pdf
- **B** Each degree entry: date range | degree and full programme title | institution | (for DHBW: dual partner) | final grade | thesis as its own sub-line | any specialisation/focus.
- **C** In academic CVs it is standard to name the thesis topic and relevant study focus, and to add the final grade where it supports the application. — https://www.jobvector.de/lebenslauf-erstellen/vorlagen/akademischer-lebenslauf/ ; https://www.wikway.de/wissen/bewerber/studium-ausbildung-und-schulabschluss-im-lebenslauf-richtig-darstellen
- **B** Semesters/modules/individual course grades do **not** belong in the CV — the Abschlusszeugnis is a separate required attachment and carries them. — §1.2
- **B** Study-abroad or exchange periods *do* belong as sub-lines under the degree (they are academic, and they evidence international orientation, which is the programme's stated purpose). — https://www2.daad.de/ausland/studieren/stipendium/de/70-stipendien-finden-und-bewerben/?detail=57503584

### 2.11 Scholarships (Friedrich-Naumann-Stiftung, e-fellows.net) — how and where?

- **DAAD SILENT** on placement.
- **C** German convention is clear and consistent: give scholarships and awards **their own section**, headed e.g. *"Stipendien und Auszeichnungen"*; place it **after professional experience and before the skills sections** (languages/IT); combine scholarships and awards into one section unless there are more than about five items; and for each, name **the awarding organisation, the period, and the purpose**. — https://www.e-fellows.net/bewerbung/lebenslauf/stipendien-und-auszeichnungen-im-lebenslauf ; https://www.e-fellows.net/stipendien/wie-gebe-ich-ein-stipendium-im-lebenslauf-an
- **C** A competing convention places awards/scholarships **directly after education and experience** when the applicant has many of them. — https://www.jobvector.de/lebenslauf-erstellen/vorlagen/akademischer-lebenslauf/
- **Recommendation (C): a dedicated "Stipendien und Auszeichnungen" section, positioned after Professional Experience and before Engagement/Skills.** With two entries it must not be inflated into a page-filling block.
- **B — the two items are not equivalent and must not be presented as equivalent:**
  - **Friedrich-Naumann-Stiftung für die Freiheit** is a *Begabtenförderungswerk* — a competitive, interview-based, state-recognised talent-support foundation. This is the single strongest third-party validation in the entire CV and it speaks directly to DAAD's own criteria (*persönliche Eignung*, societal engagement, Verantwortungsübernahme), because the FNF selects on precisely those. Give it a full line with the awarding body, the period and the nature of the support.
  - **e-fellows.net** is an online scholarship/career network with a much lower selection bar. It is worth **half a line at most**, and it is the first thing to cut if space is tight. Listing it with equal visual weight next to a Begabtenförderungswerk actively dilutes the FNF signal to a German committee that knows exactly what both are.
  - Note for the record: e-fellows.net is also a *source* used in this research (https://www.e-fellows.net/stipendien/daad-stipendium). Being a member of a network one cites is not a problem; over-weighting it in the CV is.

### 2.12 Extracurricular leadership — is quantification appropriate, or does it read as a recruiting CV?

This was flagged as a risk in the brief. The evidence says the risk is real but manageable, and that the underlying content is among the most valuable in the document.

- **A [RELAYED]** DAAD's own checklist names **außerfachliches Engagement** as required CV content. This is not optional colour — it is instructed content. — https://www2.daad.de/medien/ausland/dokumente/checkliste_bewerbungsunterlagen.pdf
- **A [RELAYED]** The selection criteria include extracurricular knowledge and abilities, **social engagement**, and the **ability to take responsibility**. — https://www.daad.de/de/in-deutschland-studieren/stipendien/hinweise-daad-stipendien/
- **C** DAAD-facing preparation guidance is explicit that the CV must be tabular, clearly structured and must take in extracurricular interests and activities, and that the committee wants to see the applicant engaging beyond the university and taking societal responsibility — good grades alone are not the criterion. — https://www.studieren-weltweit.de/tipps-auswahlgespraech-stipendium/ ; https://www.uni-bremen.de/fileadmin/user_upload/sites/international/Studieren_im_Ausland/Bewerbungshilfe_fuer_Studierende.pdf
- **Verdict (B): quantify — but quantify *responsibility*, not *achievement*.** The distinction is the whole answer:
  - **EUR 40,000 in club assets under management, monthly accounting, board meetings every three weeks** → this is *scope of entrusted responsibility*. A committee explicitly assessing Verantwortungsübernahme reads this exactly as intended. **Keep the number.**
  - **463 members** → this is *scale of the organisation in which an office is held*, which calibrates what "Zweiter Vorsitzender" means. A German reader cannot otherwise tell a 20-member from a 500-member club. **Keep the number.**
  - **700+ attendees at the Christmas theatre** → this is closest to a recruiting-CV impact metric and is the weakest of the three, because audience size is an event statistic rather than a responsibility. **Keep it only if it costs a fragment of a line**, folded into the events line; drop it first under space pressure.
  - **What would read as a recruiting CV:** three stacked achievement bullets per club, percentage growth figures, "increased X by Y%", or framing volunteer work in commercial-impact language. That is the failure mode to avoid — not the numbers themselves.
- **B** Format: **one line per office**, structured as *period | office | organisation | scope figure + 3–6 words of substance*. Three offices, three lines. This also silently demonstrates continuity and local rootedness, which is a distinct positive for a foundation funding a German citizen to study abroad and return.

### 2.13 Technical skills

- **DAAD SILENT.**
- **B** DAAD's criteria include extracurricular *knowledge and abilities* alongside academic qualification, so a compact skills block is legitimate. — https://www.daad.de/de/in-deutschland-studieren/stipendien/hinweise-daad-stipendien/
- **C** German convention: a short *"IT-Kenntnisse"* / *"Besondere Kenntnisse"* block near the end, after scholarships and languages. — https://www.e-fellows.net/bewerbung/lebenslauf/stipendien-und-auszeichnungen-im-lebenslauf ; https://www.mystipendium.de/bewerbung-stipendium/lebenslauf-stipendium
- **Recommendation (B): 2–3 lines maximum, grouped, no proficiency bars or star ratings.** Group by function (e.g. programming/data; analytics and ML tooling; business/ERP systems), not as an alphabet soup. For a Wirtschaftsinformatik applicant targeting an engineering-school MPhil this block is doing real work: it is the evidence that the quantitative claim in the motivation letter is true. But it is evidence, not a portfolio — a 12-item tool list reads as a job CV.
- **B** Rating scales ("Python ●●●●○") are a recruiting-CV device and do not belong in a document read by professors.

### 2.14 Hobbies

- **DAAD SILENT.** [SEARCH BUDGET EXHAUSTED — no dedicated search on hobbies in a DAAD CV.]
- **C** DAAD-facing guidance says the CV should take in "außerfachliche **Interessen** und Aktivitäten" — interests as well as activities — which is the closest thing to positive support found. — https://www.studieren-weltweit.de/tipps-auswahlgespraech-stipendium/
- **C** German tabular-CV convention includes a short *Interessen* line as optional and last. — https://www.mystipendium.de/bewerbung-stipendium/lebenslauf-stipendium
- **Recommendation (C): one short line, or omit.** For this applicant the honest position is that the *hobbies are already covered by the offices* — the fishing club, the sports club and the youth club are simultaneously the engagement section and the personality evidence. A separate "Interessen: Angeln, Fußball, Lesen" line directly beneath three offices in exactly those domains is redundant. Keep it only if it adds something genuinely different (e.g. a distinct intellectual or sporting interest), and never more than one line.

### 2.15 A profile / summary at the top?

- **DAAD SILENT.** [SEARCH BUDGET EXHAUSTED — no dedicated search.]
- **C** The *UK* CV genre opens with a personal profile. — https://uk.indeed.com/career-advice/cvs-cover-letters/date-of-birth-cv (and the UK-format guides in §9)
- **A [RELAYED]** The German DAAD genre is *tabellarisch* — a table, not prose. A summary paragraph is by definition not tabular. — https://www2.daad.de/medien/ausland/dokumente/checkliste_bewerbungsunterlagen.pdf
- **A [RELAYED]** DAAD already requires a **2-page Motivationsschreiben** stating academic and personal motives. A profile paragraph is a compressed, weaker duplicate of a document the committee is about to read anyway. — https://www2.daad.de/ausland/studieren/stipendium/de/70-stipendien-finden-und-bewerben/?detail=57503584
- **Recommendation (B): no profile/summary.** It is the clearest case in this report of a recruiting-CV import that is actively counterproductive: it costs 4–6 lines, it duplicates the motivation letter, and it breaks the genre DAAD named. If a compression device is wanted, use a *Schwerpunkte* sub-line inside the degree entry instead.

### 2.16 Should Abitur grades appear?

- **DAAD SILENT.** But **B**: the **Hochschulzugangsberechtigung is a separately required attachment**, so DAAD will see the Abitur certificate and its grade in full regardless of the CV. — §1.2
- **A [RELAYED]** *Lückenlos* means the school period must be **accounted for** — so the Abitur entry itself is not optional. — https://www2.daad.de/medien/ausland/dokumente/checkliste_bewerbungsunterlagen.pdf
- **C** German scholarship-CV guidance supports naming the grade in brackets where it is strong and relevant: e.g. *"Abitur JJJJ (Note: 2,3)"*. — https://stipendiumscoach.de/lebenslauf-stipendium/ ; https://www.wikway.de/wissen/bewerber/studium-ausbildung-und-schulabschluss-im-lebenslauf-richtig-darstellen
- **Recommendation (C): one line, at the bottom of the Education section, with the grade if it is strong; without the grade if it is not.** Never more than one line, no school subjects, no Leistungskurse, no school-era prizes unless genuinely exceptional. For a candidate whose Bachelor's degree is complete, the Abitur is a completeness item, not an argument.

### 2.17 Should specific university grades appear — and how should German grades be presented?

- **B** The **Abschlusszeugnis is a required separate attachment** and carries the authoritative grade record, so the CV grade is a *signal*, not the evidence. — §1.2
- **C** Naming the final grade in the CV is accepted German practice where it supports the application. — https://www.wikway.de/wissen/bewerber/studium-ausbildung-und-schulabschluss-im-lebenslauf-richtig-darstellen ; https://www.jobvector.de/lebenslauf-erstellen/vorlagen/akademischer-lebenslauf/
- **A [RELAYED]** Academic qualification is a named selection criterion, so a strong grade is decision-relevant content, not vanity. — https://www.daad.de/de/in-deutschland-studieren/stipendien/hinweise-daad-stipendien/
- **Recommendation (B): give the B.Sc. final grade, once, in the degree line.**
- **On presentation to the committee (B / D on the mechanics):** the audience here is **German** — professors who read 1,0–4,0 natively. [SEARCH BUDGET EXHAUSTED — no dedicated source on grade-conversion conventions for German scholarship CVs; the mechanics below are reasoned from the audience, classified **D**, and should be sanity-checked.]
  - **D** Write the German grade in the German form (e.g. "Abschlussnote 1,X"). Do **not** convert to a UK classification or a US GPA for the DAAD CV — conversion to a foreign scale for a German reader adds noise and invites the suspicion of flattering arithmetic.
  - **D** A **rank or percentile**, if the DHBW issues one (e.g. "Jahrgangsbester" / "unter den besten X %"), is worth more than the number itself and is the one addition that genuinely earns its space. Only claim it if the transcript or a separate document can substantiate it — the CV is read alongside the transcript, so an unsupported claim is checkable and costly.
  - **D** Do **not** list per-module grades, semester GPAs or a "relevant coursework with grades" block. That is a US-undergraduate device, it duplicates the transcript, and it looks like an applicant arguing with their own certificate.
  - **B** Conversely, the **Cambridge** CV and application *will* need the German grade contextualised (Cambridge's own entry-requirement machinery handles this). That is a different document — see §4 and §6.6.

### 2.18 Should the Bachelor's thesis have its own entry?

- **DAAD SILENT** on the CV specifically, **but B**: DAAD requires a Studienplan describing *"any research work planned as part of a master's thesis"*, so the committee is explicitly evaluating research trajectory. A prior thesis is the only completed evidence of research capability the applicant has. — https://www2.daad.de/ausland/studieren/stipendium/de/70-stipendien-finden-und-bewerben/?detail=57503584
- **C** Naming the thesis topic is standard in academic CVs, especially where the topic relates to the target. — https://www.jobvector.de/lebenslauf-erstellen/vorlagen/akademischer-lebenslauf/ ; https://essayhilfe.de/bachelorarbeit-im-lebenslauf/ ; https://schnellerzurstelle.de/thema-der-abschlussarbeit/
- **Recommendation (B): yes — as an indented sub-line under the B.Sc. entry, not as a standalone section.** Give the full title, the supervisor/institution if it adds weight, and the grade if strong. A standalone "Bachelor Thesis" section for a single thesis over-inflates it; a sub-line under the degree is the correct register and keeps the education block coherent.
- **B** The AI / claim-verification topic should be stated in its actual terms and **not** retro-fitted into manufacturing language. The committee can see a DHBW Wirtschaftsinformatik thesis on AI/claim verification and an MPhil in Industrial Systems and draw the AI-in-manufacturing line themselves — the *argument* for that line is the motivation letter's and the study plan's job, not the CV's. A CV that strains to make the thesis sound like it was always about Industry 4.0 invites the committee to check, and the thesis title is a checkable fact.

### 2.19 Publications and projects

- **A [RELAYED]** Publication lists are an explicit, separately-named attachment in DAAD's *research* lines (Postdoc, Kongressreisen: "K2 Lebenslauf … und Publikationsliste"), i.e. DAAD treats them as a distinct document where they matter. — https://www2.daad.de/ausland/studieren/stipendium/de/70-stipendien-finden-und-bewerben/?detail=57369745 ; https://www2.daad.de/medien/ausland/ausschreibungen/postdoc_checkliste_fuer_bewerbungsunterlagen.pdf
- **A [RELAYED]** No publication list is among the attachments for this Master-level programme, and **only listed attachments may be uploaded**. — §1.1, §1.2
- **C** For Master's-level scholarship applications a focused one-to-two-page academic résumé is the right genre; the full academic CV with a research/publications/teaching apparatus belongs to PhD and fellowship applications. — https://www.ucalgary.ca/live-uc-ucalgary-site/sites/default/files/teams/23/CV%20and%20Personal%20Statement%20for%20Scholarship%20Applications.pdf ; https://gradschool.cornell.edu/career-and-professional-development/pathways-to-success/prepare-for-your-career/take-action/resumes-and-cvs/ ; https://psychology.ucsd.edu/undergraduate-program/undergraduate-resources/graduate-career-resources/cv-resume-writing/index.html
- **Recommendation (B):**
  - If there are **real publications** (peer-reviewed paper, conference paper, preprint, published thesis): a short *"Publikationen"* section near the end, full citation, 1–3 items. Do not upload a separate publication list — it is not a listed attachment.
  - If there are **none**: create no such section. An empty or padded publications section on a Bachelor-level CV is worse than none.
  - **Projects** (hackathons, ML side projects, student consulting projects) belong **only** if they are substantial and topic-relevant; otherwise they are recruiting-CV filler. One line each, maximum two or three, and consider folding them into the degree entry as a *Schwerpunkte* sub-line rather than opening a section.

### 2.20 Language skills — how to present, and do test scores belong?

- **A [RELAYED]** A **Sprachnachweis is a separately required attachment.** The certificate — with its scores — is going to DAAD regardless of the CV. — §1.2
- **A [RELAYED]** DAAD explicitly counts language skills among what the committee evaluates. — https://www.daad.de/de/in-deutschland-studieren/stipendien/hinweise-daad-stipendien/
- **C** A dedicated *"Sprachkenntnisse"* section is standard German convention, placed after scholarships/engagement and before or beside IT skills. — https://www.mystipendium.de/bewerbung-stipendium/lebenslauf-stipendium ; https://www.e-fellows.net/bewerbung/lebenslauf/stipendien-und-auszeichnungen-im-lebenslauf
- **C** CEFR/GER levels (A1–C2) are the European standard descriptor, institutionalised by the Europass framework that DAAD itself co-administers. — https://europass.europa.eu/en/create-europass-cv ; https://eu.daad.de/infos-fuer-einzelpersonen/foerderung-fuer-studierende-und-graduierte/europass/de/46248-europass/
- **Recommendation (C):**
  - One line per language: *Deutsch (Muttersprache) · Englisch (C1/C2) · [weitere] (B1)*.
  - **Do include the decisive test score, once, in parentheses** — e.g. "Englisch — verhandlungssicher (IELTS 8.0, 2026)". Rationale (B): Cambridge imposes a hard language threshold, so the committee assessing whether this applicant can actually take up the place benefits from seeing the score at a glance; and the certificate is in the file anyway, so the CV line is a pointer, not a claim. **One score, one date. Not a table of sub-scores** — that is the Sprachnachweis's job.
  - **Never** use self-invented descriptors ("fluent-ish", "business fluent 90%") or bar graphics.
  - **B** State the score only if it already exists at the time of submission. If the test is not yet taken, write the planned test and date honestly, or omit — DAAD checks this against the required Sprachnachweis, and a mismatch is precisely the kind of inconsistency §1.6 warns about.

### 2.21 What belongs in a scholarship CV but NOT in a recruiting CV — and the reverse

**In the DAAD CV, not in a consulting/recruiting CV:**

| Item | Why | Class |
|---|---|---|
| Gapless coverage of every period, including school | DAAD explicitly requires *lückenlos* | A [RELAYED] — https://www2.daad.de/medien/ausland/dokumente/checkliste_bewerbungsunterlagen.pdf |
| Substantial extracurricular/voluntary offices with scope | Named selection criterion (*außerfachliches Engagement*, social engagement, Verantwortungsübernahme) | A [RELAYED] — https://www.daad.de/de/in-deutschland-studieren/stipendien/hinweise-daad-stipendien/ |
| Bachelor's thesis title | Evidence of research trajectory; committee evaluates the planned master's research | B — https://www2.daad.de/ausland/studieren/stipendium/de/70-stipendien-finden-und-bewerben/?detail=57503584 |
| Scholarships as a named section (esp. a Begabtenförderungswerk) | Third-party validation on exactly DAAD's own criteria | C — https://www.e-fellows.net/bewerbung/lebenslauf/stipendien-und-auszeichnungen-im-lebenslauf |
| Photo, date/place of birth, nationality | German-document convention; matches the portal form | C — https://www.mystipendium.de/bewerbung-stipendium/lebenslauf-stipendium |
| Abitur line | Completeness (*lückenlos*) | A [RELAYED] / C |
| Final grades | Academic qualification is a named criterion | B / C |

**In a consulting/recruiting CV, NOT in the DAAD CV:**

| Item | Why it fails here | Class |
|---|---|---|
| Profile/summary paragraph | Not tabular; duplicates the 2-page Motivationsschreiben | B — §2.15 |
| Achievement bullets with commercial impact (EUR/%/EBITDA) | Not a selection criterion; signals commercial rather than academic orientation | B — §2.9 |
| Three-to-four bullets per role | Crowds out the content DAAD actually asked for | B |
| Firm jargon, client names, project code names | Illegible and/or confidential to this audience | D |
| Skill rating bars / star ratings | Recruiting-CV device; not tabular-CV register | B — §2.13 |
| Long tool inventories | Evidence inflation | B |
| "References available on request" | Meaningless here — DAAD requires a named Gutachten from a university teacher | B — §1.2 |
| Design flourishes, colour blocks, two-column infographic layouts | Genre mismatch; *tabellarisch* means a table | A [RELAYED] / B |
| Target-role tailoring language ("seeking a position in…") | Wrong document type entirely | B |

### 2.22 How to present the DHBW dual programme — is it an asset to make explicit?

- **B** **Yes — make it explicit, and make it legible.** The DHBW model (alternating ~3-month theory and practice phases, a Dualer Partner company, admission via the company rather than the university) is *not* uniformly understood even by German professors, many of whom sit at classical universities and may read "Berufsakademie-adjacent" rather than "practice-integrated Bachelor with genuine industrial embedding". — https://www.karlsruhe.dhbw.de/mb/studienverlauf-organisatorisches.html ; https://www.dhbw.de/informationen/studieninteressierte ; https://www.dhbw.de/fileadmin/user_upload/Dokumente/Broschueren_Handbuch_Betriebe/DHBW_Leitlinien_Praxisphasen.pdf
- **C** The recommended CV mechanics for a dual degree: name the period, the degree and programme, the university, **the Dualer Partner**, and two to four relevant practice phases / projects / focus areas — and label practice phases **precisely as practice phases**, not as though they were full-time positions. — https://cvlotse.de/lebenslauf-duales-studium ; https://www.cvmaker.de/lebenslauf-vorlagen/duales-studium
- **B — why it is an asset for *this* application specifically:** the ISMM is an industrially-embedded, practice-oriented MPhil at the Institute for Manufacturing. A dual Bachelor with alternating industrial phases is the most natural possible antecedent for that, and it pre-empts the obvious committee question about a business-informatics graduate moving into industrial systems. This is a case where a single clarifying phrase converts a potential deficit into a fit argument.
- **Recommendation (B):** in the Education section, give the DHBW entry a one-clause gloss — *"duales Studium: dreimonatiger Wechsel von Theorie- und Praxisphasen; Dualer Partner: [Unternehmen]"* — and then list the practice phases **either** as sub-lines under the degree **or** as entries in the Professional Experience section. **Choose one and do not do both** — duplicating the phases in two sections is the commonest self-inflicted wound on a dual-study CV and instantly makes a 2-page CV feel padded. Recommended: practice phases as sub-lines under the degree (they are academically framed and stay adjacent to the gloss that explains them), with only genuinely separate employment (EY/EY-Parthenon, Singapore, BCG) in the Professional Experience section.
- **B** Do not over-explain. One clause. A committee that needs more will ask at interview — which, given the pre-selection-then-interview structure, is a good outcome, not a risk.

---

## 3. Style comparison table

| Dimension | **DAAD CV (Lebenslauf)** | **Academic CV** | **Consulting / recruiting CV** | **UK postgraduate application CV** |
|---|---|---|---|---|
| **Length** | Tabular, gapless, **max. 3 pages** (B [RELAYED]); 2 is the right target (C) | Unlimited in principle; min. 2 pages, often much longer (C) | 1 page (German/EU consulting), rigidly | ~2 pages (C); Cambridge sets no stated CV length, only PDF/<2 MB (A) |
| **Ordering** | DAAD SILENT; modern tabular convention = **reverse chronological** (C) | Reverse chronological within categorised sections (C) | Reverse chronological (C) | Reverse chronological (C) |
| **Photo** | DAAD silent here; German convention **yes**, discreet (C) — DAAD says "ohne Foto" explicitly where it means it (A) | Discipline/country dependent; typically none | German market: still common, declining (C) | **No** — Equality Act 2010 risk (C) |
| **Personal data** | DOB, place of birth, nationality — yes (C); also held in the portal form (B) | Minimal; contact + affiliation | German: DOB common; UK/US: none | **None** — no DOB, nationality or marital status (C) |
| **Bullet style** | Table rows; 1–2 short substantive lines per entry (B) | Categorised lists; citations, not bullets | 3–4 action-verb + quantified-result bullets | Short achievement bullets under a personal profile (C) |
| **Quantification** | Yes, but of **responsibility and scope** (EUR under management, membership size) — not commercial impact (B) | Rarely; quantification is in the publication/funding record | Central; the entire point | Moderate; "specific accomplishments over buzzwords" (C) |
| **Tone** | Sober, factual, complete, verifiable | Formal, discipline-conventional | Assertive, impact-forward, selective | Concise, evidence-forward, profile-led |
| **What leads** | Personal data block, then **Education** (degree + thesis) | Education, then research/publications | Most recent role and its impact | Personal profile, then key skills, then experience |
| **What is omitted** | Profile paragraph, impact bullets, skill bars, design flourishes, unlisted extra attachments (A/B) | Non-academic detail, hobbies, personal data | Gapless school history, voluntary offices, personal data | Photo, DOB, nationality, marital status, referee lines (C) |
| **Who reads it** | German professors + DAAD alumni, honorary committee, against named criteria (A) | Academic peers in the discipline | Recruiter / staffing partner, ~20 seconds | Departmental admissions assessors alongside a personal statement (A) |
| **Read alongside** | Motivationsschreiben (2 pp), Studienplan (5 pp), transcript, HZB, Sprachnachweis, Gutachten, **and the portal form** (A) | Research statement, publication list | Cover letter, grades sheet | Personal statement, transcripts, 2 references (A) |

Cambridge/UK cells sourced from https://www.postgraduate.study.cam.ac.uk/apply/how/supporting-documents ; https://www.postgraduate.study.cam.ac.uk/how-do-i-apply/supporting-documentation ; https://uk.indeed.com/career-advice/cvs-cover-letters/date-of-birth-cv

---

## 4. Verdict: which style should dominate, and why

**The German *tabellarischer Lebenslauf* dominates — specifically, a scholarship-weighted German tabular CV, reverse-chronological, two pages, with a light academic overlay (thesis, grades) and the consulting register stripped out.**

Four reasons, in descending strength:

1. **DAAD names the genre (A [RELAYED]).** The instruction is *tabellarisch*, *lückenlos*, *computergeschrieben*, with the degree programme named and *persönliche Eignung* and *außerfachliches Engagement* mentioned. That is a description of the German tabular Lebenslauf. Adopting a UK profile-led CV or a Europass form would be a deliberate departure from an explicit instruction, for no gain. — https://www2.daad.de/medien/ausland/dokumente/checkliste_bewerbungsunterlagen.pdf
2. **The reader is German and the criteria are German (A [RELAYED]).** Honorary committees of German university teachers, assessing academic qualification, project quality, extracurricular ability, social engagement, development potential and readiness to take responsibility. Every convention question (photo, DOB, nationality, grade notation) resolves toward German practice once the reader is identified. — https://www.daad.de/de/der-daad/wer-wir-sind/organisation/auswahlkommissionen/ ; https://www.daad.de/de/in-deutschland-studieren/stipendien/hinweise-daad-stipendien/
3. **The document is not a full academic CV, because the applicant is not a PhD applicant (C).** Master's-level scholarship applications take a focused one-to-two-page academic résumé; the research/publications/teaching apparatus of a true academic CV would be empty scaffolding here. The academic overlay is limited to: thesis as a sub-line, grades, and any genuine publications. — https://www.ucalgary.ca/live-uc-ucalgary-site/sites/default/files/teams/23/CV%20and%20Personal%20Statement%20for%20Scholarship%20Applications.pdf ; https://gradschool.cornell.edu/career-and-professional-development/pathways-to-success/prepare-for-your-career/take-action/resumes-and-cvs/
4. **The consulting CV is the specific risk to manage, not the model to follow (B).** It is the applicant's most practised format and will be the default muscle memory. Its three defining devices — the profile paragraph, the impact bullet, and ruthless one-page selection — are each wrong here: the first duplicates the motivation letter, the second optimises for a criterion DAAD does not use, and the third would delete the voluntary offices that DAAD explicitly asks for. What the consulting background *should* contribute is discipline — clean typography, no filler, consistent structure — not content style.

**One structural point that follows from the whole verdict:** this CV is read inside an eight-document file that already contains a transcript, a language certificate, a school certificate, a 5-page study plan and a 2-page motivation letter, *plus* a structured portal form with the same biographical data. The CV's comparative advantage is **weighting and legibility**, not completeness. Every design decision above — 2 pages not 3, one line per role, no profile, no module grades, no publication list — is the same decision applied repeatedly: let the other documents carry what they already carry, and use the CV to make the committee see, in one sweep, a strong academic record, real industrial exposure, and unusually substantial voluntary responsibility.

**And a separate deliverable, stated explicitly:** the **Cambridge** MPhil application requires its own CV via the Applicant Portal (A — https://www.postgraduate.study.cam.ac.uk/apply/how/supporting-documents). That one follows UK conventions: no photo, no DOB, no nationality, profile permitted, German grade contextualised. **Build two files from one content master.** Do not submit the DAAD version to Cambridge or vice versa.

---

## 5. RECOMMENDED SECTION ORDER

Two A4 pages. Reverse chronological within every section. Consistent date column on the left, content on the right (C — https://www.mygermanuniversity.com/de/articles/CV-for-DAAD-Scholarship-Application). No prose paragraphs.

---

### 1 — Header: Name and contact details (+ photo)

| | |
|---|---|
| **Why here** | Identification. The photo, if used, sits here because a German Lebenslauf places it top-right and nowhere else. |
| **Content** | Full name; postal address; phone; email; optionally LinkedIn/ORCID if genuinely maintained. Photo top-right, passport proportions. |
| **Detail** | 3–5 lines plus photo. Name in the largest type on the page; no logo, no banner, no colour block. |
| **Example types** | Name line; address line; contact line; professional photograph. |
| **Exclude** | Decorative headers; "Lebenslauf" as a giant title (a small heading or none is fine); social media that is not professional; an email address that is not sober. |

### 2 — Persönliche Daten

| | |
|---|---|
| **Why here** | German convention places it immediately after the header; it also silently mirrors the portal form, which holds the same data (B, §1.6). Placing it first gets the conventional-but-uninformative material out of the way in three lines so that Education can begin high on page 1. |
| **Content** | Date of birth; place of birth; nationality. |
| **Detail** | Three lines. Nothing else. |
| **Example types** | "Geburtsdatum / Geburtsort / Staatsangehörigkeit" as a three-row mini-table. |
| **Exclude** | Marital status, religion, parents' occupations, ID numbers, health information. These are German *old*-convention items with no upside and a privacy downside. **Omit this entire section from the Cambridge version.** |

### 3 — Akademische Ausbildung / Studium

| | |
|---|---|
| **Why here** | Academic qualification is a named DAAD selection criterion (A) and this is a scholarship for a degree. It must be the first substantive block the committee's eye lands on. Reverse-chronological order puts the completed B.Sc. and its thesis at the very top of the page — the strongest, most relevant fact in the document. |
| **Content** | B.Sc. entry: period; full degree and programme title (IMBIT / Wirtschaftsinformatik); DHBW Stuttgart; **the dual-study gloss** (§2.22); Dualer Partner; final grade (and rank, if substantiable); **thesis as an indented sub-line** with full title; optionally a *Schwerpunkte* sub-line; practice phases as sub-lines (if not placed in §5). Then any exchange/study-abroad period. Then the Abitur line at the bottom. |
| **Detail** | The richest section on the page — roughly 8–14 lines. This is where detail is *earned*. |
| **Example types** | Degree entry with institution and grade; one-clause dual-study explanation; thesis sub-line with title; focus-areas sub-line; practice-phase sub-lines; single-line Abitur entry with grade. |
| **Exclude** | Module lists; semester-by-semester grades; ECTS tallies; school subjects; Leistungskurse; primary/secondary schools before the Gymnasium; anything the Abschlusszeugnis and HZB already carry (§2.16, §2.17). |

### 4 — *(Optional)* Publikationen

| | |
|---|---|
| **Why here** | Directly after Education because it is academic output and belongs adjacent to the thesis it likely derives from. Only exists if there is real content. |
| **Content** | 1–3 full citations. |
| **Detail** | One line each. |
| **Example types** | Peer-reviewed paper; conference paper; preprint; published thesis. |
| **Exclude** | The entire section, if there are no genuine publications. Blog posts, internal client decks, seminar papers, course projects. Do **not** upload a separate publication list — not a listed attachment (A, §2.19). |

### 5 — Berufserfahrung / Praxiserfahrung

| | |
|---|---|
| **Why here** | Substantial and relevant, and it establishes industrial credibility for an ISMM application — but it is not a DAAD criterion, so it yields the top slot to Education. |
| **Content** | EY / EY-Parthenon roles; the Singapore placement (flag the location prominently — international experience is the programme's stated purpose); the planned BCG internship (see §6.5); any earlier employment needed for gaplessness. |
| **Detail** | Date | employer | role | location, then **1–2 topic-led lines** per entry. |
| **Example types** | Consulting role with a scope-and-sector line; international placement with location emphasised; internship. |
| **Exclude** | Impact/EUR/percentage bullets; client names; firm jargon; 3–4-bullet stacks; anything already listed as a DHBW practice phase in §3 (pick one location, §2.22). |

### 6 — Stipendien und Auszeichnungen

| | |
|---|---|
| **Why here** | German convention places scholarships and awards after professional experience and before the skills sections (C — e-fellows). It is also the ideal position rhetorically: the committee has just read the record, and now sees that other selective bodies reached the same conclusion. |
| **Content** | Friedrich-Naumann-Stiftung für die Freiheit (awarding body, period, nature of support) — **full line**. e-fellows.net — **half a line**, and the first cut under space pressure. Any academic prizes. |
| **Detail** | 2–3 lines total. Do not inflate. |
| **Example types** | Begabtenförderungswerk scholarship with period and purpose; career-network membership; academic prize. |
| **Exclude** | Presenting FNF and e-fellows with equal visual weight (§2.11); participation certificates; "shortlisted for" items; anything not actually awarded. |

### 7 — Ehrenamtliches Engagement

| | |
|---|---|
| **Why here** | DAAD *explicitly requires* extracurricular engagement in the CV (A) and names social engagement and readiness to take responsibility as criteria (A). It sits here — late but well above the skills blocks — because it must be unmissable on page 2 without displacing the academic record on page 1. A committee scanning for its own criteria will find it exactly where it looks. |
| **Content** | Three offices, one line each: Treasurer (Jugendclub Kirchen-Hausen e.V.); Second Chair (SG Kirchen-Hausen e.V.); Youth officer (fishing club). Each with the responsibility-scope figure (§2.12). |
| **Detail** | **One line per office.** Period | office | organisation | scope figure + 3–6 words of substance. Three lines total. |
| **Example types** | Treasurer line carrying the assets-under-management figure and the accounting cadence; vice-chair line carrying the membership figure and the events cadence; youth-officer line carrying the activity cadence and the educational content. |
| **Exclude** | Achievement bullets; growth percentages; commercial-impact framing; a paragraph per club; passive memberships with no office. |

### 8 — Sprachkenntnisse

| | |
|---|---|
| **Why here** | A named selection criterion (A) and a hard gate for Cambridge, so it must be visible — but it is a lookup fact, so it belongs in the compact back half. |
| **Content** | One line per language with a CEFR level; the decisive test score once, in parentheses, with its year. |
| **Detail** | 2–3 lines. |
| **Example types** | Native language line; English with CEFR level plus a single test score and date; a third language with CEFR level. |
| **Exclude** | Bar graphics; invented descriptors; sub-score tables (the Sprachnachweis carries those); scores for tests not yet taken (§2.20). |

### 9 — IT- und Methodenkenntnisse

| | |
|---|---|
| **Why here** | Substantiates the quantitative/technical claim underlying the ISMM fit, but it is supporting evidence, so it sits near the end. |
| **Content** | Grouped by function: programming/data; analytics and ML tooling; business/enterprise systems; methods. |
| **Detail** | **2–3 lines maximum**, grouped, comma-separated. |
| **Example types** | A programming/data-tooling group; an analytics/ML group; an enterprise-systems group. |
| **Exclude** | Rating bars or stars; 12-item tool inventories; MS Office as a listed skill; certifications that are not meaningful. |

### 10 — *(Optional)* Interessen

| | |
|---|---|
| **Why here** | Last, because it is the least decision-relevant content and the first thing to cut. |
| **Content** | One line, only if it adds something the three offices do not already show (§2.14). |
| **Detail** | One line or nothing. |
| **Example types** | A distinct intellectual, sporting or creative interest not already implied by the club offices. |
| **Exclude** | The section entirely, if it would merely restate the engagement section; "reading, travelling, sport"; anything unverifiable or attention-seeking. |

### 11 — Ort, Datum *(and signature if a signature is required)*

| | |
|---|---|
| **Why here** | German-document convention closes with place and date; it also dates the document, which matters because DAAD reads it against a form submitted the same week. |
| **Content** | Place, date. Signature **only if** the programme's attachment list asks for a signed CV (the EPOS line does; this line was not found to — A, §2.3). |
| **Detail** | One line. |
| **Example types** | "Ort, TT.MM.JJJJ". |
| **Exclude** | An image of a signature added "for effect" where none is required; a date that does not match the submission window. |

---

**Sections deliberately NOT in this order, and why:** *Profile/Summary* (duplicates the Motivationsschreiben, breaks *tabellarisch* — §2.15); *Key Skills* as a top block (UK device — §3); *References* (DAAD requires a named Gutachten — §2.21); *Certifications* as a standalone section (fold into §9); *Projects* as a standalone section (fold into §3 unless substantial — §2.19).

---

## 6. Applicant-specific calls

### 6.1 DHBW presentation

**B — Make the dual model explicit in one clause, and do not duplicate the practice phases.** Give the DHBW entry a gloss (alternating three-month theory/practice phases; named Dualer Partner) and list the practice phases as sub-lines under the degree, *not* also in Professional Experience. Label them as practice phases, not as though they were full-time positions. — §2.22 ; https://www.karlsruhe.dhbw.de/mb/studienverlauf-organisatorisches.html ; https://cvlotse.de/lebenslauf-duales-studium

**B — Treat it as a fit argument, not a caveat.** The ISMM sits in the Institute for Manufacturing and is industrially embedded; a practice-integrated Bachelor is a natural antecedent. Write the gloss neutrally and factually and let the committee draw the inference — do not editorialise ("uniquely combines theory and practice") in the CV. That sentence, if it is wanted anywhere, belongs to Agent 2's motivation letter.

### 6.2 Friedrich-Naumann-Stiftung placement

**C — Own section ("Stipendien und Auszeichnungen"), positioned after Professional Experience, before Languages/IT.** Full line: awarding body, period, nature of the support. — https://www.e-fellows.net/bewerbung/lebenslauf/stipendien-und-auszeichnungen-im-lebenslauf

**B — Do not bury it and do not equalise it with e-fellows.net.** A German committee recognises a Begabtenförderungswerk immediately and knows it implies a competitive, interview-based selection on criteria overlapping DAAD's own. e-fellows.net gets half a line and is the first cut. Listing both at equal weight costs the FNF signal for no gain. — §2.11

**D — One thing to be alert to, not to act on blindly:** a live scholarship from another funder can raise a double-funding question with DAAD. I found no DAAD source on this in the searches performed, and the search budget is exhausted. **Flag to Agent 1 / the eligibility workstream:** check DAAD's rules on parallel funding before deciding how the FNF support is *described* (past vs. ongoing). This affects wording, not placement.

### 6.3 The three club roles

**B — Keep all three, one line each, with the responsibility figures.** DAAD requires extracurricular engagement in the CV (A) and assesses Verantwortungsübernahme (A). Three offices held concurrently in three different organisations is genuinely strong evidence, and it is the part of this CV that most applicants cannot match.

**B — Quantify responsibility, not achievement.** Keep **EUR 40,000 under management** (scope of trust) and **463 members** (calibrates the office). Keep **700+ attendees** only as a fragment inside the events clause — it is the weakest of the three and the closest to a recruiting metric. Do not build achievement bullets around any of them. — §2.12

**B — Do not let the volume become three paragraphs.** The danger with this material is not that it looks like a recruiting CV; it is that it is genuinely interesting to write about and will swell. Three lines. The interview is where it expands — and the pre-selection-then-interview structure (A) means a CV line that provokes a question has done its job.

### 6.4 Singapore

**B — Make the location visually prominent on its own experience line.** The programme exists to fund international study experience (A — programme page), so an existing international placement is direct evidence that the applicant functions abroad. One line, location in the entry header, one topic line of substance. Do not create a separate "International Experience" section for a single placement.

### 6.5 The planned BCG internship

**B — This is a truthfulness call, and the conservative answer is right.** The CV is submitted in autumn 2026 and is read against a portal form the applicant certifies as complete (A, §1.1/§1.6).
- If the internship is **contractually agreed** with fixed dates by submission: list it with the dates and mark it clearly as forthcoming (e.g. *"ab MM/JJJJ (zugesagt)"*). This is honest and it is normal in German CVs.
- If it is **planned, hoped for, or in process**: **leave it out.** An unconfirmed future entry in a document whose defining requirement is *lückenlos* and whose committee will interview the applicant is a disproportionate risk for a marginal gain.
- **Never** present it without a forward-looking marker such that it reads as completed.

### 6.6 Grades

**B — Show the B.Sc. final grade once, in German notation, in the degree line.** The Abschlusszeugnis is a separate required attachment (A), so the CV grade is a signal, not the proof. — §2.17

**D — Add a rank or percentile only if substantiable.** If the DHBW issues one, it outperforms the raw number for a committee that sees hundreds of 1,x grades. Because the CV is read alongside the transcript, an unsupported rank claim is checkable and costly.

**C — Abitur: one line at the bottom of Education, grade in brackets if strong.** — https://stipendiumscoach.de/lebenslauf-stipendium/

**B — No module grades, no semester GPAs, no coursework-with-grades block.** Duplicates the transcript and reads as arguing with one's own certificate.

**B — For the Cambridge CV, this reverses.** There the German grade needs contextualising for a non-German reader, and the photo, DOB and nationality come out. Two files, one content master. — https://www.postgraduate.study.cam.ac.uk/apply/how/supporting-documents ; https://uk.indeed.com/career-advice/cvs-cover-letters/date-of-birth-cv

---

## 7. Common mistakes and what wastes space

| # | Mistake | Cost | Class / source |
|---|---|---|---|
| 1 | Submitting the consulting one-pager | Deletes the voluntary offices DAAD explicitly requires; optimises for the wrong criteria | B — §2.9, §2.12 |
| 2 | Profile/summary paragraph at the top | 4–6 lines; duplicates the 2-page Motivationsschreiben; breaks *tabellarisch* | B — §2.15 |
| 3 | Using Europass because "DAAD requires it" | False for this line; burns a page on template chrome; cannot be weighted | A [RELAYED] — §2.3 |
| 4 | Padding to 3 pages because 3 are allowed | Reads as inflation on a Bachelor-level record | B / C — §2.1 |
| 5 | Listing DHBW practice phases twice (Education *and* Experience) | The single commonest dual-study CV error; instantly makes the CV feel padded | B — §2.22 |
| 6 | Achievement bullets with EUR/% impact | Signals commercial rather than academic orientation to a professorial committee | B — §2.9 |
| 7 | Module lists / semester grades / ECTS tables | Duplicates the Abschlusszeugnis, a separate required attachment | B — §2.17 |
| 8 | Any unexplained gap | Violates the one thing DAAD explicitly polices (*lückenlos*) | A [RELAYED] — §1.4 |
| 9 | CV dates contradicting the portal form | The form and CV are read together; mismatch is a credibility hit | A [RELAYED] / B — §1.6 |
| 10 | Uploading extra attachments (publication list, certificates, portfolio) | Only listed attachments may be uploaded | A [RELAYED] — §1.1 |
| 11 | Non-PDF, or a scanned/encrypted file | Portal accepts PDF only | A [RELAYED] — §1.1 |
| 12 | Skill bars, star ratings, infographic two-column layouts | Genre mismatch; *tabellarisch* means a table | A [RELAYED] / B — §2.13 |
| 13 | Listing e-fellows.net at the same weight as the FNF | Dilutes the strongest validation in the document | B — §2.11 |
| 14 | Listing the BCG internship as if completed | Truthfulness risk in a document that leads to an interview | B — §6.5 |
| 15 | Language self-descriptors or sub-score tables | The Sprachnachweis is a separate attachment | C — §2.20 |
| 16 | Hobbies line that restates the club offices | Pure redundancy at the point where space is tightest | C — §2.14 |
| 17 | "Referenzen auf Anfrage" | Meaningless; DAAD requires a named academic Gutachten | B — §2.21 |
| 18 | Submitting the DAAD version (photo/DOB/nationality) to Cambridge | UK convention and Equality Act practice run the other way | C — §4, §6.6 |
| 19 | Incomplete submission / late submission | Not considered; completeness is the applicant's responsibility; submit days early | A [RELAYED] — §1.1, §1.7 |

---

## 8. Contradictions and unverified items

### 8.1 Methodological limitation affecting everything above

**`WebFetch` was blocked for every domain attempted**, so no source page was read directly; all content is search-engine-relayed and marked `[RELAYED]`. **Every A-classification must be re-verified by opening the URL before submission.** The `[RELAYED]` marker is the honest status of these claims, not a formality. See §0.1.

### 8.2 Genuine contradictions between sources

| # | Contradiction | Resolution |
|---|---|---|
| 1 | **Photo.** German/DAAD-facing advice says include (C); UK practice says never (C); DAAD itself says "bitte ohne Foto" in *other* programme lines (A) and is silent here. | Include for DAAD (German document, German reader, DAAD bans photos explicitly where it means to); omit for Cambridge. Two files. — §2.6 |
| 2 | **Ordering.** Traditional German convention (chronological ascending) vs. modern tabular/international (reverse). DAAD is silent. | Reverse chronological. Costs nothing on either side, puts the decision-relevant material first, and is the modern German tabular default. — §2.5 |
| 3 | **Europass.** Widely repeated as a DAAD requirement; true for EPOS, false for the Master study-scholarship lines. | Do not use Europass — **but re-check the live attachment list; an explicit A instruction would override.** — §2.3 |
| 4 | **Length.** DAAD's standard "max. 3 Seiten" vs. German scholarship convention "max. 2 pages". | Not truly contradictory: 3 is a ceiling, 2 is the right target for this record. — §2.1 |
| 5 | **Scholarship section placement.** e-fellows: after experience, before skills. jobvector: directly after education and experience when numerous. | Both put it after experience; with two items, after Professional Experience and before Languages. — §2.11 |

### 8.3 Unverified / low-confidence items — do not build on these without checking

1. **The "max. 3 Seiten" limit for *this specific programme*.** The wording was relayed in association with a cluster of DAAD database pages, and reported as explicitly applying to Studienstipendien-Master and ERP lines — but **I could not verify it on detail=57503584 itself.** Classified B, not A. **Check the programme page.**
2. **The full 2026/27 attachment list for "Master im Ausland"**, read off the programme page rather than assembled from relayed snippets plus e-fellows. **Check the portal.**
3. **The exact UK-region deadline** for the December-selection round. §1.7 reports three region-dependent dates; which applies to the UK was not established.
4. **"Even if the programme does not require a photo you must submit one anyway"** — single commercial source, no DAAD corroboration. Classified **D**. Do not rely on it. — https://www.mygermanuniversity.com/de/articles/CV-for-DAAD-Scholarship-Application
5. **Whether DAAD requires a signed CV on this line.** EPOS requires a hand-signed Europass CV (A); no signature requirement was found here. **Check the attachment list.**
6. **German grade-presentation mechanics** (§2.17) — reasoned from the audience, classified **D**; no dedicated source, search budget exhausted.
7. **Consulting-bullet translation** (§2.9) — reasoned from DAAD's stated criteria, classified **C/D**; no dedicated source.
8. **Hobbies** (§2.14) and **profile paragraphs** (§2.15) in a DAAD CV specifically — no dedicated search; conclusions rest on genre logic plus the *tabellarisch* instruction and the existence of the Motivationsschreiben.
9. **Parallel-funding rules** re: an active FNF scholarship (§6.2) — not researched. **Refer to the eligibility workstream.**
10. **Whether the ISMM/IfM course page imposes CV-specific requirements** beyond the university-wide "upload a CV" rule — `www.ifm.eng.cam.ac.uk` was blocked and the domain-limited search returned only university-level guidance. Relevant to the *Cambridge* CV, not the DAAD one.

---

## 9. Source appendix

All accessed **2026-09-17** via `WebSearch` (search-engine-relayed content; `WebFetch` blocked — see §0.1).

| # | Source | URL | Tier | Type | Supports | Class |
|---|---|---|---|---|---|---|
| 1 | DAAD — Stipendien für ein Masterstudium im Ausland (programme page) | https://www2.daad.de/ausland/studieren/stipendium/de/70-stipendien-finden-und-bewerben/?detail=57503584 | 1 | Official programme page | Document list, Studienplan 5 pp, Motivationsschreiben 2 pp, portal/Anlagen, completeness, pre-selection then interview, deadlines, eligibility | A |
| 2 | DAAD — Checkliste Bewerbungsunterlagen (PDF) | https://www2.daad.de/medien/ausland/dokumente/checkliste_bewerbungsunterlagen.pdf | 1 | Official checklist PDF | "computergeschrieben, lückenlos und tabellarisch"; degree programme named; persönliche Eignung; außerfachliches Engagement | A |
| 3 | DAAD — Bewerbung um ein DAAD-Stipendium | https://www.daad.de/de/im-ausland-studieren-forschen-lehren/stipendien-finanzierung/bewerbung/ | 1 | Official process page | Portal-only application; Anlagen; PDF only; only listed attachments; forms for application + Gutachten | A |
| 4 | Mein DAAD — Wie kann ich meine Bewerbung einreichen? | https://www.meindaad.de/de/help/wie-kann-ich-meine-bewerbung-einreichen-o/ | 1 | Official portal help | "Bewerbungszusammenfassung" PDF; form filled offline and re-uploaded; personal + project data in the form | A |
| 5 | Mein DAAD — Wie registriere ich mich für eine Bewerbung? | https://www.meindaad.de/de/help/wie-registriere-ich-mich-fuer-eine-bewerbung-a/ | 1 | Official portal help | Registration; programme pre-filled from database | A |
| 6 | Mein DAAD — Datenschutzhinweise Bewerbungsformular | https://www.meindaad.de/de/datenschutzhinweise-bewerbungsformular/ | 1 | Official privacy notice | Form collects personal data | B |
| 7 | DAAD — Wichtige Hinweise zu den DAAD-Stipendien | https://www.daad.de/de/in-deutschland-studieren/stipendien/hinweise-daad-stipendien/ | 1 | Official guidance | Selection criteria: academic qualification, project quality, non-academic criteria, social engagement, development potential, Verantwortungsübernahme | A |
| 8 | DAAD — Wichtige Hinweise zu DAAD-Stipendien (Ausland) | https://www.daad.de/de/im-ausland-studieren-forschen-lehren/stipendien-finanzierung/wichtige-hinweise-zu-daad-stipendien/ | 1 | Official guidance | Same criteria, outbound programmes | A |
| 9 | DAAD — Auswahlkommissionen | https://www.daad.de/de/der-daad/wer-wir-sind/organisation/auswahlkommissionen/ | 1 | Official organisational page | Honorary committees, mainly German university teachers | A |
| 10 | DAAD — Studienstipendien, Masterstudium für alle wiss. Fächer | https://www2.daad.de/deutschland/stipendium/datenbank/de/21148-stipendiendatenbank/?detail=50026200 | 1 | Official database entry | 3-page CV accepted; Europass NOT required on this line | A/B |
| 11 | DAAD — EPOS (Entwicklungsbezogene Postgraduiertenstudiengänge) | https://www2.daad.de/deutschland/stipendium/datenbank/de/21148-stipendiendatenbank/?detail=50076777 | 1 | Official database entry | Europass template **required** on this line; gapless CV | A |
| 12 | DAAD — EPOS FAQ (EN, PDF) | https://www2.daad.de/medien/deutschland/stipendien/formulare/epos_faq_en.pdf | 1 | Official FAQ PDF | Europass specimen form; hand-signed CV | A |
| 13 | DAAD — Kongressreisenprogramm | https://www2.daad.de/ausland/studieren/stipendium/de/70-stipendien-finden-und-bewerben/?detail=57369745 | 1 | Official programme page | "K2 Lebenslauf (bitte ohne Foto)" + Publikationsliste — proof DAAD states no-photo explicitly when it means it | A |
| 14 | DAAD — HAW.International: Kongressreisen | https://www2.daad.de/ausland/studieren/stipendium/de/70-stipendien-finden-und-bewerben/?detail=57479681 | 1 | Official programme page | CV without photo | A |
| 15 | DAAD — Checkliste Doktorandenstipendien (kurz, PDF) | https://www2.daad.de/medien/ausland/dokumente/checkliste_bewerbung_doktoranden_kurz_deutsche_de.pdf | 1 | Official checklist | "tabellarischer Lebenslauf inklusive außerfachlichem Engagement" | A |
| 16 | DAAD — Postdoc Checkliste (PDF) | https://www2.daad.de/medien/ausland/ausschreibungen/postdoc_checkliste_fuer_bewerbungsunterlagen.pdf | 1 | Official checklist | Gapless tabular CV + publication list as separate attachment | A |
| 17 | DAAD — Checkliste Programmlinie 1 (PDF) | https://static.daad.de/media/daad_de/pdfs_nicht_barrierefrei/im-ausland-studieren-forschen-lehren/checkliste_bewerbung_proglinie_1.pdf | 1 | Official checklist | Gapless tabular CV, German or English | A |
| 18 | DAAD — Portal-Bewerbung erstellen und verwalten (PDF) | https://static.daad.de/media/daad_de/pdfs_nicht_barrierefrei/im-ausland-studieren-forschen-lehren/daad_kr_portal-bewerbung_erstellen_und_verwalten.pdf | 1 | Official portal guide | Offline form fill; auto-generated grey fields; attachment upload | A/B |
| 19 | DAAD — Chancen.Digital (digital Master option) | https://www2.daad.de/ausland/studieren/stipendium/de/70-stipendien-finden-und-bewerben/?detail=57694370 | 1 | Official programme page | 6-page Studienplan variant (contrast case) | A |
| 20 | DAAD/NA Erasmus+ — Europass | https://eu.daad.de/infos-fuer-einzelpersonen/foerderung-fuer-studierende-und-graduierte/europass/de/46248-europass/ | 1 | Official (DAAD as National Agency) | DAAD's institutional Europass role — origin of the folk claim; CEFR framework | A |
| 21 | DAAD/NA — Der Europass | https://eu.daad.de/mit-erasmus-ins-ausland/foerderung-fuer-studierende-und-graduierte/der-europass/ | 1 | Official | Europass as career tool, not an application mandate | A |
| 22 | Europass — CV editor | https://europass.europa.eu/en/create-europass-cv | 1 | Official EU | CEFR levels; Europass template structure | C |
| 23 | Cambridge — Gather your supporting documents | https://www.postgraduate.study.cam.ac.uk/apply/how/supporting-documents | 1 | Official Cambridge | All applicants must upload a CV; PDF, <2 MB, unencrypted; transcripts; 2 referees | A |
| 24 | Cambridge — Supporting documentation | https://www.postgraduate.study.cam.ac.uk/how-do-i-apply/supporting-documentation | 1 | Official Cambridge | Personal statement scope; document requirements by course | A |
| 25 | Cambridge — Applying for postgraduate courses | https://www.postgraduate.study.cam.ac.uk/apply | 1 | Official Cambridge | Applicant Portal; documents ready before starting | A |
| 26 | Cambridge Dept. of Engineering — Applying | https://www.eng.cam.ac.uk/postgraduates/applying-for-postgraduate-study | 1 | Official Cambridge | Departmental application route | B |
| 27 | DAAD Polen — Lebenslauf und Motivationsschreiben (PDF, 10/2024) | https://www.daad.pl/files/2024/10/Prezentacja_CV_Motivation.pdf | 2 | DAAD office presentation | Uniform application design; motivation letter max 2 pp; CV/LOM tips | C |
| 28 | Uni Bremen — Allgemeine Bewerbungshilfe (PDF) | https://www.uni-bremen.de/fileadmin/user_upload/sites/international/Studieren_im_Ausland/Bewerbungshilfe_fuer_Studierende.pdf | 2 | University Int'l Office | CV conveys personality/goals; German CV 1–2 pp; tabular for DAAD | C |
| 29 | studieren weltweit (DAAD-operated) — Auswahlgespräch | https://www.studieren-weltweit.de/tipps-auswahlgespraech-stipendium/ | 2 | DAAD-operated portal | CV tabular, clearly structured, covering extracurricular interests and activities; committee 3–6 people; grades are not everything | C |
| 30 | studieren weltweit — Mit dem DAAD ins Ausland | https://www.studieren-weltweit.de/mit-dem-daad-ins-ausland-warum-die-bewerbung-sich-lohnt/ | 2 | DAAD-operated portal | Prepare 4–5 months ahead | C |
| 31 | FU Berlin — Die Bewerbung beim DAAD (PDF) | https://www.fu-berlin.de/studium/international/media/Hinweise_DAAD_Brosch__re_2014-15.pdf | 2 | University Int'l Office | DAAD application FAQ (note: dated 2014/15) | C/D |
| 32 | HS Aalen — DAAD-Stipendien: Wie bewerbe ich mich richtig? (PDF) | https://www.hs-aalen.de/uploads/mediapool/media/file/1972/2660_1_DAAD_Informationsdokument_Wie_bewerben.pdf | 2 | University guidance | DAAD application walkthrough | C |
| 33 | Uni Hannover IPW — DAAD-Stipendium Masterstudiengänge im Ausland (PDF) | https://www.ipw.uni-hannover.de/fileadmin/ipw/AB5_Dateien/Departmental_International_Office_-_DIO/DAAD_Bewerbungsprozess.pdf | 2 | Departmental Int'l Office | Programme-specific process and tips | C |
| 34 | gostralia/gomerica — DAAD Bewerbungsleitfaden (PDF) | https://gostralia-gomerica.de/fileadmin/user_upload/gostralia-gozealand/Bewerbungsdokumente/DAAD_Bewerbungsleitfaden.pdf | 2/3 | Reproduced DAAD guide | "Deine Chance DAAD — Wie bewerbe ich mich richtig?"; CV tabular/clearly structured, gapless, includes extracurricular activities | C |
| 35 | Uni Freiburg — PROMOS Checkliste Praktika | https://www.international.uni-freiburg.de/de/promos/files/checkliste-praktika | 2 | University Int'l Office | Gapless tabular CV requirement | C |
| 36 | e-fellows.net — Stipendien und Auszeichnungen im Lebenslauf | https://www.e-fellows.net/bewerbung/lebenslauf/stipendien-und-auszeichnungen-im-lebenslauf | 3 | Scholarship/career portal | Own section; after experience, before skills; combine if <5; name body, date, purpose | C |
| 37 | e-fellows.net — Wie gebe ich ein Stipendium im Lebenslauf an? | https://www.e-fellows.net/stipendien/wie-gebe-ich-ein-stipendium-im-lebenslauf-an | 3 | Scholarship portal | Awarding organisation, exact designation, date, purpose | C |
| 38 | e-fellows.net — DAAD-Stipendium: Tipps für deine Bewerbung | https://www.e-fellows.net/stipendien/daad-stipendium | 3 | Scholarship portal | Document list incl. tabular CV, Studienplan, Motivationsschreiben, Gutachten | C |
| 39 | e-fellows.net — Welche Unterlagen für welches Stipendium? | https://www.e-fellows.net/stipendien/unterlagen-bewerbung-stipendium | 3 | Scholarship portal | Document sets across scholarship types | C |
| 40 | mygermanuniversity — CV for a DAAD Scholarship (DE) | https://www.mygermanuniversity.com/de/articles/CV-for-DAAD-Scholarship-Application | 3 | Commercial guide | Tabular, dates left/content right, reverse chronological; photo advice; Europass only where asked | C (photo-mandatory claim = **D**) |
| 41 | mygermanuniversity — CV for a DAAD Scholarship (EN) | https://www.mygermanuniversity.com/articles/CV-for-DAAD-Scholarship-Application | 3 | Commercial guide | "If DAAD does not ask for Europass, do not use it"; EPOS vs Master lines | C |
| 42 | mygermanuniversity — CV for German Universities | https://www.mygermanuniversity.com/articles/CV-for-German-Universities | 3 | Commercial guide | German CV conventions, photo | C |
| 43 | stipendiumscoach.de — Der Lebenslauf fürs Stipendium | https://stipendiumscoach.de/lebenslauf-stipendium/ | 3 | Scholarship advisory | Tabular = antichronologisch, max 2 pp; narrative = chronological; Abitur grade in brackets | C |
| 44 | myStipendium — Lebenslauf für die Stipendienbewerbung | https://www.mystipendium.de/bewerbung-stipendium/lebenslauf-stipendium | 3 | Scholarship portal | Tabular CV structure; personal data block; sections | C |
| 45 | cvlotse.de — Lebenslauf Stipendium | https://cvlotse.de/ratgeber/lebenslauf-stipendium | 3 | CV advisory | Tabular vs narrative forms | C |
| 46 | cvlotse.de — Lebenslauf mit oder ohne Foto | https://cvlotse.de/ratgeber/lebenslauf-mit-oder-ohne-foto | 3 | CV advisory | Photo optional in modern German practice | C |
| 47 | bewerbung.net — Lebenslauf Foto: Ja oder Nein? | https://bewerbung.net/lebenslauf-foto | 3 | CV advisory | German photo trend | C |
| 48 | workwise.io — Bewerbung mit oder ohne Foto | https://www.workwise.io/karriereguide/bewerbung/bewerbungsfoto-ja-nein | 3 | Career portal | German photo trend | C |
| 49 | zety.de — Ausformulierter Lebenslauf | https://zety.de/blog/ausformulierter-lebenslauf | 3 | CV advisory | Narrative CV is chronological; tabular is reverse | C |
| 50 | Indeed DE — Antichronologischer Lebenslauf | https://de.indeed.com/karriere-guide/bewerbung/antichronologischer-lebenslauf | 3 | Career portal | Reverse-chronological as German default | C |
| 51 | lebenslaufmuster.de — Tabellarischer Lebenslauf | https://www.lebenslaufmuster.de/tabellarischer-lebenslauf/ | 3 | CV templates | Tabular structure incl. personal data block | C |
| 52 | Indeed UK — Date of Birth on Your CV | https://uk.indeed.com/career-advice/cvs-cover-letters/date-of-birth-cv | 3 | Career portal | UK: no photo, no DOB, no marital status; Equality Act 2010 | C |
| 53 | jobvector — Akademischer Lebenslauf | https://www.jobvector.de/lebenslauf-erstellen/vorlagen/akademischer-lebenslauf/ | 3 | Academic CV guide | Thesis topic and focus areas standard; awards/scholarships after education and experience when numerous | C |
| 54 | WIKWAY — Studium/Schulabschluss im Lebenslauf | https://www.wikway.de/wissen/bewerber/studium-ausbildung-und-schulabschluss-im-lebenslauf-richtig-darstellen | 3 | CV advisory | Final grade where it supports the application | C |
| 55 | essayhilfe.de — Bachelorarbeit im Lebenslauf | https://essayhilfe.de/bachelorarbeit-im-lebenslauf/ | 3 | Advisory | Thesis topic customary in academic CVs | C/D |
| 56 | schnellerzurstelle.de — Thema der Abschlussarbeit nennen | https://schnellerzurstelle.de/thema-der-abschlussarbeit/ | 3 | Advisory | Naming the thesis where topic-relevant | C/D |
| 57 | UCalgary — CV and Personal Statements for Scholarship Applications (PDF) | https://www.ucalgary.ca/live-uc-ucalgary-site/sites/default/files/teams/23/CV%20and%20Personal%20Statement%20for%20Scholarship%20Applications.pdf | 2 | University careers guidance | Scholarship CV conventions; academic vs professional | C |
| 58 | Cornell Graduate School — Resumes and CVs | https://gradschool.cornell.edu/career-and-professional-development/pathways-to-success/prepare-for-your-career/take-action/resumes-and-cvs/ | 2 | University careers guidance | CV unlimited/academic vs résumé 1–2 pp | C |
| 59 | UC San Diego Psychology — Academic CV and Professional Resume Writing | https://psychology.ucsd.edu/undergraduate-program/undergraduate-resources/graduate-career-resources/cv-resume-writing/index.html | 2 | University careers guidance | CV vs résumé distinction | C |
| 60 | seachscholarship.com — Build a Scholarship CV | https://seachscholarship.com/how-to-build-a-scholarship-cv-academic-resume/ | 3 | Scholarship advisory | 1–2 pp for Bachelor/Master scholarships; longer CV for PhD | C |
| 61 | DHBW Karlsruhe — Studienverlauf & Organisatorisches | https://www.karlsruhe.dhbw.de/mb/studienverlauf-organisatorisches.html | 1 | Official DHBW | Three-month alternation of theory and practice phases | A |
| 62 | DHBW — Studieninteressierte | https://www.dhbw.de/informationen/studieninteressierte | 1 | Official DHBW | Application via the Dualer Partner, not the university | A |
| 63 | DHBW — Leitlinien Praxisphasen (PDF) | https://www.dhbw.de/fileadmin/user_upload/Dokumente/Broschueren_Handbuch_Betriebe/DHBW_Leitlinien_Praxisphasen.pdf | 1 | Official DHBW | Theory/practice integration model | A |
| 64 | cvlotse.de — Lebenslauf duales Studium | https://cvlotse.de/lebenslauf-duales-studium | 3 | CV advisory | Name period, programme, university, Dualer Partner, 2–4 practice phases; label as practice phase, not a full-time post | C |
| 65 | cvmaker.de — Lebenslauf duales Studium | https://www.cvmaker.de/lebenslauf-vorlagen/duales-studium | 3 | CV templates | Dual-study CV entry structure | C |
| 66 | DAAD — Abschlussbericht "Determinanten der Auswahl" (PDF) | https://www2.daad.de/medien/der-daad/medien-publikationen/publikationen-pdfs/studie_determinanten_der_auswahl.pdf | 1 | Official DAAD study | Empirical study of DAAD selection determinants — **not read (fetch blocked); flagged as a high-value follow-up** | — |

**Highest-value unread source:** #66, DAAD's own study on the determinants of selection. It was surfaced by search but could not be opened. If any single document would upgrade the B-classifications in §2.9, §2.12 and §5 to evidence-backed A/B, it is this one. **Recommend it to whichever agent still has fetch capability or to the user directly.**
