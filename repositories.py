import sqlite3

class Repositories:
    
    def __init__(self):
        self.repos = "[Sqlite db file]"
        self.dbtable = "[Name of table in DB]"
        
    def getGitRepos(self):
        reposList = []
        DB = sqlite3.connect(self.repos)
        cur = DB.cursor()
        Query = "SELECT * FROM " + str(self.dbtable)
        cur.execute(Query)
        result = cur.fetchall()
        
        for data in result:
            reposList.append({
                'id': data[0],
                'name': data[1],
                'local': data[2],
                'remote': data[3],
                'build': data[4]
            })
            
        return reposList   
    
    def getRepoByID(self, id):
        repo = []
        DB = sqlite3.connect(self.repos)
        cur = DB.cursor()
        Query = "SELECT * FROM " + str(self.dbtable) + " WHERE id = " + str(id)
        cur.execute(Query)
        result = cur.fetchone()
        
        repo.append({
            'id': result[0],
            'name': result[1],
            'local': result[2],
            'remote': result[3],
            'build': result[4]
        })
            
        return repo[0]    