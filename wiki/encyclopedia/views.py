from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from . import util
import random
from django.shortcuts import redirect

from markdown2 import markdown


def index(request):
    entries=util.list_entries()
    path=random.choice(entries)
    data={"entries":entries, "path":path}
    if request.method == "POST": 
         if 'submit' in request.POST:
            data = dict(request.POST)
            page = data["page"]
            strin = page[0] #string from searchbar
            entries = util.list_entries() #list of all intries
            i = 0
            li=[]
            check = False
            while i < len(entries):
                if strin.title() == entries[i]:
                    stri = "/page/"+strin.title()
                    return redirect(stri)
                elif strin.title() in entries[i]:
                    li.append(entries[i])
                    check = True
                elif strin.title() not in entries[i] and bool(check):
                    data = {"list":li, "search":strin} 
                    return render(request, "encyclopedia/searchresults.html", context = data)
                i = i + 1
            return HttpResponse("Nothing found")
    return render(request, "encyclopedia/index.html", context=data)

def search(request, title):
    if request.method == "POST": 
        if 'submit' in request.POST:
            data = dict(request.POST)
            page = data["page"]
            strin = page[0] #string from searchbar
            entries = util.list_entries() #list of all intries
            i = 0
            li=[]
            check = False
            while i < len(entries):
                if strin.title() == entries[i]:
                    stri = "/page/"+strin.title()
                    return redirect(stri)
                elif strin.title() in entries[i]:
                    li.append(entries[i])
                    check = True
                elif strin.title() not in entries[i] and bool(check):
                    data = {"list":li, "search":strin} 
                    return render(request, "encyclopedia/searchresults.html", context = data)
                i = i + 1
            return HttpResponse("Nothing found")
    text = markdown(util.get_entry(title))
    path=random.choice(util.list_entries())
    if not text:
        return HttpResponse("Nothing found", status=404)
    else:
        with open("encyclopedia/templates/encyclopedia/temp.html", 'w') as fw:
            with open("encyclopedia/static/encyclopedia/b.html", 'r') as b:
                b_text=b.read()
            text=b_text+'\n'+text
            fw.write(text)
    return render(request, "encyclopedia/temp.html", context={"path":path, "title":title})

def editpage(request,title):
    if 'confirm' in request.POST:
        data = dict(request.POST)
        textarea_text = data["txtarea"]
        util.save_entry(title,textarea_text[0])
        return redirect('page', title=title)
    elif 'submit' in request.POST:
            data = dict(request.POST)
            page = data["page"]
            strin = page[0] #string from searchbar
            entries = util.list_entries() #list of all intries
            i = 0
            li=[]
            check = False
            while i < len(entries):
                if strin.title() == entries[i]:
                    stri = "/page/"+strin.title()
                    return redirect(stri)
                elif strin.title() in entries[i]:
                    li.append(entries[i])
                    check = True
                elif strin.title() not in entries[i] and bool(check):
                    data = {"list":li, "search":strin} 
                    return render(request, "encyclopedia/searchresults.html", context = data)
                i = i + 1
            return HttpResponse("Nothing found")
    rand=random.choice(util.list_entries())
    content=util.get_entry(title)
    data = {'title':title, "content":content, "rand":rand}
    return render(request, "encyclopedia/editpage.html", context=data)

def create(request):
    if request.method == "POST": 
        entries = util.list_entries()
        if 'confirm' in request.POST:
            data = dict(request.POST)
            titletext = data["titlearea"]
            if titletext[0] == "":
                return HttpResponse("Empty entry title")
            elif titletext[0] in entries:
                return HttpResponse("Page already exists")
            else:
                textarea = data["txtarea"]
                pagetitle = titletext[0]
                util.save_entry(pagetitle.title(),textarea[0])
                stri = "/page/"+titletext[0]
                return redirect(stri)
        elif 'submit' in request.POST:
            data = dict(request.POST)
            page = data["page"]
            strin = page[0] #string from searchbar
            entries = util.list_entries() #list of all intries
            i = 0
            li=[]
            check = False
            while i < len(entries):
                if strin.title() == entries[i]:
                    stri = "/page/"+strin.title()
                    return redirect(stri)
                elif strin.title() in entries[i]:
                    li.append(entries[i])
                    check = True
                elif strin.title() not in entries[i] and bool(check):
                    data = {"list":li, "search":strin} 
                    return render(request, "encyclopedia/searchresults.html", context = data)
                i = i + 1
            return HttpResponse("Nothing found")
    rand=random.choice(util.list_entries())
    return render(request, "encyclopedia/newpage.html", context={"rand":rand})

def deletepage(request, title):
    util.delete_entry(title)
    return redirect('/')