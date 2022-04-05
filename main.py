from gitbuild import GitBuild
from repositories import Repositories

print("------------------------------------------------------------------ \n")
print("Python script to save your changes to Git \n")
print("------------------------------------------------------------------ \n")

repos = Repositories()
for repo in repos.getGitRepos():
    print(str(repo['id']) + ') ' + str(repo['name']))

print("")
reponr = int(input("Choose repository to commit: "))
commitmsg = str(input("Commit message: "))

repo = repos.getRepoByID(reponr)

if commitmsg:
        
    GitBuild = GitBuild(repo['local'], repo['remote'],commitmsg)
    GitBuild.SaveToGit()
    
    # npm build for React projects
    if repo['react'] == True:
        GitBuild.ReactCreateBuild()