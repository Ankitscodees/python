def search(word, sentences):
    results = []
    for sentence in sentences:
        if word.lower() in sentence.lower():  # Case-insensitive search
            results.append(sentence)
    return results

# List of sentences
sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is a versatile programming language.",
    "This is an example of a search function.",
    "We are learning Python basics."
]

# Example usage
word_to_search = "python"
matches = search(word_to_search, sentences)
print("Search Results:")
for match in matches:
    print(f"- {match}")
