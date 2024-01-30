from django.shortcuts import render
from django.shortcuts import redirect
from django import forms
from . import util
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def random_template(request):
    title = util.random()
    response = redirect('/wiki/{}'.format(title))
    return response

def search(request):
    try:
        search_item = request.POST['name']
    except:
        return redirect("/")
    if search_item == "":
        return redirect("/")
    all_entries = util.list_entries()
    valid_entries = []
    for entry in all_entries:
        if entry.lower() == search_item.lower():
            response = redirect('/wiki/{}'.format(entry))
            return response
        if search_item.lower() in entry.lower():
            valid_entries.append(entry)
    
    print(all_entries)
    return render(request, "encyclopedia/index.html", {
        "entries": valid_entries
    })

def create(request):
    if request.method == 'GET':
        return render(request, "encyclopedia/create.html", {
            'error_message': ""
        })
    if request.method == 'POST':
        entry = request.POST['title']
        if entry == "":
            return render(request, "encyclopedia/create.html", {
            'error_message': "title cannot be empty"
        })
        entries = util.list_entries()
        for e in entries:
            if e.lower() == entry.lower():
                return render(request, "encyclopedia/create.html", {
             'error_message': "title already exist in the wiki"
        })
        content = request.POST['content']
        util.save_entry(entry, content)
        response = redirect('/wiki/{}'.format(entry))
        return response