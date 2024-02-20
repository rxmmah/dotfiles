
/* 
 * Datei:  tabelle.c
 * Autor:  Soenke Hoffmann
 *
 * Erstellt am 05. Oktober 2008
 *
 * Das Programm berechnet eine Tabelle 
 * mit Quadrat- und Kubikzahlen 
 * fuer n = 1 bis 10
 */

#include <stdio.h>

int main(void) {
    
    int n;
    int quadrat;
    int kubik;
    
    printf("Tabelle der Quadrat- und Kubikzahlen\n");
    printf("====================================\n");
    printf(" n quadrat   kubik\n");

    /* zaehlergesteuerte Schleife */
    for(n=1; n<=10; n=n+1) {
        quadrat = n * n;
        kubik = quadrat * n;
        printf("%2d     %3d    %4d\n", n, quadrat, kubik);
    }
    
    return (0);
}

