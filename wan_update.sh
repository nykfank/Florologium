#!
cd ~/wan
curl -s ifconfig.me >address.txt
git add address.txt 
git commit -m "Update"
git push https://nykfank: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@github.com/nykfank/wan.git --all

