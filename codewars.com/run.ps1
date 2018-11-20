param($sourceFile)
if(-not (test-path $sourceFile)) { throw 'need source file' } 

if(-not (test-path 'bin')) { mkdir 'bin' > $null } 

if(-not (test-path 'packages')) { 
	mkdir packages  > $null
	pushd packages 
	Write-Host 'downloading nuget...'
	& curl https://dist.nuget.org/win-x86-commandline/latest/nuget.exe -O -k -s
	Write-Host 'installing packages...'
	.\nuget.exe install NUnit.Runners.lite 
	.\nuget.exe install Microsoft.Net.Compilers
	popd
} 

ls (resolve-path .\packages\NUnit.Runners.lite*\*) -include *dll,*exe,*config | copy -desti 'bin\' -force 
ls (resolve-path .\packages\NUnit.Runners.lite*\lib\*) | copy -dest 'bin\' -force

Write-Host 'compiling...'
. "$((resolve-path .\packages\Microsoft.Net.Compilers*).Path)\tools\csc.exe" `
	/debug `
	/t:library $sourceFile `
	/r:.\bin\nunit.framework.dll `
	/r:System.Numerics.dll 
if($LASTEXITCODE -ne 0) { return }

$fileWithoutExtension = (split-path $sourceFile -leaf) -replace '.cs$',''
move "$fileWithoutExtension.dll","$fileWithoutExtension.pdb" -destin 'bin\' -force

Write-Host "testing...`n"

pushd bin
try { 
	.\nunit-console.exe "$fileWithoutExtension.dll"
}
finally {
	popd
}
