#! python3
# pw.py password manager

PASSWORDS = {
    'email': 'sasfuhdiashdioashdoahd',
    'blog': 'dnadnsadnuasdbas',
    'luggage': '12345'
}

import sys
if len(sys.argv):
    print('How to use : python pw.py')
    print('copy password to clipboard')
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print(account + 'のパスワードをcopy to clipboard')
else:
    print(account + 'というアカウントはありません')
