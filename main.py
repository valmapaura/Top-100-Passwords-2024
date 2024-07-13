import collections
import time
import os

# Function to process the file and create the output files
def process_large_file(input_file, output_dir):
    # Initialize a counter to keep track of the passwords of text
    counter = collections.Counter()

    # Start timer for the entire process
    start_time = time.time()

    # Get the total number of lines in the input file
    with open(input_file, 'r') as infile:
        total_lines = sum(1 for _ in infile)

    print(f"Total lines to process: {total_lines}")

    # Calculate progress check points
    progress_check_points = {i * (total_lines // 100) for i in range(1, 101)}

    # Open the input file and process it line by line
    process_start_time = time.time()
    with open(input_file, 'r') as infile:
        for i, line in enumerate(infile, 1):
            # Split the line by ':'
            parts = line.strip().split(':')
            if len(parts) == 2:
                # Extract the password and update the counter
                password = parts[1].strip()
                counter[password] += 1

            # Print progress every 1% of total lines
            if i in progress_check_points:
                progress = (i / total_lines) * 100
                print(f"Processing: {progress:.2f}% complete")

    process_end_time = time.time()
    print(f"Processing lines took {process_end_time - process_start_time:.2f} seconds")

    # Calculate the total count of all passwords of text
    total_count = sum(counter.values())

    # Sort the counter by count in descending order
    sort_start_time = time.time()
    sorted_counter = sorted(counter.items(), key=lambda item: item[1], reverse=True)
    sort_end_time = time.time()
    print(f"Sorting took {sort_end_time - sort_start_time:.2f} seconds")

    # Write the sorted results to a new file
    write_start_time = time.time()
    with open(f"{output_dir}/sorted_results.txt", 'w') as outfile:
        outfile.write("Password (Count) Percentage\n")
        for word, count in sorted_counter:
            percentage = (count / total_count) * 100
            outfile.write(f"{word} ({count}) {percentage:.2f}%\n")

    # Write the total unique words count to a new file
    unique_words_count = len(counter)
    with open(f"{output_dir}/unique_words_count.txt", 'w') as outfile:
        outfile.write(f"Total unique words: {unique_words_count}\n")

    # Write the top N frequent words to a new file
    top_n = 100
    top_n_frequent_words = sorted_counter[:top_n]
    with open(f"{output_dir}/top_{top_n}_frequent_words.txt", 'w') as outfile:
        outfile.write(f"Top {top_n} frequent words:\n")
        for word, count in top_n_frequent_words:
            percentage = (count / total_count) * 100
            outfile.write(f"{word} ({count}) {percentage:.2f}%\n")

    # Write the frequency distribution to a new file
    frequency_distribution = collections.Counter(count for word, count in counter.items())
    with open(f"{output_dir}/frequency_distribution.txt", 'w') as outfile:
        outfile.write("Frequency distribution:\n")
        for freq, num_words in sorted(frequency_distribution.items()):
            outfile.write(f"{num_words} words appear {freq} times\n")
    write_end_time = time.time()
    print(f"Writing files took {write_end_time - write_start_time:.2f} seconds")

    end_time = time.time()
    print(f"Total processing time: {end_time - start_time:.2f} seconds")
    print("Processing complete. Results written to the specified directory.")

# Define the input file path and output directory
input_file = '7MillionAccounts.txt'
output_dir = 'analysis_results'

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Call the function to process the file
process_large_file(input_file, output_dir)
