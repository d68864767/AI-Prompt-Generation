from typing import List

def generate_prompts(document: List[str]) -> List[str]:
    prompts = []
    
    for line in document:
        if not line:  # If the line is empty, skip it.
            continue
        elif line.endswith('?'):  # If the line ends with a question mark, it's a question.
            prompts.append(f"Answer the question: {line}")
        else:  # Otherwise, it's a statement.
            prompts.append(f"Discuss the statement: {line}")
    
    # After processing all lines, add the end prompt.
    prompts.append("You have reached the end of the document. Reflect on the overall content.")
    
    return prompts
