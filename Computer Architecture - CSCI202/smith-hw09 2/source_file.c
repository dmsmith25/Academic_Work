
/*
 * source_file.c
 */
#include <stdio.h>
#include <math.h>
#include <stdint.h>

// function declarations
uint64_t str_to_num(char *c);
void fully_associative_readin();
uint64_t exponent(int t, int power);
uint64_t getOffset(uint64_t add);
uint64_t getTag(uint64_t add);
void fully_associative_hom (uint64_t tag);
void direct_mapped_hom(uint64_t tag, uint64_t entry);
void direct_mapped_readin();
uint64_t getEntry(uint64_t add);
void set_associative_readin();
uint64_t setAssociativeTag(uint64_t add);
uint64_t setAssociativeEntry(uint64_t add);
void set_associative_hom(uint64_t tag, uint64_t entry);
void reset_ham();

// global variables
int hits = 0;
int misses = 0;
uint64_t cache[512];
int LRU[512];
char* read_file;


int main(int argc, char *argv[])
{

    // name of file to read in
    read_file = "large";


    // use fully associative cache on file
    fully_associative_readin();
    printf("fully associative hits: %d\n", hits);
    printf("fully associative misses: %d\n", misses);
    reset_ham();

    // use direct mapped cache on file
    direct_mapped_readin();
    printf("direct mapped hits: %d\n", hits);
    printf("direct mapped misses: %d\n", misses);
    reset_ham();
    
    // use 8 way set associative cache on file
    set_associative_readin();
    printf("8 way associative hits: %d\n", hits);
    printf("8 way associative misses: %d\n", misses);
    reset_ham();

 

}

/*
* The function reset_ham() resets the hits and misses variables to 0
* and loops through the LRU and Cache arrays and clears them so they
* consist of all 0's.
*/
void reset_ham(){
    hits = 0;
    misses = 0;

    int g;

    for(g = 0; g < 512; g = g + 1){
        cache[g] = 0;
        LRU[g] = 0;
    }
}

/*
* This function takes two parameters: t and power. Where the function
* raises the input t to the power of "power" and returns the value as
* a 64 bit integer
*
* Parameters:
* t: type = int
* power: type = int
*/
uint64_t exponent(int t, int power){
    int i;
    uint64_t res = 1;
    for(i = 0; i < power; i = i + 1){
        res = res * t;
    }
    return res;
}


/*
* This function takes in a parameter c which is a string of a number
* in hex which the function then converts to a 64 bit integer and returns
* this value. This function implements the exponent() function for each
* character in the string.
*
* Parameters:
* c: type = *char
*/
uint64_t str_to_num(char *c)
{
    uint64_t sum = 0;
    int i;
    int q = 1;
    int r = 0;

    // while there are no more chars
    while(q > 0){
        if(c[r] == 10){
            q = 0;
        }else{
            r = r + 1;
        }
    }

    // for chars in the string
    for(i = 0; i < r; i = i + 1){
        
        if(c[i] >= 97){
            int t = c[i] - 87;
            uint64_t e = exponent(16, r - i - 1);
            uint64_t expo = t * e;
            sum = sum + expo;
        }else{
            int t = c[i] - 48;
            uint64_t e = exponent(16, r - i - 1);
            uint64_t expo = t * e;
            sum = sum + expo;
        }
    }
    
    return sum;

}


/*
* This function reads through the global variable "read_file" and
* for each string in the file, it uses the str_to_num() function
* to get the numeric value of the string in hex. The function then
* gets the tag of the value for a fully associative cache.
* Then runs fully_associative_hom() to use the value to interact with the global cache
* and LRU arrays.
*/
void fully_associative_readin(){
    int i = 0;
    char str[150];
    FILE* fp;
    fp = fopen(read_file, "r");

    while (fgets(str,150, fp)) {
        i++;
        uint64_t val = str_to_num(str);

        uint64_t tag = getTag(val);

        fully_associative_hom(tag);
        
    }
}

/*
* This function reads through the global variable "read_file" and
* for each string in the file, it uses the str_to_num() function
* to get the numeric value of the string in hex. The function then
* gets the tag and entry of the value for a direct mapped cache.
* Then runs direct_mapped_hom() to use the value to interact with the global cache
* and LRU arrays.
*/
void direct_mapped_readin(){
    int i = 0;
    char str[150];
    FILE* fp;
    fp = fopen(read_file, "r");

    while (fgets(str,150, fp)) {
        i++;
        uint64_t val = str_to_num(str);

        uint64_t tag = getTag(val);
        uint64_t entry = getEntry(val);



        direct_mapped_hom(tag, entry);
        
    }
}

/*
* This function reads through the global variable "read_file" and
* for each string in the file, it uses the str_to_num() function
* to get the numeric value of the string in hex. The function then
* gets the tag and entry of the value for a set associative cache.
* Then runs direct_mapped_hom() to use the value to interact with the global cache
* and LRU arrays.
*/
void set_associative_readin(){
    int i = 0;
    char str[150];
    FILE* fp;
    fp = fopen(read_file, "r");

    while (fgets(str,150, fp)) {
        i++;
        uint64_t val = str_to_num(str);

        uint64_t tag = setAssociativeTag(val);
        uint64_t entry = setAssociativeEntry(val);

        set_associative_hom(tag, entry);

    }
}


/*
* This function takes in two parameters: tag and entry. The function uses the tag and entry
* values to interact with the Cache and LRU array in a way that a set associative cache
* would operate.
*
* Parameters:
* tag: type = 64 int
* entry: type = 64 int
*/
void set_associative_hom(uint64_t tag, uint64_t entry){

    // 1 if there is a hit and 0 if it is a miss
    int hit = 0;

    // specify end and start indexes of the 8 value set
    int end_index = ((entry + 1) * 8) - 1;
    int start_index = end_index - 7;

    // 1 is set is empty 0 if set is full
    int empty = 0;

    // if the set is not full, then this is where the value will be placed in the cache
    int t;


    // counters
    int i;
    int k;
    int q;
    int h;
    int a;

    // for each value in the given set
    for(i = 0; i < 8; i = i + 1){
        // if the value is empty and there has not been an empty value yet
        if(cache[i + start_index] == 0 && empty == 0){
            empty = 1;
            t = i + start_index;
        }
        // if there is a match
        if(cache[i + start_index] == tag){
            hit = 1;
            h = i + start_index;
        }
    }

    // if the call is a hit
    if(hit == 1){
        hits = hits + 1;
        LRU[h] = 1;
        // for each value in the LRU array
        for(k = 0; k < 8; k = k + 1){
            if(LRU[k + start_index] != 0 && k + start_index != h){
                LRU[k + start_index] = LRU[k + start_index] + 1;
            }
        }

    // if the call is a miss
    }else{
        misses = misses + 1;
        
        // if the cache is empty
        if(empty == 1){
            cache[t] = tag;
            LRU[t] = 1;
            k = 0;
            // for each value in the LRU array
            for(k = 0; k < 8; k = k + 1){
                if(LRU[k + start_index] != 0 && k + start_index != t){
                    LRU[k + start_index] = LRU[k + start_index] + 1;
                }
            }
        // if set is full
        }else{
            // get the least recently used value
            int max = 0;
            int ind;

            // for every element in LRU array
            for(a = 0; a < 8; a = a + 1){
                if(LRU[a + start_index] > max){
                    max = LRU[a + start_index];
                    ind = a + start_index;
                }
            }

            // implement eviction policy
            cache[ind] = tag;
            LRU[ind] = 1;
            k = 0;
            // for every element in LRU
            for(k = 0; k < 8; k = k + 1){
                if(LRU[k + start_index] != 0 && k + start_index != ind){
                    LRU[k + start_index] = LRU[k + start_index] + 1;
                }
            }

        }

    }
    
    


}



/*
* This function takes in two parameters: tag and entry. The function uses the tag and entry
* values to interact with the Cache and LRU array in a way that a direct mapped cache
* would operate.
*
* Parameters:
* tag: type = 64 int
* entry: type = 64 int
*/
void direct_mapped_hom(uint64_t tag, uint64_t entry){
    
    // if the place where the value should go does not match the value in the cache
    if(cache[entry] != tag){
        misses = misses + 1;
        cache[entry] = tag;
    
    // if the place where the value should go does match the value in the cache
    }else{
        hits = hits + 1;
    }

}

/*
* This function takes in two parameters: tag. The function uses the tag 
* value to interact with the Cache and LRU array in a way that a fully associative cache
* would operate.
*
* Parameters:
* tag: type = 64 int
*/
void fully_associative_hom(uint64_t tag){

    // 1 if cache is not full and 0 if cache is full
    int empty = 0;

    // if cache is not full and call is a miss this is where the value will go
    int t;

    // 1 if hit 0 if miss
    int hit = 0;


    // counters
    int i;
    int k;
    int q;
    int h;
    int a;

    // for every item in cache
    for(i = 0; i < 512; i = i + 1){
        // if cache has not yet seen an empty value and there is an empty value
        if(cache[i] == 0 && empty == 0){
            empty = 1;
            t = i;
        }
        // if the tag matches
        if(cache[i] == tag){
            hit = 1;
            h = i;
        }
    }

    // if call is a hit
    if(hit == 1){
        hits = hits + 1;
        LRU[h] = 1;
        // for every item in the cache
        for(k = 0; k < 512; k = k + 1){
            // if spot is not empty and does not equal the index of the hit
            if(LRU[k] != 0 && k != h){
                LRU[k] = LRU[k] + 1;
            }
        }
    // if call is a miss
    }else{
        misses = misses + 1;
        // if cache is not full
        if(empty == 1){
            cache[t] = tag;
            LRU[t] = 1;
            k = 0;
            // for every item in cache
            for(k = 0; k < 512; k = k + 1){
                // if spot is not empty and does not equal the index of the next available spot
                if(LRU[k] != 0 && k != t){
                    LRU[k] = LRU[k] + 1;
                }
            }

        // if cache is full
        }else{
            int max = 0;
            int ind;

            // for every item in cache
            for(a = 0; a < 512; a = a + 1){
                if(LRU[a] > max){
                    max = LRU[a];
                    ind = a;
                }
            }

            // implements eviction policy
            cache[ind] = tag;
            LRU[ind] = 1;
            k = 0;
            // for every item in cache
            for(k = 0; k < 512; k = k + 1){
                // if spot is not empty and does not equal the index of the least recently used value
                if(LRU[k] != 0 && k != ind){
                    LRU[k] = LRU[k] + 1;
                }
            }

        }

    }
}


/*
* This function takes a 64 bit integer add as a parameter and returns the
* last 6 binary bits as a 64 bit integer.
*
* Parameters:
* add: type = 64 int
*/
uint64_t getOffset(uint64_t add){
    uint64_t mask = 0x3f;
    uint64_t bottom_six_bits = add & mask;

    return bottom_six_bits;
}

/*
* This function takes a 64 bit integer add as a parameter and returns the
* first 26 binary bits as a 64 bit integer.
*
* Parameters:
* add: type = 64 int
*/
uint64_t getTag(uint64_t add){
    uint64_t mask = 0xffffffc0;
    uint64_t top_26_bits = add & mask;

    return top_26_bits;
}

/*
* This function takes a 64 bit integer add as a parameter and returns the
* last 15 thorugh 7 binary bits as a 64 bit integer.
*
* Parameters:
* add: type = 64 int
*/
uint64_t getEntry(uint64_t add){
    uint64_t mask = 0x7fc0;
    uint64_t entry = add & mask;
    entry = entry >> 6;

    return entry;
}

/*
* This function takes a 64 bit integer add as a parameter and returns the
* last 20 binary bits as a 64 bit integer.
*
* Parameters:
* add: type = 64 int
*/
uint64_t setAssociativeTag(uint64_t add){
    uint64_t mask = 0xfffff000;
    uint64_t top_20_bits = add & mask;

    return top_20_bits;
}

/*
* This function takes a 64 bit integer add as a parameter and returns the
* last 12 thorugh 7 binary bits as a 64 bit integer.
*
* Parameters:
* add: type = 64 int
*/
uint64_t setAssociativeEntry(uint64_t add){
    uint64_t mask = 0xfc0;
    uint64_t entry = add & mask;
    entry = entry >> 6;

    return entry;
}



