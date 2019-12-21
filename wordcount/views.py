from django.http import HttpResponse
from django.shortcuts import render
import operator

def firstcar(request):
    return HttpResponse("Ciaz was the first car I bought")

def landing(request):
    return render(request,'landing.html',{'India':'Delhi', 'USA':'Washington'})

def about(request):
    return render(request,'about.html')

def count(request):
    #Use the GET method to get the content from the Form Box - fulltext
    fulltext = request.GET['fulltext']

    #To count we can use the split method.
    wordlist = fulltext.split()

    #To count occurrences of individual words, create a dictionary of all words
    #Then assign as values to them their occurrences
    count_words = {}

    for word in wordlist:
        if word in count_words:
            count_words[word]+=1
        else:
            count_words[word]=1

    #Return the text back on to the count page as dictionary
    # return render(request,'count.html', {'yourtext':fulltext, 'wordcount':len(wordlist), 'count_words':count_words})

    #Performing Sorting
    #key=operator.itemgetter(1) constructs a callable and fetches (1)th element of it - Here the value.
    sorted_words = sorted(count_words.items(), key=operator.itemgetter(1), reverse=True)

    #Return the text back on the count page as List
    return render(request,'count.html', {'yourtext':fulltext, 'wordcount':len(wordlist), 'sorted_words':sorted_words})
