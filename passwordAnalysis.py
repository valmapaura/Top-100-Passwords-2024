import collections
import os
import re
import time

# Function to process the file and create the output files
def process_large_file(input_file, output_dir):
    # Initialize a counter to keep track of the passwords
    counter = collections.Counter()

    # Variables for additional analysis
    total_length = 0
    longest_password = ""
    shortest_password = None
    special_char_count = 0
    number_count = 0
    strong_password_count = 0

    # Define regex patterns for special characters, numbers, and strong passwords
    special_char_pattern = re.compile(r"[!@#$%^&*(),.?\":{}|<>]")
    number_pattern = re.compile(r"\d")
    strong_password_pattern = re.compile(r"(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*(),.?\":{}|<>]).{8,}")

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

                # Update the total length for average calculation
                total_length += len(password)

                # Update longest and shortest passwords
                if len(password) > len(longest_password):
                    longest_password = password
                if shortest_password is None or len(password) < len(shortest_password):
                    shortest_password = password

                # Count passwords with special characters and numbers
                if special_char_pattern.search(password):
                    special_char_count += 1
                if number_pattern.search(password):
                    number_count += 1

                # Count strong passwords
                if strong_password_pattern.search(password):
                    strong_password_count += 1

            # Print progress every 1% of total lines
            if i in progress_check_points:
                progress = (i / total_lines) * 100
                print(f"Processing: {progress:.2f}% complete")

    process_end_time = time.time()
    print(f"Processing lines took {process_end_time - process_start_time:.2f} seconds")

    # Calculate the total count of all passwords
    total_count = sum(counter.values())

    # Calculate average password length
    average_length = total_length / total_count if total_count > 0 else 0

    # Sort the counter by count in descending order
    sort_start_time = time.time()
    sorted_counter = sorted(counter.items(), key=lambda item: item[1], reverse=True)
    sort_end_time = time.time()
    print(f"Sorting took {sort_end_time - sort_start_time:.2f} seconds")

    # Write the sorted results to a new file
    write_start_time = time.time()
    with open(f"{output_dir}/sorted_results.txt", 'w') as outfile:
        for idx, (word, count) in enumerate(sorted_counter, 1):
            percentage = (count / total_count) * 100
            if idx <= 100:
                top_100_percentage = (count / sum(count for _, count in sorted_counter[:100])) * 100
                outfile.write(f"{idx}. {word} ({count}) {percentage:.2f}% \n")
            else:
                outfile.write(f"{idx}. {word} ({count}) {percentage:.2f}%\n")

    # Write the total unique words count to a new file
    unique_words_count = len(counter)
    with open(f"{output_dir}/unique_words_count.txt", 'w') as outfile:
        outfile.write(f"Total unique words: {unique_words_count}\n")

    # Write the top N frequent words to a new file
    top_n = 100
    top_n_frequent_words = sorted_counter[:top_n]
    with open(f"{output_dir}/top_{top_n}_frequent_words.txt", 'w') as outfile:
        outfile.write(f"Top {top_n} frequent words:\n")
        for idx, (word, count) in enumerate(top_n_frequent_words, 1):
            percentage = (count / total_count) * 100
            top_100_percentage = (count / sum(count for _, count in sorted_counter[:100])) * 100
            outfile.write(f"{idx}. {word} ({count}) {percentage:.2f}% ({top_100_percentage:.2f}% of top 100)\n")

    # Write the frequency distribution to a new file
    frequency_distribution = collections.Counter(count for word, count in counter.items())
    with open(f"{output_dir}/frequency_distribution.txt", 'w') as outfile:
        outfile.write("Frequency distribution:\n")
        for freq, num_words in sorted(frequency_distribution.items()):
            outfile.write(f"{num_words} words appear {freq} times\n")

    # Write the additional analysis results to a new file
    with open(f"{output_dir}/password_analysis.txt", 'w') as outfile:
        outfile.write("Password Analysis:\n")
        outfile.write(f"1. Longest password: {longest_password} (Length: {len(longest_password)})\n")
        outfile.write(f"2. Shortest password: {shortest_password} (Length: {len(shortest_password)})\n")
        outfile.write(f"3. Average password length: {average_length:.2f}\n")
        outfile.write(f"4. Passwords with special characters: {special_char_count} ({(special_char_count / total_count) * 100:.2f}%)\n")
        outfile.write(f"5. Passwords with numbers: {number_count} ({(number_count / total_count) * 100:.2f}%)\n")
        outfile.write(f"6. Strong passwords: {strong_password_count} ({(strong_password_count / total_count) * 100:.2f}%)\n")

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
