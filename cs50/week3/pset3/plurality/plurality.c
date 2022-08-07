#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <strings.h>

// Max number of candidates
#define MAX 9

// Candidates have name and vote count
typedef struct
{
    string name;
    int votes;
}
candidate;

// Array of candidates
candidate candidates[MAX];

// Number of candidates
int candidate_count;

// Function prototypes
bool vote(string name);
void print_winner(void);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: plurality [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
    }

    int voter_count = get_int("Number of voters: ");

    // Loop over all voters
    for (int i = 0; i < voter_count; i++)
    {
        string name = get_string("Vote: ");

        // Check for invalid vote
        if (!vote(name))
        {
            printf("Invalid vote.\n");
        }
    }

    // Display winner of election
    print_winner();
}

// Update vote totals given a new vote
bool vote(string name)
{
    // TODO
    bool voteName = false;
    for(int l = 0; l < candidate_count; l++){
        if(strcasecmp(name, candidates[l].name) == 0){
            candidates[l].votes+=1;
            voteName = true;
        }
    }
    return voteName;

}

// Print the winner (or winners) of the election
void print_winner(void)
{
    int winner = -1;
    // TODO
    for(int g = 0; g < candidate_count; g++){
        if(candidates[g].votes > winner){
            winner = candidates[g].votes;
        }

    }
        for(int t = 0; t < candidate_count; t++){
                if(candidates[t].votes == winner){
                printf("%s\n", candidates[t].name);
        }        }
}
