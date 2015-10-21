import sys
import subprocess

user_name = sys.argv[1]
github_repo_name = sys.argv[2]
gitbook_repo_name = sys.argv[3]

github_repo_url = "https://github.com/{name}/{repo}.git".format(name=user_name, repo=github_repo_name)
gitbook_repo_url = "https://git.gitbook.com/{name}/{repo}.git".format(name=user_name, repo=gitbook_repo_name)

subprocess.call("git remote set-url --add --push origin "+github_repo_url, shell=True)
print "> Add pushurl {} to remote origin".format(github_repo_url)
subprocess.call("git remote set-url --add --push origin "+gitbook_repo_url, shell=True)
print "> Add pushurl {} to remote origin".format(gitbook_repo_url)
print "> Mission Complete"
