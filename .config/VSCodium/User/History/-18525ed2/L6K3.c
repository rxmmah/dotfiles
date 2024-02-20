#include <stdio.h>
#include <math.h>
#include <stdlib.h>
int main(){
    int i, zaehler, wert=0;
    for (i=0; i<= 2; i++){
        zaehler = abs(i);
        while (zaehler <= round(pow(i,2))){
            wert += i * zaehler;
            zaehler++;
        }
    }
}