$output = $null
$testout = $null

# Test 1
"123" | .\ex_5-1_getint.exe | tee -var output | select-string "(0: 123)" | tee -var testout
if($testout -eq $null)
{
	throw 'FAILED'
}
