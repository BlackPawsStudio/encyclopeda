from django.shortcuts import render
from . import util
import random

from markdown2 import markdown


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def title(request, file):
    with open(f"entries/{file}.md") as f:
         md_text = f.read()
         with open("encyclopedia/templates/encyclopedia/temp.html", 'w') as fw:
            st=(markdown(md_text))
            with open("encyclopedia/static/encyclopedia/b.html", 'r') as b:
                b_text=b.read()
            st=b_text+'\n'+st
            fw.write(st)
            print(st)
    return render(request, "encyclopedia/temp.html") 

def rand(request):
    entr = util.list_entries()
    p = random.choice(entr)    
    with open(f"entries/{p}.md") as f:
         md_text = f.read()
         with open("encyclopedia/templates/encyclopedia/temp.html", 'w') as fw:
            st=(markdown(md_text))
            with open("encyclopedia/static/encyclopedia/b.html", 'r') as b:
                b_text=b.read()
            st=b_text+st
            fw.write(st)
    return render(request, "encyclopedia/temp.html") 