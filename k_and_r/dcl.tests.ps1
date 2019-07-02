$ErrorActionPreference = "Stop"
pushd (Split-Path $MyInvocation.InvocationName -resolve)

$compiler_output
cl .\dcl.c | tee -var compiler_output
if($compiler_output -match ' : error \w+:') { throw 'Failed to compile' }

function test([string]$name, [string] $given, [string] $expected, [string[]] $switches)
{
  $out = ""

  Write-Output ` "`nTEST - $name ('$switches')`n===================="
  $given | .\dcl.exe $switches | out-string | tee -var out | out-null

  $out = $out.trim("`n")
  $expected = $expected.trim("`n")
  if($out -notmatch [regex]::escape($expected)) { write-host "FAILED" -foreground red }
  else { write-host  "SUCCESS" -foreground green }
  write-output ("Given: '$given'`nExected: '$expected'`nActual: '$out'")
}

& test "test 1" -g "char *argv" -e "argv: pointer to char"
# dcl 
#  dirdcl -> { name = ..{
# >dcl  > 'pointer to'

& test "test 2" -g "int (*daytab)[13]" -e "daytab: pointer to array[13] of int"
# main -> 'int'
# dcl 
#  dirdcl {'('}
#   dcl {ns++}
#    dirdcl {name}
#   >dcl -> 'pointer to
#  >dirdcl 
#

& test "test 3" -g "int *daytab[13]" -e "daytab: array[13] of pointer to int"
& test "test 4" -g "void *comp()" -e "comp: function returning pointer to void"
& test "test 4 with whitespace" `
	-g "void *comp(  )" `
	-e "comp: function returning pointer to void"
& test "test 5" -g "void (*comp)()" -e "comp: pointer to function returning void"
& test "test 6" -g "char (*(*x())[])()" -e "x: function returning pointer to array[] of pointer to function returning char"
& test "test 7" -g "char (*(*x[3])())[5]" -e "x: array[3] of pointer to function returning pointer to array[5] of char"

& test "Var declaration" -given "char var1" -exp "var1: char"

& test "Pointer to poiter" `
	-given "char **pointertopointertochar" `
	-exp "pointertopointertochar: pointer to pointer to char"

& test "Error: no first datatype" `
	-given "[]char var1" `
	-exp "Failed to parse: first token should be datatype"

& test "Only name" -g "int var1" -e "var1: int"

& test "arguments test" `
	-g "void *comp(int)" `
	-e "comp: function of (int ) returning pointer to void"
& test "arguments test 2" `
	-g "void *comp(int, int)" `
	-e "comp: function of (int and int ) returning pointer to void"
& test "arguments test 3" `
	-g "void *comp(int (*)(), int)" `
	-e "comp: function of (pointer to function returning int and int ) returning pointer to void"


popd
