// Trying some input output things.
// To compile use 
// clang -lczmq -lzmq -o zmq_t zmq_t.c
// or clang -lczmq -o zmq_t zmq_t.c
#include<stdio.h>
#include<stdlib.h>
#include<czmq.h>
#include<zlist.h>



int main(int arg, char **args){
    //zlist_t *list = zlist_new_list ();
    zlist_t *list = zlist_new ();
    zlist_append(list, "apple");
    zlist_append(list, "potato");
    printf("%zd\n", zlist_size(list));
    printf("%s - %s \n", zlist_first(list), zlist_next(list));
    return 0;
} 
