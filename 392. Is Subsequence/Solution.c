#include <string.h>
bool isSubsequence(char * s, char * t){
  int j = 0;
  for(int i =0 ; i<strlen(t) ; i++){
    if(j<strlen(s) && s[j] == t[i]){
      j += 1;
    }
  }
  return j == strlen(s);
}