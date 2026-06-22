# Autonomous Scholar: Academic Outreach & MEXT Concierge Agent

Autonomous Scholar is an intelligent, multi-skill personal assistant developed inside **Antigravity 2.0** for the **Kaggle 5-Day AI Agents Intensive Vibe Coding Capstone Project**. 

The agent streamlines the highly fragmented process of international graduate school applications and competitive funding opportunities (like the MEXT scholarship) by parsing student credentials, finding matching real-world faculty profiles, and safely preparing high-etiquette cold outreach material.

## Key Features
* **Zero-Configuration Context Ingestion:** Drop your raw `resume.md` and `research_proposal.md` directly into your workspace. No rigid database formatting needed.
* **Dynamic Cross-Border Localization:** Automatically translates computational keywords into target languages (e.g., Japanese characters) to locate hidden laboratory subdomains.
* **Anti-Hallucination Guardrails:** Enforces strict citation constraints. The agent is explicitly forbidden from generating unverified professor data or imaginary publications.
* **Human-in-the-Loop (HITL) Security:** Implements a strict gatekeeping policy. The agent can never execute email delivery actions without an explicit, literal text confirmation string provided by the user.

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
