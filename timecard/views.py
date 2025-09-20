from django.shortcuts import render

def timecard(request):
    return render(
        request,
        'punch.html'
    )
