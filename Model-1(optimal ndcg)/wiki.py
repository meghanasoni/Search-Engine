import wikipedia

def get_concepts(word):
    try:
        # Get the summary of the Wikipedia page for the given word
        summary = wikipedia.summary(word)

        # Split the summary into words
        words = summary.split()

        # Get the first 5 words as concepts
        concepts = words[:5]

        return concepts

    except wikipedia.exceptions.DisambiguationError as e:
        # If the given word is ambiguous, print the options and return None
        print(f"{word} is ambiguous. Options are: {e.options}")
        return None

    except wikipedia.exceptions.PageError:
        # If the given word doesn't have a Wikipedia page, return None
        print(f"No Wikipedia page found for {word}")
        return None
print(get_concepts("aerodynamics"))