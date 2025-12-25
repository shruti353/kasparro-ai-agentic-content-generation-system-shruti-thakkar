import json
from core.models import Product
from core.blocks import generate_questions, compare_products
from core.templates import faq_template, product_page_template, comparison_page_template


class DataParsingAgent:
    def run(self, raw_json_path: str):
        with open(raw_json_path, "r") as f:
            data = json.load(f)

        return Product(
            name=data["product_name"],
            concentration=data["concentration"],
            skin_type=data["skin_type"],
            key_ingredients=data["key_ingredients"],
            benefits=data["benefits"],
            how_to_use=data["how_to_use"],
            side_effects=data["side_effects"],
            price=data["price"]
        )


class QuestionGenerationAgent:
    def run(self, product: Product):
        return generate_questions(product)


class FAQAssemblyAgent:
    def run(self, questions):
        # Convert to Q&A pairs (basic placeholder logic)
        faqs = []
        for q in questions[:5]:
            faqs.append({
                "question": q["question"],
                "answer": "Answer based on product data."
            })
        return faq_template(faqs)


class ProductPageAgent:
    def run(self, product: Product):
        return product_page_template(product)


class ComparisonAgent:
    def run(self, product: Product):
        fictional_productB = {
            "name": "ClearSkin Radiance Serum",
            "key_ingredients": ["Vitamin C", "Niacinamide"],
            "benefits": ["Brightening", "Reduces acne marks"],
            "price": "₹799"
        }
        comp = compare_products(product, fictional_productB)
        return comparison_page_template(comp)
