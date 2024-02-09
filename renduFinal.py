import hashlib
import time


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


def find_hash_with_suffix(target_string, suffix='0000000'):
    start_time = time.time()  # Start timing
    counter = 0
    sequence = []  # Start with an empty sequence

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

        # Optional: Limit the length of sequences to avoid excessive computation
        if len(sequence) > 5:  # Example limit
            break

    # If not found within the character set and length limit, return indication
    return None, None, counter, time.time() - start_time


# Initial string
initial_string = "Alex Szpakiewicz, Léonard Roussard and Sara Thibierge."
print(f"Initial string: {initial_string}")
print(f"Initial SHA-256 hash: {generate_hash(initial_string)}")

# Use the incremental approach to find a hash with the specified suffix
modified_string, final_hash, attempts, computing_time = find_hash_with_suffix(initial_string)
if modified_string:
    print(f"Modified string (after {attempts} attempts): {modified_string}")
    print(f"Final SHA-256 hash ending with the specified suffix: {final_hash}")
else:
    print("A hash with the specified suffix was not found within the allowed sequence length.")
print(f"Computing time: {computing_time:.2f} seconds")
