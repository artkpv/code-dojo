
DIR=$PWD

ssh -i ~/.ssh/id_rsa webmaster@35.204.103.96 'rm ~/tmp -rf > /dev/null; mkdir ~/tmp'

scp -i ~/.ssh/id_rsa $DIR/* 'webmaster@35.204.103.96:~/tmp'

ssh -i ~/.ssh/id_rsa 'webmaster@35.204.103.96' 'cd ~/tmp; mcs -sdk:4 -optimize -o pr.exe pr.cs; for i in in*.txt; do echo "Executing '$i' test"; ./pr.exe < $i; done'
