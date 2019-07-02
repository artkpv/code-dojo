// Author: Artyom K., July, 2015
// w1ld at inbox dot ru

/* squeeze: delete all toDelete from s */
void squeeze(char s[], char toDelete[])
{
	int i, j;
	for (i = j = 0; s[i] != '\0'; i++)
	{
		int hasToDelete = 0, k = 0;
		char c;
		while((c = toDelete[k++]) != '\0')
		{
			if(c == s[i])
				hasToDelete = 1;
		}
		
		if (!hasToDelete)
			s[j++] = s[i];
	}
	s[j] = '\0';
}

void assert_squeeze(char s[], char s1[], char expected[])
{
	squeeze(s, s1);
	int isEqual = 1;
	int i = -1;
	while(1)
	{
		if(s[--i] == '\0')
			break;
		if(s[--i] != s1[i])
			isEqual = 0;
	}
	if(!isEqual)
	{
		printf("FAILED to squeeze with %s: %s != %s\n", s1, s, expected);
	}
	else
	{
		printf("SUCCESS squeeze with %s: %s\n", s1, s);
	}
}

int main(void)
{
	assert_squeeze("abcdefg", "be", "acdfg");
	assert_squeeze("aaaabbbbccceeee", "b", "aaaaccceeee");
	return 0;
}
