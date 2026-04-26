# AI-Powered-Talent-Scouting-Engagement-Agent
AI-powered talent scouting agent that matches, ranks, and engages candidates based on job descriptions.
This is a simple AI-based tool I built to help with candidate screening.

The idea is to reduce manual effort in hiring by:
- matching candidates with a job description
-  ranking them based on relevance
- simulating whether they might be interested
- showing a short explanation for each match

How it works:
You paste a job description, click a button, and the system shows a ranked list of candidates with scores and reasoning.

Tech used:
Python and Streamlit

How to run:
pip install -r requirements.txt
streamlit run app.py

Notes:
This is a prototype. The matching is based on skills and experience, and the interest is simulated.

Future improvements:
(i) better NLP-based matching
(ii) real resume parsing
(iii) integration with job platforms
