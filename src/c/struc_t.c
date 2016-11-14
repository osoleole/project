// Trying some input output things.
#include<stdio.h>
#include<stdlib.h>

#define TSIZE 1048576    

typedef struct vocab{
    char *word;
    int count;
    struct vocab *next;
}VOCAB;

VOCAB ** vocabs_tab(){
    VOCAB **vc;
    vc = (VOCAB **) malloc(sizeof(VOCAB*) * TSIZE);
    return vc;
}


int main(int arg, char **args){
    printf("###########Trying structs############\n");
    char w1[] = "Wonderful";
    char w2[] = "World";
    // Define vocab1
    VOCAB vocab1;
    vocab1.word = w2;
    vocab1.count = 2;
    // Define vocab
    VOCAB vocab;
    vocab.word = w1;
    vocab.count = 1;
    vocab.next = &vocab1;
    // Print vocab content
    printf("VOCAB word - %s, count - %d, pointer to next - %p\n", vocab.word, vocab.count, vocab.next);
    // Print vocab1 content through vocab *next pointer from vocab to vocab1
    printf("VOCAB1 word %s\n", (*vocab.next).word);
    
    // Work with VOCAB
    VOCAB **table = vocabs_tab();
    *table[0] = &vocab;
    //*table[1] = vocab1;
    printf("Size of vocabulary struct %lu\n", sizeof(vocab));
    printf("Size of allocated table %lu\n", sizeof(**table));
    free(*table);
} 
