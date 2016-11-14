// Trying some input output things.
#include<stdio.h>
#include<stdlib.h>


int main(int arg, char **args){
    // sprintf 
    char format[20];
    sprintf(format,"Print me %d %s\n", 20, "times");
    int i = 0;
    while(format[i] != '\0'){
        printf("%c", format[i++]);
    }
}

