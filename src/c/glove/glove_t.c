#include<stdio.h>
#include<stdlib.h>

typedef double real;

int vector_size = 50;
int vocab_size = 50;
real *W, *gradsq, *cost;



void initialize_parameters() {
	long long a, b;
	vector_size++; // Temporarily increment to allocate space for bias
    
	/* Allocate space for word vectors and context word vectors, and correspodning gradsq */
	a = posix_memalign((void **)&W, 128, 2 * vocab_size * (vector_size + 1) * sizeof(real)); // Might perform better than malloc
    if (W == NULL) {
        fprintf(stderr, "Error allocating memory for W\n");
        exit(1);
    }
    a = posix_memalign((void **)&gradsq, 128, 2 * vocab_size * (vector_size + 1) * sizeof(real)); // Might perform better than malloc
	if (gradsq == NULL) {
        fprintf(stderr, "Error allocating memory for gradsq\n");
        exit(1);
    }
	for (b = 0; b < vector_size; b++) for (a = 0; a < 2 * vocab_size; a++) W[a * vector_size + b] = (rand() / (real)RAND_MAX - 0.5) / vector_size;
	for (b = 0; b < vector_size; b++) for (a = 0; a < 2 * vocab_size; a++) gradsq[a * vector_size + b] = 1.0; // So initial value of eta is equal to initial learning rate
	vector_size--;
}



int main(int arg, char **args){
    initialize_parameters();

    for(int i = 0; i < 5100; i++) printf("Weight matrix size %f \n", gradsq[i]);
    free(W);
    free(gradsq);
}
