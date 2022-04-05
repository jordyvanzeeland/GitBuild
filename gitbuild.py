import git, subprocess, os, shutil
import pysftp   

class GitBuild:
    
    def __init__(self, local, remote, commitmsg):
        self.local = local
        self.remote = remote
        self.commitmsg = commitmsg  

    def SaveToGit(self):
        
        # Get local repository
        repo = git.Repo(self.local)
        
        # Add files that changed
        repo.git.add('--all')
        
        # Commit the files
        repo.git.commit('-m', self.commitmsg)
        
        # Push to git
        repo.remotes.origin.set_url(self.remote)
        repo.git.push('origin', 'master')
        
        print("Saved to Git!")
        
    def ReactCreateBuild(self):
        
        # Run build
        if os.path.exists(self.local):
            
            print("Create build")
            
            # Delete existing build map
            if os.path.exists(self.local + '/build'):
                shutil.rmtree(self.local + '/build');
                
            # change current work sirectory and run build
            os.chdir(self.local)
            subprocess.check_call('npm run build', shell=True)
            
            print("Build created")