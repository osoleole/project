# Tools for analyzing text files

### Convert all spaces to new line
cat all.txt | tr -sc 'A-Za-z' '\n'

### Conver and sort
cat all.txt | tr -sc 'A-Za-z' '\n' | sort | less

### Show uniq words with counts
cat all.txt | tr -sc 'A-Za-z' '\n' | sort | uniq -c | less

### Sort by frequecy
cat all.txt | tr -sc 'A-Za-z' '\n' | sort | uniq -c | sort -r -n | less

### Map all upper case to lower case words 
cat all.txt | tr 'A-Z' 'a-z' | tr -sc 'A-Za-z' '\n' | sort | uniq -c | sort -r -n | less

### Find words  ending with 'ing'
cat all.txt | tr 'A-Z' 'a-z' | tr -sc 'A-Za-z' '\n' | grep 'ing$' | sort | uniq -c | sort -r -n | less

### Find words ending with 'ing' and having vowel before
cat all.txt | tr 'A-Z' 'a-z' | tr -sc 'A-Za-z' '\n' | grep '[aeoiu].*ing$' | sort | uniq -c | sort -r -n | less
