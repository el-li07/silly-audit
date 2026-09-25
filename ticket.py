def generate_ticket(analysis, result, recommendations):
    if result is None:
        return """
----------------------------------------
SILLY AUDIT
----------------------------------------

Unable to classify incident.

Recommendation:
Provide additional information.

----------------------------------------
"""

    threat = result["threat"]

    actors = ", ".join(analysis["actors"]) or "Unknown"
    assets = ", ".join(analysis["assets"]) or "Unknown"

    recommendation_text = "\n".join(
        f"- {recommendation}"
        for recommendation in recommendations
    )

    return f"""
----------------------------------------
SILLY AUDIT
----------------------------------------

Threat: {threat["name"]}

Asset: {assets}

Actor: {actors}

Severity: {threat["severity"]}

Recommendations:
{recommendation_text}

----------------------------------------
"""