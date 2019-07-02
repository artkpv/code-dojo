void throw(char s[])
{
	printf(s);
	printf("\n");
	exit();
}

int convert_hex(char c)
{
	if(c >= '0' && c <= '9')
		return c - '0';

	if(c >= 'a' && c <= 'f')
		return 10 + (c - 'a');

	if(c >= 'A' && c <= 'F')
		return 10 + (c - 'A');

	printf("(converting '%c')\n", c);
	throw("can not convert to hex");
	return 0;
}

int htoi(char s[])
{
	int i = 0;
	char c;

	int isPrefixed = s[0] == '0' && (s[1] == 'x' || s[1] == 'X');
	if(isPrefixed) i = 2;

	int n = 0;
	while((c = s[i]) != '\0')
	{
		int hex = convert_hex(c);
		n = n * 16 + hex;
		i++;
	}
	return n;
}

void assert_htoi(char s[], int expected)
{
	int r = htoi(s);
	if(r != expected)
	{
		printf("expected %d but returned %d of %s\n", expected, r, s);
		throw("fail\n");
	}
	else
	{
		printf("success: htoi(\"%s\") == %d, expected %lx\n", s, r, expected);
	}
}

int main(void)
{
	assert_htoi("f", 15);
	assert_htoi("ff", 255);
	assert_htoi("F", 15);
	assert_htoi("FF", 255);
	assert_htoi("0xFF", 255);
	assert_htoi("0xF", 15);
	assert_htoi("0xAABBE604", 2864440836);  // TODO: why prints this? htoi("0xAABBE604") == -1430526460, expected aabbe604
	return 0;
}

