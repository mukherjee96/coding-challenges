#include<stdio.h>
#include<conio.h>

int main() {

	int i, j, c = 1, n;

	scanf("%d", &n);

	for(i=0; i<n; i++) {

		for(j=n-i-1; j>=0; j--) {
			printf(" ");
		}

		for(j=i+c; j>0; j--) {
			printf("*");
		}

		printf("\n");

		c++;
	}

	c = c-2;

	for(i=n-2; i>=0; i--) {

		for(j=n-i-1; j>=0; j--) {
			printf(" ");
		}

		for(j=i+c; j>0; j--) {
			printf("*");
		}

		printf("\n");

		c--;
	}

	return 0;
}