from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from . import util
import markdown2


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
        "title": markdown2.markdown(find_title)
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
    return render(request, "encyclopedia/new.html", {
        "title": request.GET.get('title')
    })


def edit():
    return None


def random():
    return None


'''# def random(request, random):
# return render(request, "encyclopedia/random.html", {
    # "random": util.get_entry(random)
# })'''
