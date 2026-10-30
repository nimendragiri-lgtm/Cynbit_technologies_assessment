# ⚡ Cynbit ScopeAI: Technical Discovery & Architecture Agent
> Technical Assessment Submission for **AI/ML Engineer Intern** at **Cynbit Technologies**  
> **Applicant:** Nimendra Giri  
> **Target Entity:** [Cynbit Technologies](https://www.cynbit.in/)  

---

## 🚀 Live Application & Resources
* **Live Interactive Demo:** [https://nimendragiri-lgtm-cynbit-technologies-assessment-app-91puum.streamlit.app/](https://nimendragiri-lgtm-cynbit-technologies-assessment-app-91puum.streamlit.app/)
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

## 📋 Assessment Deliverables Summary

| Deliverable | Description | Link |
| :--- | :--- | :--- |
| **Interactive Prototype** | Streamlit Web App with live Groq LLM & deterministic fallback | [Launch App](https://nimendragiri-lgtm-cynbit-technologies-assessment-app-91puum.streamlit.app/) |
| **AI Opportunity Report** | Strategic market analysis, Cynbit ecosystem mapping & ROI projections | [View Report](docs/AI_Opportunity_Report.md) |
| **Technical Approach Report** | System architecture, pipeline design, tradeoffs & execution plan | [View Report](docs/Technical_Approach_Report.md) |
| **GitHub Repository** | Source code, architecture specifications, and setup instructions | [View Repository](https://github.com/nimendragiri-lgtm/Cynbit_technologies_assessment) |

---

## 👤 Author
* **Applicant:** Nimendra Giri
* **Role:** AI/ML Engineer Intern Assessment Submission
* **Target Entity:** [Cynbit Technologies](https://www.cynbit.in/)