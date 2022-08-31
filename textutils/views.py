# I have created this file - Harry
from pyexpat.errors import messages
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')
    if djtext < '0':
        return render(request, 'analyze_if_not_written.html')

    else:
        #Get the text
        djtext = request.POST.get('text', 'default')

        # Check checkbox values
        removepunc = request.POST.get('removepunc', 'off')
        fullcaps = request.POST.get('fullcaps', 'off')
        lowercase = request.POST.get('lowercase', 'off')
        newlineremover = request.POST.get('newlineremover', 'off')
        extraspaceremover = request.POST.get('extraspaceremover', 'off')
        numberremover = request.POST.get('numberremover','off')

        #Check which checkbox is on
        if removepunc == "on":
            punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
            analyzed = ""
            for char in djtext:
                if char not in punctuations:
                    analyzed = analyzed + char

            params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
            djtext = analyzed

        if(fullcaps=="on"):
            analyzed = ""
            for char in djtext:
                analyzed = analyzed + char.upper()

            params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
            djtext = analyzed

        if(lowercase=="on"):
            analyzed = ""
            for char in djtext:
                analyzed = analyzed + char.lower()

            params = {'purpose': 'Changed to Lowercase', 'analyzed_text': analyzed}
            djtext = analyzed

        if(extraspaceremover=="on"):
            analyzed = ""
            for index, char in enumerate(djtext):
                # It is for if a extraspace is in the last of the string
                if char == djtext[-1]:
                        if not(djtext[index] == " "):
                            analyzed = analyzed + char

                elif not(djtext[index] == " " and djtext[index+1]==" "):                        
                    analyzed = analyzed + char

            params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
            djtext = analyzed

        if (newlineremover == "on"):
            analyzed = ""
            for char in djtext:
                if char != "\n" and char!="\r":
                    analyzed = analyzed + char

            params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
            djtext = analyzed
        
        if (numberremover == "on"):
            analyzed = ""
            numbers = '0123456789'

            for char in djtext:
                if char not in numbers:
                    analyzed = analyzed + char
            
            params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
            djtext = analyzed

        
        if(removepunc != "on" and newlineremover!="on" and extraspaceremover!="on" and fullcaps!="on" and  lowercase!="on" and numberremover != "on"):
            return render(request, 'analyze_if_not_selected.html')
        

        return render(request, 'analyze.html', params)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')