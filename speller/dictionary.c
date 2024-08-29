// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

//Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

//Choose number of buckets in hash table
const unsigned int N = 10000;

//Counter for the number of words in the dictionary
int counter = 0;

//Hash table
node *table[N];

//Returns true if word is in dictionary, else false
bool check(const char *word)
{
    int index = hash(word);

    node *cursor = table[index];

    while (cursor != NULL)
    {
        if (strcasecmp(cursor->word, word) != 0)
        {
            cursor = cursor->next;
        }
        else
        {
            return true;
        }
    }

    return false;
}

//Hashes word to a number
unsigned int hash(const char *word)
{
    int points = 0;

    for (int i = 0, len = strlen(word); i < len; i++)
    {
        points += toupper(word[i]) - 'A';
    }

    return points % N;
}

//Loads dictionary into memory, return true if successful, else false
bool load(const char *dictionary)
{
    FILE *file = fopen(dictionary, "r");

    if (file == NULL)
    {
        return false;
    }
    char word[LENGTH + 1];

    while (fscanf(file, "%s", word) != EOF)
    {
        node *n = malloc(sizeof(node));

        if (n == NULL)
        {
            return false;
        }

        strcpy(n->word, word);
        n->next = NULL;

        int index = hash(word);

        n->next = table[index];
        table[index] = n;
        counter++;
    }

    fclose(file);

    return true;
}

//Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    return counter;
}

//Unloads dictionary from memory, return true if successful, else false
bool unload(void)
{
    node *cursor = NULL;

    for (int i = 0; i < N; i++)
    {
        cursor = table[i];

        while (cursor != NULL)
        {
            node *temp = cursor;
            cursor = cursor->next;

            free(temp);
        }
    }

    return true;
}
