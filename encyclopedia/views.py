from django.shortcuts import render
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

# def random(request, random):
	# return render(request, "encyclopedia/random.html", {
		# "random": util.get_entry(random)
	# })

def error():
	return None

def new():
	return None
	
def edit():
	return None

def random():
	return None
