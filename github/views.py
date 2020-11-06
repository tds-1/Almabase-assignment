from django.shortcuts import render
from .core import core
# Create your views here.
from .forms import searchForm


def main(request):
    form = searchForm()
    return render(request, "main.html",{'form':form})

def repo(request):
    global topMCommitteesDict
    if request.method == 'POST':
        form = searchForm(request.POST)
        topNRepoDict, topMCommitteesDict = core.logic(form.data['organisation'], form.data['n'], form.data['m'])
        
        return render(request, "repo.html",{'topNRepoDict':topNRepoDict,'organisation':form.data['organisation']})
    form = searchForm()
    return render(request, "main.html",{'form':form})

def user(request,repo):
    global topMCommitteesDict
    return render(request, "user.html",{'userlist':topMCommitteesDict[repo],'repo':repo})
