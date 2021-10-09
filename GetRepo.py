import requests
import unittest
import json

from unittest import mock
from unittest.mock import Mock




# def getRepoAndCommit (username):


#     if (not isinstance(username,str)):
        
#         return "username should be a string."

    
#     if(len(username.strip()) == 0):
        
#         return "username cannot be just empty spaces."


#     response  = requests.get('https://api.github.com/users/' + username +'/repos')

    
    
   
#     if(response.status_code != 200):
        

#         return "Cannot access data."


#     repos = json.loads(response.text)

#     repoNames = []

#     result = []


#     for repo in repos:
        
#         # name = repo['name']

#         # repoNames.append(name)

#         # response2 = requests.get('https://api.github.com/repos/' + username + '/' + repo['name'] +'/commits')

#         # commits = json.loads(response2.text)

#         # single = "Repo: " + name + " Number of commits: " + str(len(commits))
        
#         # # print(single)

#         # result.append(single)
#         result.append(repo['name'])
        


#     if(len(repoNames) == 0):
       
#         return "this user has no repos."


      

#     return result


'''
Since my original function calls requests.get() multiple times, and mock can only return 1 fixed data for requests.get(), 
I have to rewrite my funciton into 2 different functions, one for get repo and one for get commit.
'''

def getRepo(username):
    if (not isinstance(username,str)):
        
        return "username should be a string."

    
    if(len(username.strip()) == 0):
        
        return "username cannot be just empty spaces."


    response  = requests.get('https://api.github.com/users/' + username +'/repos')

    
    
   
    if(response.status_code != 200):
        

        return "Cannot access data."


    repos = json.loads(response.text)

    # repos = response.json()

  

    result = []

    for repo in repos:
        result.append(repo.get('name'))

    return result



def getCommit(username, repo):
    if (not isinstance(username,str)):
        
        return "username should be a string."

    
    if(len(username.strip()) == 0):
        
        return "username cannot be just empty spaces."

    
    if (not isinstance(repo,str)):
        
        return "username should be a string."

    
    if(len(repo.strip()) == 0):
        
        return "username cannot be just empty spaces."

    response  = requests.get('https://api.github.com/users/' + username +'/' + repo +'/commits')
    commits = json.loads(response.text)

    return len(commits)



class APITest (unittest.TestCase):


    @mock.patch('requests.get')

    def test1(self, mockedReq):

        mockedReq.return_value = Mock(status_code = 200, text = '[{"name":"Complexity"}, {"name": "repo2"}]')
        

        self.assertEqual(len(getRepo("nebulouspianist")),2)
        self.assertEqual(getRepo("nebulouspianist"), ['Complexity','repo2'])

    



    @mock.patch('requests.get')
    
    def test2(self, mockedReq):
        mockedReq.return_value = Mock(status_code = 200, text = '[{"commit": "commit1"}, {"commit": "commit2"},{"commit": "commit3"}]')
        self.assertEqual(getCommit("nebulouspianist","Complexity"), 3)




    
    def test3(self):
        self.assertEqual(getRepo(123), "username should be a string.")

    


if __name__ == "__main__":
    unittest.main()
    





    





