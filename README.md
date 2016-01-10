This is WriteUps for ksnctf

## How to commit files?
git clone https://github.com/tatsuhiko36/ksnctf_WriteUps.git\r\n
git add [file]\r\n
git commit -m "write a comment for commit"\r\n
git remote add origin https://github.com/tatsuhiko36/ksnctf_WriteUps.git\r\n
git push -u origin master\r\n

## If you got an error like below...
error: The requested URL returned error: 403 Forbidden while accessing https://github.com/tatsuhiko36/ksnctf_WriteUps.git/info/refs

## Edit .git/config as below
url = https://tatsuhiko36@github.com/tatsuhiko36/ksnctf_WriteUps.git # add accountname@