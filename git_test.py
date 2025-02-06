import os
ch = input('Ready to Commit Answers? (Y/N)')
if ch == 'Y':
    os.system("git status")
    os.system("git add .")
    os.system("git commit -m 'Testing' ")