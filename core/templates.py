def faq_template(faq_items):
    return {
        "page_type": "faq_page",
        "faqs": faq_items
    }


def product_page_template(product: "Product"):
    return {
        "page_type": "product_page",
        "product_details": {
            "name": product.name,
            "concentration": product.concentration,
            "skin_type": product.skin_type,
            "key_ingredients": product.key_ingredients,
            "benefits": product.benefits,
            "usage": product.how_to_use,
            "side_effects": product.side_effects,
            "price": product.price
        }
    }


def comparison_page_template(comparison_data: dict):
    return {
        "page_type": "comparison_page",
        "comparison": comparison_data
    }
