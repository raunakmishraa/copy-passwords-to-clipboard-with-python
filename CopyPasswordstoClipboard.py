import os
import sys,pyperclip
email_pswd = os.environ.get('pswdkr077')
email409 = os.environ.get('pswd409')
passwords = {
    'kremail': email_pswd,
    'clzemail': email409
    }

account = sys.argv[1]
if account in passwords:
    pyperclip.copy(passwords[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    error = "There is no account named "+account
    pyperclip.copy(error)
    print(error)
