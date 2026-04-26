def compute_match_score(jd_text, candidate):
    # simple working version (no heavy models)
    
    skills = candidate["skills"]
    experience = candidate["experience"]
    
    score = 0
    
    # simple keyword match
    for skill in skills:
        if skill.lower() in jd_text.lower():
            score += 1
    
    score = score / len(skills)
    
    # add experience weight
    score += min(experience / 5, 1) * 0.5
    
    return round(score, 2)