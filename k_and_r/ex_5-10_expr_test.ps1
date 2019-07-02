
cl ex_5-10_expr.c

if($LASTEXITCODE)
{
	throw 'Compile error'
}

$output = $null
& .\ex_5-10_expr.exe 2 3 4 + * | tee -var output
if([string]::isnullorwhitespace($output))
{
	throw "FAIL test: ""2 3 4 + *""; no output"
}
$result = [int]::parse($output)
if($result -ne 14) 
{
	throw "FAIL test: ""2 3 4 + *""; $$result=$result"
}
write-output "Success test:  ""2 3 4 + *""; result=$result"

