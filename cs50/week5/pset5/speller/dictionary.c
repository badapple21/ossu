// Implements a dictionary's functionality

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <strings.h>
#include <ctype.h>
#include "dictionary.h"


// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 10000;

// Hash table
node *table[N];


unsigned long int dict_size = 0;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO

    int entry = hash(word);

    node *n = table[entry];

    while(n != NULL){
        if(strcasecmp(word, n->word)==0){
            return true;
        }
        n = n->next;
    }

    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    //Function should take a string and return an index
    // This hash function adds the ASCII values of all characters in     the word together
    long sum = 0;
    for (int i = 0; i < strlen(word); i++)
    {
        sum += tolower(word[i]);
    }
    return sum % N;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO

    //open file
    FILE *f = fopen(dictionary, "r");
    if(f==NULL){
        printf("File was NULL\n");
        return false;
    }

    //readstrings from file
    char words[LENGTH+1];
    int rtnvalue = 0;
    while((fscanf(f, "%s",words)) != EOF)
    {
        node *n = malloc(sizeof(node));
        if(n==NULL){
            printf("Ran out off memory\n");
            return false;
        }
        strcpy(n->word, words);

        int entry = hash(words);
        n->next = table[entry];
        table[entry] = n;

        dict_size++;
    }

    fclose(f);


    //copy word to word feild
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return dict_size;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // Iterate over hash table and free nodes in each linked list
    for (int i = 0; i < N; i++)
    {
        // Assign cursor
        node *n = table[i];
        // Loop through linked list
        while (n != NULL)
        {
            // Make temp equal cursor;
            node *tmp = n;
            // Point cursor to next element
            n = n->next;
            // free temp
            free(tmp);
        }
        if (n == NULL && i == N - 1)
        {
            return true;
        }
    }
    return false;
}
