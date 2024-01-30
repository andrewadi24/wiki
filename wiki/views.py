from django.shortcuts import render
from django.shortcuts import redirect
from encyclopedia import util
import markdown2
def wiki(request, title):
     return render(request, "wiki/index.html", {
          "title" : title,
          "content":  markdown2.markdown(util.get_entry(title))
     })

def edit(request, title):
     if request.method == 'POST':
        content = request.POST['content']
        util.save_entry(title, content)
        response = redirect('/wiki/{}'.format(title))
        return response
     content = util.get_entry(title)
     return render(request, "wiki/edit.html", {
          'title' : title,
          'content' : content
     })


     