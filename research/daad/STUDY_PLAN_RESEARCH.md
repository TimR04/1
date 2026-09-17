# Study Plan / Studienplan Research

**Agent:** 3 — Study Plan / Studienplan Research
**Date of research:** 2026-09-17
**Target:** DAAD "Stipendien für ein Masterstudium im Ausland" → MPhil ISMM, University of Cambridge (IfM), start October 2027

---

## ⚠️ TOOL CONSTRAINT — READ FIRST (affects confidence of everything below)

Two hard environment limits shaped this research and MUST be understood before the findings are used:

1. **`WebFetch` was blocked for every domain tried.** The egress proxy returned `EGRESS_BLOCKED` for `www.daad.de`, `www2.daad.de`, `static.daad.de`, `www.ifm.eng.cam.ac.uk`, `www2.ifm.eng.cam.ac.uk`, `www.postgraduate.study.cam.ac.uk`, `www.ipw.uni-hannover.de` and even `en.wikipedia.org`. A direct `curl` to `https://www.ifm.eng.cam.ac.uk/education/ismm/` returned `CONNECT tunnel failed, response 403`. **I could not open a single primary page directly.**
2. **The session-wide `WebSearch` budget (200 calls, shared across all 9 agents) was exhausted** partway through Half B.

Consequence: **all quotations below are reconstructed from WebSearch result summaries, which paraphrase and occasionally re-order source text.** They are substantively reliable (the same wording recurred across independent queries) but they are **NOT character-exact verbatim quotes**. Everywhere I mark a quote, I mark it as *search-summary reconstruction*, not as a transcribed quotation.

**Mandatory next step before drafting:** a human (or an agent with working WebFetch) must open the three pages listed in §9.1 and transcribe the German wording exactly. Do not paste any "quote" from this file into an application document.

---

## 0. Research log

| # | Query (language) | Purpose | Yield |
|---|---|---|---|
| 1 | `DAAD Studienplan Zeitplan Stipendium Masterstudium Ausland Bewerbung` (DE) | Locate programme page | Programme page 57503584; "max. 5 Seiten"; upload slot = "Zeitplan" |
| 2 | `DAAD "Studienplan" Merkblatt Stipendium Masterstudium im Ausland Unterlagen` (DE) | Document list | Full document list; confirmation of 5-page / 2-page split |
| 3 | `"Studienplan" DAAD "max. 5 Seiten" "detaillierte Beschreibung des Studienvorhabens" Forschungsvorhaben Masterarbeit` (DE) | Exact wording | **Core wording found**; plus "briefly describe content of courses/modules + credit points"; plus "understandable to non-specialists" |
| 4 | `DAAD Portal Zeitplan hochladen Studienplan Bewerbung Hinweise Was gehört hinein` (DE) | Portal mechanics | Studienplan uploaded under "Zeitplan"; Motivationsschreiben must stay a **separate** document |
| 5 | `DAAD "Ein Studienplan soll das angestrebte akademische Ziel..." Credit Points` (DE) | Pin the canonical sentence | Confirmed sentence; **"Die Kursübersicht kann auch in tabellarischer Form erstellt werden"** |
| 6 | `DAAD Bewerbung Stipendium "Studienplan" "Forschungsvorhaben" fachfremde Auswahlkommission` (DE) | Committee composition | Committees are lay-academic, mixed-discipline, appointed by DAAD board; criteria incl. "Durchführbarkeit und Konsistenz des Arbeits- und Zeitplans" |
| 7 | `"Wichtige Hinweise zu DAAD-Stipendien" Studienplan Kursübersicht tabellarischer Form` (DE, domain-restricted to daad.de) | Confirm Tier 1 attribution | Confirmed the guidance sits on the official `daad.de` "Wichtige Hinweise" page |
| 8 | `DAAD Auswahlkriterien Stipendium Masterstudium Ausland fachliche Qualifikation Motivation Studienvorhaben` (DE) | Selection criteria | "Qualifikation der Bewerbenden, Qualität des Studien- bzw. Forschungsvorhabens, Potenzial" |
| 9 | `DAAD Auswahlkriterien Motivation Qualifikation Vorbereitung "Durchführbarkeit des Studienvorhabens"` (DE) | Criteria decomposition | Three-block structure Motivation / Qualifikation / Vorbereitung confirmed |
| 10 | `DAAD scholarship study plan example master abroad what to include structure tips` (EN) | English-language guidance | Mostly returned the **inbound** programme — flagged as a confusion trap (§9.3) |
| 11 | `DAAD Stipendium Master im Ausland Erfahrungsbericht Studienplan Aufbau` (DE) | Alumni accounts | Confirms Studienplan + Motivationsschreiben are decisive; funding figures |
| 12 | `"Studienplan" DAAD Auslandsstudium Gliederung Vorlage Muster Beispiel Akademisches Auslandsamt PDF` (DE) | University-office templates | **Best structural guidance found**: tabular course overview across all semesters, per-course justification, host-choice justification, integration into overall degree |
| 13 | `gostralia "DAAD Bewerbungsleitfaden" Studienplan Kurse tabellarisch` (DE) | Corroborate #12 | Independent corroboration of the tabular-overview advice |
| 14 | `FU Berlin "Die Bewerbung beim DAAD" Studienplan Länge Sprache` (DE) | Language question | Inconclusive on this page |
| 15 | `DAAD Bewerbung Unterlagen Sprache deutsch oder englisch Motivationsschreiben Studienplan` (DE) | Language question | **Resolved**: German *or* English; mixed languages across documents explicitly permitted |
| 16 | `DAAD Portal Bewerbung ... "Zeitplan" Feld Pflichtdokument` (DE) | Portal slot | Confirms "Zeitplan" slot also accepts a Learning Agreement |
| 17 | `DAAD "Master im Ausland" 2027 Bewerbungsfrist Programmausschreibung Unterlagen` (DE) | Cycle timing | Deadlines 16 Sep – 1 Dec 2026; **Western Europe 25 Sep 2026**; selection March, start Sept 2027 |
| 18 | `MPhil Industrial Systems Manufacture and Management ISMM Cambridge ... structure modules` (EN, domain-restricted to cam.ac.uk) | ISMM skeleton | Duration, calendar, M0+5 core+1 elective, 4 projects, study tour, 18-week dissertation |
| 19 | `Cambridge ISMM ... taught modules industrial projects dissertation` (EN) | ISMM detail | 'learn it / see it / do it'; in-company projects; study tour rationale |
| 20 | `IfM Cambridge ISMM taught modules M0 M1 ... elective` (EN, domain-restricted) | Module names | Confirmed M0 + 5 core + 1 elective; names not exposed by codes |
| 21 | `ISMM Cambridge modules "Data and Modelling" "Manufacturing Processes" "Operations and Supply Chain" "New Business Development"` (EN) | **Verify the four strands** | **All four verified as real modules with content descriptions** |
| 22 | `IfM ISMM taught modules "Industrial Systems" module ... elective options list` (EN, domain-restricted) | Fifth core module | "Industrial Systems" module confirmed; elective list not exposed |
| 23 | `"ifm.eng.cam.ac.uk" ISMM "taught modules" induction ... elective sustainability digital` (EN) | Elective list | Not exposed; confirmed value-chain scope incl. industrial sustainability |
| 24 | `Cambridge ISMM "M1"..."M5" module titles` (EN) | Code→name mapping | **Failed** — mapping not publicly indexed |
| 25 | `IfM ISMM assessment and feedback coursework dissertation weighting` (EN, domain-restricted) | Assessment | **Full assessment structure obtained**, incl. ≤15,000-word dissertation and 'big issue' essay |
| 26 | `Cambridge ISMM industrial projects four projects eight weeks ... 18 weeks` (EN) | Project mechanics | 4 projects × 2 weeks, students usually in **pairs**; 2-week overseas tour |
| 27–28 | ISMM projects page / dissertation supervision | Project supply & supervision | **BUDGET EXHAUSTED — not executed.** See §9.2 |

**Not researched due to budget exhaustion:** IfM research-group names and named academics, elective module list, ISMM project-sourcing mechanics, dissertation supervisor allocation, current 2026-27/2027-28 fee and cohort data, DAAD country-specific UK page. These are listed as open items in §9.2.

---

## 1. What DAAD officially requires of the Studienplan

### 1.1 The programme call (Tier 1 — `www2.daad.de` programme 57503584)

*Search-summary reconstruction of the German wording:*

> **„Studienplan (max. 5 Seiten): detaillierte Beschreibung des Studienvorhabens sowie ggf. der im Rahmen einer Masterarbeit vorgesehenen Forschungsarbeit. Bitte laden Sie den Studienplan im Portal unter ‚Zeitplan' hoch."**

Four operative facts, each **Classification A**:

| Fact | Classification |
|---|---|
| Maximum **5 pages** | **A** |
| It is a **„detaillierte Beschreibung des Studienvorhabens"** — a *description of the study project*, not a bare calendar | **A** |
| It must ALSO cover **„ggf. der im Rahmen einer Masterarbeit vorgesehenen Forschungsarbeit"** — the research work planned within the Master's thesis, *where applicable* | **A** |
| It is uploaded in the DAAD portal under the field label **„Zeitplan"** | **A** |

The field label / document name mismatch ("Zeitplan" slot, "Studienplan" document) is a **portal artefact, not a content instruction**. DAAD explicitly tells applicants to upload the *Studienplan* there. The same slot also accepts a Learning Agreement. **(A)**

### 1.2 The cross-programme guidance (Tier 1 — `daad.de` „Wichtige Hinweise zu DAAD-Stipendien")

This is the single most content-bearing official passage found. *Search-summary reconstruction:*

> **„Ein Studienplan soll das angestrebte akademische Ziel des Auslandsaufenthalts beschreiben und die geplanten Lehrveranstaltungen an der Gasthochschule aufführen. Beschreiben Sie kurz die Inhalte der voraussichtlichen Kurse bzw. Module und machen Sie Angaben dazu, wie viele Credit Points dafür vergeben werden. Die Kursübersicht kann auch in tabellarischer Form erstellt werden. Stellen Sie außerdem dar, wie sich Ihr Vorhaben im Ausland in Ihren bisherigen und zukünftigen Studienverlauf einfügt, und begründen Sie kurz Ihre Wahl."**

Decomposed into six explicit obligations — **all Classification A**:

| # | Obligation (official) | Verb DAAD uses |
|---|---|---|
| A1 | Describe the **intended academic goal** of the stay abroad | *beschreiben* |
| A2 | **List the planned courses** at the host institution | *aufführen* |
| A3 | **Briefly describe the content** of those courses/modules | *kurz beschreiben* |
| A4 | State **how many credit points** each carries | *Angaben machen* |
| A5 | **Show how the project fits** into your previous **and future** course of study | *darstellen* |
| A6 | **Briefly justify your choice** | *kurz begründen* |
| A7 | The course overview **may be presented in tabular form** (permission, not obligation) | *kann* |

### 1.3 Audience instruction (Tier 1/Tier 2)

> *„Formulieren Sie den Studienplan bzw. das Forschungsvorhaben so, dass sich auch fachfremde Auswahlkommissionsmitglieder ein ausreichendes Bild machen können."*

DAAD's own description of the committees: *„Die Auswahlkommissionen setzen sich nach fachlichen und regionalen Gesichtspunkten zusammen. Die ehrenamtlichen Kommissionsmitglieder werden vom Vorstand des DAAD berufen und sind in erster Linie Hochschullehrende deutscher Hochschulen."* **(A)**

**Operational consequence:** the reader is a German professor who is an academic but probably *not* a manufacturing engineer. Jargon like "digital twin", "OEE", "MES/ERP integration", "asset administration shell" must be glossed on first use. **(B — strong inference from A)**

### 1.4 Selection criteria the Studienplan is scored against (Tier 1 + Tier 2)

DAAD states the commissions assess **(a) the applicant's academic qualification, (b) the quality of the study or research project, (c) the applicant's potential**. **(A)**

The three-block decomposition recurring across DAAD and university-office material:

| Block | Sub-criteria (reconstructed) | Which document carries it |
|---|---|---|
| **Motivation** | Begründung des Auslandsstudiums; Wahl der Gastinstitution; sinnvolle Einbindung in den Studienverlauf; fachlicher Nutzen; Notwendigkeit des Auslandsaufenthalts | Motivationsschreiben **+ Studienplan** |
| **Qualifikation** | Studienleistungen; Notenentwicklung; **Qualität des wissenschaftlichen Vorhabens**; Sprachkenntnisse; ggf. Praktika/Berufserfahrung | CV, transcripts, **Studienplan** |
| **Vorbereitung** | **Durchführbarkeit des Studienvorhabens**; Stand der fachlichen, methodischen und sprachlichen Vorbereitung; Kontakte zur Institution; Kenntnis der Lehr- und Forschungsmöglichkeiten; **Angemessenheit des gewählten Zeitpunkts** | **Studienplan (primarily)** |

Also recurring in DAAD criteria language: **„Durchführbarkeit und Konsistenz des Arbeits- und Zeitplans"** — feasibility *and internal consistency* of the work and time plan. **(A)**

**This is the decisive analytical finding of Half A:** the "Vorbereitung" block is scored almost entirely from the Studienplan, and its sub-criteria are *Durchführbarkeit*, *Kenntnis der Lehr- und Forschungsmöglichkeiten* and *Angemessenheit des Zeitpunkts*. The document must therefore *prove knowledge of the host institution's actual teaching and research offer* and *prove the plan can be executed in the time available*. **(B)**

### 1.5 Explicit separation from the Motivationsschreiben (Tier 1)

- Motivationsschreiben: **max. 2 Seiten**, *„begründen Sie persönlich kurz und prägnant … weshalb Sie Ihr Vorhaben an der gewählten Gastinstitution realisieren möchten. Gehen Sie darauf ein, warum das Vorhaben für Sie in fachlicher und persönlicher Hinsicht wichtig ist und weshalb es an der gewünschten Institution durchgeführt werden soll."* **(A)**
- It **must be uploaded as its own document** and must not be merged with the Studienplan. **(A)**

### 1.6 Language (Tier 1)

*„Wenn in der Stipendienausschreibung nicht anders angegeben, können Sie Ihre Bewerbung entweder auf Deutsch oder Englisch einreichen."* Documents may be submitted as PDFs in German **or** English, and **different documents may be in different languages** (explicit DAAD example: CV in German, motivation letter in English). **(A)**

---

## 2. Genre question: schedule vs proposal vs rationale vs research plan — verdict and evidence

### Verdict

> **The DAAD Studienplan is a COURSE-SELECTION-AND-RATIONALE DOCUMENT, organised chronologically, with a research-proposal component grafted on for the Master's thesis. It is NOT primarily a Zeitplan, and it is NOT primarily a research proposal.**
>
> Weighting for this application: **~55 % course selection + per-course rationale, ~20 % chronological structure, ~20 % thesis/research proposal, ~5 % goal statement.** **(B)**

### Evidence chain

| Candidate genre | Verdict | Evidence |
|---|---|---|
| **Chronological schedule ("Zeitplan")** | **Structural device, not the genre.** | The word "Zeitplan" appears only as a **portal upload-field label** (A, §1.1). DAAD's own content instruction (§1.2) contains *no* instruction to give dates. But "Durchführbarkeit **und Konsistenz des Arbeits- und Zeitplans**" and "Angemessenheit des gewählten Zeitpunkts" are scored criteria (A, §1.4) — so a timeline must be *visible*, just not dominant. |
| **Course-selection document** | **Yes — this is the spine.** | Three of DAAD's six obligations are course-level: *aufführen* (list), *kurz beschreiben* (describe content), *Credit Points angeben* (state credits). A7 explicitly permits a **course table**. University offices independently converge on "tabellarische Übersicht aller Kurse für alle Semester + Begründung je Kurs" (C, corroborated by ≥2 independent Tier-2 sources). |
| **Rationale for the programme** | **Yes — co-equal with course selection.** | A5 (*Einfügung in bisherigen und zukünftigen Studienverlauf*) + A6 (*Wahl begründen*) are explicit. "Sinnvolle Einbindung in den Studienverlauf" is a named Motivation sub-criterion. |
| **Academic / research proposal** | **Yes, but as one bounded component.** | Explicit in the call: *„sowie ggf. der im Rahmen einer Masterarbeit vorgesehenen Forschungsarbeit"* (A). The "ggf." (where applicable) matters: it is conditional. For ISMM, where an **18-week, ≤15,000-word research dissertation** is a compulsory, named, timetabled component (see §4), the condition is **unambiguously triggered** — omitting it would be a scored failure under "Qualität des wissenschaftlichen Vorhabens". **(B)** |
| **Pure research proposal** | **No.** | That is the genre of the *Forschungsstipendien* programmes (separate DAAD calls), where "Qualität des Forschungsvorhabens (Originalität, Aktualität, Relevanz)" is the headline criterion. In the Master-abroad call, the research element is subordinate ("ggf.", "im Rahmen einer Masterarbeit"). Importing research-grant conventions wholesale would misfit the genre. **(B)** |

### The one-sentence test for every paragraph drafted

> *Does this paragraph help a non-specialist German professor score one of: "Wahl der Gastinstitution begründet?", "sinnvolle Einbindung in den Studienverlauf?", "Durchführbarkeit?", "Kenntnis der Lehr- und Forschungsmöglichkeiten?", "Qualität des wissenschaftlichen Vorhabens?"* If not, it is filler. **(B)**

---

## 3. Answers to the 15 specific questions

### 3.1 Should individual modules be described? How detailed?

**YES — explicitly required. Classification A.**

DAAD: *„die geplanten Lehrveranstaltungen an der Gasthochschule aufführen"* + *„Beschreiben Sie **kurz** die Inhalte der voraussichtlichen Kurse bzw. Module"*.

Depth: the operative word is **kurz**. **(A)** Practical calibration: **2–4 sentences per module maximum**, of which at most one sentence is descriptive content and the rest is *why this module, for me*. **(B)** With 6 assessed modules (5 core + 1 elective) plus 4 industrial projects plus a dissertation to cover in 5 pages, anything longer arithmetically crowds out the rationale and the research component.

**Anti-pattern (the failure mode the task brief names):** copying the IfM module blurb. DAAD asks you to describe content *and* to justify the choice (A6). A copied blurb satisfies A3 and fails A6, and it is instantly recognisable to a committee that reads hundreds of these. **(B)**

### 3.2 Should ECTS / terms / dates be shown?

**Split answer.**

- **Credits: YES, required — `„machen Sie Angaben dazu, wie viele Credit Points dafür vergeben werden"`. Classification A.**
- **Critical complication:** Cambridge does **not** award ECTS for the MPhil. ISMM is assessed as **six module coursework pieces + four project assessments + one integrative essay + one dissertation of ≤15,000 words** (verified, §4) — no credit-point tariff was found on any official Cambridge page in this research. **NOT VERIFIED that ECTS exist for ISMM; provisionally: they do not.**
- **Recommended handling (B):** do not invent ECTS numbers. Instead satisfy A4 by stating the *assessment weight and workload proxy* Cambridge actually publishes — e.g. a column headed "Assessment / workload" giving "coursework, ~3,000-word report", "2-week in-company project, presentation + executive summary", "18-week dissertation, ≤15,000 words". Add **one explanatory line**: that Cambridge operates a full-time 11-month MPhil not denominated in ECTS, and that the full programme corresponds to a full Master's year. Fabricating a "90 ECTS" figure is a verifiable falsehood in front of German professors who know the ECTS system intimately — a serious risk. **(B)**
- **Terms: YES.** Michaelmas / Lent / Easter are the host institution's own vocabulary; using them demonstrates *Kenntnis der Lehr- und Forschungsmöglichkeiten*. **(B)** Note: I could **not verify** on an official page how ISMM's 11-month block maps onto the three Cambridge terms — the IfM pages describe the year in **weeks and months**, not terms (§9.2). **Use the week/month structure Cambridge actually publishes; do not assert a term mapping you cannot cite.**
- **Dates: YES, at month granularity.** "Oct 2027", "Jan–Feb 2028". Day-level dates are unverifiable a year out and create hostages to fortune. **(B)**

### 3.3 Should industrial projects be included?

**YES — emphatically. Classification B, built on A-grade Cambridge facts.**

They are not optional colour: the **four in-company projects (8 weeks, pairs, 2 weeks each) are separately assessed components of the degree** (verified, §4). Under A2/A3 they are part of "die geplanten Lehrveranstaltungen"; under "Durchführbarkeit" and "Kenntnis der Lehr- und Forschungsmöglichkeiten" they are exactly the kind of specific programme knowledge that scores.

They are also this applicant's strongest structural argument: a **DHBW dual-study graduate** is proposing a Master's whose pedagogy ("learn it, see it, do it", verified) is *the same practice-integrated model at postgraduate level*. That is a genuine, non-generic fit claim — and one almost no other applicant can make. **(B)**

### 3.4 Should the dissertation be described? Should a topic be proposed? How specific?

**YES to description. YES to proposing a topic — but as a bounded, clearly-hedged direction, not a locked thesis. Classification A (that it belongs) + B (how specific).**

- **That it belongs: A.** The call names *„die im Rahmen einer Masterarbeit vorgesehene Forschungsarbeit"*. ISMM's dissertation is compulsory, 18 weeks, ≤15,000 words, working with IfM researchers (verified). The "ggf." condition is triggered.
- **How specific: B.** Propose **one primary direction plus one named fallback**, at the level of a *research question and method*, not a title. Roughly **¾ of a page to 1 page**, containing: (i) the question, (ii) why it matters industrially and academically, (iii) the method/data you would use, (iv) why IfM specifically can host it, (v) the 18-week internal timeline (weeks 1–4 literature & scoping, 5–12 data/fieldwork, 13–16 analysis, 17–18 writing), (vi) an explicit one-line statement that the final topic is agreed with the supervisor within IfM's research portfolio.
- **Why hedge:** DAAD scores *Durchführbarkeit*. A first-year applicant who claims a locked thesis topic 12 months before matriculation, at an institution that allocates dissertation topics internally, reads as under-informed. A named direction + named fallback + explicit acknowledgement of supervisor allocation reads as *well-prepared*. **(B)**
- **Why not omit:** "Qualität des wissenschaftlichen Vorhabens" is a scored Qualifikation sub-criterion. A Studienplan with no research content scores zero there. **(B)**
- **Leverage point:** the applicant's **B.Sc. thesis in AI / claim verification** is directly usable as the methodological credential ("Stand der fachlichen und methodischen Vorbereitung" — an explicit Vorbereitung sub-criterion, A). It should be named in the dissertation section, not only in the CV. **(B)**

### 3.5 Should the plan explain how each module addresses a specific skill gap?

**YES — this is the single highest-leverage structural decision in the document. Classification B (strong inference from A5 + A6).**

A5 requires showing how the project fits the **previous and future** course of study; A6 requires justifying the choice. A gap argument satisfies both simultaneously, per module, in one sentence. The construction is:

> *[what my B.Sc./work already gave me] → [what it did not give me] → [which named ISMM module supplies it] → [what that enables].*

Do this for **every** module, but compress: one sentence each, not a paragraph each. **(B)**

**Caution (B):** the gap framing must not tip into self-deprecation. DAAD is simultaneously scoring *Qualifikation*. Frame gaps as *complementarity* ("Wirtschaftsinformatik gave me the data and systems layer; ISMM supplies the physical production layer that layer must control"), not deficiency.

**Specific honest gap for this applicant:** the B.Sc. Wirtschaftsinformatik and the EY/EY-Parthenon consulting background give information systems, analytics and business transformation, but **no engineering treatment of physical production processes, materials, or factory-level manufacturing systems**. ISMM's *Manufacturing Processes* and *Industrial Systems* modules are the precise, verifiable answer to that. This is a real, defensible, non-generic gap argument. **(B)**

### 3.6 Should previous academic experience be discussed?

**YES — but instrumentally, never biographically. Classification A (that it belongs) + B (how).**

A5 names the *bisheriger Studienverlauf* explicitly. But the CV already lists it and the Motivationsschreiben already narrates it. In the Studienplan its only legitimate function is as the **left-hand side of the gap equation** (§3.5) and as **evidence of feasibility** ("Stand der fachlichen und methodischen Vorbereitung").

Budget: **no standalone "my background" section longer than ~⅓ page**, and prefer distributing it into the per-module justifications. **(B)**

Concrete items worth naming, each tied to a module or to the dissertation:
- B.Sc. Wirtschaftsinformatik (IMBIT, DHBW Stuttgart) → data/systems foundation for *Data and Modelling*
- DHBW dual-study model → prepares for the in-company project format
- B.Sc. thesis in AI / claim verification → methodological readiness for the dissertation
- EY / EY-Parthenon, Singapore, analytics & digital transformation → *Operations and Supply Chain*, *New Business Development*, project work

### 3.7 How should ISMM be linked to a B.Sc. in Business Information Systems (Wirtschaftsinformatik)?

**Classification B throughout — this is inference, but well-grounded inference.**

Three framings, in descending order of strength:

1. **The layer argument (strongest).** Wirtschaftsinformatik is the discipline of the *interface between business processes and information systems*. Industry 4.0 / digital manufacturing is precisely that interface **applied to physical production**. The B.Sc. supplies the information-systems and process layer; ISMM supplies the **physical layer it must be grounded in** — production processes, materials, factory systems, supply-chain physics. This is not a career change; it is the same discipline acquiring its missing substrate. This framing turns the "why is a Wirtschaftsinformatiker doing a manufacturing MPhil?" objection into the thesis of the document.
2. **The continuity argument.** ISMM's *Data and Modelling* module (verified content: sampling, regression, data mining, simulation, sensitivity analysis) is **methodologically continuous** with a quantitative Wirtschaftsinformatik degree. This proves *Durchführbarkeit*: the applicant can already do the analytical work, so the year is not a remedial year.
3. **The DHBW argument.** The DHBW dual model is practice-integrated by design; ISMM is practice-integrated by design ("learn it, see it, do it", 4 in-company projects). The applicant is not adapting to an unfamiliar pedagogy — this is the postgraduate form of the one he was trained in. **This is also the answer to a latent risk:** German committees know DHBW is a *Duale Hochschule*, and a Bachelor's-to-Cambridge-MPhil jump may raise an academic-depth question. Pre-empting it by naming the model as a *fit* rather than letting it sit as an unspoken doubt is the better play. **(B)**

**Do NOT** claim the B.Sc. already covers manufacturing. It does not, and the committee can read the transcript. The honest gap (§3.5) is the stronger argument.

### 3.8 How should industry experience be integrated?

**YES, integrate — as evidence of feasibility and of problem-selection maturity, NOT as a career narrative. Classification B; the underlying criterion "ggf. einschlägige Praktika oder Berufserfahrung" is A.**

Three legitimate uses:
1. **Feasibility evidence.** Consulting at EY/EY-Parthenon, international work including Singapore → proves the applicant can execute four 2-week in-company projects in pairs under time pressure, and can function on a 2-week overseas study tour. This maps directly onto "Durchführbarkeit". **(B)**
2. **Problem provenance.** The research question in the dissertation section should visibly *come from somewhere*. "I observed X in digital-transformation engagements; the literature treats it as Y; ISMM lets me test Z" is far stronger than a question assembled from the IfM website. **(B)**
3. **Return-relevance.** DAAD's programme purpose is German-relevant qualification. Industry experience is the credible bridge to a stated post-degree contribution in German industrial transformation. **(B)**

**Budget: keep it to sentences embedded in module/dissertation justifications, plus at most 2–3 lines in the outlook.** A consultancy CV replayed in prose is the most common way a Studienplan turns into a second motivation letter. **(B)**

**Caution (D→B):** do not let the document read as "consultant collecting a Cambridge credential". DAAD funds *academic* projects. The academic question must lead; the industry experience must be in service of it.

### 3.9 Should it include a semester/month timeline?

**YES — but as a compact spine, not the body. Classification A (that a time plan is scored) + B (how much).**

Evidence: portal slot is literally labelled "Zeitplan" (A); "Durchführbarkeit **und Konsistenz des Arbeits- und Zeitplans**" and "Angemessenheit des gewählten Zeitpunkts" are scored (A). But the content instruction in §1.2 contains no date requirement, so a date-dominated document misallocates space.

**Recommendation (B):** exactly **two** time artefacts:
1. A **one-third-page overview table or band** on page 1–2 mapping the 11 months + 1 assessment month onto phases (taught modules → 4 industrial projects → overseas study tour → 18-week dissertation → assessment), month-granular.
2. A **short internal timeline inside the dissertation section** (the 18 weeks, broken into 4 phases).

Anything more is a calendar, and the genre verdict (§2) says the genre is not a calendar.

### 3.10 Should professional goals appear?

**YES, but briefly and at the end. Classification B.**

"Zukünftiger Studienverlauf" is explicitly in A5, and the Motivation block includes "fachlicher Nutzen" and "Notwendigkeit des Auslandsaufenthalts". But career narrative is the Motivationsschreiben's job.

**Recommendation (B):** a closing section of **~⅓ page**, framed as the *academic and professional trajectory the plan enables*, with a concrete German/European anchor (Industry 4.0 capability in German industry; the DAAD programme's implicit return-orientation). Keep it forward-looking and specific; avoid "I want to be a leader in…" formulations.

### 3.11 How much duplication with the motivation letter is appropriate?

**Near-zero duplication of *content*; deliberate consistency of *claims*. Classification B; the separation itself is A.**

DAAD requires them as separate uploads and gives them different briefs (A, §1.5). The clean division of labour:

| | Motivationsschreiben (2 pp.) | Studienplan (5 pp.) |
|---|---|---|
| Register | Personal, persuasive, first-person narrative | Academic, evidential, structured |
| Answers | **WHY me, why this, why there** | **WHAT exactly, WHEN, and HOW I know it works** |
| Cambridge content | Institution-level, one or two anchors | Module-level, project-level, dissertation-level, named |
| Biography | Yes, narrated | Only as gap-analysis input |
| Career | Yes | Only in the closing outlook |

**Permitted and desirable overlap:** the *central claim* (the layer argument, §3.7) should appear in both — stated in one sentence in the letter, *demonstrated* across five pages in the plan. A committee reading both should feel one coherent candidate, not two documents. **(B)**

**Practical test (B):** if a paragraph of the Studienplan would work unchanged in the Motivationsschreiben, it is in the wrong document.

### 3.12 Are tables useful? Are diagrams/figures useful?

**Tables: YES — explicitly permitted by DAAD. Classification A.**

> *„Die Kursübersicht kann auch in tabellarischer Form erstellt werden."*

Independent Tier-2 corroboration (≥2 sources: a university international-office guide and a study-abroad advisory guide) goes further and *recommends* leading with a tabular overview of all courses across all semesters. **(C)**

**No source found in this research penalises tables.** **(A for permission; no contrary evidence found.)**

Recommended tables (**B**):
- The course/module table (module | 1-line content | why me / gap closed | assessment & workload | timing) — the backbone.
- The programme-phase timeline table.
- Optionally a compact two-column "capability I bring / capability ISMM adds" table.

**Diagrams/figures: PERMITTED BY SILENCE, USE SPARINGLY. Classification B (no A-grade evidence either way — see §9).**

- **No DAAD source found permits or forbids figures.** This is a genuine evidential gap, not a finding. Marked **NOT VERIFIED**.
- The safe inference: DAAD permits tables and sets a hard page limit but no formatting rules; a figure is a formatting choice within the applicant's discretion. **(B)**
- Risk: figures consume page budget fast, and PDF rendering/legibility in the portal is uncontrolled. A page of the 5 spent on a diagram is a page not spent on rationale.
- **Recommendation (B): at most ONE simple figure**, and only if it does work prose cannot — the strongest candidate being a single horizontal timeline band showing the 11+1 month structure with the four phases, which simultaneously discharges §3.9 and demonstrates programme knowledge. Prefer tables over diagrams everywhere else. No decorative graphics, no logos, no screenshots of the IfM website.

### 3.13 Is a 5-page document expected to actually use all five pages?

**Use 4.5–5 pages. Do not pad; do not stop at 3. Classification B/C — no official statement exists.**

- **NOT VERIFIED:** no DAAD source found states an expected length within the maximum. "max. 5 Seiten" is a ceiling only. **(A: ceiling. Everything else: B.)**
- Argument for using the space: the document must discharge **seven A-grade obligations** (§1.2, A1–A7) across **six modules, four industrial projects, one overseas study tour, one 18-week dissertation, a gap analysis, a timeline and an outlook**, for a **non-specialist reader** who needs concepts glossed. Doing that well in three pages is not realistic. A visibly short Studienplan also reads as weak "Vorbereitung" — the applicant appears not to know enough about the host institution to fill the space. **(B)**
- Argument against padding: "Qualität des Vorhabens" is scored, not word count. Filler is visible.
- **Target: ~4.5 pages of substance + a source/reference line if used.** If the draft runs to 3 pages, the diagnosis is almost always *missing per-module rationale* or *missing dissertation section*, not "I am concise". **(B)**

### 3.14 Language: German or English?

**GERMAN. Classification B — strongly recommended, though either is formally permitted (A).**

- **Formally: either.** DAAD permits German or English, and even mixed languages across documents. **(A, §1.6)**
- **Strategically: German**, for three reasons:
  1. **The audience is German professors** — *„in erster Linie Hochschullehrende deutscher Hochschulen"* (A), reading in a German-language process, against German-language criteria. Writing in their working language reduces friction on every page.
  2. **The "fachfremd" instruction** (A, §1.3) is about comprehension. German prose with English technical terms glossed on first use ("Industrie 4.0", "digitale Fertigung", "digitaler Zwilling / digital twin") is easier for a mixed-discipline German panel than dense English.
  3. **Programme framing.** This is the *outbound* programme for German students; German is the unmarked, expected choice.
- **Handle the Cambridge material like this (B):** German prose, but keep **module names, the degree title and the institution name in English, verbatim and unaltered** (*„Data and Modelling"*, *„MPhil in Industrial Systems, Manufacture and Management"*, *„Institute for Manufacturing"*). Translating official module names is both inaccurate and unverifiable. This mixed handling is standard and reads as precise, not sloppy.
- **Counter-case (D):** if any other document in the package is in English, or if the applicant's German academic register is weaker than his English, consistency may argue otherwise. But on the evidence found, German is the default. **Check the specific 2026/27 call text for any language stipulation before finalising** — the permission is conditioned on *„wenn in der Stipendienausschreibung nicht anders angegeben"*.

### 3.15 What differentiates a strong Studienplan from a website paraphrase?

See **§8** for the full treatment. Headline: **a paraphrase describes the programme; a strong Studienplan describes a decision.** The test is whether any sentence could have been written by someone who had read the IfM website but knew nothing about the applicant. **(B)**

### 3.16 Summary table

| # | Question | Answer | Class. | Source basis |
|---|---|---|---|---|
| 1 | Describe individual modules? | Yes; **kurz** — 2–4 sentences, mostly rationale | **A** / B (depth) | DAAD Wichtige Hinweise |
| 2 | Show ECTS / terms / dates? | Credits **required (A)** but ISMM has no verified ECTS → use assessment/workload + one explanatory line; terms & month-level dates yes | **A** / B (handling) | DAAD Wichtige Hinweise; IfM assessment page |
| 3 | Include industrial projects? | Yes, prominently — separately assessed degree components | **B** (on A facts) | IfM course + assessment pages |
| 4 | Describe dissertation / propose topic? | Yes; one direction + one fallback + method + 18-week plan + supervisor caveat; ¾–1 page | **A** (that) / **B** (how) | DAAD call ("ggf. … Masterarbeit"); IfM assessment page |
| 5 | Module → skill gap? | Yes — highest-leverage move; one sentence per module | **B** | DAAD A5 + A6 |
| 6 | Discuss previous academic experience? | Yes, instrumentally; ≤⅓ page standalone | **A** (that) / **B** (how) | DAAD A5; "Stand der fachlichen Vorbereitung" |
| 7 | Link ISMM ↔ Wirtschaftsinformatik? | Layer argument + methodological continuity + DHBW/practice-integration fit | **B** | Inference on verified module content |
| 8 | Integrate industry experience? | Yes — feasibility, problem provenance, return-relevance; distributed, not narrated | **B** (criterion "ggf. Berufserfahrung" = A) | DAAD criteria |
| 9 | Semester/month timeline? | Yes — one overview band + one dissertation sub-timeline; month granularity | **A** (that) / **B** (scale) | Portal field "Zeitplan"; "Durchführbarkeit … Zeitplans" |
| 10 | Professional goals? | Yes, ~⅓ page, closing | **B** | DAAD A5 "zukünftiger Studienverlauf" |
| 11 | Duplication with motivation letter? | Near-zero content overlap; shared central claim | **B** (separation = A) | DAAD separate-upload rule |
| 12 | Tables? Figures? | **Tables explicitly permitted (A)** and recommended (C). Figures: no rule found (**NOT VERIFIED**) → at most one timeline band | **A** / **B** | DAAD: "kann auch in tabellarischer Form" |
| 13 | Use all 5 pages? | Yes — target ~4.5; ceiling is A, target is inference | **B** | Obligation count vs. page budget |
| 14 | German or English? | **German** (English formally permitted); English module names kept verbatim | **A** (either allowed) / **B** (choose German) | DAAD language rule; committee composition |
| 15 | Strong vs. paraphrase? | Describes a **decision**, not a programme — see §8 | **B** | Selection-criteria analysis |

---

## 4. Cambridge ISMM programme map

**Every fact below carries a Cambridge URL. Facts I could not verify are marked NOT VERIFIED and must not be used.**

**Evidence caveat:** obtained via WebSearch summaries of these pages; the pages themselves could not be opened (see top-of-file constraint). Re-verify before citing in the application.

### 4.1 Identity and official pages

| Item | Detail | Source |
|---|---|---|
| Full title | **MPhil in Industrial Systems, Manufacture, and Management (ISMM)** | https://www.postgraduate.study.cam.ac.uk/courses/directory/egegmpimm |
| Course code | `egegmpimm` | same |
| Faculty / dept | Department of Engineering, University of Cambridge | https://www.eng.cam.ac.uk/postgraduates/postgraduate-courses/taught-courses-mphil-and-mres |
| Delivering institute | **Institute for Manufacturing (IfM)** | https://www.ifm.eng.cam.ac.uk/ |
| Main course page | | https://www.ifm.eng.cam.ac.uk/education/industrial-systems-manufacture-management-course/ |
| Course overview | | https://www.ifm.eng.cam.ac.uk/education/industrial-systems-manufacture-management-course/course-overview/ |
| Course content | | https://www.ifm.eng.cam.ac.uk/education/ismm/course/ |
| Taught modules | | https://www.ifm.eng.cam.ac.uk/education/ismm/course/taught/ · https://www.ifm.eng.cam.ac.uk/education/industrial-systems-manufacture-management-course/taught-modules/ |
| Projects | | https://www.ifm.eng.cam.ac.uk/education/ismm/course/projects/ |
| Assessment & feedback | | https://www.ifm.eng.cam.ac.uk/education/ismm/assessment-and-feedback/ |
| Why ISMM | | https://www.ifm.eng.cam.ac.uk/education/ismm/whyismm/ |
| How to apply | | https://www.ifm.eng.cam.ac.uk/education/industrial-systems-manufacture-management-course/how-to-apply/ |
| Enquiries | `ismm-enquiries@eng.cam.ac.uk` | assessment-and-feedback page |

> ⚠️ Note the **two course codes in circulation**: `egegmpimm` (found via the Cambridge postgraduate directory in this research) and `egegmpism` (which I guessed and could not confirm). **Use `egegmpimm`.** Third-party aggregators also list the course; ignore them — cite IfM and the Cambridge postgraduate directory only.

### 4.2 Duration and calendar — VERIFIED

| Fact | Detail | Source |
|---|---|---|
| Type | One-year full-time postgraduate Master's (MPhil) | ifm.../course-overview/ |
| Start | **Beginning of October** | ifm.../course-overview/ |
| Total structure | **11 months of taught programme + 1 month of assessment** (= 12 months) | ifm.../course-overview/ |
| Project block | **8 weeks of project work**, covering **4 projects** | ifm.../ismm/course/ |
| Overseas study tour | **2 weeks**, "either in mainland Europe or further afield" | ifm.../ismm/course/ |
| Christmas break | **3 weeks** | ifm.../ismm/course/ |
| Easter break | **1 week** | ifm.../ismm/course/ |
| Dissertation | **18-week dissertation project** | ifm.../ismm/course/ |

**Resolution of the "9 vs 12 months" question in the brief:** neither. Cambridge's own framing is **11 months taught + 1 month assessment**. Some third-party aggregators list "11 months". **Use Cambridge's own formulation.** **(A)**

**NOT VERIFIED:** how the 11+1 months map onto **Michaelmas / Lent / Easter** terms. IfM describes the year in weeks and months, not Cambridge terms. Do not assert a term mapping.

**NOT VERIFIED:** the exact 2027-28 start date. Use "early October 2027".

### 4.3 Pedagogy — VERIFIED

> "The learning ethos that underpins the course is best described as **'learn it', 'see it', 'do it'**." — https://www.ifm.eng.cam.ac.uk/education/industrial-systems-manufacture-management-course/course-overview/

> "The programme is structured around **taught modules, company visits and in-company projects solving live business or technical problems**." — same

> "The course modules are normally taught in Cambridge and consist of **lectures, case studies, exercises and structured visits**, all run either by University staff or by **visitors, usually from industry**, with a specific expertise." — ifm.../taught-modules/

Stated purpose: "designed to equip outstanding graduates with the **skills, personal development and industrial experience to be immediately effective in their early careers**." — ifm.../course-overview/

### 4.4 Module architecture — VERIFIED (structure) / PARTIALLY VERIFIED (names)

**Structure (VERIFIED):**
> "The course begins with an **induction module (M0)**. There are **5 core modules**, each of which is assessed by an independent piece of coursework. Students will also choose **one elective module**." — ifm.../ismm/course/taught/

Total assessed modules: **6** (5 core + 1 elective) — corroborated by the assessment page's "six modules, each assessed by an independent piece of coursework".

**Module content areas (VERIFIED as real modules with these names/descriptions):**

| Module | Verified description | Source |
|---|---|---|
| **Industrial Systems** | "introduces all of the theory and principles required to develop a manufacturing system" | ifm.../ismm/course/taught/ |
| **Manufacturing Processes** | "an introduction to the manufacturing processes of the major materials used in industry"; introduces "critical manufacturing processes and their implications on production" | ifm.../taught-modules/ |
| **Operations and Supply Chain** | "spans the core domains of **procurement, upstream and supply chain collaborations; value creation within the factory; distribution and end-to-end (E2E) integrated supply chain management**" | ifm.../taught-modules/ |
| **Data and Modelling** | "introduces the **data analytics and modelling techniques used for analysing manufacturing data**. The aim is that students should be able to approach a range of managerial problems in a structured way, using analytical methods. The content includes: **sampling, regression, data mining, simulations and sensitivity analysis**." | ifm.../taught-modules/ |
| **New Business Development** | "introduces the interrelated concepts of **Entrepreneurship, Business Strategy, Sales and Marketing and Design Innovation**, all of which are required in high growth and service businesses" | ifm.../taught-modules/ |

✅ **The four strands named in the applicant's brief — Data & Modelling, Manufacturing Processes, Operations & Supply Chain, New Business Development — are all VERIFIED as real ISMM modules.** A fifth, **Industrial Systems**, is also verified. Together with M0 induction and one elective, this accounts for the published architecture.

**NOT VERIFIED:**
- The mapping of these five names onto the codes M1–M5. Do **not** write "M3 Data and Modelling".
- The **list of elective module options**. Do **not** name an elective.
- Whether the module set changes for 2027-28 entry.
- Any credit weighting per module.

### 4.5 Industrial / in-company projects — VERIFIED

| Fact | Detail | Source |
|---|---|---|
| Number | **Four** company projects | ifm.../ismm/course/ |
| Total time | **8 weeks** | ifm.../ismm/course/ |
| Each | **2 weeks** | ifm.../ismm/course/ |
| Working mode | Students "usually working in **pairs**" | ifm.../ismm/course/ |
| Nature | "in-company projects **solving live business or technical problems**" | ifm.../course-overview/ |
| Company range | "we try and give students **as wide a range of opportunities as possible by working with lots of different-sized companies**" | ifm.../ismm/course/projects/ (via course pages) |
| Positioning | "In-company projects solving real business or technical problems are **what makes ISMM unique**" | same |
| Assessment | "Each of the 4 industry projects is **assessed independently**, with students **presenting their findings to the host company** and submitting a **short executive summary** of their conclusions, as well as any supporting evidence." | ifm.../ismm/assessment-and-feedback/ |

**NOT VERIFIED:** exactly how projects are sourced and allocated, whether students can express preferences, and the identity of any host company. **Do not name a company.**

### 4.6 Company visits, placements and international visits — PARTIALLY VERIFIED

| Fact | Status | Source |
|---|---|---|
| **Company visits** are a structural element ("taught modules, company visits and in-company projects") | VERIFIED | ifm.../course-overview/ |
| Modules include "**structured visits**" | VERIFIED | ifm.../taught-modules/ |
| **Overseas study tour: 2 weeks, "either in mainland Europe or further afield"** | VERIFIED | ifm.../ismm/course/ |
| Purpose: "An overseas study tour offers a **broader international context**" | VERIFIED | ifm.../ismm/course/ |
| Destination for 2027-28 | **NOT VERIFIED** — varies by year | — |
| Any separate "placement" distinct from the 4 projects | **NOT VERIFIED** — no evidence of one; the projects appear to *be* the industrial placement element | — |

### 4.7 Dissertation / research project — VERIFIED

| Fact | Detail | Source |
|---|---|---|
| Length of time | **18 weeks** | ifm.../ismm/course/ |
| Word limit | "a research dissertation thesis of **not more than 15,000 words**" | ifm.../ismm/assessment-and-feedback/ |
| Setting | "working with **researchers for the Institute for Manufacturing** applying **new theories to industrial applications**" | ifm.../ismm/course/ |
| Purpose | "the individual research dissertation allows for **greater depth of study in a specific area of manufacturing**" | ifm.../ismm/course/ |
| Position in year | Final block of the 11-month taught programme, before the assessment month | ifm.../ismm/course/ |

**NOT VERIFIED:** how dissertation topics are chosen or proposed, how supervisors are allocated, whether students may bring their own topic, and whether dissertations are industrially sponsored. **This is a significant gap — see §9.2.** Because of it, the Studienplan must phrase its research proposal as a *direction to be agreed within IfM's research portfolio*, not as a fixed project.

### 4.8 Assessment structure — VERIFIED

From https://www.ifm.eng.cam.ac.uk/education/ismm/assessment-and-feedback/:

1. **Six modules**, each assessed by an independent piece of coursework — "which might be a **short report (e.g. 3000 words)**, a **group exercise culminating in a presentation**, or a **class-based test**".
2. **Four industry projects**, each assessed independently — **presentation to the host company** + **short executive summary** + supporting evidence.
3. **One integrative essay** — "an essay which seeks to **integrate ideas in the course for a 'big issue'**".
4. **One research dissertation** — **≤ 15,000 words**.

**NOT VERIFIED:** numerical weightings between these four components. The IfM page does not publish them; the page itself directs enquiries to `ismm-enquiries@eng.cam.ac.uk`. **Do not state a weighting.**

### 4.9 Subject scope — VERIFIED

> "ISMM students develop an **integrated view of manufacturing engineering** which spans **production processes, operations management and supply chains, data and simulation, marketing, strategy, delivery of products and services, and industrial economics**." — ifm.../course-overview/

> "The course addresses **the whole value chain** and builds an integrated view of manufacturing spanning: production processes, operations management and supply chain, data and simulation, marketing, strategy, product/service delivery and **industrial sustainability**." — ifm.../ismm/course/

**Note for the applicant:** "**data and simulation**" appears in Cambridge's *own* one-sentence definition of the degree's scope. That is a directly citable anchor for a data-oriented specialisation, in Cambridge's own words. **(A)**

---

## 5. IfM research groups and digital-manufacturing anchor points

### 5.1 What is verified

| Item | Status |
|---|---|
| The dissertation is done "working with **researchers for the Institute for Manufacturing**, applying **new theories to industrial applications**" | **VERIFIED** — ifm.../ismm/course/ |
| The IfM is part of the Cambridge **Department of Engineering** | **VERIFIED** — eng.cam.ac.uk postgraduate taught-courses page |
| **IfM Engage** exists as the IfM's knowledge-transfer arm, running courses | **VERIFIED (existence only)** — https://engage.ifm.eng.cam.ac.uk/courses/ |
| The IfM also teaches the undergraduate **MET** (Manufacturing Engineering Tripos), whose module pages include **"Industrial Systems, Operations and Services"**, **"Manufacturing Systems Engineering"** and **"Sustainable Manufacturing"** | **VERIFIED that these MET module pages exist** — https://www.ifm.eng.cam.ac.uk/education/met/b/industrial-systems/ · /met/b/systems/ · /met/b/sustainable/ |

⚠️ **The MET modules are NOT ISMM modules.** They belong to the undergraduate Manufacturing Engineering Tripos. They are listed here only as evidence of the IfM's teaching footprint — **do not cite them as part of ISMM.**

### 5.2 What is NOT verified — DO NOT USE

I could **not verify a single IfM research group name or a single academic's name** in this session. The web-search budget was exhausted before reaching the research-group pages, and WebFetch was blocked throughout.

**The following, named in the task brief, are therefore all marked NOT VERIFIED IN THIS SESSION:**

- Distributed Information & Automation Laboratory — **NOT VERIFIED**
- Centre for Industrial Sustainability — **NOT VERIFIED**
- Cambridge Service Alliance — **NOT VERIFIED**
- IfM Engineering Design Centre — **NOT VERIFIED**
- Technology Management (group) — **NOT VERIFIED**
- Production Processes (group) — **NOT VERIFIED**
- **Any named academic whatsoever** — **NOT VERIFIED**

**Instruction (binding):** none of these names may appear in the Studienplan until each is confirmed on a live `ifm.eng.cam.ac.uk` page, together with (i) the group's current name, (ii) confirmation it is active, (iii) at least one current research theme, and (iv) — if an academic is to be named — that person's current IfM affiliation. **Naming a lab that has been renamed or a professor who has left is exactly the error a Cambridge-literate reader catches, and it destroys the "Kenntnis der Lehr- und Forschungsmöglichkeiten" credit the naming was meant to earn.** See §9.2 for the verification task.

### 5.3 Anchor points that ARE safely usable today

These are verified and require no further checking:

1. **"data and simulation"** — inside Cambridge's own definition of the degree's scope. *(ifm.../course-overview/)*
2. **The Data and Modelling module** — verified name and verified content list (sampling, regression, data mining, simulations, sensitivity analysis). *(ifm.../taught-modules/)*
3. **The Industrial Systems module** — "all of the theory and principles required to develop a manufacturing system". *(ifm.../ismm/course/taught/)*
4. **The Operations and Supply Chain module** — verified E2E supply-chain scope. *(ifm.../taught-modules/)*
5. **The four in-company projects** — verified format, verified assessment. *(ifm.../ismm/course/, .../assessment-and-feedback/)*
6. **The 18-week, ≤15,000-word dissertation with IfM researchers** "applying new theories to industrial applications". *(ifm.../ismm/course/, .../assessment-and-feedback/)*
7. **"industrial sustainability"** in the course's stated value-chain scope. *(ifm.../ismm/course/)*

**A Studienplan built only on items 1–7 is already specific, accurate and far above a website paraphrase.** Research-group names would strengthen §5 of the plan, but they are an enhancement, not a prerequisite.

---

## 6. Plausible specialisation pathways for this applicant

**Everything in this section is Classification B — inference grounded in the §4 verified facts. Nothing here is an official Cambridge statement about specialisation.** ISMM is a broad integrated manufacturing degree; it is **not** a digital-manufacturing degree. The correct framing is *specialisation built across a general programme*, not *a digital-manufacturing track*.

### Pathway 1 — Data-driven manufacturing via *Data and Modelling* (strongest, fully verified base)

**Grounding:** *Data and Modelling* verifiably teaches sampling, regression, data mining, simulation and sensitivity analysis **applied to manufacturing data**; Cambridge's own scope sentence names "data and simulation". **(A facts)**

**Inference (B):** this is the one module that sits directly on the applicant's existing Wirtschaftsinformatik competence *and* points at his stated interest. It is the natural spine of a data-driven manufacturing specialisation: he arrives able to do the analytics and spends the year learning the **manufacturing domain the analytics must be about**. This inverts the usual gap story and is a strong, honest claim.

**Risk to manage (B):** because he can already do the methods, the module alone does not justify the year. The argument must be *domain acquisition*, not *method acquisition*.

### Pathway 2 — Industry 4.0 / digital transformation via *Industrial Systems* + *Operations and Supply Chain*

**Grounding:** *Industrial Systems* = "theory and principles required to develop a manufacturing system"; *Operations and Supply Chain* = procurement, upstream collaboration, in-factory value creation, distribution, **end-to-end integrated supply chain management**. **(A facts)**

**Inference (B):** "Industry 4.0" is, operationally, the digitalisation of exactly these two objects — the factory system and the end-to-end supply chain. These two modules supply the **system-level object** that the applicant's IT/data background currently lacks. E2E supply-chain integration in particular is where his consulting transformation work and a manufacturing-systems education meet.

**Honest limitation to state (B):** neither module is verified to teach Industry 4.0 technologies as such. The plan should say *these modules give me the manufacturing-systems foundation on which digital transformation acts*, not *these modules teach Industry 4.0*.

### Pathway 3 — Industrial AI, located in the dissertation

**Grounding:** 18-week, ≤15,000-word dissertation, **with IfM researchers**, explicitly "**applying new theories to industrial applications**"; applicant has a **B.Sc. thesis in AI / claim verification**. **(A facts)**

**Inference (B):** the dissertation is the only component of ISMM with enough depth and freedom to host a genuine industrial-AI research contribution, and IfM's own framing of it ("new theories → industrial applications") is almost a description of applied industrial AI. This is where the specialisation claim becomes *academic* rather than *elective-shopping*, and where the applicant's existing research credential does real work.

**This is the pathway that should carry the most weight in the Studienplan**, because it is the component DAAD's call explicitly asks about ("die im Rahmen einer Masterarbeit vorgesehene Forschungsarbeit") and the one where "Qualität des wissenschaftlichen Vorhabens" is scored.

**Constraint (B):** topic selection and supervision mechanics are **NOT VERIFIED** (§4.7). Phrase as a direction, name a fallback, acknowledge supervisor agreement.

### Pathway 4 — Industrial transformation via the four in-company projects

**Grounding:** four independently assessed 2-week in-company projects on **live business or technical problems**, in **pairs**, across **different-sized companies**; assessed by **presentation to the host company + executive summary**. **(A facts)**

**Inference (B):** this is the applicant's home turf — it is structurally a consulting engagement, assessed the way a consulting engagement is assessed. The Studienplan should say plainly that he intends to steer project selection, where the programme permits, toward digitalisation and data problems, **while acknowledging that project allocation is the course's to make**. It should also say what he brings *to* the projects (EY/EY-Parthenon delivery experience, international work), not only what he takes from them — this is one of the few places where a Studienplan can credibly show the applicant contributing to the host institution.

### Pathway 5 — IoT / digital twins — **WEAKEST; handle with care**

**Grounding: none verified.** No ISMM module verified in this research mentions IoT, digital twins, cyber-physical systems, or Industry 4.0 by name. **(NOT VERIFIED)**

**Recommendation (B):** do **not** claim ISMM teaches IoT or digital twins. Either (a) drop IoT as a named specialisation and fold it into the dissertation direction under Pathway 3, or (b) re-open it only if the §9.2 research-group verification turns up an IfM group with a current, citable IoT/digital-twin research theme that could host a dissertation. **Claiming an IoT curriculum that cannot be found on the IfM site is the highest-risk factual error available in this document.**

### Recommended composite framing (B)

> **Spine:** manufacturing-systems and process domain knowledge the applicant does not yet have (*Industrial Systems*, *Manufacturing Processes*) →
> **Method continuity:** *Data and Modelling*, where his existing quantitative competence meets manufacturing data →
> **System scope:** *Operations and Supply Chain*, the E2E object digital transformation acts on →
> **Practice:** four in-company projects, steered where possible toward digitalisation problems →
> **Academic contribution:** an 18-week dissertation with IfM researchers on a data/AI-in-manufacturing question, building on his AI B.Sc. thesis.

This composite uses **only verified facts**, is genuinely specific to ISMM, and is genuinely specific to *this* applicant. It is the architecture §7 builds on.

---

## 7. IDEAL 4–5 PAGE ARCHITECTURE

**Design principles:**
- Every one of DAAD's seven obligations (A1–A7) is discharged on an identified page.
- The document is organised **chronologically through the ISMM year** — this makes the "Zeitplan" framing true without the document becoming a calendar.
- Each ISMM component appears **exactly once**, with its rationale attached, so nothing is described twice.
- Target **~4.5 pages of substance**; German prose; English module names verbatim.

---

### Page 1 — Ausgangslage, Zielsetzung und Überblick über das Studienvorhaben

**Objective:** Establish the academic problem the year is meant to solve, state the goal of the stay (DAAD obligation **A1**), and give the reader the whole shape of the year in one glance so that everything following is legible. Make the "why Cambridge, why ISMM, why now" decision visible in the first 20 lines.

**Content:**
- Opening (~8–10 lines): the **layer argument** (§3.7) as the thesis of the document — Wirtschaftsinformatik gives the information-systems and process layer; industrial transformation requires the physical production layer; ISMM supplies it. One sentence naming the intended specialisation direction (data-driven manufacturing / industrial AI).
- **Zielsetzung** (~6–8 lines): 3–4 numbered academic objectives for the year, phrased as capabilities to be acquired, not aspirations. (**A1**)
- **Kurzprofil des Studiengangs** (~8 lines): MPhil ISMM, Institute for Manufacturing, Department of Engineering; **11 months taught + 1 month assessment**; start early October 2027; the "learn it / see it / do it" ethos quoted in one short clause; the verified scope sentence ("production processes, operations management and supply chains, **data and simulation**, marketing, strategy, delivery of products and services, industrial economics"). Every claim citable.
- **Überblickstabelle / Zeitschiene** (~⅓ page): the whole year in phases — taught modules → 4 in-company projects (8 weeks) → 2-week overseas study tour → 18-week dissertation → assessment month. Month-granular. (**A7**, and discharges §3.9's first artefact.)

**Cambridge-specific evidence to cite:**
`ifm.../course-overview/` (11+1 months, October start, 'learn it/see it/do it', integrated-view scope sentence); `ifm.../ismm/course/` (8 weeks / 4 projects, 2-week overseas tour, 18-week dissertation, "whole value chain"); `postgraduate.study.cam.ac.uk/courses/directory/egegmpimm` (official course identity).

**Applicant-specific link:** B.Sc. Wirtschaftsinformatik (IMBIT, DHBW Stuttgart) named once, as the left-hand side of the layer argument. No biography, no career narrative.

**Approximate space allocation:** ~1 page. Roughly ⅔ prose, ⅓ overview table/band.

**Use of tables/figures:** **One** artefact — either a compact phase table or a single horizontal timeline band. If a figure is used anywhere in the document, this is the place. Nothing decorative.

---

### Page 2 — Studienstruktur und Modulwahl I: Fachliche Grundlagen (Industrial Systems, Manufacturing Processes)

**Objective:** Discharge **A2** (list the courses), **A3** (briefly describe content), **A4** (credits/workload) and **A6** (justify the choice) for the modules that close the applicant's largest and most honest gap: physical manufacturing and factory-level systems. This page is where the gap analysis does its heaviest work.

**Content:**
- **Lead-in (~4 lines): the gap statement.** Explicit, complementarity-framed: Wirtschaftsinformatik and consulting deliver data, systems and transformation method; they do not deliver an engineering treatment of production processes, materials or manufacturing systems. ISMM does. (**A5** partly)
- **Modultabelle, part 1** — columns: *Modul | Inhalt (1 Satz) | Kompetenzlücke, die geschlossen wird | Leistungsnachweis / Arbeitsaufwand | Zeitraum*.
  - **Industrial Systems** — "theory and principles required to develop a manufacturing system"; closes: no systems-level model of a factory; assessment: independent coursework (report ~3,000 words / group exercise / class test).
  - **Manufacturing Processes** — "manufacturing processes of the major materials used in industry", implications on production; closes: no process/materials foundation.
  - Include the **M0 induction module** as a table row for completeness (verified to exist).
- **Prose justification (~12–15 lines)** for these two modules: *why they are prerequisite to any credible work on digital manufacturing* — the argument that digitalising a process you cannot model is the characteristic failure of IT-led Industry 4.0 projects, and that this is the competence the applicant is deliberately acquiring. This is the paragraph that proves the applicant has thought, not browsed.
- **Credit-point handling (~3 lines):** the explanatory line from §3.2 — Cambridge assesses the MPhil through coursework, project assessments, an integrative essay and a dissertation rather than an ECTS tariff; the full-time 11-month programme corresponds to a complete Master's year. (**A4**, honestly discharged.)

**Cambridge-specific evidence to cite:**
`ifm.../ismm/course/taught/` (M0 + 5 core + 1 elective; Industrial Systems description); `ifm.../taught-modules/` (Manufacturing Processes; teaching mode: lectures, case studies, exercises, structured visits, industry visitors); `ifm.../ismm/assessment-and-feedback/` (coursework formats).

**Applicant-specific link:** the honest gap (§3.5); DHBW practice-integrated training as evidence he can absorb applied engineering content quickly.

**Approximate space allocation:** ~1 page. ~40 % table, ~60 % prose.

**Use of tables/figures:** Table yes (the module table begins here and continues on page 3 — keep one continuous table across the two pages rather than two separate ones). No figure.

---

### Page 3 — Studienstruktur und Modulwahl II: Spezialisierung (Data and Modelling, Operations and Supply Chain, New Business Development, Wahlmodul) + Industrieprojekte und Studienreise

**Objective:** Complete **A2/A3/A4/A6** for the remaining modules, then discharge the same obligations for the **four in-company projects** and the **overseas study tour**. This is the page where the specialisation argument (§6) becomes concrete and where the applicant's professional experience is shown as an *asset to the programme*.

**Content:**
- **Modultabelle, part 2** (continuation):
  - **Data and Modelling** — content quoted tightly: sampling, regression, data mining, simulations, sensitivity analysis on manufacturing data; rationale: *method continuity, domain acquisition* (§6 Pathway 1). Flag this as the core of the intended specialisation.
  - **Operations and Supply Chain** — procurement, upstream collaboration, in-factory value creation, distribution, E2E integrated supply-chain management; rationale: the system-level object that digital transformation acts on (§6 Pathway 2).
  - **New Business Development** — entrepreneurship, business strategy, sales and marketing, design innovation; rationale: connects to the applicant's strategy/transaction work; keep *shorter* than the others — it is the module least central to the specialisation, and inflating it would be dishonest.
  - **Wahlmodul (elective)** — state that one elective is chosen, state the *criterion* by which it will be chosen (proximity to data-driven manufacturing / industrial digitalisation). **Do NOT name an elective** — the option list is NOT VERIFIED (§4.4).
- **Industrieprojekte (~10–12 lines):** 4 projects × 2 weeks = 8 weeks, in pairs, at companies of varying size, on live business or technical problems; assessed by presentation to the host company + executive summary. Rationale: (i) the format matches the DHBW dual model at postgraduate level; (ii) intention to steer project selection toward digitalisation/data problems **where the course permits**; (iii) one honest sentence on what he *brings* — EY / EY-Parthenon delivery experience, international work including Singapore.
- **Zweiwöchige Studienreise (~4–5 lines):** 2 weeks, mainland Europe or further afield; rationale in one sentence — comparative international manufacturing context, and one sentence connecting it to the applicant's existing international experience rather than treating it as tourism.

**Cambridge-specific evidence to cite:**
`ifm.../taught-modules/` (Data and Modelling, Operations and Supply Chain, New Business Development descriptions); `ifm.../ismm/course/` (8 weeks / 4 projects / pairs / 2-week overseas tour); `ifm.../ismm/course/projects/` (range of company sizes, "live business or technical problems"); `ifm.../ismm/assessment-and-feedback/` (project assessment mechanism).

**Applicant-specific link:** quantitative B.Sc. → *Data and Modelling*; consulting/transaction work → *Operations and Supply Chain* and *New Business Development*; DHBW dual model + EY delivery experience → the in-company projects; Singapore → the study tour.

**Approximate space allocation:** ~1 page. ~45 % table, ~55 % prose.

**Use of tables/figures:** Table (continuation). No figure.

---

### Page 4 — Forschungsvorhaben: Masterarbeit / Dissertation

**Objective:** Discharge the second half of the DAAD call's core sentence — *„sowie ggf. der im Rahmen einer Masterarbeit vorgesehenen Forschungsarbeit"* — and score the "Qualität des wissenschaftlichen Vorhabens" criterion. **This is the page that separates a strong Studienplan from a good one.**

**Content:**
- **Rahmen (~5 lines):** the 18-week research dissertation, ≤15,000 words, undertaken with IfM researchers, "applying new theories to industrial applications"; its position at the end of the taught programme. (**A2/A3 for the research component.**)
- **Forschungsrichtung (~12–15 lines):** ONE clearly formulated research direction at the level of a *question*, in the area of data-driven manufacturing / industrial AI, derived visibly from (i) the applicant's B.Sc. thesis in AI / claim verification and (ii) a problem observed in digital-transformation practice. Must contain: the question; why it matters industrially; why it matters academically; what makes it a *research* question rather than a consulting question.
- **Methodisches Vorgehen (~8 lines):** the intended method and data, phrased at a level a non-specialist professor can follow (**§1.3, A**). Connect to the verified *Data and Modelling* toolkit where genuinely applicable (simulation, regression, data mining) — this shows the coursework feeding the research, which is exactly the internal consistency DAAD scores.
- **Alternative Forschungsrichtung (~3–4 lines):** one named fallback direction. Signals realism and preparation.
- **Arbeits- und Zeitplan der 18 Wochen (~⅓ page):** small table or compact list — Wochen 1–4 Literatur & Scoping; 5–12 Datenerhebung/Fallstudie; 13–16 Analyse; 17–18 Verschriftlichung. This is the artefact that most directly discharges **„Durchführbarkeit und Konsistenz des Arbeits- und Zeitplans"** (A).
- **Betreuung (~3 lines):** an explicit, honest statement that the dissertation is carried out with IfM researchers and that the final topic is agreed with the supervisor within the IfM's research portfolio. **Do not name a supervisor or a research group unless §9.2 verification succeeds.**
- **Fachliche Vorbereitung (~4 lines):** the B.Sc. thesis in AI / claim verification named explicitly as evidence of methodological readiness — this discharges "Stand der fachlichen und methodischen Vorbereitung" (A).

**Cambridge-specific evidence to cite:**
`ifm.../ismm/course/` (18 weeks, with IfM researchers, "applying new theories to industrial applications", "greater depth of study in a specific area of manufacturing"); `ifm.../ismm/assessment-and-feedback/` (≤15,000 words).
**If and only if §9.2 verification succeeds:** one named IfM research group with one current research theme, cited to its live IfM page.

**Applicant-specific link:** the strongest page for this applicant — his B.Sc. AI thesis, his analytics work, and his observed industry problems all converge here. This is where he stops being a strong consultant applying to Cambridge and starts being a researcher with a question.

**Approximate space allocation:** ~1 page — do not let this page shrink. If the document overruns, cut page 3's prose, not this.

**Use of tables/figures:** One compact 18-week phase table. No figure.

---

### Page 5 (half to three-quarters page) — Einordnung in den Studienverlauf, Machbarkeit und Ausblick

**Objective:** Discharge **A5** (fit into previous *and future* course of study) and **A6** (justify the choice) as an explicit, standalone argument; close the "Vorbereitung" criterion (feasibility, language, timing); and land a short forward-looking outlook.

**Content:**
- **Einbettung in den Studienverlauf (~10 lines):** the retrospective and prospective halves of A5 stated directly — what the B.Sc. and the professional years built, why ISMM is the coherent next step rather than an interruption, and what it opens. This is where the *Warum jetzt?* is answered: **„Angemessenheit des gewählten Zeitpunkts"** is a named criterion (A).
- **Begründung der Hochschulwahl (~6–8 lines):** why ISMM/IfM **specifically** — and the argument must be one that does not transfer to another university. The defensible version: the combination of (i) integrated whole-value-chain manufacturing education, (ii) four assessed in-company projects, and (iii) an 18-week research dissertation with IfM researchers, in a single 12-month programme. Name the combination, not the reputation. (**A6**)
- **Machbarkeit / Vorbereitung (~6 lines):** language readiness (English at academic level, evidenced by the certificate in the application and by international work); the 11+1 month structure fitting the DAAD funding period; awareness of the admissions route (`ifm.../how-to-apply/`); confirmation that the programme is full-time and residential in Cambridge. Discharges "Durchführbarkeit" and "Stand der sprachlichen Vorbereitung" (A).
- **Ausblick (~6–8 lines):** the academic and professional trajectory the year enables, with a concrete German/European anchor — industrial digitalisation capability in German manufacturing. Forward-looking, specific, and short. (§3.10)

**Cambridge-specific evidence to cite:**
`ifm.../education/ismm/whyismm/`; `ifm.../how-to-apply/`; `ifm.../course-overview/` (one-year, immediately-effective framing, 11+1 months).

**Applicant-specific link:** the timing argument (post-B.Sc., post-consulting-exposure, pre-specialisation); international experience as language and mobility evidence; the return-to-German-industry framing.

**Approximate space allocation:** ~0.5–0.75 page. The document should end at roughly 4.5 pages of substance, comfortably under the 5-page ceiling.

**Use of tables/figures:** None. Prose only — this page is an argument, and an argument should look like one.

---

### 7.1 Space budget summary

| Page | Section | Target | DAAD obligations discharged |
|---|---|---|---|
| 1 | Ausgangslage, Zielsetzung, Überblick + Zeitschiene | 1.0 p | A1, A7, (A6 opened) |
| 2 | Module I: fachliche Grundlagen + Kompetenzlücke | 1.0 p | A2, A3, A4, A5(part), A6, A7 |
| 3 | Module II: Spezialisierung + Industrieprojekte + Studienreise | 1.0 p | A2, A3, A4, A6, A7 |
| 4 | Forschungsvorhaben / Masterarbeit + 18-Wochen-Plan | 1.0 p | Call's research clause; "Durchführbarkeit … Zeitplans"; "Qualität des Vorhabens" |
| 5 | Einordnung, Machbarkeit, Ausblick | 0.5–0.75 p | A5 (full), A6 (full), "Angemessenheit des Zeitpunkts" |
| | **Total** | **~4.5 p** | All of A1–A7 |

### 7.2 Alternative 4-page compression (if needed)

If the document must come down to 4 pages, merge pages 2 and 3 into a single continuous module table with tighter per-module prose (one sentence of rationale each instead of a paragraph), and keep pages 1, 4 and 5 intact. **Never compress page 4.** **(B)**

---

## 8. What separates a strong Studienplan from a website paraphrase

### 8.1 The diagnostic test

> **Read any sentence and ask: could this have been written by someone who read the IfM website but knew nothing about the applicant?**
> If yes for more than ~20 % of the document, it is a paraphrase.
>
> **Conversely: could this have been written by someone who knew the applicant but had never opened the IfM website?**
> If yes for more than ~20 %, it is a second motivation letter.
>
> A strong Studienplan fails **both** tests: every substantive sentence needs *both* inputs.

### 8.2 The seven differentiators

| # | Paraphrase | Strong Studienplan | Grounded in |
|---|---|---|---|
| 1 | Describes **what the programme is** | Describes **a decision the applicant made**, with the alternatives implicitly rejected | A6 *„begründen Sie kurz Ihre Wahl"* |
| 2 | Module blurb copied, then "this is very interesting to me" | Module blurb compressed to one clause, then **a specific capability gap it closes for this person** | A3 + A5 + A6 |
| 3 | Lists modules | Shows **modules feeding each other and feeding the dissertation** — coursework method → research method | "Konsistenz des Arbeits- und Zeitplans" |
| 4 | Mentions Cambridge's reputation | Names the **structural feature combination** (integrated value-chain curriculum + 4 assessed in-company projects + 18-week IfM dissertation in 12 months) that does not transfer to another university | "Wahl der Gastinstitution" |
| 5 | No research content, or a grandiose locked thesis title | **One bounded research direction + method + fallback + 18-week plan + supervisor caveat** | Call's research clause; "Durchführbarkeit" |
| 6 | Only takes from the institution | Shows what the applicant **brings** (delivery experience into the in-company projects; AI research method into the dissertation) | "Qualifikation"; "Potenzial" |
| 7 | Jargon-dense, or vague | **Precise but glossed** — a German professor from another discipline can follow every paragraph | §1.3 *„fachfremde Auswahlkommissionsmitglieder"* |

### 8.3 The five most common failure modes for *this specific applicant*

1. **Writing a second motivation letter.** The consulting-trained instinct is to persuade. The Studienplan's job is to *evidence*. Register discipline is the single biggest risk. **(B)**
2. **Naming an unverified IfM research group or academic.** High reward if right, disqualifying if wrong (§5.2). **(B)**
3. **Inventing ECTS.** German professors know the ECTS system; a fabricated figure is verifiable and fatal. **(B)**
4. **Claiming ISMM teaches IoT / digital twins / Industry 4.0 by name.** Not verified anywhere (§6 Pathway 5). **(B)**
5. **Letting the consulting CV crowd out the academic question.** DAAD funds academic projects. The industry experience must serve the question, not replace it. **(B/D)**

### 8.4 The positive formulation

> A strong Studienplan reads as though **the applicant has already begun the year in his head**: he knows the shape of the calendar, he knows what each block will demand, he knows which parts will be easy for him and which will not, he knows what he wants to find out in the eighteen weeks that matter most, and he knows what he will be able to do in March 2029 that he cannot do in September 2026. **A paraphrase reads as though he has decided to apply. A strong plan reads as though he has decided what to do.**

---

## 9. Contradictions, ambiguities, unverified items

### 9.1 URGENT — verify these three pages verbatim before drafting

Because WebFetch was blocked, **no quotation in §1 is character-exact**. Transcribe the German wording directly from:

1. **DAAD programme page 57503584** — `https://www2.daad.de/ausland/studieren/stipendium/de/70-stipendien-finden-und-bewerben/?detail=57503584` — the Studienplan requirement, the page limit, the "Zeitplan" upload instruction, the document list, the deadline for Western Europe.
2. **DAAD „Wichtige Hinweise zu DAAD-Stipendien"** — `https://www.daad.de/de/im-ausland-studieren-forschen-lehren/stipendien-finanzierung/wichtige-hinweise-zu-daad-stipendien/` — the A1–A7 sentence, the tabular-form permission, the "fachfremd" instruction.
3. **DAAD „Bewerbung um ein DAAD-Stipendium"** — `https://www.daad.de/de/im-ausland-studieren-forschen-lehren/stipendien-finanzierung/bewerbung/` — the language rule, the Motivationsschreiben brief.

Also confirm the **2026/27 call PDF** for this cycle, since programme calls are re-issued annually and wording can change.

### 9.2 Open research items (budget exhausted before these could be run)

| # | Item | Why it matters | Where to look |
|---|---|---|---|
| 1 | **IfM research group names and current activity** | §5.2 — nothing may be named until verified | `ifm.eng.cam.ac.uk` research pages |
| 2 | **Named academics in digital manufacturing / industrial AI / IoT at IfM** | Would strengthen page 4 materially | IfM people pages |
| 3 | **ISMM elective module list** | Page 3 currently names no elective | `ifm.../ismm/course/taught/` |
| 4 | **M1–M5 code-to-name mapping** | Would let the plan use Cambridge's own codes | `ifm.../ismm/course/taught/` |
| 5 | **How dissertation topics and supervisors are allocated** | Determines how firmly page 4 may propose a topic | `ifm.../ismm/course/` and course handbook |
| 6 | **How in-company projects are sourced/allocated; can students express preference?** | Page 3 currently hedges | `ifm.../ismm/course/projects/` |
| 7 | **Whether ISMM carries any credit tariff** | Determines the A4 handling in §3.2 | postgraduate.study.cam.ac.uk `egegmpimm` |
| 8 | **2027-28 term dates and exact start date** | Page 1 timeline precision | Cambridge term-dates page |
| 9 | **Whether DAAD publishes any rule on figures/graphics** | §3.12 currently NOT VERIFIED | DAAD portal help texts, FAQ |
| 10 | **The UK/Western-Europe country page and 2026/27 deadline** | Deadline appears to be **25 Sep 2026** — i.e. **~8 days from today**. Must be confirmed immediately. | DAAD country pages (likely Agent 1's remit) |

### 9.3 Contradictions and traps identified

| # | Issue | Resolution |
|---|---|---|
| 1 | **"Studienplan" vs the portal field "Zeitplan"** | Not a contradiction — DAAD instructs the Studienplan to be uploaded under "Zeitplan". **Do not restructure the document as a calendar because of the field label.** (A) |
| 2 | **Inbound vs outbound DAAD programme confusion** | English-language searches overwhelmingly return *„Study Scholarships – Master Studies for All Academic Disciplines"*, the **inbound** programme for foreign students coming to Germany (1–3 page motivation letter, different criteria). **This applicant is in the OUTBOUND programme *„Stipendien für ein Masterstudium im Ausland"* (max. 2-page Motivationsschreiben, max. 5-page Studienplan).** Any advice sourced in English must be checked for which programme it describes. **This is the biggest research trap in this file.** |
| 3 | **"Quality-assurance section is mandatory in the Studienplan"** | This appears in the **Chancen.Digital / digitales Masterstudium** variant of the programme, NOT the standard one. **Almost certainly does not apply here — verify against the 57503584 call text before including or omitting.** |
| 4 | **"Reverse chronological / American format, tabular"** attributed to the Studienplan in one search summary | Near-certainly guidance for the **Lebenslauf**, mis-attributed by the search summariser. **Do not apply reverse-chronological ordering to the Studienplan.** (D — rejected) |
| 5 | **"9 vs 12 months" ISMM duration** | Cambridge's own framing is **11 months taught + 1 month assessment**. Third parties say "11 months" or "1 year". Use Cambridge's formulation. (A) |
| 6 | **Course code `egegmpimm` vs `egegmpism`** | `egegmpimm` is the one returned by the Cambridge postgraduate directory in this research. `egegmpism` was my own guess and is **unconfirmed** — do not use it. |
| 7 | **ECTS for ISMM** | No credit tariff found on any official Cambridge page. DAAD requires credit information (A). Conflict resolved by §3.2's handling — report assessment/workload honestly, add one explanatory line, invent nothing. |
| 8 | **Michaelmas/Lent/Easter mapping** | IfM describes the year in weeks/months, not terms. **NOT VERIFIED.** Use weeks/months. |
| 9 | **IoT / digital twins in the ISMM curriculum** | **No evidence found.** Do not claim. (§6 Pathway 5) |
| 10 | **Whether DAAD expects 5 pages to be filled** | No official statement. Ceiling is A; the ~4.5-page target is B inference. |

### 9.4 Items explicitly NOT verified — binding do-not-use list

- Any IfM **research group** name (incl. all six named in the task brief)
- Any **academic's name**
- Any **elective module** name
- Any **M1–M5 code mapping**
- Any **ECTS / credit-point figure** for ISMM
- Any **assessment weighting** percentage
- Any **host company** name for the in-company projects
- Any **overseas study tour destination** for 2027-28
- Any **exact start date** beyond "early October"
- Any claim that ISMM teaches **IoT, digital twins, cyber-physical systems, or Industry 4.0** by name
- Any **Michaelmas/Lent/Easter** term mapping for ISMM

---

## 10. Source appendix

All accessed **2026-09-17**. **Access mode for every row: WebSearch result summary only** — direct page retrieval (WebFetch and curl) was blocked by the egress proxy for all domains (see top-of-file constraint). Tier per the scheme in `00_APPLICANT_PROFILE.md`.

### 10.1 DAAD and German-side sources

| Source | URL | Tier | Type | What it supports | Class. |
|---|---|---|---|---|---|
| DAAD — Stipendien für ein Masterstudium im Ausland (programme 57503584) | https://www2.daad.de/ausland/studieren/stipendium/de/70-stipendien-finden-und-bewerben/?detail=57503584 | 1 | Official programme call | Studienplan max. 5 pp.; "detaillierte Beschreibung des Studienvorhabens sowie ggf. … Masterarbeit"; upload under "Zeitplan"; document list; Motivationsschreiben max. 2 pp.; funding duration ≤24 months | **A** |
| DAAD — same call, PDF export | https://www2.daad.de/ausland/studieren/stipendium/de/70-stipendien-finden-und-bewerben.pdf?detail=57503584 | 1 | Official PDF | Same as above | **A** |
| DAAD — Wichtige Hinweise zu DAAD-Stipendien | https://www.daad.de/de/im-ausland-studieren-forschen-lehren/stipendien-finanzierung/wichtige-hinweise-zu-daad-stipendien/ | 1 | Official guidance | **A1–A7**: academic goal, list courses, describe content briefly, state credit points, **tabular form permitted**, fit into previous/future study, justify choice; "fachfremde Auswahlkommissionsmitglieder" | **A** |
| DAAD — Bewerbung um ein DAAD-Stipendium | https://www.daad.de/de/im-ausland-studieren-forschen-lehren/stipendien-finanzierung/bewerbung/ | 1 | Official guidance | Language rule (German **or** English, mixed permitted); Motivationsschreiben brief; incomplete applications rejected | **A** |
| DAAD — Wichtige Hinweise zu den DAAD-Stipendien (inbound variant) | https://www.daad.de/de/in-deutschland-studieren/stipendien/hinweise-daad-stipendien/ | 1 | Official guidance | Selection criteria structure (Motivation / Qualifikation / Vorbereitung); committee composition | **A** (criteria) / flagged: inbound programme |
| DAAD — Jahresstipendien für Studienaufenthalte im Ausland (57503530) | https://www2.daad.de/ausland/studieren/stipendium/de/70-stipendien-finden-und-bewerben/?detail=57503530 | 1 | Official programme call | Comparator programme; corroborates Studienplan conventions | **A** (for that programme) |
| DAAD — Chancen.Digital / digitales Masterstudium (57694370) | https://www2.daad.de/ausland/studieren/stipendium/de/70-stipendien-finden-und-bewerben/?detail=57694370 | 1 | Official programme call | **Source of the "quality-assurance section" requirement — belongs to THIS variant, not the standard one** | **A** (for that variant) |
| DAAD — Digitale Option im Programm „Master im Ausland" | https://www.daad.de/de/im-ausland-studieren-forschen-lehren/stipendien-finanzierung/digitales-masterstudium/ | 1 | Official guidance | Same — scope boundary for the QA-section rule | **A** |
| DAAD — Forschungsstipendien (Postdoc, 57243862) | https://www2.daad.de/ausland/studieren/stipendium/de/70-stipendien-finden-und-bewerben.pdf?detail=57243862 | 1 | Official programme call | Contrast case: research-grant criteria ("Originalität, Aktualität, Relevanz"; "Durchführbarkeit und Konsistenz des Arbeits- und Zeitplans") — used in §2 to distinguish genres | **A** (for that programme) |
| Uni Bremen — Hilfe für DAAD-Bewerbungen | https://www.uni-bremen.de/fileadmin/user_upload/sites/international/Studieren_im_Ausland/Bewerbungshilfe_fuer_Studierende.pdf | 2 | University int'l office PDF | Studienplan must show "Bedeutung und Mehrwert"; researching the host institution in advance demonstrates motivation and initiative; Diploma Supplement / grading scale as annexes | **C** |
| HS Aalen — DAAD-Stipendien: Wie bewerbe ich mich richtig? | https://www.hs-aalen.de/uploads/mediapool/media/file/1972/2660_1_DAAD_Informationsdokument_Wie_bewerben.pdf | 2 | University int'l office PDF | Criteria decomposition (Motivation / Qualifikation / Vorbereitung with sub-criteria) | **C** (corroborates A) |
| GOstralia!-GOmerica! — DAAD Bewerbungsleitfaden | https://gostralia-gomerica.de/fileadmin/user_upload/gostralia-gozealand/Bewerbungsdokumente/DAAD_Bewerbungsleitfaden.pdf | 3 | Advisory-service guide | Max 5 pp.; **tabular overview of all courses for all semesters**; per-course justification; host-choice justification; integration into overall degree | **C** |
| FU Berlin — Die Bewerbung beim DAAD (FAQ brochure) | https://www.fu-berlin.de/studium/international/media/Hinweise_DAAD_Brosch__re_2014-15.pdf | 2 | University int'l office PDF | Corroborates tabular course-overview structure. **⚠ 2014/15 edition — dated; use only as corroboration** | **C** (dated) |
| Uni Hannover IPW — DAAD-Stipendium Masterstudiengänge im Ausland: Bewerbungsprozess & Tipps | https://www.ipw.uni-hannover.de/fileadmin/ipw/AB5_Dateien/Departmental_International_Office_-_DIO/DAAD_Bewerbungsprozess.pdf | 2 | Departmental int'l office PDF | Studienplan and Motivationsschreiben are decisive for this programme | **C** |
| studieren-weltweit.de — DAAD-Stipendium für einen Master im Ausland | https://www.studieren-weltweit.de/infocard/stipendium-master-im-ausland/ | 2 | DAAD-affiliated portal | Programme overview; funding figures; document list | **C** |
| e-fellows.net — DAAD Stipendien Masterstudium im Ausland | https://www.e-fellows.net/stipendien-datenbank/daad-stipendien-fuer-ein-masterstudium-im-ausland | 3 | Scholarship database | Document list corroboration | **C** |
| WiWi-TReFF forum — DAAD Studienvorhaben / DAAD-Stipendium threads | https://www.wiwi-treff.de/Stipendien-and-Finanzierung/DAAD-Studienvorhaben/Diskussion-5659 · .../DAAD-Stipendium-fuer-ein-Mastersutudium-im-Ausland/Diskussion-101641 | 3 | Applicant forum | Applicant-perception context only. **Not used for any recommendation.** | **D** |

### 10.2 Cambridge sources

| Source | URL | Tier | Type | What it supports | Class. |
|---|---|---|---|---|---|
| IfM — Masters in ISMM (main course page) | https://www.ifm.eng.cam.ac.uk/education/industrial-systems-manufacture-management-course/ | 1 | Official course page | Course identity; one-year MPhil; positioning | **A** |
| IfM — Course overview | https://www.ifm.eng.cam.ac.uk/education/industrial-systems-manufacture-management-course/course-overview/ | 1 | Official course page | **11 months taught + 1 month assessment**; start beginning of October; 'learn it / see it / do it'; taught modules + company visits + in-company projects; integrated-view scope sentence incl. "data and simulation" | **A** |
| IfM — Course content | https://www.ifm.eng.cam.ac.uk/education/ismm/course/ | 1 | Official course page | 8 weeks project work / 4 projects; 2-week overseas study tour (mainland Europe or further afield); 3 weeks Christmas + 1 week Easter; **18-week dissertation with IfM researchers**; "whole value chain" incl. industrial sustainability | **A** |
| IfM — Taught modules (ISMM) | https://www.ifm.eng.cam.ac.uk/education/ismm/course/taught/ | 1 | Official course page | **M0 induction + 5 core + 1 elective**; **Industrial Systems** module description | **A** |
| IfM — Taught modules (alt. path) | https://www.ifm.eng.cam.ac.uk/education/industrial-systems-manufacture-management-course/taught-modules/ | 1 | Official course page | **Manufacturing Processes**, **Operations and Supply Chain**, **Data and Modelling**, **New Business Development** descriptions; teaching mode (lectures, case studies, exercises, structured visits, industry visitors) | **A** |
| IfM — Projects (ISMM) | https://www.ifm.eng.cam.ac.uk/education/ismm/course/projects/ | 1 | Official course page | 4 company projects in pairs, 2 weeks each; range of company sizes; "live business or technical problems"; "what makes ISMM unique" | **A** |
| IfM — Assessment and feedback | https://www.ifm.eng.cam.ac.uk/education/ismm/assessment-and-feedback/ | 1 | Official course page | **Six modules** each by independent coursework (~3,000-word report / group exercise + presentation / class test); **4 industry projects assessed independently** (presentation to host company + executive summary); **integrative 'big issue' essay**; **dissertation ≤15,000 words**; enquiries address | **A** |
| IfM — Why ISMM? | https://www.ifm.eng.cam.ac.uk/education/ismm/whyismm/ | 1 | Official course page | Programme positioning for §7 page 5 | **A** |
| IfM — How to apply | https://www.ifm.eng.cam.ac.uk/education/industrial-systems-manufacture-management-course/how-to-apply/ | 1 | Official course page | Admissions route (for the Machbarkeit paragraph) | **A** |
| IfM — Contact us (ISMM) | https://www.ifm.eng.cam.ac.uk/education/industrial-systems-manufacture-management-course/contact-us/ | 1 | Official course page | `ismm-enquiries@eng.cam.ac.uk` — route for resolving §9.2 items 3–7 | **A** |
| IfM — Features and news from ISMM | https://www.ifm.eng.cam.ac.uk/education/ismm/features-and-news/ | 1 | Official news page | Not yet mined — potential source of project/dissertation examples | — |
| Cambridge Postgraduate Study — MPhil in Industrial Systems, Manufacture, and Management | https://www.postgraduate.study.cam.ac.uk/courses/directory/egegmpimm | 1 | Official course directory | Official course identity and code `egegmpimm` | **A** |
| Cambridge Dept. of Engineering — Taught courses (MPhil and MRes) | https://www.eng.cam.ac.uk/postgraduates/postgraduate-courses/taught-courses-mphil-and-mres | 1 | Official department page | Departmental placement of ISMM | **A** |
| IfM Engage — Courses | https://engage.ifm.eng.cam.ac.uk/courses/ | 1 | Official IfM page | Existence of IfM Engage only. Not part of ISMM. | **A** (existence) |
| IfM — MET module pages (Industrial Systems, Operations and Services; Manufacturing Systems Engineering; Sustainable Manufacturing) | https://www.ifm.eng.cam.ac.uk/education/met/b/industrial-systems/ · /met/b/systems/ · /met/b/sustainable/ | 1 | Official course pages | **UNDERGRADUATE MET modules — NOT ISMM.** Listed only to prevent misattribution. | **A** (that they are MET) |
| Third-party aggregators (whatuni, TopUniversities, Mastersportal, Prospects, UCAS, postgrad.com, Uni4Edu, Complete University Guide, cambridgefilmworks, ultimatemanagementsystem, youapply) | various | 3 | Aggregators | **Not used for any factual claim.** Listed because they dominate search results and are a misinformation risk (e.g. the "9 months" / "11 months" duration variants). | **D** — do not cite |

---

*End of Agent 3 output. No application text was drafted, per instruction.*
