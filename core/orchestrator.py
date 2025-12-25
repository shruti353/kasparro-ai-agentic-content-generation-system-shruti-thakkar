import json
from core.agents import (
    DataParsingAgent,
    QuestionGenerationAgent,
    FAQAssemblyAgent,
    ProductPageAgent,
    ComparisonAgent
)

class Orchestrator:
    def __init__(self):
        self.data_agent = DataParsingAgent()
        self.question_agent = QuestionGenerationAgent()
        self.faq_agent = FAQAssemblyAgent()
        self.product_agent = ProductPageAgent()
        self.comparison_agent = ComparisonAgent()

    def run(self):
        product = self.data_agent.run("data/product_data.json")
        questions = self.question_agent.run(product)

        faq_page = self.faq_agent.run(questions)
        product_page = self.product_agent.run(product)
        comparison_page = self.comparison_agent.run(product)

        return {
            "faq": faq_page,
            "product_page": product_page,
            "comparison_page": comparison_page
        }

    def save_outputs(self, outputs):
        with open("outputs/faq_page.json", "w") as f:
            json.dump(outputs["faq"], f, indent=4)

        with open("outputs/product_page.json", "w") as f:
            json.dump(outputs["product_page"], f, indent=4)

        with open("outputs/comparison_page.json", "w") as f:
            json.dump(outputs["comparison_page"], f, indent=4)
