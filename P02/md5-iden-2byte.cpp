/* https://www.openssl.org/docs/manmaster/man3/MD5_Update.html
   
   Compile with: g++ -O3 md5.cpp -Wall -lssl  -lcrypto
*/
#include <openssl/md5.h>

#include <iostream>
#include <stdio.h>
#include <string>
#include <cstring>

using namespace std;

int main(){

    unsigned char output[16] = {};  // 128bits is 16 bytes
    // MD5 outputs a 128bit message digest, which is 16 bytes long

    for(int i = 0; i < 256 * 256; i++){
        short int in = i;
        MD5((unsigned char*)&in, 2, output);
        if(memcmp(&in, output, sizeof(in)) == 0 ){
            cout << "Input: " << i << ", is the same as output: " << i << endl;
        }
    }
    cout << endl;
}