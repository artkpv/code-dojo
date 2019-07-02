
int x = '0';

void foo(char s[], char s1[])
{
	printf("Foo called with %s, %s\n", s, s1);
	s[0] = x;
	x++;
	printf("Foo exits with %s, %s\n", s, s1);
}

int main(void)
{
	foo("bar", "bar");
	foo("bar", "bar");
}
