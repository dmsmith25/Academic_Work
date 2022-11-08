
#include <string.h>

void bystander(){

}

void function(char *str) {
    char buffer[16];

    memcpy(buffer,str, 256);
}

void main() {
    char large_string[256];
    int i;

    for( i = 0; i < 255; i++){
        large_string[i] = '\x68';
    }

    function(large_string);
}