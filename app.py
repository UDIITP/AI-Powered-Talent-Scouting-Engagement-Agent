import streamlit as st
import json
from matcher import compute_match_score
from chat import simulate_interest
def generate_reason(c):
    skills = ", ".join(c["skills"])
    exp = c["experience"]

    return f"{c['name']} seems like a strong candidate with experience in {skills}. They have around {exp} years of experience, which fits well for this role."

st.set_page_config(page_title="AI Talent Agent", layout="wide")

st.title("🤖 AI Talent Scouting & Engagement Agent")

jd = st.text_area("📄 Paste Job Description", height=150)

if st.button("🔍 Find Candidates"):
    with open("data/candidates.json") as f:
        candidates = json.load(f)

    results = []

    for c in candidates:
        match_score = compute_match_score(jd, c)
        chat_response, interest_score = simulate_interest(c)

        results.append({
            "name": c["name"],
            "match": match_score,
            "interest": interest_score,
            "reason":generate_reason(c),
            "chat": chat_response
        })

    results = sorted(results, key=lambda x: (x["match"], x["interest"]), reverse=True)
    
    st.subheader("📊 Ranked Candidates")

    for i, r in enumerate(results):
        with st.container():
            if i == 0:
                 st.success("🏆 Top Match")
            st.markdown(f"### 👤 {r['name']}")
            col1, col2 = st.columns(2)

            with col1:
                st.metric("Match Score", f"{int(r['match']*100)}%")
                st.metric("Interest Score", f"{int(r['interest']*100)}%")

            with col2:
                st.markdown("**🧠 Why this candidate?**")
                st.info(r["reason"])

                st.markdown("**💬 Candidate says:**")
                st.success(r["chat"])
                

            st.divider()