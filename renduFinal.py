import hashlib
import time
import random
import string


# Function to generate SHA-256 hash
def generate_hash(input_string):
    return hashlib.sha256(input_string.encode('utf-8')).hexdigest()


def get_next_sequence(current_sequence, start=0x20, end=0x7E):
    """
    Increment the current sequence of characters.
    If the last character is at the max value, append a new character starting from `start`.
    Otherwise, increment the last character.
    """
    if not current_sequence:
        return [start]
    sequence = list(current_sequence)
    i = len(sequence) - 1
    while i >= 0:
        if sequence[i] < end:
            sequence[i] += 1
            return sequence
        sequence[i] = start
        i -= 1
    sequence.append(start)
    return sequence


def find_hash_with_suffix(target_string, suffix_length=7):
    start_time = time.time()  # Start timing
    counter = 0
    sequence = []  # Start with an empty sequence
    suffix = '0' * suffix_length
    while True:
        sequence = get_next_sequence(sequence)
        char_str = ''.join([chr(c) for c in sequence])
        modified_string = target_string + char_str
        new_hash = generate_hash(modified_string)
        counter += 1
        if new_hash.endswith(suffix):
            end_time = time.time()  # End timing
            elapsed_time = end_time - start_time  # Calculate elapsed time
            return modified_string, new_hash, counter, elapsed_time

        if len(sequence) > 5:
            break

    # If not found within the character set and length limit, return indication
    return None, None, counter, time.time() - start_time
def statistical_analysis(target_string, n, repetitions=30):
    times_n = []
    times_n_plus_1 = []

    for i in range(repetitions):
        print(f"Repetition {i + 1}/{repetitions}")
        current_string = target_string + "a" * i
        _, _, _, time_n = find_hash_with_suffix(current_string, n)
        _, _, _, time_n_plus_1 = find_hash_with_suffix(current_string, n + 1)
        times_n.append(time_n)
        times_n_plus_1.append(time_n_plus_1)
        

    average_time_n = sum(times_n) / len(times_n)
    average_time_n_plus_1 = sum(times_n_plus_1) / len(times_n_plus_1)

    ratio = average_time_n_plus_1 / average_time_n if average_time_n > 0 else float('inf')
    return average_time_n, average_time_n_plus_1, ratio

# Initial string

initial_string = "Alex Szpakiewicz and Léonard Roussard."

suffix_length = 7
print(f"Initial string: {initial_string}")
print(f"Initial SHA-256 hash: {generate_hash(initial_string)}")

modified_string, final_hash, attempts, computing_time = find_hash_with_suffix(initial_string,suffix_length)
if modified_string:
    print(f"Modified string (after {attempts} attempts): {modified_string}")
    print(f"Final SHA-256 hash ending with the specified suffix: {final_hash}")
else:
    print("A hash with the specified suffix was not found within the allowed sequence length.")
print(f"Computing time: {computing_time:.2f} seconds")


suffix_length_stats = 4
average_time_n, average_time_n_plus_1, ratio = statistical_analysis(initial_string, suffix_length_stats)

# Impression des résultats
print(f"Temps moyen pour {suffix_length_stats} zéros (Tn): {average_time_n:.4f} secondes")
print(f"Temps moyen pour {suffix_length_stats+1} zéros (Tn+1): {average_time_n_plus_1:.4f} secondes")
print(f"Rapport Tn+1/Tn: {ratio:.4f}")

