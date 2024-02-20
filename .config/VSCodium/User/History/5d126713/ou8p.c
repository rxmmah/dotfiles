/* signed.c */

#include <stdio.h>
#include <stdlib.h>

int main(void) {
    
	signed int a = 5; // Äquivalent zu:   int a = 5;
	unsigned int b = -5;

    printf("a: %d \n", a);
	printf("a: %u \n", a);
	printf("b: %d \n", b);
	printf("b: %d \n", b);
	
	printf("a: %d \n", abs(a));
	printf("a: %u \n", abs(a));
	printf("b: %d \n", abs(b));
	printf("b: %u \n", abs(b));
	
	printf("%d \n", -5);
	printf("%u \n", -5);
	
	printf("%d \n", -7);
	printf("%u \n", -7);
	
    return 0;
}