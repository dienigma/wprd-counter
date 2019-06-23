from django.http import HttpResponse
from django.shortcuts import render
import operator


def homepage(request):
    return render(request,'home.html',{'hithere':'This is me'})

def count(request):

    fulltext = request.GET['fulltext']

    wordList = fulltext.split(' ')

    wordDictonary ={}

    for word in wordList:
        if word in wordDictonary:
            # Increase
            wordDictonary[word] += 1
        else:
            # Decrease
            wordDictonary[word] = 1
    sortedwords = sorted(wordDictonary.items(),key=operator.itemgetter(1),reverse=True)
    return render(request,'count.html',{'fulltext':fulltext,'count':len(wordList),'sortedwords': sortedwords})

def about(request):
    return render(request,'about.html')
