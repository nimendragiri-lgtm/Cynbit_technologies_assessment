# ⚡ Cynbit ScopeAI: Technical Discovery & Architecture Agent
> Technical Assessment Submission for **AI/ML Engineer Intern** at **Cynbit Technologies**  
> **Applicant:** Nimendra Giri  
> **Target Entity:** [Cynbit Technologies](https://www.cynbit.in/)  

---

## 🚀 Live Application & Resources
* **Live Interactive Demo:** [Insert your deployed Streamlit App link here]
* **Primary GitHub Repository:** [nimendragiri-lgtm/Cynbit_technologies_assessment](https://github.com/nimendragiri-lgtm/Cynbit_technologies_assessment)
* **AI Opportunity Report:** `docs/AI_Opportunity_Report.md`
* **Technical Approach Report:** `docs/Technical_Approach_Report.md`

---

## 📌 Project Overview
**Cynbit ScopeAI** is an autonomous client discovery and technical scoping platform designed to eliminate the operational bottleneck in Cynbit’s pre-sales workflow. 

It ingests unstructured client RFPs and problem briefs, analyzes whether machine learning is required, aligns project requirements with Cynbit's core technical stack (FastAPI, React/Next.js, LangChain, Pinecone, AWS), generates sequential architecture dataflows, outlines a 6-sprint development roadmap, and exports client-ready Statements of Work (SOWs) in one click.

---

## 🌟 Key Engineering Highlights
* **Dynamic Model Orchestration:** Interacts with Groq Cloud LLM endpoints (`llama-3.3-70b-versatile`, `llama-3.1-8b-instant`) with an auto-detecting model registry.
* **Resilient Offline Fallback:** Integrated with a deterministic mock engine that guarantees 100% demo availability even without API keys or in case of rate limits.
* **Robust Parser Sanitation:** Employs boundary-seeking JSON decoders (`json.JSONDecoder().raw_decode`) and regex cleaners to eliminate JSON parse failures.
* **Deep Tech Stack Matrix:** Evaluates every proposed technology with its exact project role, architectural necessity, and evaluated industry alternatives.
* **Cynbit Ecosystem Synergy:** Automatically detects cross-sell opportunities with Cynbit's proprietary products, such as **Revio** for multi-channel review analytics.

---

## 📂 Repository Structure

```text
cynbit-scope-ai/
├── app.py                            # Streamlit Prototype & Orchestrator
├── requirements.txt                  # Dependencies
├── README.md                         # Documentation & Architecture
└── docs/
    ├── AI_Opportunity_Report.md      # Strategic Business Opportunity Report
    └── Technical_Approach_Report.md  # Architecture, Pipeline & Execution Plan
```

---

## 🛠️ Quickstart (Run Locally)

1. **Clone the repository:**
   ```bash
   git clone https://github.com/nimendragiri-lgtm/Cynbit_technologies_assessment.git
   cd Cynbit_technologies_assessment
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Launch the application:**
   ```bash
   streamlit run app.py
   ```
   *(Note: The app contains a deterministic mode, so it functions immediately without an external API key).*

---

### Deliverable 5: Submission Portal Form Filling Guide

When submitting your work in the candidate portal:

#### Links Structure
* **Primary Deliverable Link \*:**  
  `https://github.com/nimendragiri-lgtm/Cynbit_technologies_assessment`
* **Additional Link 1:**  
  `https://<your-app-name>.streamlit.app` *(Streamlit Cloud Live App)*
* **Additional Link 2:**  
  `https://github.com/nimendragiri-lgtm/Cynbit_technologies_assessment/blob/main/docs/AI_Opportunity_Report.md` *(AI Opportunity Report)*
* **Additional Link 3:**  
  `https://github.com/nimendragiri-lgtm/Cynbit_technologies_assessment/blob/main/docs/Technical_Approach_Report.md` *(Technical Approach Report)*

#### Text for "Execution Notes & Campaign Rationale (Optional)"
Paste this directly into the portal text box:

```text
Applicant: Nimendra Giri
Role: AI/ML Engineer Intern
Target: Cynbit Technologies (cynbit.in)

Challenge Overview & Approach:
After analyzing Cynbit's service catalog (Autonomous Agents, LLM Automation, Cloud Migration, Full-Stack Engineering) and proprietary SaaS portfolio (Revio, TenantEase, Cynbit Studio), I identified that Cynbit's largest pre-sales bottleneck lies in the manual translation of unstructured client requirements into technical blueprints and SOWs.

To address this, I built "Cynbit ScopeAI" — an autonomous technical discovery agent that:
1. Ingests raw client problem briefs and RFPs (including built-in test presets for Healthcare Triage and Revio E-Commerce Feedback Intelligence).
2. Evaluates whether ML is needed, recommending domain-specific transformer architectures with clinician or human-in-the-loop validation.
3. Performs a deep tech stack tradeoff analysis (FastAPI, Next.js, Pinecone, AWS ECS) outlining exact use cases, architectural justification, and viable alternatives.
4. Generates a clear sequential architecture route flow, a 6-sprint milestone plan, and risk mitigations.
5. Provides a 1-click downloadable Statement of Work (SOW) markdown export.

Deliverables Provided:
- Complete GitHub Repository with clean git history, documentation, and architecture specifications.
- Live Interactive Streamlit Prototype with dynamic Groq LLM integration and deterministic offline evaluation fallback.
- AI Opportunity Report & Technical Approach Report detailing industry landscape analysis, model choices, data pipeline safeguards, and execution roadmap.
```