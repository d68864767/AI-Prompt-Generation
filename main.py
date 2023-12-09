# main.py

from prompt_generator import generate_prompts

def main():
    # Example document as provided in the project description
    document = [
        "What is the meaning of life?", 
        "Life is a journey, not a destination.", 
        "", 
        "To be, or not to be, that is the question.",
        "Some infinities are bigger than other infinities."
    ]

    # Generate prompts based on the document
    prompts = generate_prompts(document)

    # Print each prompt to the console
    for prompt in prompts:
        print(prompt)

if __name__ == "__main__":
    main()
