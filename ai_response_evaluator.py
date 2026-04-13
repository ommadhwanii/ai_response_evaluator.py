import re

def clean_text(text):
    return re.sub(r'[^a-zA-Z\s]', '', text).lower()

def score_response(response, keywords):
    response = clean_text(response)
    score = 0

    # Score based on keyword presence
    for word in keywords:
        if word in response:
            score += 2

    # Score based on length (more informative = better)
    score += len(response.split()) * 0.1

    return score

def evaluate_responses(response_a, response_b, keywords):
    score_a = score_response(response_a, keywords)
    score_b = score_response(response_b, keywords)

    print(f"Response A Score: {score_a}")
    print(f"Response B Score: {score_b}")

    if score_a > score_b:
        print("\nBetter Response: A")
    elif score_b > score_a:
        print("\nBetter Response: B")
    else:
        print("\nBoth responses are equally good")

# Sample Data
response_a = "AI is a powerful technology that helps automate tasks."
response_b = "AI helps in automation."

keywords = ["ai", "technology", "automation", "tasks"]

evaluate_responses(response_a, response_b, keywords)