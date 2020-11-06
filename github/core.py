import heapq
import requests

import os
import environ

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

tokenId = env('TOKEN_ID')
apiPrefix = 'https://api.github.com/'
queryString = '?access_token='+tokenId+'&per_page=100&page='

#Collection of input from user
class core:
    def logic(orgName, N, M):
        N = int(N)
        M = int(M)
        repoList=[]
        topNRepoDict = {}
        topMCommitteesDict = {}
        pageNum=1
        while(True):    
            request = requests.get(apiPrefix+'orgs/'+orgName+'/repos'+queryString+str(pageNum))
            json = request.json()
            if(len(json) == 0):        
                break
            for repo in range(len(json)):
                x = json[repo]
                repoList.append((x["forks_count"],x["name"], x["stargazers_count"], x["language"])) #storing no. of forks and repo name in repoList as tuples
            pageNum+=1
        
        repoList.sort(reverse=True)

        for count in range(0,min(N,len(repoList))):
            forkCount,repoName,star,language = repoList[count]
            topNRepoDict[repoName] = (forkCount,star,language)     
            topMCommitteesDict[repoName] = []      

        for repo in topMCommitteesDict:
            committeesList = [] 
            pageNum = 1
            while(True):  
                request = requests.get(apiPrefix+'repos/'+orgName+'/'+repo+'/contributors'+queryString+str(pageNum))
                json = request.json()
                if(len(json) == 0):
                    break
                for contributor in range(len(json)):
                    x = json[contributor]
                    committeesList.append((x["contributions"],x["login"],x["avatar_url"],x["html_url"])) 
                pageNum+=1

            committeesList.sort(reverse=True)
            
            for count in range(0,min(M,len(committeesList))):
                contributionCount,contributorName,avtar,url=committeesList[count]
                topMCommitteesDict[repo].append((contributorName,contributionCount,avtar,url))

        return (topNRepoDict,topMCommitteesDict)
