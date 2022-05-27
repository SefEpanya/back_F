from django.shortcuts import render
# Views for fifi app


def fileFinder(request):
    """
    Handle files uploads
    Args:
        request (POST): New file upload
    """
    return render(request, "index.html")


def registration(request):
    return render(request, "register-page.html")


def upload(request):
    title = request.POST['title']
    item = request.POST['item']
    context = {"title": title, "item": item}
    return render(request, "landing-page.html", context)


def userPage(request):
    return render(request, "profile-page.html")
    