$ErrorActionPreference = "Stop"
pushd (Split-Path $MyInvocation.InvocationName -resolve)

$compiler_output
cl xsort.c | tee -var compiler_output


if($compiler_output -match ' : error \w+:') { throw 'Failed to compile' } 

function test([string]$name, [string] $given, [string] $expected, [string[]] $switches) 
{
  $out = ""
  
  Write-Output ` "`nTEST - $name (switches: $switches)`n===================="
  $given | .\xsort.exe $switches | out-string | tee -var out | out-null
  
  $out = $out.trim("`n")
  $expected = $expected.trim("`n")
  if($out.equals($expected)) { write-output "FAILED" }
  else { write-output  "SUCCESS" }
  write-output ("Given: '$given'`nExected: '$expected'`nActual: '$out'")
}

& test "Folding test" -given "a`nA" -exp "a`nA" -s @("-f")
& test "Non directory test: sorts by nonalpha" -g "#A`n!A" -e "!A`n#A" -s @("")
& test "Directory test: skips '#'" -g "#A`n!A" -e "#A`n!A" -s @("-d")
& test "Directory test: skips '#'" -g "#a`n!A" -e "!A`n#a" -s @("-d -f")

popd
