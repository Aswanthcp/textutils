from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    params = {
        'name': 'Aswanth',
        'place': 'mars'
    }

    return render(request, 'index.html', params)


def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {
            'purpose': 'Remove punctuation',
            'analyzed_text': analyzed
        }
        djtext = analyzed

    if fullcaps == 'on':
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {
            'purpose': 'Uppercase',
            'analyzed_text': analyzed
        }
        djtext = analyzed

    if newlineremover == 'on':
        analyzed = ""
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed = analyzed + char
        params = {
            'purpose': 'Remove Newline',
            'analyzed_text': analyzed
        }
        djtext = analyzed

    if extraspaceremover == 'on':
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params = {
            'purpose': 'Remove Extra space',
            'analyzed_text': analyzed
        }
        djtext = analyzed

    if charcount == 'on':
        count = 0
        for index in enumerate(djtext):
            count = count + 1
        params = {
            'purpose': 'Count of letters',
            'analyzed_text': count,
        }

    if charcount != "on" and extraspaceremover != "on" and newlineremover != "on" and fullcaps != "on" and removepunc != "on":
        return HttpResponse("Please select operation!")

    return render(request, 'analyze.html', params)
