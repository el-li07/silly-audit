from rules import KEYWORDS, THREATS, RECOMMENDATIONS
from ticket import generate_ticket

def find_matches(text, rules):
    matches = []

    for category, keywords in rules.items():
        for keyword in keywords:
            if keyword in text:
                matches.append(category)
                break

    return matches

def analyze(text):
    text = text.lower()

    return {
        "actions": find_matches(text, KEYWORDS["actions"]),
        "assets": find_matches(text, KEYWORDS["assets"]),
        "modifiers": find_matches(text, KEYWORDS["modifiers"]),
        "actors": find_matches(text, KEYWORDS["actors"]),
    }

def score_threat(analysis, threat):
    score = 0

    for field, conditions in threat["conditions"].items():
        actual_values = analysis[field]

        for value, points in conditions.items():
            if value in actual_values:
                score += points

    return score

def score_all_threats(analysis):
    results = []

    for threat in THREATS:
        score = score_threat(analysis, threat)

        results.append({
            "threat": threat,
            "score": score,
        })

    return results

def detect_threat(analysis):
    results = score_all_threats(analysis)

    best_match = max(results, key=lambda result: result["score"])

    if best_match["score"] == 0:
        return None

    return best_match

def detect_threat(analysis):
    results = score_all_threats(analysis)

    best_match = max(results, key=lambda result: result["score"])

    if best_match["score"] == 0:
        return None

    return best_match

def get_recommendations(analysis):
    recommendations = []

    for field, values in analysis.items():
        field_rules = RECOMMENDATIONS.get(field, {})

        for value in values:
            recommendations.extend(
                field_rules.get(value, [])
            )

    return list(dict.fromkeys(recommendations))

def main():
    print("SILLY AUDIT")
    print("Describe the incident.")
    print()

    text = input("> ")

    analysis = analyze(text)
    result = detect_threat(analysis)
    recommendations = get_recommendations(analysis)

    ticket = generate_ticket(
        analysis,
        result,
        recommendations
    )

    print(ticket)

if __name__ == "__main__":
    main()