# I have created this file - Sanket
from django.http import HttpResponse
from django.shortcuts import render

# Code for Personal Navigator
# def index(request):
#    return HttpResponse ('<h1>Welcome to our personal Navigator</h1><a href="https://www.codewithharry.com/">Code with Harry Official</a><br><a href="https://www.youtube.com/">Youtube</a>')
# def about(request):
#     return HttpResponse("About Sanket")

# Code for Pipeline
def index(request):
    return render(request,'index.html')

def analyze(request):
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','Off')
    fullcaps = request.POST.get('fullcaps','Off')
    charcount = request.POST.get('charcount','Off')
    firstcap = request.POST.get('firstcap','Off')
    spaceremover = request.POST.get('spaceremover','Off')
    newlineremover = request.POST.get('newlineremover','Off')


    if removepunc == "on":
        punctutations = '''!()-[]{};:'"\,<>./?@#$%^&*_~''' 
        analyzed = ""
        for char in djtext:
            if char not in punctutations:
                analyzed = analyzed + char
        djtext = analyzed
        params = {'purpose':'Removed Punctutation', 'analyzed_text':analyzed}
        
    if fullcaps == "on":
        analyzed = djtext.upper()
        djtext = analyzed
        params = {'purpose':' Changed to Uppercase', 'analyzed_text':analyzed}
       

    if firstcap == "on":
        analyzed = djtext.capitalize()
        djtext = analyzed
        params = {'purpose':' Changed to Capitalized', 'analyzed_text':analyzed}
       


    if spaceremover == "on":
        analyzed = " "
        for char in range(len(djtext)):
            if djtext[char] == " " and djtext[char+1] == " ":
                pass
            else:
                analyzed = analyzed + djtext[char]
        djtext = analyzed
        params = {'purpose':' Changed to Capitalized', 'analyzed_text':analyzed}
        

    if charcount == "on":
        analyzed = len(djtext)
        params = {'purpose':' Count Character', 'analyzed_text':analyzed}
        
    
    if newlineremover == "on":
        analyzed = " "
        for i in djtext:
            if i != "\n" and i!="\r":
                analyzed = analyzed +i
        djtext = analyzed
        params = {'purpose':' Changed to Capitalized', 'analyzed_text':analyzed}
       
    if (removepunc != "on",fullcaps != "on",spaceremover != "on",firstcap != "on",charcount != "on",newlineremover != "on"):
        return (HttpResponse("Please Select atleast one Operation"))
        
    return render(request,'analyze.html',params)





# def capfirst(request):
#     return HttpResponse("Capitilise first <a href='/'> back </a>")  

# def newlineremove(request):
#     return HttpResponse("newlineremove <a href='/'> back </a>")

# def spaceremover(request):
#     return HttpResponse("Space Remover <a href='/'> back </a>")

# def charcount(request):
#     return HttpResponse("Character Count <a href='/'> back </a>")

