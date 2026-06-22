Research Proposal 
on 
Computational Linguistics for Next-Generation Pedagogy: Leveraging 
Natural Language Processing and Large Language Models in Educational 
Management Systems 
1. Introduction & Motivation 
Educational platforms including Learning Management Systems (LMS) like Moodle, Canvas, 
and Open edX have become fundamental to modern global education, generating vast 
repositories of digital content. To date, institutional analytics have predominantly relied on 
structured metadata, such as enrollment figures, clickstream logs, submission timestamps, and 
quantitative grades. While valuable, these metrics fail to capture the qualitative nuances of the 
learning experience. 
The core intellectual and pedagogical value of education is embedded within unstructured textual 
data: student discussion forums, peer-to-peer interactions, qualitative course feedback, 
assignment commentaries, and syllabi learning outcomes. This rich linguistic data remains 
largely unexploited due to its high dimensionality and semantic complexity. 
This research proposes a comprehensive framework that utilizes advanced Natural Language 
Processing (NLP) and Large Language Models (LLMs) to mine, analyze, and interpret textual 
data within educational ecosystems. By transforming passive text into actionable pedagogical 
intelligence, this work seeks to decode the underlying linguistic signals that dictate student 
engagement, course quality, and automated yet empathetic feedback mechanisms. 
2. Research Questions 
To address these gaps, the study will investigate the following foundational research questions: 
• RQ1 (Information Extraction & Sentiment Mining): How can specialized NLP 
techniques—specifically Named Entity Recognition (NER), aspect-based sentiment 
analysis, and dynamic topic modeling—be effectively orchestrated to extract granular, 
real-time insights from highly unstructured student discussions and feedback? 
• RQ2 (Quantitative Pedagogical Metrics): Can we engineer robust, language-based 
computational metrics to objectively quantify course quality, structural clarity, and the 
semantic alignment between stated learning outcomes and actual student discourse? 
• RQ3 (Domain-Specific LLM Adaptation): How can open-source, Japanese-centric 
foundation models (such as Swallow) be optimally fine-tuned or prompted via advanced 
alignment techniques to deliver contextually precise, pedagogically sound, and 
personalized feedback for student submissions? 
• RQ4 (Predictive Linguistics): What specific syntactic, semantic, or conversational 
linguistic patterns serve as statistically significant predictors of student satisfaction, 
persistent engagement, and academic success in digital learning environments? 
3. Methodology & Research Plan 
The research will be executed across four highly integrated phases over a two-year timeline. 
Phase 1: Data Acquisition, Anonymization & Preprocessing    
Phase 2: Core NLP Engine & Pedagogical Metric Engineering  
Phase 3: LLM Domain Adaptation & Instruction Fine-Tuning   
Phase 4: Rigorous Evaluation & Human-centric Validation   
Phase 1: Data Collection & Advanced Preprocessing 
• Data Sourcing: Curate a heterogeneous dataset from public LMS repositories, 
institutional archives, and open educational data lakes containing multi-year student 
discussions, feedback logs, and course syllabi. 
• Privacy & Anonymization: Implement strict differential privacy standards and 
automated named-entity scrubbing pipelines to reliably strip away Personally Identifiable 
Information (PII) before any downstream processing. 
• Text Normalization: Build specialized preprocessing pipelines tailored to educational 
jargon, multi-lingual code-switching (English/Japanese), formulas, and conversational 
shorthand typically found in student forums. 
Phase 2: Core NLP Engine & Metric Engineering 
• Semantic Analytics: Deploy Deep Learning-based NER to map key concepts floating 
through student discourse. Utilize Aspect-Based Sentiment Analysis (ABSA) to isolate 
specific pain points regarding course materials versus instructional delivery. 
• Dynamic Topic Modeling: Employ advanced topic modeling techniques (e.g., 
BERTopic) to track how discussion themes evolve across a semester, catching drop-off 
points or conceptual bottlenecks in real time. 
• Metric Formulation: Construct semantic similarity matrices using dense embedding 
models to score the alignment between a course syllabus (intended outcomes) and forum 
interactions (actual student focus). 
Phase 3: LLM Domain Adaptation (The Swallow Framework) 
• Base Model Selection: Utilize the Swallow LLM series, exploiting its superior 
tokenization and deep foundational understanding of the Japanese language alongside 
standard English capabilities. 
• Adaptation Strategy: Implement Parameter-Efficient Fine-Tuning (PEFT) methods like 
LoRA/QLoRA alongside Direct Preference Optimization (DPO) to ground the model. 
The model will be trained on curated pedagogical instruction datasets to act as a 
supportive teaching assistant. 
• Contextual Guardrails: Implement Retrieval-Augmented Generation (RAG) 
referencing course textbooks and lecture transcripts to minimize factual hallucinations 
and keep automated feedback strictly accurate. 
Phase 4: Evaluation & Validation 
• Statistical Correlation: Run regression analyses to test if our extracted linguistic 
markers reliably predict actual student retention rates and final grades. 
• Comparative Human Evaluation: Set up double-blind user studies where expert 
educators evaluate LLM-generated feedback alongside human instructor feedback, 
scoring on accuracy, clarity, tone, and actionability. 
4. Expected Contributions 
This research aims to deliver distinct contributions to both the computer science and educational 
technology fields: 
1. Open Benchmark Datasets: A fully anonymized, heavily curated dataset of educational 
text, providing a standard baseline for future researchers tackling NLP in education. 
2. Algorithmic Frameworks for Course Assessment: A suite of reproducible, language
driven metrics capable of evaluating course delivery quality without relying solely on 
biased, low-response student surveys. 
3. Localized Low-Resource LLM Insights: Practical empirical strategies on how to 
successfully adapt localized foundation models (like Swallow) to highly specialized, 
empathetic domain tasks like grading and mentoring. 
5. Timeline 
Timeframe 
Key Research Objectives & Deliverables 
Year 1: H1 
Institutional review, secure data pipelines, complete anonymization 
architectures, and establish baseline text preprocessing. 
Year 1: H2 
Construct the core NLP engine (NER, ABSA, Topic Modeling) and 
formulate initial course alignment metrics. Prepare findings for initial 
workshop submission. 
Year 2: H1 
Execute fine-tuning and prompting strategies on the Swallow model. 
Develop the educational RAG system and begin generating feedback loops. 
Year 2: H2 
Conduct rigorous user studies and statistical validations. Finalize the thesis 
body and submit core papers to top-tier NLP or EdTech conferences (e.g., 
ACL, EMNLP, or EDM). 
6. Relevance to Professor Okazaki's Laboratory 
This proposed research is designed to be a natural extension of the pioneering work being done 
in Professor Naoaki Okazaki’s laboratory. 
The lab's prominent leadership on the Swallow project presents an ideal ecosystem for this 
work. While the lab excels at building large-scale, high-performance language models, this 
project offers a direct path to exploring domain adaptation challenges within an socially 
impactful niche education. Applying the lab's established expertise in sentiment analysis, opinion 
extraction, and information retrieval to unstructured classroom text creates a highly 
complementary research synergy. 
By bridging my background in building educational application frameworks with the Okazaki 
Lab’s unparalleled strength in computational linguistics, this research will push forward the 
boundaries of how localized language models can be safely and effectively deployed in real
world educational infrastructure.