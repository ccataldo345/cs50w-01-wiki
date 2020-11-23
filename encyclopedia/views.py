from django.shortcuts import render, redirect
from . import util
import markdown2
import random
from django import forms


class PageForm(forms.Form):
    title = forms.CharField(max_length=32, widget=forms.Textarea(
        attrs={'class': 'textarea', 'id': 'title', 'required': True}))
    content = forms.CharField(max_length=1024, widget=forms.Textarea(
        attrs={'class': 'textarea', 'id': 'content'}))


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def title(request, title):
    find_title = util.get_entry(title)
    if not find_title:
        return render(request, "encyclopedia/wiki/error.html", {
            "title": title,
            "error_message": "Your requested page was not found."
        })
    return render(request, "encyclopedia/wiki/title.html", {
        "title": title,
        "content": markdown2.markdown(find_title)
    })


def rnd_title(request):
    rnd_title = random.choice(util.list_entries())
    return render(request, "encyclopedia/wiki/title.html", {
        "title": rnd_title,
        "content": markdown2.markdown(util.get_entry(rnd_title))
    })


def search(request):
    query = request.GET.get('q').capitalize()
    entries = util.list_entries()
    substring = [i for i in entries if query in i]
    if query in entries:
        return redirect(f"wiki/{query}")
    elif substring:
        return render(request, "encyclopedia/search.html", {
            "query": query,
            "entries": substring
        })
    else:
        return render(request, "encyclopedia/wiki/error.html", {
            "title": query,
            "error_message": "Your requested page was not found."
        })


def new(request):
    if request.method == "POST":
        title = request.POST.get('title').capitalize()
        content = request.POST.get('content')
        if title not in util.list_entries():
            util.save_entry(title, content)
            return redirect(f"wiki/{title}")
        else:
            return render(request, "encyclopedia/wiki/error.html", {
                "title": title,
                "error_message": "This page already exists!"
            })
    return render(request, "encyclopedia/new.html", {
        "form": PageForm()
    })


def edit(request):
    title = request.GET.get('q')
    find_title = util.get_entry(title)
    content = markdown2.markdown(find_title)
    if request.method == "POST":
        content = request.POST.get('content')
        util.save_entry(title, content)
        return redirect(f"wiki/{title}")
    return render(request, "encyclopedia/edit.html", {
        "title": title,
        "form": PageForm(initial={'content': content})
    })
