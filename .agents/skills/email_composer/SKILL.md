---
name: email_composer
description: Reads user resume/transcripts and drafts highly tailored, context-aware cold emails to targeted academic professors.
triggers:
  - "draft cold email"
  - "write email template"
  - "prepare outreach"
dependencies:
  - .agents/skills/professor_matcher
---

# Cold Email Composer Skill

## Cultural & Contextual Formatting Rules

### East Asian Academic Contexts (e.g., MEXT, Japan, Korea)
* **Tone:** Ultra-formal, polite, and respectful of hierarchy. Use proper honorifics.
* **Length:** Strictly under 250 words.
* **Structure:** State your current university/status immediately, clearly state your intent (seeking MEXT supervision), explicitly reference one specific recent paper they published, and ask for a brief window to discuss your research proposal.

### Western Academic Contexts (e.g., US, Europe)
* **Tone:** Professional, direct, and outcome-oriented.
* **Length:** Under 200 words.
* **Structure:** Hook them with how your background directly bridges a gap in their current lab focus. Keep the call to action low-friction.

## Workspace Alignment Blueprint
When drafting the email body:
1. Scan the local `resume.md` or `transcripts.md` in the root workspace directory.
2. Cross-reference the student's highest achievements with the professor's recent projects found by the `professor_matcher` skill.
3. Insert these elements seamlessly into the template text without sounding generic.