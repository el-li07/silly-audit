def generate_ticket(analysis, result, recommendations):
    if result is None:
        return """
----------------------------------------
  ______   _ _   _   _____  ____ ____
  [__ ||   |  \_/    |__||  ||  \| |
  ___]||___|___|     |  ||__||__/| | 

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
  ______   _ _   _   _____  ____ ____
  [__ ||   |  \_/    |__||  ||  \| |
  ___]||___|___|     |  ||__||__/| | 

----------------------------------------

Threat: {threat["name"]}

Asset: {assets}

Actor: {actors}

Severity: {threat["severity"]}

Recommendations:
{recommendation_text}

----------------------------------------
"""