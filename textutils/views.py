# I have created this file - varaliya mohammed
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')

def analyze(request):
    # get the text
    djtext = request.POST.get('text', 'default')

    # check checkbox values
    removepunc = request.POST.get('removepunc', 'Off')
    fullcaps = request.POST.get('fullcaps', 'Off')
    newlineremover = request.POST.get('newlineremover', 'Off')
    extraspaceremover = request.POST.get('extraspaceremover', 'Off')
    charcounter = request.POST.get('charcounter', 'Off')

    # check which checkbox is on
    if removepunc == "on":
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Remove Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

    if(fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'changed to uppercase', 'analyzed_text': analyzed}
        djtext = analyzed

    if(newlineremover == "on"):
        analyzed = " "
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'remove new line', 'analyzed_text': analyzed}
        djtext = analyzed

    if(extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'remove extra space', 'analyzed_text': analyzed}
        djtext = analyzed

    if(charcounter == "on"):
        charcount = 0
        for char in enumerate(djtext):
            charcount += 1
            analyzed = (f"Total character : {str(charcount)}")
        params = {'purpose': 'count the character', 'analyzed_text': analyzed}
        djtext = analyzed

    if (removepunc != "on" and fullcaps != "on" and newlineremover != "on" and extraspaceremover != "on" and charcounter != "on"):
        analyzed = "Please Select Any Operation And Try Agin!!"
        params = {'purpose': 'You have not select any operation, so', 'analyzed_text': analyzed}
        return render(request, 'analyze_if_not_selected.html', params)

    return render(request, 'analyze.html', params)
