param($url=$(throw 'need ur'))

$uri = [uri]::new($url)
$p = $uri.LocalPath
$p = $p -replace '^\/', ''
$p = $p -replace '\/$', ''
$p = $p -replace '\/problem', ''
if ($p -notmatch '[a-zA-Z-]+$') { throw 'invalid url' }
$name = $Matches[0]
$absPath = [System.IO.Path]::Combine($PSScriptRoot, $p)
mkdir $absPath
$pythonFile =  ([System.IO.Path]::Combine($absPath, $name)) + '.py'
"#!python3" > $pythonFile
gvim $pythonFile
