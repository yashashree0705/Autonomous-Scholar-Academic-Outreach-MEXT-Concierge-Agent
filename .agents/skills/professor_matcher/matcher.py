import os
import json

def extract_keywords_from_proposal(proposal_path):
    """Reads the local research proposal file and extracts core topics."""
    if not os.path.exists(proposal_path):
        return ["Computer Science"]
        
    with open(proposal_path, 'r', encoding='utf-8') as f:
        content = f.read().lower()
    
    potential_keywords = ["nlp", "machine learning", "compiler design", "computer vision", "distributed systems"]
    found_keywords = [kw for kw in potential_keywords if kw in content]
    
    return found_keywords if found_keywords else ["Computer Science Faculty"]

def search_faculty(keywords, university="Kyoto University"):
    """
    Simulates calling the built-in Antigravity browser tool 
    to scrape or search faculty profiles safely.
    """
    print(f"[Antigravity Skill] Initializing /browser search for: {keywords} at {university}...")
    
    # Mock output matching your requirements for execution testing:
    mock_results = [
        {
            "professor": "Dr. Kenji Tanaka",
            "lab": "Intelligent Systems Lab",
            "recent_paper": "Optimizing Transformers for Low-Resource Languages (2025)",
            "email": "tanaka.k@kyoto-u.ac.jp"
        }
    ]
    return mock_results

if __name__ == "__main__":
    proposal = "research_proposal.md" 
    keywords = extract_keywords_from_proposal(proposal)
    matches = search_faculty(keywords)
    print(json.dumps(matches, indent=2))