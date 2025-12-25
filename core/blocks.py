def generate_questions(product: "Product"):
    """
    Returns 15 categorized user questions.
    """
    categories = {
        "Informational": [
            f"What is {product.name}?",
            f"Is {product.name} suitable for {product.skin_type} skin?",
        ],
        "Usage": [
            "How do I apply the serum?",
            "Can I use it at night?",
            "Can it be layered with moisturizer?"
        ],
        "Safety": [
            "Does it cause irritation?",
            "Is it safe for sensitive skin?",
            "What side effects should I expect?"
        ],
        "Purchase": [
            "What is the price?",
            "Where can I buy it?"
        ],
        "Comparison": [
            f"Is {product.name} better than other Vitamin C serums?",
            "How does it compare to a hyaluronic acid serum?"
        ]
    }

    all_qs = []
    for cat, qs in categories.items():
        for q in qs:
            all_qs.append({"category": cat, "question": q})

    return all_qs[:15]


def compare_products(prodA: "Product", prodB: dict):
    return {
        "name_comparison": f"{prodA.name} vs {prodB['name']}",
        "ingredient_overlap":
            list(set(prodA.key_ingredients) & set(prodB["key_ingredients"])),
        "price_difference": f"{prodA.price} vs {prodB['price']}",
        "benefit_comparison": {
            "product_A": prodA.benefits,
            "product_B": prodB["benefits"]
        }
    }
