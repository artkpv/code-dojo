
// Author : Artyom K., w1ld at inbox dot ru; Jul, 2015

int any(char s[], char s1[])
{
	char c;
	for(int i = 0; (c = s[i]) != '\0'; i++)
	{
		int j = -1;
		while(s1[++j] != '\0')
		{
			if(s1[j] == c)
				return i;
		}
	}

	return -1;
}

void assert_any(char s[], char s1[], int expected)
{
	int i = any(s, s1);
	if(i != expected)
	{
		printf("FAIL: any(%s, %s) : %d != %d\n", s, s1, i, expected);
	}
	else
	{
		printf("SUCC: any(%s, %s) : %d == %d\n", s, s1, i, expected);
	}
}

int main(void)
{
	assert_any("abc", "bc", 1);
	assert_any("abc", "c", 2);
	assert_any("abc", "defc", 2);
	assert_any("abc", "de", -1);
}
