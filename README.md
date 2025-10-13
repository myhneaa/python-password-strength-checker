# Password Strength Checker
Simple CLI python script that checks the strength of a given password

v1.0 - First release!

Features:
- Checks password against a common passwords list (https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/100k-most-used-passwords-NCSC.txt)
- Length analysis (<= 8 -> +0 score; 8 <= length < 12 -> +1 score etc)
- Improvement advisory
		

Prerequisites: 
- Python 3.x minimum
  
Installtation:
- cd into script directory and run "python psc.py"
- alternatively, run the script inside an IDE
- or any other method that works, really	

Todo:
- GUI interface (maybe??)
