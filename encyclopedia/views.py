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
            "error_message": "Your requested page was not found."
        })
    return render(request, "encyclopedia/wiki/title.html", {
        "title": markdown2.markdown(find_title)
    })


def search(request):
    query = request.GET.get('q').capitalize()
    if query in util.list_entries():
        return redirect(f"wiki/{query}")


def new():
    return None


def edit():
    return None


def random():
    return None


'''# def random(request, random):
# return render(request, "encyclopedia/random.html", {
    # "random": util.get_entry(random)
# })'''
