import random
import hashlib
import time
import hashlib
import random
import time

# Function to generate SHA-256 hash

def random_utf8_char():
    # Exclude the surrogate pair range
    valid_ranges = [(0x0000, 0xD7FF), (0xE000, 0xFFFF), (0x10000, 0x10FFFF)]
    chosen_range = random.choice(valid_ranges)
    return chr(random.randint(*chosen_range))

def find_hash_with_suffix(target_string, suffix='00000'):
    start_time = time.time()  # Start timing
    counter = 0
    while True:
        modified_string = target_string + random_utf8_char()
        new_hash = hashlib.sha256(modified_string.encode('utf-8')).hexdigest()
        if new_hash.endswith(suffix):
            end_time = time.time()  # End timing
            elapsed_time = end_time - start_time  # Calculate elapsed time
            return modified_string, new_hash, counter, elapsed_time
        counter += 1

# Initial string
initial_string = "Alex Szpakiewicz, Léonard Roussard and Sara Thibierge.Et quibusdam eligendi corrupti omnis id quas consequatur id fugiat consequatur rerum."
initial_hash    = hashlib.sha256(initial_string.encode('utf-8')).hexdigest()
print(f"Initial SHA-256 hash: {initial_hash}")

modified_string, final_hash, attempts, computing_time = find_hash_with_suffix(initial_string)
print(f"Modified string (after {attempts} attempts): {modified_string}")
print(f"Final SHA-256 hash ending with the specified suffix: {final_hash}")
print(f"Computing time: {computing_time} seconds")

