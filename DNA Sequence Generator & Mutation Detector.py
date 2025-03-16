import random

# Generate a random DNA sequence
def generate_dna(length=10):
    return ''.join(random.choice("ATCG") for _ in range(length))

# Introduce a mutation in the DNA sequence
def introduce_mutation(dna):
    mutation_index = random.randint(0, len(dna) - 1)
    original_base = dna[mutation_index]
    mutated_base = random.choice([b for b in "ATCG" if b != original_base])
    mutated_dna = dna[:mutation_index] + mutated_base + dna[mutation_index + 1:]
    return mutated_dna, mutation_index, original_base, mutated_base

# Detect mutation
def detect_mutation(original, mutated):
    for i in range(len(original)):
        if original[i] != mutated[i]:
            return i, original[i], mutated[i]
    return None

# Main program
original_dna = generate_dna(10)
mutated_dna, index, original_base, mutated_base = introduce_mutation(original_dna)

print(f"Original DNA : {original_dna}")
print(f"Mutated DNA  : {mutated_dna}")

detected_mutation = detect_mutation(original_dna, mutated_dna)
if detected_mutation:
    print(f"Mutation detected at position {detected_mutation[0]}: {detected_mutation[1]} → {detected_mutation[2]}")
else:
    print("No mutation detected.")
