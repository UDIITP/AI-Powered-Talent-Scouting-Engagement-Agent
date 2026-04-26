import random

def simulate_interest(candidate):
    # make randomness based on candidate name (stable)
    random.seed(candidate["name"])
    
    responses = [
        ("Hey! This role sounds interesting, I’d love to learn more.", 0.9),
        ("This looks like a decent opportunity. Can you share more details?", 0.6),
        ("Thanks for reaching out, but I’m not actively looking right now.", 0.2)
    ]
    
    return random.choice(responses)