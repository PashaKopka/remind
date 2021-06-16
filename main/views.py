from django.shortcuts import render
from django.views.generic.base import View


class HomePageView(View):

    def get(self, request):
        return render(request, 'main/homepage.html')
