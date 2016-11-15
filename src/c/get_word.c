// Trying some input output things.
#include<stdio.h>
#include<stdlib.h>

#define WORDS_FILE "words.txt"
    static const int MAX_STRING_LENGTH = 1000;

// Get first one word from the file
int get_word(char *word, FILE *fin) {
    int i = 0, ch;
    while (!feof(fin)) {
        ch = fgetc(fin);
        if (ch == 13) continue;
        if ((ch == ' ') || (ch == '\t') || (ch == '\n')) {
            if (i > 0) {
                if (ch == '\n') ungetc(ch, fin);
                break;
            }
            if (ch == '\n') return 1;
            else continue;
        }
        word[i++] = ch;
        if (i >= MAX_STRING_LENGTH - 1) i--;   // truncate words that exceed max length
    }
    word[i] = 0;
    return 0;
}


int main(int arg, char **args){
    char str[MAX_STRING_LENGTH + 1];
    FILE *fot = fopen(WORDS_FILE, "r");
    get_word(str, fot);

    printf("Word is -  %s\n", str);

    fclose(fot);
    return 0;
} 
