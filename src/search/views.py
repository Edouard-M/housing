from django.shortcuts import render


def search(request):

    context = {
        "title": "Search App",
    }

    return render(request, "search/index.html", context=context)
