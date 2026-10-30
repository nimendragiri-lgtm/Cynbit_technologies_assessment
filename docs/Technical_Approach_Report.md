# Technical Approach Report: Architecture, Pipeline, and Execution Plan for Cynbit ScopeAI

**Candidate:** Nimendra Giri | **Role:** AI/ML Engineer Intern

## 1. System Architecture & Multi-Tier Topology

The current proof of concept runs as a Streamlit application:

1. **Streamlit UI** collects the client organization, project name, brief, target platforms, compliance preferences, and reasoning-engine selection.
2. **Validation and decoding layer** selects mock or live inference, requests structured output, strips optional code fences, decodes a JSON object, and normalizes technology-stack entries for display.
3. **Groq-hosted Llama model** optionally generates the technical scope. Auto-detection lists available models and selects a preferred supported candidate. The selected model can vary based on account availability.
4. **Deterministic mock fallback** supplies a fixed sample result when mock mode is selected or live inference/decoding raises an error. It keeps the UI demonstrable but is not a project-specific analysis engine.
5. **Streamlit results and SOW export** display the summary, ML assessment, technology stack, written architecture flow, roadmap, and risks, and generate a downloadable Markdown SOW.

The topology is therefore:

**Streamlit UI -> input collection -> Groq/Llama inference or mock engine -> JSON decoding and normalization -> results view -> Markdown SOW export**

The prototype does not currently have a separate deployed API tier, persistent database, or external CRM/EHR/Shopify integration. Those require additional design and implementation.

## 2. Model Selection Rationale

- **Llama 3.3 70B Versatile:** a candidate for more complex reasoning and richer structured drafts, subject to provider availability, latency, and quota.
- **Llama 3.1 8B Instant:** a candidate for faster, lower-latency prototyping and simpler requests, subject to the same availability constraints.
- **Auto-detect:** queries the provider's available model list and prefers configured candidates, with a fallback selection if model discovery fails.
- **Deterministic Mock Engine:** returns a fixed sample response without calling the LLM provider. It supports offline-style UI demonstrations when the local app is available, but does not analyze the entered brief.

Model names and availability can change. Confirm the current Groq account's supported models and JSON-mode behavior before deployment. Model output remains probabilistic and must be validated and reviewed.

## 3. Data Pipeline & Parser Sanitation

The live request asks the provider for a JSON object and uses the SDK's JSON response mode. The response handling then:

1. Reads the response content and rejects an empty or non-object response.
2. Strips optional Markdown JSON fences if present.
3. Uses Python's JSON decoder to decode the first object, avoiding the prior failure when extra trailing text followed a valid object.
4. Checks that `tech_stack_analysis` is a list and wraps string entries as technology objects for compatibility with the UI.
5. Uses safe display defaults for some missing fields and falls back to the deterministic mock result if the live inference path raises an exception.

This is response sanitation, **not complete schema enforcement**. A production version should validate every required field and nested type with a schema (for example, Pydantic), reject or repair invalid values in a controlled way, and test truncated responses, unexpected types, and provider errors. It should also avoid implying that a fallback is a live project-specific result.

## 4. Deep Tech Stack Decision Matrix

The following technologies are candidates in generated project recommendations. They are not all dependencies or implemented infrastructure in this Streamlit proof of concept.

| Technology | Potential role | Why it may fit | Alternatives considered |
|---|---|---|---|
| **FastAPI** | Backend APIs and integration services for a production version | Python ecosystem, typed request models, and async request handling can fit AI and integration workloads | Django REST Framework, Flask, Node.js/Express |
| **Next.js 14** | Production web dashboard if the UI outgrows the Streamlit prototype | React ecosystem, server rendering options, and a broad UI/tooling ecosystem | Streamlit for internal tools, React SPA, Vue/Nuxt |
| **Pinecone** | Managed vector search for retrieval over approved case studies and service material | Managed operations and semantic retrieval can support grounded recommendations | pgvector, Qdrant, Weaviate, Milvus |
| **AWS ECS Fargate** | Container deployment for independently scaled services | Managed container orchestration without managing worker nodes directly | AWS App Runner, EKS, Azure Container Apps, Google Cloud Run |

Selection should be based on actual functional, compliance, operational, and cost requirements. The prototype currently uses Streamlit and Groq; it does not provision these proposed services.

## 5. Three-Phase Execution Roadmap

### Phase 1: Streamlit proof of concept — completed

- Create the Streamlit brief-entry workflow and Healthcare and Revio e-commerce presets.
- Add live Groq analysis and deterministic mock mode.
- Present technology analysis, ML necessity assessment, written route flow, sprint roadmap, and risks.
- Export a Markdown SOW.

### Phase 2: Retrieval-augmented recommendations — proposed

- Curate approved, non-sensitive Cynbit service descriptions and historical case studies.
- Anonymize and obtain authorization for any project examples before indexing.
- Retrieve relevant evidence for each brief and cite sources in the generated draft.
- Evaluate relevance, unsupported claims, latency, and cost before pilot use.

### Phase 3: Workflow integrations — proposed

- Add authenticated CRM and Slack/webhook integrations with explicit user approval.
- Store project drafts and review status with role-based access and audit events.
- Add retry, rate-limit, and observability controls for external services.
- Pilot integrations in a sandbox before enabling production data.

## Deployment Notes

The repository is deployable as a Streamlit app with dependencies in the root `requirements.txt`. For Streamlit Community Cloud, configure secrets through the platform rather than committing keys. Review provider data-handling settings and organizational privacy requirements before submitting client information.
