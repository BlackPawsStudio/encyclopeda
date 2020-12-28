import re
from django.shortcuts import render
from django.shortcuts import redirect
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage


def list_entries():
    """
    Returns a list of all names of encyclopedia entries.
    """
    _, filenames = default_storage.listdir("entries")
    return list(sorted(re.sub(r"\.md$", "", filename)
                for filename in filenames if filename.endswith(".md")))


def save_entry(title, content):
    """
    Saves an encyclopedia entry, given its title and Markdown
    content. If an existing entry with the same title already exists,
    it is replaced.
    """
    filename = f"entries/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
    default_storage.save(filename, ContentFile(content))

def delete_entry(title):
    filename = f"entries/{title}.md"
    default_storage.delete(filename)

def get_entry(title):
    """
    Retrieves an encyclopedia entry by its title. If no such
    entry exists, the function returns None.
    """
    try:
        f = default_storage.open(f"entries/{title}.md")
        return f.read().decode("utf-8")
    except FileNotFoundError:
        return None

def pagesearch(request):
    data = dict(request.POST)
    page = data["page"]
    strin = page[0] #string from searchbar
    entries = list_entries() #list of all intries
    i = 0
    li=[]
    check = False
    while i < len(entries):
        if strin.title() == entries[i]:
            stri = "/page/"+strin.title()
            return 0,stri
        elif strin.title() in entries[i]:
            li.append(entries[i])
            check = True
        elif i == (len(entries)-1) and bool(check):
            data = {"list":li, "search":strin} 
            return 1,data
        elif i == (len(entries)-1) and not bool(sheck):
            return 2,2
        i = i + 1
