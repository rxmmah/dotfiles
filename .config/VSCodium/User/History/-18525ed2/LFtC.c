#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int main(){
    int i, zaehler, wert=0;
    for (i=0; i<= 2; i++){
        zaehler = abs(i);
        double placeholder = round(pow(i, 2));
        while (zaehler <= placeholder) {
          wert += i * zaehler;
          zaehler++;
        }
    }
}