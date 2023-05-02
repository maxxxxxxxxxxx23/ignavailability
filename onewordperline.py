def keep_first_word(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    with open(output_file, 'w') as f:
        for line in lines:
            first_word = line.split()[0]
            f.write(first_word + '\n')

input_file = "/Users/yourusername/Documents/input.txt"
output_file = "/Users/yourusername/Documents/output.txt"
keep_first_word(input_file, output_file)
