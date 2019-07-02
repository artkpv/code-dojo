import subprocess, re

subprocess.check_output(["gcc", "-o", "getword.out", "getword.c"],
		universal_newlines=True)

def call_test(name, given, expected):
	print("\n==========\nTEST: " + name)
	out = subprocess.check_output( ["./getword.out"],
			input=given,
			universal_newlines=True)
	print(" out:\n " + out)
	actual = dict()
	for line in out.split('\n'):
		m = re.search("\s*(\d+)\s+(\w+)", line)
		if(m):
			actual[m.group(2)] = int(m.group(1))

	for k in expected.keys():
		if(k not in actual):
			print("FAIL: key '{}' not found in".format(k))
			print(repr(actual))
			return
		if(expected[k] != actual[k]):
			print("FAIL: for '{}' key, expected {}, but was {}".format(k, expected[k],
					actual[k]))
			return
	print(" SUCCESS")

call_test("three whiles", """\
while
while
while
break;
""", {"while": 3, "break": 1} )

call_test("underscore test", """\
while(1) {
	while_;
	_while;
}
while(1)
	true;
void main(void* p) {
	_void;
}
""", {"while": 2, "void": 2} )

call_test("skips string constants", """\
auto myvar = "auto \\" auto";

""", {"auto": 1} )

call_test("skips comments", """\
auto myvar;
while(1);
//auto myvar;
/*
auto myvar*/

// while

""", {"auto": 1, "while": 1} )


call_test("skips preprocessor", """\
auto myvar;
#define something auto
""", {"auto": 1} )
