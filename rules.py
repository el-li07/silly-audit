KEYWORDS = {
    "actions": {
        "consumption": [
            "ate",
            "eaten",
            "drank",
            "consumed",
        ],

        "taking": [
            "took",
            "taken",
            "borrowed",
            "stole",
            "stolen",
        ],

        "damage": [
            "broke",
            "broken",
            "damaged",
            "destroyed",
            "spilled",
        ],

        "movement": [
            "moved",
            "relocated",
            "removed",
        ],
    },

    "assets": {
        "food": [
            "yogurt",
            "cake",
            "dinner",
            "energy drink",
            "cookies",
            "snack",
            "food",
            "lunch",
            "milk",
            "coffee",
        ],

        "property": [
            "charger",
            "headphones",
            "phone",
            "bag",
            "backpack",
            "keys",
            "book",
        ],

        "computer": [
            "computer",
            "laptop",
            "keyboard",
            "mouse",
            "file",
            "account",
            "password",
        ],

        "premises": [
            "door",
            "room",
            "flat",
            "office",
            "apartment",
            "house",
        ],
    },

    "modifiers": {
        "unauthorized": [
            "without asking",
            "without permission",
            "without my permission",
            "behind my back",
        ],

        "repeated": [
            "again",
            "once again",
            "every time",
            "keeps",
            "always",
        ],

        "accidental": [
            "accidentally",
            "by accident",
            "unintentionally",
        ],
    },

    "actors": {
        "coworker": [
            "coworker",
            "colleague",
        ],

        "roommate": [
            "roommate",
            "flatmate",
        ],

        "friend": [
            "friend",
            "bro",
        ],

        "unknown": [
            "someone",
            "somebody",
            "stranger",
        ],

        "cat": [
            "cat",
            "kitten",
        ],
    },
}

THREATS = [
    {
        "name": "Unauthorized Asset Access",

        "conditions": {
            "actions": {
                "taking": 2,
            },
            "assets": {
                "property": 2,
            },
            "modifiers": {
                "unauthorized": 3,
            },
        },

        "severity": "MEDIUM",
    },

    {
        "name": "Unauthorized Consumption",

        "conditions": {
            "actions": {
                "consumption": 3,
            },
            "assets": {
                "food": 3,
            },
        },

        "severity": "LOW",
    },

    {
        "name": "Accidental Asset Damage",

        "conditions": {
            "actions": {
                "damage": 3,
            },
            "modifiers": {
                "accidental": 2,
            },
        },

        "severity": "LOW",
    },

    {
        "name": "Potential Unauthorized Physical Access",

        "conditions": {
            "actions": {
                "movement": 2,
            },
            "assets": {
                "premises": 3,
            },
        },

        "severity": "HIGH",
    },
]

RECOMMENDATIONS = {
    "assets": {
        "food": [
            "Clearly label personal food.",
        ],
        "property": [
            "Clearly identify the asset owner.",
            "Store the asset in a designated location.",
        ],
        "computer": [
            "Restrict access to critical equipment.",
        ],
        "premises": [
            "Review physical access controls.",
        ],
    },

    "modifiers": {
        "unauthorized": [
            "Establish an explicit access policy.",
        ],
        "repeated": [
            "Document repeated incidents.",
            "Escalate the issue to the responsible party.",
        ],
        "accidental": [
            "Review environmental factors that may have contributed to the incident.",
        ],
    },

    "actors": {
        "coworker": [
            "Clarify access expectations with the coworker.",
        ],
        "friend": [
            "Try not to kill your friend (optional).",
        ],
        "roommate": [
            "Establish clear ownership and access rules.",
        ],
        "unknown": [
            "Review access controls and identify the responsible actor.",
        ],
        "cat": [
            "Review feline access privileges.",
        ],
    },
}