import re

def filter_words(input_file, output_file):
    with open(input_file, 'r') as f:
        words = f.read().split()
    filtered_words = [word for word in words if re.match(r'^[a-zA-Z]{3,16}$', word)]
    with open(output_file, 'w') as f:
        for word in filtered_words:
            f.write(word + '\n')

input_file = '/Users/*****/Documents/available_usernames2.txt' # Input
output_file = '/Users/*****/Documents/filtered_words.txt' # Output
filter_words(input_file, output_file)
