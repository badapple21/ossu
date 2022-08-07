#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <strings.h>

string encryption(string plainText, string key);

int main(int argc, string argv[])
{
    string key="";
    int goodKey = 0;
    int total = 0;
    string alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    int repeat = 1;
    int nums[26];

    //store key
    if(argc==2){
        if(strlen(argv[1])==26){
            key = argv[1];
            goodKey = 1;
            }else{
                printf("To long\n");
                return 1;
            }
        }else{
            printf("Key must contain 26 characters.\n");
            return 1;
    }

    //checks key
    for(int i = 0, n = strlen(key);i < n;i++){
        if(isalpha(key[i])){

        }else{
            printf("Bad Key\n");
            return 1;
        }

    nums[i]=(int) key[i];
    total+=(int) toupper(key[i]);

    }
    for(int j = 0; j < 26;j++){
        for(int l = 0; l < 26;l++){
            if(nums[l]==nums[j] && l!=j){
                printf("Bad Key\n");
                return 1;
            }
        }
    }

    if(total!=2015){
        printf("Bad Key\n");
        return 1;
    }
    if(goodKey==0){
        printf("Usage: ./substitution key\n");
    }

    //ask user for plain text
    string plainText = get_string("Plain text: ");

    //call encryption function
    string enc = encryption(plainText, key);

    //print values
    printf("ciphertext: %s\n", enc);
}
//encrytiopn function
string encryption(string plainText, string key){
    //define varibles
    int position;

    // loop through each letter in text
    for(int i = 0, n = strlen(plainText);i < n;i++){
        //index of letter
        if(isalpha(plainText[i])){
            if(islower(plainText[i])){
                position = (int) plainText[i]-97;
                plainText[i] = tolower(key[position]);
            }else{
                position = (int) plainText[i]-65;
                plainText[i] = toupper(key[position]);
            }
    }
    }
    return plainText;
}