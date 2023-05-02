def cross_reference_words(word_file, common_word_file):
    with open(word_file, 'r') as f:
        words = f.read().split()
    with open(common_word_file, 'r') as f:
        common_words = f.read().split()
    common_set = set(common_words)
    intersect_set = set(words).intersection(common_set)
    return intersect_set

word_file = '/path/to/word_file.txt'
common_word_file = '/path/to/common_word_file.txt'

intersect_set = cross_reference_words(word_file, common_word_file)

for word in intersect_set:
    print(word)
