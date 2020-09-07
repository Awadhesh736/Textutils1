# i have created this file - Awadhesh
from django.http import HttpResponse
from django.shortcuts import render


def index(request):

    return render(request,'index.html',)
    # return HttpResponse("hello awadhesh")
def analyze(request):
    # get the text
    djtext =request.POST.get('text','default')

    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charactercounter = request.POST.get('charactercounter', 'off')
    if removepunc=="on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

        # analyse the text
        # return render(request, 'analyze.html', params)
    if(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed= analyzed + char.upper()
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)
    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char!="\n" and char!="\r":
                analyzed = analyzed + char

        params = {'purpose': 'New line is removed', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if (extraspaceremover == "on"):
        analyzed = ""
        for index,char in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1]==" ":
                pass
            else:
                analyzed = analyzed + char

        params = {'purpose': 'Extra space is removed', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if (charactercounter == "on"):
        analyzed = 0
        for char in djtext:

                analyzed = analyzed + 1

        params = {'purpose': 'number of character', 'analyzed_text': analyzed}
        djtext = analyzed
        return render(request, 'analyze.html', params)



    return render(request, 'analyze.html', params)


# def capfirst(request):
#     #get the text.
#
#     return HttpResponse("Capitalize")
# def newlineremove(request):
#     return HttpResponse("new line remove")
# def spacecount(request):
#     return HttpResponse("space count")
# def charcount(request):
#     return HttpResponse("char count")