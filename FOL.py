import re

# Predicates for translation
predicates = {
    "is a human": "H",  # e.g., John is a human
    "is mortal": "M",   # e.g., John is mortal
    "loves": "L",       # e.g., John loves Mary
    "is a dog": "D",    # e.g., John is a dog
    "is an animal": "A", # e.g., John is an animal
    "is brown": "B",    # e.g., John is brown
    "is a person": "P",  # e.g., John is a person
    "is a teacher": "T",  # e.g., John is a teacher
    "is a student": "S",  # e.g., John is a student
    "respects": "R",     # e.g., John respects Mary
    "knows": "K",       # e.g., John knows Mary
    "likes mathematics": "Lm",  # John likes mathematics
    "likes science": "Ls",     # John likes science
    "is married to": "Ma",  # John is married to Mary
    "is a bachelor": "Bch", # John is a bachelor
    "is a parent of": "Pnt", # John is a parent of someone
    "is raining": "R",    # It is raining
    "is wet": "G",        # The ground is wet
    "is a man": "R",      # John is a man
    "is a woman": "W",    # Mary is a woman
}

# Constants: John (j) and Mary (m)
constants = {
    "John": "j",
    "Mary": "m",
    "Alice": "a",
}

# Function to handle sentence translation
def translate_to_fol(sentence):
    sentence = sentence.strip().lower()

    # Handle sentence structures
    if "is a human" in sentence:
        return translate_is_a_human(sentence)

    if "is mortal" in sentence:
        return translate_is_mortal(sentence)

    if "loves" in sentence:
        return translate_loves(sentence)

    if "every" in sentence:
        return translate_every(sentence)

    if "there exists" in sentence or "there is" in sentence:
        return translate_exists(sentence)

    if "not all" in sentence:
        return translate_not_all(sentence)

    if "if" in sentence and "then" in sentence:
        return translate_if_then(sentence)

    if "nobody" in sentence:
        return translate_nobody(sentence)

    if "and" in sentence:
        return translate_conjunction(sentence)

    return "Translation not available for this sentence structure."

# Helper functions for specific cases
def translate_is_a_human(sentence):
    match = re.match(r"([a-zA-Z]+) is a human", sentence)
    if match:
        subject = match.group(1)
        subject_const = constants.get(subject, subject)
        return f"H({subject_const})"
    return "Invalid sentence structure."

def translate_is_mortal(sentence):
    match = re.match(r"([a-zA-Z]+) is mortal", sentence)
    if match:
        subject = match.group(1)
        subject_const = constants.get(subject, subject)
        return f"M({subject_const})"
    return "Invalid sentence structure."

def translate_loves(sentence):
    match = re.match(r"([a-zA-Z]+) loves ([a-zA-Z]+)", sentence)
    if match:
        subject = match.group(1)
        object_ = match.group(2)
        subject_const = constants.get(subject, subject)
        object_const = constants.get(object_, object_)
        return f"L({subject_const}, {object_const})"
    return "Invalid sentence structure."

def translate_every(sentence):
    match = re.match(r"every ([a-zA-Z]+) is ([a-zA-Z]+)", sentence)
    if match:
        subject = match.group(1)
        predicate = match.group(2)
        return f"∀x ({subject}(x) → {predicate}(x))"
    return "Invalid sentence structure."

def translate_exists(sentence):
    match = re.match(r"there exists ([a-zA-Z]+) who ([a-zA-Z]+) ([a-zA-Z]+)", sentence)
    if match:
        subject = match.group(1)
        predicate = match.group(2)
        object_ = match.group(3)
        subject_const = constants.get(subject, subject)
        object_const = constants.get(object_, object_)
        return f"∃x ({predicate}(x, {object_const}))"
    return "Invalid sentence structure."

def translate_not_all(sentence):
    match = re.match(r"not all ([a-zA-Z]+) like both ([a-zA-Z]+) and ([a-zA-Z]+)", sentence)
    if match:
        subject = match.group(1)
        subject1 = match.group(2)
        subject2 = match.group(3)
        return f"¬∀x ({subject}(x) → ({subject1}(x) ∧ {subject2}(x)))"
    return "Invalid sentence structure."

def translate_if_then(sentence):
    match = re.match(r"if ([a-zA-Z]+) is ([a-zA-Z]+), then ([a-zA-Z]+) teaches mathematics", sentence)
    if match:
        subject = match.group(1)
        subject_const = constants.get(subject, subject)
        return f"{subject_const}(x) → Teaches(x, Mathematics)"
    return "Invalid sentence structure."

def translate_conjunction(sentence):
    match = re.match(r"([a-zA-Z]+) and ([a-zA-Z]+) are both students", sentence)
    if match:
        subject1 = match.group(1)
        subject2 = match.group(2)
        subject1_const = constants.get(subject1, subject1)
        subject2_const = constants.get(subject2, subject2)
        return f"S({subject1_const}) ∧ S({subject2_const})"
    return "Invalid sentence structure."

# Function to handle "nobody" sentences
def translate_nobody(sentence):
    match = re.match(r"nobody is ([a-zA-Z]+) than themselves", sentence)
    if match:
        predicate = match.group(1)  # For example: "taller"
        return f"¬∃x ({predicate}(x, x))"  # This means "Nobody is taller than themselves"
    return "Invalid sentence structure."

# Main loop to interact with the user
def main():
    print("Enter a sentence like:")
    print("1. John is a human.")
    print("2. Every human is mortal.")
    print("3. John loves Mary.")
    print("4. There exists someone who loves Mary.")
    print("Type 'exit' to quit.")

    while True:
        sentence = input("\nEnter a sentence: ").strip()

        if sentence.lower() == 'exit':
            print("Goodbye!")
            break

        # Translate the sentence into FOL
        fol_translation = translate_to_fol(sentence)
        print("First-Order Logic Translation:", fol_translation)

# Run the program
if __name__ == "__main__":
    main()
