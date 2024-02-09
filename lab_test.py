import hashlib
import random
import time
from multiprocessing import Pool, cpu_count


def random_utf8_char():
    # Using a simplified range for characters to maintain clarity
    return chr(random.randint(0x20, 0x7E))  # Printable ASCII characters


def generate_hash_with_suffix(args):
    target_string, suffix = args
    random_char = random_utf8_char()
    modified_string = target_string + random_char
    new_hash = hashlib.sha256(modified_string.encode('utf-8')).hexdigest()
    return new_hash.endswith(suffix), modified_string, new_hash


def find_hash_with_suffix_parallel(initial_string, suffix, pool_size=None):
    if pool_size is None:
        pool_size = cpu_count()
        print(f"Using {pool_size} processes")

    with Pool(processes=pool_size) as pool:
        counter = 0
        start_time = time.time()
        while True:
            # Create a batch of tasks for the pool
            tasks = [(initial_string, suffix) for _ in range(1000)]  # Adjust the batch size if needed
            results = pool.map(generate_hash_with_suffix, tasks)
            for result in results:
                match, modified_string, new_hash = result
                if match:
                    end_time = time.time()
                    return modified_string, new_hash, counter, end_time - start_time
                counter += 1


# Example usage
if __name__ == '__main__':
    initial_string = "Alex Szpakiewicz, Léonard Roussard and Sara Thibierge."
    print(f"Initial string: {initial_string}")
    print(f"Initial SHA-256 hash: {hashlib.sha256(initial_string.encode('utf-8')).hexdigest()}")

    modified_string, final_hash, attempts, computing_time = find_hash_with_suffix_parallel(initial_string, '000')
    print(f"Modified string (after {attempts} attempts): {modified_string}")
    print(f"Final SHA-256 hash ending with the specified suffix: {final_hash}")
    print(f"Computing time: {computing_time:.2f} seconds")
