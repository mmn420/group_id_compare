import random
import argparse

def generate_pattern_entry(pattern_number):
    size = round(random.uniform(0.01, 100), 2)  # Random size between 0.01 and 100
    class_id = random.randint(1, 10)  # Random class_id between 1 and 4
    return f"Pattern{pattern_number}\nSize:{size}\nClass_id:{class_id}\n"

# Set up argument parser
parser = argparse.ArgumentParser(description='Generate pattern entries.')
parser.add_argument('num_entries', type=int, help='Number of pattern entries to generate')

# Parse arguments
args = parser.parse_args()

# Number of entries to generate
num_entries = args.num_entries

# Open the file in write mode
with open('generated_patterns.txt', 'w') as file:
    for i in range(1, num_entries + 1):
        entry = generate_pattern_entry(i)
        file.write(entry)

print(f"{num_entries} pattern entries have been generated and written to 'generated_patterns.txt'.")