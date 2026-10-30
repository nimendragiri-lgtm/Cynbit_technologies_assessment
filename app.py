import streamlit as st
import json
import re

FALLBACK_CANDIDATES = (
    "llama-3.3-70b-versatile",
    "llama-3.1-8b-instant",
    "mixtral-8x7b-32768",
    "gemma2-9b-it",
)


st.set_page_config(
    page_title="Cynbit ScopeAI | Autonomous Technical Scoping",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------- Custom Enterprise Styling -----------------
st.markdown("""
    <style>
    /* Metric Card Custom Container */
    .metric-container {
        display: flex;
        gap: 12px;
        margin-bottom: 20px;
    }
    .custom-card {
        flex: 1;
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
        border: 1px solid #334155;
        border-radius: 12px;
        padding: 16px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.15);
    }
    .custom-card-title {
        color: #94a3b8 !important;
        font-size: 0.78rem !important;
        font-weight: 700 !important;
        text-transform: uppercase !important;
        letter-spacing: 0.06em !important;
        margin-bottom: 6px;
    }
    .custom-card-value {
        color: #38bdf8 !important;
        font-size: 1.45rem !important;
        font-weight: 800 !important;
        white-space: normal !important;
        word-break: break-word !important;
        line-height: 1.2;
    }
    
    /* Tech Stack Cards */
    .stack-analysis-card {
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 10px;
        padding: 14px 18px;
        margin-bottom: 12px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }
    .stack-title {
        font-size: 1.05rem;
        font-weight: 700;
        color: #0f172a;
    }
    .stack-synergy {
        display: inline-block;
        padding: 4px 10px;
        border-radius: 16px;
        background: #ecfdf5;
        color: #065f46;
        border: 1px solid #a7f3d0;
        font-size: 0.8rem;
        font-weight: 600;
        margin-bottom: 6px;
    }
    </style>
""", unsafe_allow_html=True)

# ----------------- Cynbit Knowledge Base -----------------
CYNBIT_SERVICES = """
Cynbit Technologies Core Capabilities:
- Services: Autonomous AI Agents, LLM Automation (document parsing, invoice extraction, workflow automation), AI Voice Assistants, Custom SaaS Platforms, Cloud Migration & DevOps.
- Tech Stack: Python, FastAPI, Django, React, Next.js, LangChain, LlamaIndex, PyTorch, Pinecone, PostgreSQL, Docker, AWS, Azure.
- Proprietary Products: Revio (AI review and feedback intelligence), TenantEase (PropTech operations), Cynbit Studio (EdTech career analytics).
"""

st.title("⚡ Cynbit ScopeAI: Technical Discovery & Architecture Agent")
st.markdown(
    "**Applicant:** Nimendra Giri | **Role Assessment:** AI/ML Engineer Intern  \n"
    "*Automating the bridge between raw client problem briefs and production-grade engineering blueprints.*"
)
st.caption("For the best results and analysis, use your own Groq API key. To preview how the app looks and works, select Mock Engine (Deterministic) in Agent Settings.")
about_col, improvements_col = st.columns(2)
with about_col:
    st.info(
        "**What it is & does**\n"
        "- Turns project briefs into technical scopes and estimates.\n"
        "- Recommends a tech stack and ML approach.\n"
        "- Offers AI-powered or mock analysis."
    )
with improvements_col:
    st.info(
        "**Further improvements**\n"
        "- Add architecture diagrams and downloadable reports.\n"
        "- Connect live data sources and save project history.\n"
        "- Support higher-volume analysis; live AI is subject to Groq API limits."
    )
st.warning(
    "If you encounter an API error, please try again. If it persists, let me know "
    "so I can investigate the issue and improve the app."
)
st.divider()

# ----------------- Sidebar Configuration -----------------
with st.sidebar:
    st.header("⚙️ Agent Settings")
    api_key = st.text_input(
        "Groq API Key (Optional)", 
        type="password", 
        help="Paste your gsk_... key here or use Mock Engine for deterministic review."
    )
    
    model_choice = st.selectbox(
        "Reasoning Engine", 
        [
            "Auto-Detect Available Model",
            "llama-3.3-70b-versatile",
            "llama-3.1-8b-instant",
            "Mock Engine (Deterministic)"
        ]
    )
    
    st.markdown("---")
    st.markdown("### 🏢 Cynbit Ecosystem Alignment")
    st.markdown("""
    - 🤖 **Autonomous Multi-Agent Chains**
    - ⚡ **FastAPI High-Throughput APIs**
    - 🧠 **Vector RAG (Pinecone / Pgvector)**
    - ☁️ **Cloud Native (AWS ECS / Azure)**
    - 📊 **Revio / TenantEase SaaS Hooks**
    """)
    st.caption("Cynbit Technologies Assessment © 2026")

# ----------------- Main Input Area -----------------
HEALTHCARE_PRESET = {
    "client_name": "HealthPulse Systems",
    "project_title": "AI-Powered Patient Triage & EHR Summarization",
    "project_desc": (
        "We need an enterprise platform where physicians upload consultation audio "
        "transcripts and messy medical notes. The system must summarize findings, "
        "extract high-risk medical alerts, map standard ICD-10 diagnostic codes, and "
        "sync automatically into our legacy EHR database. Latency must be under 2s "
        "with strict HIPAA zero-trust cloud security."
    ),
}

REVIO_PRESET = {
    "client_name": "GlobalMarket E-Commerce",
    "project_title": "Revio Multi-Channel Feedback Intelligence",
    "project_desc": (
        "We run a multi-vendor retail marketplace and want an automated system to "
        "collect customer reviews from Amazon, Trustpilot, and our website. It should "
        "use aspect-based sentiment analysis to group feedback by product, alert store "
        "managers when negative trends spike, and draft empathetic responses for "
        "support agents to review and approve before sending. Integrate with our "
        "Shopify store and customer support platform, process up to 20,000 reviews "
        "per day, and show new feedback in the dashboard within five minutes. Provide "
        "a web dashboard and REST API, with a pilot for one product category before "
        "expanding to the full catalog."
    ),
}


def load_preset(preset):
    for field, value in preset.items():
        st.session_state[field] = value


for field, value in HEALTHCARE_PRESET.items():
    st.session_state.setdefault(field, value)

col_left, col_right = st.columns([1, 1], gap="large")

with col_left:
    st.subheader("📋 Inbound RFP & Client Requirements")
    client_name = st.text_input("Client Organization", key="client_name")
    project_title = st.text_input("Project Codename", key="project_title")
    
    preset_cols = st.columns(2)
    with preset_cols[0]:
        st.button(
            "🏥 Load Healthcare RFP",
            use_container_width=True,
            on_click=load_preset,
            args=(HEALTHCARE_PRESET,),
        )
    with preset_cols[1]:
        st.button(
            "🛍️ Load Revio E-Commerce RFP",
            use_container_width=True,
            on_click=load_preset,
            args=(REVIO_PRESET,),
        )

    project_desc = st.text_area(
        "Client Brief / Technical Specifications",
        key="project_desc",
        height=180
    )
    
    b_col1, b_col2 = st.columns(2)
    with b_col1:
        target_platform = st.multiselect("Target Platforms", ["Web App", "REST API", "Mobile App", "Slack/Webhook Bot"], default=["Web App", "REST API"])
    with b_col2:
        compliance_req = st.multiselect("Compliance Standard", ["SOC2", "HIPAA", "GDPR", "Zero-Trust AWS"], default=["HIPAA", "Zero-Trust AWS"])
        
    generate_btn = st.button("🚀 Synthesize Architecture & Estimate Scope", use_container_width=True, type="primary")

# ----------------- Inference Functions -----------------
def mock_inference(title, desc):
    return {
        "summary": "Enterprise-grade asynchronous clinical assistant utilizing medical transcription pipelines, strict entity extraction, and bidirectional EHR synchronization via event-driven microservices.",
        "feasibility_score": "94 / 100",
        "complexity_level": "High (Compliance)",
        "estimated_duration": "10-12 Weeks (6 Sprints)",
        "architecture_overview": (
            "1. Clinician Portal -> API Gateway: submits consultation audio or notes.\n"
            "2. API Gateway -> Authentication and Audit Service: verifies role and logs the request.\n"
            "3. API Gateway -> Audio Processing Queue -> Transcription Worker: transcribes audio.\n"
            "4. Transcription Worker -> Clinical NLP Service: sends the transcript for summarization and entity extraction.\n"
            "5. Clinical NLP Service -> Vector Search: matches clinical terms to coding references.\n"
            "6. Clinical NLP Service -> Clinician Portal: returns draft summary and diagnosis suggestions for review.\n"
            "7. Clinician Portal -> FHIR Integration Service -> Hospital EHR: sends only clinician-approved updates.\n"
            "8. FHIR Integration Service -> Encrypted PostgreSQL: stores approved records; services write audit events."
        ),
        "ml_algorithm_assessment": {
            "needed": "Yes",
            "recommendation": "Clinical-domain transformer (such as BioClinicalBERT) for medical entity recognition and diagnosis classification, with clinician review.",
            "rationale": "It can identify clinical concepts in unstructured notes; validate and evaluate it on representative, de-identified data before clinical use."
        },
        "tech_stack_analysis": [
            {
                "technology": "FastAPI",
                "use_case": "High-throughput asynchronous backend gateway handling low-latency transcription streaming and API routing.",
                "why_needed": "Native Python async support allows non-blocking I/O operations for heavy AI inference calls and fast response cycles (<2s).",
                "alternatives": "Django Ninja, Node.js / Express, Flask"
            },
            {
                "technology": "Next.js 14 + TailwindCSS",
                "use_case": "Physician dashboard interface for review of clinical findings, triage alert badges, and manual edits.",
                "why_needed": "Server-side rendering (SSR) delivers optimal security and fast initial page loads for clinic workstations.",
                "alternatives": "React SPA, Vue.js / Nuxt, Angular"
            },
            {
                "technology": "Whisper API / Open-source Med-Whisper",
                "use_case": "Transcribing ambient audio recordings of doctor-patient consultations into clinical text.",
                "why_needed": "State-of-the-art accuracy on conversational speech and medical domain nomenclature with timestamp alignment.",
                "alternatives": "AWS Transcribe Medical, Google Speech-to-Text, Deepgram"
            },
            {
                "technology": "Pinecone + pgvector",
                "use_case": "Vector similarity search for matching extracted symptoms to standardized ICD-10 diagnostic code directories.",
                "why_needed": "Sub-millisecond semantic retrieval across thousands of medical coding entries with low maintenance overhead.",
                "alternatives": "Qdrant, Milvus, ChromaDB, Weaviate"
            },
            {
                "technology": "AWS ECS (Fargate) & PostgreSQL",
                "use_case": "Containerized orchestration and HIPAA-compliant relational storage for encrypted patient records.",
                "why_needed": "Serverless container management guarantees auto-scaling during peak morning hospital hours without manual server provisioning.",
                "alternatives": "GCP Cloud Run, Kubernetes (EKS), Azure App Services"
            }
        ],
        "cynbit_synergy": [
            "Autonomous Agent Workflow Automation",
            "Custom LLM & Document Extraction Engine",
            "Enterprise AWS Infrastructure & Cloud DevOps"
        ],
        "sprint_breakdown": [
            {"sprint": "Sprint 1", "objective": "Architecture spike, zero-trust HIPAA cloud setup, and PostgreSQL schemas."},
            {"sprint": "Sprint 2", "objective": "Audio ingestion pipeline with asynchronous Celery/Redis worker queues."},
            {"sprint": "Sprint 3", "objective": "ICD-10 clinical entity extraction chain & RAG vector integration."},
            {"sprint": "Sprint 4", "objective": "Bidirectional legacy EHR webhook connectors & role-based access control."},
            {"sprint": "Sprint 5", "objective": "Next.js dashboard engineering with live physician triage alerts."},
            {"sprint": "Sprint 6", "objective": "Load testing, end-to-end security penetration testing, and CI/CD pipelines."}
        ],
        "risk_factors": [
            "HIPAA compliance validation requirement for cloud audio storage buckets.",
            "High variance in noisy ambient audio during physician consultations."
        ]
    }

def run_llm_inference(title, desc, key, selected_model):
    from groq import Groq
    client = Groq(api_key=key.strip())

    target_model = selected_model
    if selected_model == "Auto-Detect Available Model":
        try:
            available = client.models.list().data
            chat_models = [
                m.id for m in available 
                if not any(k in m.id.lower() for k in ["whisper", "guard", "orpheus", "vision", "embed", "canopylabs", "prompt"])
            ]
            chat_model_ids = set(chat_models)
            target_model = next(
                (model for model in FALLBACK_CANDIDATES if model in chat_model_ids),
                chat_models[0] if chat_models else "llama-3.1-8b-instant",
            )
        except Exception:
            target_model = "llama-3.1-8b-instant"

    prompt = f"""You are the Chief Solutions Architect at Cynbit Technologies (cynbit.in).
Analyze this inbound client request and produce a complete, enterprise-grade technical scope.

Cynbit Services & Capabilities: {CYNBIT_SERVICES}

Client Project: {title}
Client Problem Description: {desc}

Respond ONLY with a single valid JSON object. No conversational intro, no markdown text outside the JSON.
Required JSON Keys:
- "summary": string
- "feasibility_score": string (e.g. "92 / 100")
- "complexity_level": string ("Low", "Medium", "High")
- "estimated_duration": string (e.g. "10-12 Weeks (6 Sprints)")
- "architecture_overview": string with one numbered connection per line in the format "Source Node -> Destination Node: what data or action moves"; keep each explanation concise and understandable, include decision/response paths where relevant, and do not produce Mermaid or a diagram
- "ml_algorithm_assessment": object with keys "needed" (Yes or No), "recommendation" (name a suitable algorithm/model if needed, otherwise explain why none is needed), and "rationale"
- "tech_stack_analysis": list of objects with keys:
    * "technology": Name of the tool/framework
    * "use_case": Exact role in this specific client project
    * "why_needed": Architectural justification and benefits
    * "alternatives": Viable industry alternatives
- "cynbit_synergy": list of strings
- "sprint_breakdown": list of objects with keys "sprint" and "objective"
- "risk_factors": list of strings
"""

    response = client.chat.completions.create(
        model=target_model,
        messages=[
            {"role": "system", "content": "You are a software architect that outputs strictly raw JSON. Never output markdown code fences, backticks, or introductory chat."},
            {"role": "user", "content": prompt}
        ],
        response_format={"type": "json_object"},
        temperature=0.1,
        max_tokens=3000
    )
    
    raw_content = response.choices[0].message.content or ""
    raw_content = raw_content.strip()
    
    # Strip markdown backticks if model wrapped it in ```json ... ```
    if raw_content.startswith("```"):
        raw_content = re.sub(r"^```(?:json)?", "", raw_content, flags=re.IGNORECASE).strip()
        raw_content = re.sub(r"```$", "", raw_content).strip()
        
    start_idx = raw_content.find("{")
    if start_idx == -1:
        raise ValueError("The AI response did not contain a JSON object.")

    result, _ = json.JSONDecoder().raw_decode(raw_content, start_idx)
    if not isinstance(result, dict):
        raise ValueError("The AI response JSON must be an object.")

    tech_stack = result.get("tech_stack_analysis", [])
    if isinstance(tech_stack, str):
        tech_stack = [tech_stack]
    if not isinstance(tech_stack, list):
        raise ValueError("The AI response tech_stack_analysis must be a list.")
    result["tech_stack_analysis"] = [
        item if isinstance(item, dict) else {"technology": item}
        for item in tech_stack
        if isinstance(item, (dict, str))
    ]
    return result

# ----------------- Right Column: Results & Visualization -----------------
with col_right:
    st.subheader("📊 Architectural Blueprint & Estimation")
    if generate_btn:
        with st.spinner("Synthesizing system architecture and engineering timeline..."):
            result = None
            if api_key and model_choice != "Mock Engine (Deterministic)":
                try:
                    result = run_llm_inference(project_title, project_desc, api_key, model_choice)
                    st.success("✅ Architecture synthesized via Groq LLM Engine.")
                except Exception as e:
                    st.warning(f"Live API fallback: {str(e)}. Rendering deterministic solution.")
                    result = mock_inference(project_title, project_desc)
            else:
                result = mock_inference(project_title, project_desc)
            
            # Key Metrics Cards - Clean HTML (No truncation, proper contrast)
            f_score = result.get("feasibility_score", "90 / 100")
            c_level = result.get("complexity_level", "Medium")
            e_dur = result.get("estimated_duration", "8-10 Weeks")
            
            st.markdown(f"""
            <div class="metric-container">
                <div class="custom-card">
                    <div class="custom-card-title">Feasibility Score</div>
                    <div class="custom-card-value">{f_score}</div>
                </div>
                <div class="custom-card">
                    <div class="custom-card-title">Complexity Level</div>
                    <div class="custom-card-value">{c_level}</div>
                </div>
                <div class="custom-card">
                    <div class="custom-card-title">Estimated Timeline</div>
                    <div class="custom-card-value">{e_dur}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("#### **Executive Technical Summary**")
            st.info(result.get("summary"))
            
            # Interactive Tabs
            tab1, tab2, tab3, tab4 = st.tabs([
                "🏗️ Deep Tech Stack Analysis",
                "🔀 Architecture Flow",
                "📅 6-Sprint Roadmap", 
                "⚠️ Risks & Safeguards"
            ])
            
            with tab1:
                ml_assessment = result.get("ml_algorithm_assessment", {})
                st.markdown("##### ML Algorithm Assessment:")
                st.markdown(
                    f"**Is an ML algorithm needed?** "
                    f"{ml_assessment.get('needed', 'Not assessed')}"
                )
                st.markdown(
                    f"**Recommendation:** "
                    f"{ml_assessment.get('recommendation', 'Not provided')}"
                )
                st.markdown(
                    f"**Rationale:** "
                    f"{ml_assessment.get('rationale', 'Not provided')}"
                )

                st.markdown("##### Detailed Component Justification & Tradeoffs:")
                tech_list = result.get("tech_stack_analysis", [])
                
                if tech_list:
                    for t in tech_list:
                        tech_name = t.get("technology", "Framework")
                        use_case = t.get("use_case", "Core implementation module.")
                        why_needed = t.get("why_needed", "Provides required performance.")
                        alternatives = t.get("alternatives", "Custom solutions")
                        
                        st.markdown(f"""
                        <div class="stack-analysis-card">
                            <div class="stack-title">🔧 {tech_name}</div>
                            <p style="margin: 6px 0 4px 0; color: #1e293b; font-size: 0.92rem;"><strong>Role in Project:</strong> {use_case}</p>
                            <p style="margin: 0 0 4px 0; color: #475569; font-size: 0.90rem;"><strong>Why We Need It:</strong> {why_needed}</p>
                            <p style="margin: 0; color: #64748b; font-size: 0.85rem;"><strong>Viable Alternatives:</strong> <em>{alternatives}</em></p>
                        </div>
                        """, unsafe_allow_html=True)
                else:
                    for s in result.get("recommended_stack", []):
                        st.markdown(f"- 🔧 `{s}`")
                
                st.markdown("##### Cynbit Core Synergy Alignment:")
                for syn in result.get("cynbit_synergy", []):
                    st.markdown(f'<span class="stack-synergy">⚡ {syn}</span>', unsafe_allow_html=True)


            with tab2:
                st.markdown("##### Written Architecture Flow:")
                st.caption("Follow the numbered steps in order. Each arrow shows which component sends data or a request to the next.")
                architecture_overview = result.get(
                    "architecture_overview",
                    "Architecture flow was not provided.",
                )
                if isinstance(architecture_overview, str) and architecture_overview.strip():
                    architecture_steps = re.split(
                        r"\s+(?=\d+[.)]\s)",
                        architecture_overview.strip(),
                    )
                    if len(architecture_steps) == 1 and "\n" in architecture_overview:
                        architecture_steps = architecture_overview.splitlines()

                    for index, step in enumerate(architecture_steps, start=1):
                        step = re.sub(r"^\s*\d+[.)]\s*", "", step).strip()
                        if not step:
                            continue
                        route, separator, explanation = step.partition(":")
                        if separator:
                            st.markdown(f"**{index}. {route.strip()}**")
                            st.write(explanation.strip())
                        else:
                            st.markdown(f"**{index}.** {step}")
                else:
                    st.write("Architecture flow was not provided.")
            
            with tab3:
                st.markdown("##### Engineering Milestones:")
                for sp in result.get("sprint_breakdown", []):
                    with st.expander(
                        f"📌 {sp.get('sprint', 'Sprint not provided')}: "
                        f"{sp.get('objective', 'Objective not provided')}",
                        expanded=True,
                    ):
                        st.write("Target Deliverables: Code scaffolding, test fixtures, integration hooks.")
                        
            with tab4:
                st.markdown("##### Identified Technical Risks & Mitigations:")
                for r in result.get("risk_factors", []):
                    st.warning(f"⚠️ {r}")
            
            # Downloadable Statement of Work Export
            tech_sow_lines = []
            for t in result.get("tech_stack_analysis", []):
                tech_sow_lines.append(f"- **{t.get('technology')}**: {t.get('use_case')} (Why: {t.get('why_needed')} | Alternatives: {t.get('alternatives')})")
            
            tech_summary_block = chr(10).join(tech_sow_lines) if tech_sow_lines else chr(10).join(['- ' + s for s in result.get('recommended_stack', [])])

            sow_markdown = f"""# Statement of Work (SOW) - Cynbit Technologies
**Project:** {project_title}  
**Client:** {client_name}  
**Feasibility:** {result.get('feasibility_score')} | **Estimated Duration:** {result.get('estimated_duration')}

## Executive Summary
{result.get('summary')}

## Written Architecture Flow
{result.get('architecture_overview', 'Architecture overview was not provided.')}

## Proposed Tech Stack & Component Justifications
{tech_summary_block}

## Sprint Roadmap
{chr(10).join([f"- **{s.get('sprint', 'Sprint not provided')}**: {s.get('objective', 'Objective not provided')}" for s in result.get('sprint_breakdown', [])])}

## Risk Assessment
{chr(10).join(['- ' + r for r in result.get('risk_factors', [])])}

---
*Generated autonomously via Cynbit ScopeAI Discovery Agent*
"""
            st.divider()
            st.download_button(
                label="📥 Download Client SOW Document (.md)",
                data=sow_markdown,
                file_name=f"Cynbit_SOW_{client_name.replace(' ', '_')}.md",
                mime="text/markdown",
                use_container_width=True
            )
            
    else:
        st.info("👈 Select or modify the client brief on the left, then click **Synthesize Architecture & Estimate Scope**.")