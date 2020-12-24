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
    return render(request, "encyclopedia/layout.html", context=data)

def search(request, title):
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
    return render(request, "encyclopedia/temp.html", context={"path":path})

def editpage(request,title):
    if request.method == "POST":
        data = dict(request.POST)
        textarea_text = data["txtarea"]
        util.save_entry(title,textarea_text[0])
        return redirect('page', title=title)
    content=util.get_entry(title)
    data = {'title':title, "content":content}
    return render(request, "encyclopedia/editpage.html", context=data)