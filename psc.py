#################################
### PASSWORD STRENGTH CHECKER ###
#################################

### Shoutouts to Daniel Miessler for the common passwords list!
### https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/100k-most-used-passwords-NCSC.txt

import string
import os

def checkCommonPasswords(password):
    baseDir = os.path.dirname(os.path.abspath(__file__)) # get working directory path
    filePath = os.path.join(baseDir, 'pw.txt') # concatenate filename to directory path
    
    with open(filePath, 'r') as pw:
        common = pw.read().splitlines() # opens common passwords file and splits the string at each line break into a string

    pw.close()

    if password in common:
        return True
    return False

def checkPasswordStrength(password):
    score = 0
    length = len(password)

    lowerCase = any(c.islower() for c in password) # True if lowercase found / False if not
    upperCase = any(c.isupper() for c in password) # True if uppercase found / False if not
    digit = any(c.isdigit() for c in password) # True if digit found / False if not
    special = any(c in string.punctuation for c in password) # True if special character found / False if not

    characters = [lowerCase, upperCase, digit, special] # bool array: min sum 0, max sum 4

    if length > 8: # 1 point for length at least 8 characters
        score += 1
    if length > 12: # 2 points for length at least 12 characters
        score += 1
    if length > 17: # 3 points for length at least 17 characters
        score += 1
    if length > 20: # 4 points for length at least 20 characters
        score += 1

    score += sum(characters) - 1 # adds the sum of bool array: 0 if no conditions met, 4 if all conditions met
    
    if score < 4:
        return "Weak", score
    elif score == 4:
        return "Okay", score
    elif 4 < score < 6:
        return "Good", score
    else:
        return "Strong", score
    

def feedback(password):
    if not password:
        return "Enter a password!"
    
    if checkCommonPasswords(password):
        return "Common password! Score: 0/7" # common passwords list in pw.txt
    
    strength, score = checkPasswordStrength(password) # string strength, int score

    feedback = f"Password strength: {strength} (Score: {score}/7)\n"

    if score < 4:
        feedback += "Suggestions for password improvement:\n"

        if len(password) <= 8:
            feedback += "- Use a longer password (More than 8 characters).\n"

        if not any(c.islower() for c in password):
            feedback += "- Use at least a lowercase letter.\n"
        
        if not any(c.isupper() for c in password):
            feedback += "- Use at least an uppercase letter.\n"

        if not any(c.isdigit() for c in password):
            feedback += "- Use at least a digit.\n"

        if not any(c in string.punctuation for c in password):
            feedback += "- Use at least a special character (@, !, -, _ etc)"

    return feedback

password = input("Enter the password: ")
print(feedback(password))

###########
### END ###
###########
