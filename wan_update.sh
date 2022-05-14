#!
cd ~/wan
curl -s ifconfig.me >address.txt
git add address.txt
git commit -m "Update" --quiet
git push https://nykfank:GITHUB_PUBLIC_ACCESS_KEY@github.com/nykfank/wan.git --all

