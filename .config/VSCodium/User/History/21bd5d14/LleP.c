
/* 
 * Datei:   addition.c
 * Aufgabe: Addition von 2 Zahlen
 */

#include <stdio.h>

int main(void) {
        
    int zahl1;  // Speichervariable fuer die erste ganze Zahl  
    int zahl2;  // Speichervariable fuer die zweite ganze Zahl
    int ergebnis;  // Speichervariable fuer das Ergebnis
    
    // Ausgabe Text auf der Konsole
    printf("Gib eine ganze Zahl ein: ");
    // Eingabe eines Wertes fuer die erste ganze Zahl
    scanf("%d", &zahl1);
    
    // Ausgabe Text auf der Konsole
    printf("Gib noch eine ganze Zahl ein: ");
    // Eingabe eines Wertes fuer die zweite ganze Zahl
    scanf("%d", &zahl2);
    
    // Addition der beiden Zahlenwerte
    ergebnis = zahl1 + zahl2;
    
    // Anzeige der Summe auf der Konsole
    printf("\n%2d + %3d = %4d\n", zahl1, zahl2, ergebnis);
    
    // Programmende
    return (0);
}

