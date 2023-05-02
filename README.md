# ignavailability
Checks availability of Minecraft igns using basic python script

Super easy to use

paste in a python compiler (i recommend VS Code) and run by changing the list in line 4 keep the format to avoid errors.

available_words2.txt is a list of 466k available usernames words provided by https://github.com/dwyl/english-words using beta1.py

Correct as of 2/05/2023 Australian Format

# Different files 
basic.py checks In game names (IGNS) that are listed in the file when you run it, it will print if available/not as it runs. Refer to line 4.

better.py is the same as basic.py except it prints all the avaialable IGNS at the end. Refer to line 4.

comparing.py compares the two lists and prints all the words in common

filtering.py gets rid of symbols and words too short/long, note even though underscores are accepted it still removes them.

filtered_words.txt contains filtered words that are available as IGNS using dwyl's github list.

beta1.py checks all words listing in a file and prints them if they are available to another file. Refer to lines 5-6.
