from django.shortcuts import render


# Create your views here.
def index(request):
    """
    code-block:: python
    a=y+mx+b
    """
    return render(request, "project/index.html")
