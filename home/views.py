from django.shortcuts import render

# Create your views here.
from django.views import View


class HomeView(View):
    """Homepage"""

    def get(self, request):
        return render(request, 'home/home.html')