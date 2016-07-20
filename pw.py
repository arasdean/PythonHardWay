#! python3
# pw.py -- password locker program

PASSWORDS = {'arasdean@berkeley.edu': 'hello124',
'Nihari':'123Nihari', 'luggage': '12345'}

import sys, pyperclip
if len(sys.arv) < 3:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]           #first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')

else:
    print('There is no account named' + account)
