import os, sys

if len(sys.argv) > 1:
    commit_name = sys.argv[1]
else:
    commit_name = input("commit name:\n")

os.system("git add .")
os.system(f'git commit -am "{commit_name}"')
os.system("git push origin main");