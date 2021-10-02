import requests
import unittest
import json



def getRepoAndCommit (username):


    if (not isinstance(username,str)):
        
        return "username should be a string."

    
    if(len(username.strip()) == 0):
        
        return "username cannot be just empty spaces."


    response  = requests.get('https://api.github.com/users/' + username +'/repos')

    
    
   
    if(response.status_code != 200):
        

        return "Cannot access data."


    repos = json.loads(response.text)

    repoNames = []

    result = []


    for repo in repos:
        
        name = repo['name']

        repoNames.append(name)

        response2 = requests.get('https://api.github.com/repos/' + username + '/' + repo['name'] +'/commits')

        commits = json.loads(response2.text)

        single = "Repo: " + name + " Number of commits: " + str(len(commits))
        
        # print(single)

        result.append(single)


    if(len(repoNames) == 0):
       
        return "this user has no repos."

        

    return result



# print(getRepoAndCommit("nebulouspianist"))


class Test (unittest.TestCase):

    def test1(self):

        # since it will be too messy to test the whole list, I will just test the length of the list.
        self.assertEqual(len(getRepoAndCommit("nebulouspianist")),19)

 
    
    def test2(self):
        self.assertEqual(getRepoAndCommit('   '), "username cannot be just empty spaces.")
    
    def test3(self):
        self.assertEqual(getRepoAndCommit(123), "username should be a string.")

    

if __name__ == "__main__":
    unittest.main()
    

    



    





