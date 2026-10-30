# ⚡ Cynbit ScopeAI: Technical Discovery & Architecture Agent

**Candidate:** Nimendra Giri | **Role:** AI/ML Engineer Intern

Cynbit ScopeAI is a Streamlit proof of concept for turning a client brief into an initial technical scope, architecture-flow description, and project estimate.

**Live application:** [Add deployed Streamlit Cloud URL]

## Core features

- Healthcare and Revio e-commerce sample RFP presets.
- Groq-powered analysis with selectable or auto-detected models, plus a deterministic mock mode.
- Assessment of whether an ML algorithm is appropriate, with a recommendation when relevant.
- Technology-stack explanations, alternatives, and project-fit rationale.
- Written, sequential architecture flow showing which component connects to the next.
- Six-sprint roadmap and risk summary.
- One-click export of the project scope as a Markdown SOW.

## Repository structure

```text
.
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── docs/
    ├── AI_Opportunity_Report.md
    └── Technical_Approach_Report.md
```

## Local setup

```powershell
git clone <repository-url>
cd <repository-folder>
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run app.py
```

To use live analysis, enter a Groq API key in the app's sidebar. The mock engine can be selected to preview the interface without making an LLM request. Keep API keys private; do not commit them to the repository.

## Reports

- [High-Value AI Opportunity Report](docs/AI_Opportunity_Report.md)
- [Technical Approach Report](docs/Technical_Approach_Report.md)

## Deployment

Deploy the repository through Streamlit Community Cloud, select `app.py` as the entry point, and configure `GROQ_API_KEY` through the platform's secrets settings if using a server-side key. The current app also accepts a key through its sidebar. Never commit secrets.

This project is an assessment proof of concept, not a production-ready clinical, compliance, or business decision system. Outputs require review and validation before real-world use.
