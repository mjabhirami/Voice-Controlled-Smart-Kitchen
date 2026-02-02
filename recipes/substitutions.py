"""Simple ingredient substitution rules.

This is a minimal, extensible mapping used by the API to suggest substitutes.
"""

SUBSTITUTIONS = {
    "buttermilk": [
        {"ingredient": "milk + lemon/ vinegar", "notes": "mix 1 cup milk with 1 tbsp lemon, rest 5 min"},
        {"ingredient": "yogurt", "notes": "use equal volume, thin with water if needed"}
    ],
    "egg": [
        {"ingredient": "flax egg", "notes": "1 tbsp flaxseed + 3 tbsp water per egg"},
        {"ingredient": "applesauce", "notes": "use 1/4 cup per egg for baking"}
    ],
    "chicken": [
        {"ingredient": "tofu", "notes": "firm tofu as protein substitute"},
        {"ingredient": "tempeh", "notes": "works well in stir fry"}
    ],
    "butter": [
        {"ingredient": "margarine", "notes": "1:1 swap"},
        {"ingredient": "olive oil", "notes": "use ~3/4 oil for 1 butter"}
    ]
}


def get_substitutes(ingredient: str):
    key = ingredient.strip().lower()
    return SUBSTITUTIONS.get(key, [])
