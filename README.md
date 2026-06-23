# Autonomous Scholar: Academic Outreach & MEXT Concierge Agent

## Rationale & Problem Definition
Securing admission into elite international graduate programs or fully-funded opportunities like the Japanese government’s MEXT scholarship is an overwhelming administrative bottleneck for students. The process demands that applicants manually parse hundreds of university faculty subdomains, map their own technical skills against highly niche research lab portfolios, and craft flawless, culturally respectful cold outreach emails.

## Solution
Autonomous Scholar is an intelligent, multi-skill personal assistant developed inside **Antigravity 2.0** 
The agent streamlines the highly fragmented process of international graduate school applications and competitive funding opportunities (like the MEXT scholarship) by parsing student credentials, finding matching real-world faculty profiles, and safely preparing high-etiquette cold outreach material.

## Key Features
* **Zero-Configuration Context Ingestion:** Drop your raw `resume.md` and `research_proposal.md` directly into your workspace. No rigid database formatting needed.
* **Dynamic Cross-Border Localization:** Automatically translates computational keywords into target languages (e.g., Japanese characters) to locate hidden laboratory subdomains.
* **Anti-Hallucination Guardrails:** Enforces strict citation constraints. The agent is explicitly forbidden from generating unverified professor data or imaginary publications.
* **Human-in-the-Loop (HITL) Security:** Implements a strict gatekeeping policy. The agent can never execute email delivery actions without an explicit, literal text confirmation string provided by the user.

## Instructions for setup/to start the agent
Launching the Agent in Antigravity 2.0

1. Boot up your standalone **Antigravity 2.0 Desktop Application**.
    
2. Click **Open Workspace** (or `File > Add Folder to Workspace`) and select your `academic-outreach-agent` root folder.
    
3. The platform will automatically scan and register your specialized `.agents/` workflows and structural safety guardrails.
    
4. Click **New Conversation** on the left dashboard pane and enter the execution goal:
    

Plaintext

```
/browser
/goal Read my research_proposal.md. Target the MEXT scholarship at Osaka University. Activate the professor_matcher skill to locate 2 active computer science professors on their domain. Pass that data along to draft a custom outreach email template using email_composer. Present the draft as an artifact for my review.
```

---

## Project Architecture

```text
academic-outreach-agent/
│
├── .agents/
│   ├── rules/
│   │   └── academic_policy.md          # Core safety & grounding rules
│   └── skills/
│       ├── professor_matcher/
│       │   ├── SKILL.md                # Declarative routing parameters
│       │   └── matcher.py              # Computational extraction engine
│       └── email_composer/
│           └── SKILL.md                # Contextual formatting rules
│
├── resume.md                           # User profile drop-zone
├── research_proposal.md                # Research intent file
└── .gitignore                          # Protects your local environment
