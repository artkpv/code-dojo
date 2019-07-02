#include <stdio.h>

int main(void)
{
	char c;
	while((c = getch()) != EOF)
	{
		printf("%c\n", c);
	}

	printf("END\n");
	return 0;
}
