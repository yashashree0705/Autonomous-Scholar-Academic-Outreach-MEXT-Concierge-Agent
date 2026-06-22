---
name: professor_matcher
description: Dynamically extracts research topics and uses live web browsing to find matching professors across global universities.
triggers:
  - "find professors"
  - "search university directories"
  - "target university"
tools:
  - builtins/google_search
  - builtins/url_context
---

# Global Professor Search Protocol

## 1. Domain & Country Analysis
* Read the user's local `research_proposal.md` to flag tech keywords.
* Identify the target country and institution from the user prompt.

## 2. Localization Adjustments (e.g., Japan / MEXT)
* If the user specifies **Japan** or **MEXT**:
  1. Translate core technical keywords into Japanese (e.g., "Machine Learning" ➔ "機械学習").
  2. Execute a search query structured specifically to find laboratory landing pages: 
     `"site:.ac.jp [University Name] [English Keyword] OR [Japanese Translated Keyword] lab OR faculty"`
* For **Western countries** (US/Europe):
  1. Use standard academic strings: `"site:.edu [University Name] computer science faculty [Keyword]"`

## 3. Data Compilation
* Use the `url_context` tool to read the text of the top faculty pages.
* Extract: Professor Name, Email, Lab Title, and a quote or paper title from their recent work.
* Output this directly into a workspace file named `found_professors.md`.