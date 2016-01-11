This is WriteUps for ksnctf

## How to commit files?
git clone https://github.com/tatsuhiko36/ksnctf_WriteUps.git
git add [file]
git commit -a -m "write a comment for commit"
git remote add origin https://github.com/tatsuhiko36/ksnctf_WriteUps.git
git push -u origin master

## If you got an error like below...
error: The requested URL returned error: 403 Forbidden while accessing https://github.com/tatsuhiko36/ksnctf_WriteUps.git/info/refs

## Edit .git/config as below
url = https://tatsuhiko36@github.com/tatsuhiko36/ksnctf_WriteUps.git # add accountname@
