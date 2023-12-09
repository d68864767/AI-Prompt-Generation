import unittest
from prompt_generator import generate_prompts

class TestPromptGenerator(unittest.TestCase):

    def test_empty_document(self):
        document = []
        expected = ["You have reached the end of the document. Reflect on the overall content."]
        self.assertEqual(generate_prompts(document), expected)

    def test_all_empty_lines(self):
        document = ["", "", ""]
        expected = ["You have reached the end of the document. Reflect on the overall content."]
        self.assertEqual(generate_prompts(document), expected)

    def test_questions_only(self):
        document = [
            "What is the meaning of life?",
            "Is there life on Mars?",
            "How do you solve an equation?"
        ]
        expected = [
            "Answer the question: What is the meaning of life?",
            "Answer the question: Is there life on Mars?",
            "Answer the question: How do you solve an equation?",
            "You have reached the end of the document. Reflect on the overall content."
        ]
        self.assertEqual(generate_prompts(document), expected)

    def test_statements_only(self):
        document = [
            "Life is beautiful.",
            "The sky is blue.",
            "Programming is fun."
        ]
        expected = [
            "Discuss the statement: Life is beautiful.",
            "Discuss the statement: The sky is blue.",
            "Discuss the statement: Programming is fun.",
            "You have reached the end of the document. Reflect on the overall content."
        ]
        self.assertEqual(generate_prompts(document), expected)

    def test_mixed_content(self):
        document = [
            "What is the meaning of life?", 
            "Life is a journey, not a destination.", 
            "", 
            "To be, or not to be, that is the question.",
            "Some infinities are bigger than other infinities."
        ]
        expected = [
            "Answer the question: What is the meaning of life?", 
            "Discuss the statement: Life is a journey, not a destination.", 
            "Answer the question: To be, or not to be, that is the question.", 
            "Discuss the statement: Some infinities are bigger than other infinities.", 
            "You have reached the end of the document. Reflect on the overall content."
        ]
        self.assertEqual(generate_prompts(document), expected)

    def test_large_document(self):
        document = ["This is a statement."] * 10**5
        expected = ["Discuss the statement: This is a statement."] * 10**5
        expected.append("You have reached the end of the document. Reflect on the overall content.")
        self.assertEqual(generate_prompts(document), expected)

if __name__ == '__main__':
    unittest.main()
