from itertools import permutations

def anagram_generator():
    print("Welcome to the Name Anagram Generator!")
    name = input("\nEnter a name to generate its anagrams: ").strip()
    
    anagrams = set(permutations(name))
    print(f"\nAnagrams of '{name}':")
    for anagram in sorted(anagrams):
        print("".join(anagram))

# Generate anagrams
anagram_generator()
