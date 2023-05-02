# ignavailability

I made this in hope to find an oguser but did'y succeed. I'm unware if there is open source code like this and if there is I'd appreciate if you fowarded it to me.

Checks availability of Minecraft igns using basic python script

Super easy to use

available_words2.txt is a list of 466k available usernames words provided by https://github.com/dwyl/english-words using beta1.py

Correct as of 2/05/2023 Australian Format

I came to the conclusion that almost no words are available that are commonly used. Using comparing.py I checked https://www.lextutor.ca/freq/lists_download/longman_3000_list.pdf and found these words that 'aren't' taken: naked, almost, where, every, restrict. Some of which are locked or are glitched. I checked https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_5000.pdf as well and found similar results with them either being blocked by Mojang, glitched or locked. Here they are: erect, congratulate, slavery, naked, fundraising, regardless, suicide, citizenship, coordinator, sexy, restrict, substantially   

# Different files 
basic.py checks In game names (IGNS) that are listed in the file when you run it, it will print if available/not as it runs. Refer to line 4.

better.py is the same as basic.py except it prints all the avaialable IGNS at the end. Refer to line 4.

comparing.py compares the two lists and prints all the words in common

filtering.py gets rid of symbols and words too short/long, note even though underscores are accepted it still removes them.

filtered_words.txt contains filtered words that are available as IGNS using dwyl's github list.

beta1.py checks all words listing in a file and prints them if they are available to another file. Refer to lines 5-6.

onewordperline.py only allows for one word in each line in a txt file, this is to allow the python scripts to run with ease.
