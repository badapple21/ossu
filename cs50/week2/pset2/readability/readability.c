#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <math.h>

int calculateRead(string words);


int main(void)
{
    //get input from user
    string text = get_string("Text: ");

    //calls algorithm
    int index = calculateRead(text);

    //prints result
    if(index < 1){
        printf("Before Grade 1\n");
    }else if(index > 16){
        printf("Grade 16+\n");
    }else{
        printf("Grade %i\n", index);
    }

}
// algorithm
int calculateRead(string words){
    //defines varibles
    float numberOfWords = 1.0;
    float numberOfletters = 0;
    float numberOfSentences = 0;
    float percentSentences = 0;
    bool lastletterNotSpace = true;
    float index;

    //lops through eact letter in the text
    for(int i = 0, n = strlen(words); i < n;i++){
        //checks for spaces
        if(words[i]==' ' && lastletterNotSpace){
            numberOfWords+=1.0;
            lastletterNotSpace = false;
        // cheacksfor end of sentence
        }else if(words[i]=='.' || words[i]=='?' || words[i]=='!'){
            numberOfSentences+=1.0;
            lastletterNotSpace = true;
        //checks for letter
        }else if(isalpha(words[i])){
            numberOfletters+=1.0;
            lastletterNotSpace = true;
        }
    }

    //number of letters per 100 words
    float percentletters = numberOfletters/numberOfWords*100;


    // sentences per 100 words
    percentSentences = numberOfSentences/numberOfWords*100;

    //algo
    index  = round(0.0588 * percentletters - 0.296 * percentSentences - 15.8);

    return index;
}