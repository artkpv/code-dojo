
cl .\ex_5-2_getfloat.c

if($lastexitcode) {
	throw 'Fail to compile'
}

"TEST 1"
"======"
$output
"123.45" | .\ex_5-2_getfloat.exe | tee -var output
if($output -notmatch '123\.45') { write-output 'FAIL: 123.45' }
else { write-output 'SUCCESS: 123.45' } 
