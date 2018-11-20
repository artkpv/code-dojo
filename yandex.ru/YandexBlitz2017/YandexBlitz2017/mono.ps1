echo 'compiling..'
& "C:\Program Files\Mono\bin\dmcs.bat" -r:System.Numerics -sdk:4 -optimize -out:mono.o @args
echo 'running..'
& "C:\Program Files\Mono\bin\mono.exe" .\mono.o

