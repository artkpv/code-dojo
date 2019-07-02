import subprocess, re

subprocess.check_output(["gcc", "-o", "preprocessor.out", "-g", "preprocessor.c"],
		universal_newlines=True)

def call_test(name, given, expected):
	print("\n==========\nTEST: " + name)
	out = subprocess.check_output( ["./preprocessor.out"],
			input=given,
			universal_newlines=True)

	print(" actual:\n " + out)
	print(" expected:\n " + expected)
	if(out != expected) :
		print(" FAILED")
	else:
		print(" SUCCESS")


call_test("one define one substitude", """\
#define TEST 1
while(TEST) ;
""", """\
#define TEST 1
while(1) ;
""")

call_test("", """\
/* getline:  read a line into s, return length  */
int mygetline(char *s, int lim)
{
	int c, i;

	for (i=0; i < lim-1 && (c=getchar())!=EOF && c!='\\n'; ++i)
		*(s++) = c;
	if (c == '\\n') {
		*(s++) = c;
		++i;
	}
	*s = '\\0';
	return i;
}

#define HASHSIZE 101
""", """\
/* getline:  read a line into s, return length  */
int mygetline(char *s, int lim)
{
	int c, i;

	for (i=0; i < lim-1 && (c=getchar())!=EOF && c!='\\n'; ++i)
		*(s++) = c;
	if (c == '\\n') {
		*(s++) = c;
		++i;
	}
	*s = '\\0';
	return i;
}

#define HASHSIZE 101
""")

