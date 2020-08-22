from django.shortcuts import render , get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView
                                  )
from .models import ads
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import authentication_classes, permission_classes

def home(request):
    context = {
        'all_ads' : ads.objects.all()
    }
    return render(request, 'Advertisements/home.html', context)

class AdsListView(ListView):
    model = ads
    template_name = 'Advertisements/home.html'
    context_object_name = 'all_ads'
    ordering = ['-start_date']
    paginate_by = 5

class UserAdsListView(ListView):
    model = ads
    template_name = 'Advertisements/user_ads.html'
    context_object_name = 'all_ads'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username') )
        return ads.objects.filter(user=user).order_by('-start_date')

class AdsDetailView(DetailView):
    model = ads

class AdsCreateView(LoginRequiredMixin, CreateView):
    model = ads
    fields = ['title', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AdsCreateView, self).form_valid(form)

class AdsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = ads
    fields = ['title', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AdsUpdateView, self).form_valid(form)

    def test_func(self):
        ad = self.get_object()
        if self.request.user == ad.user:
            return True
        return False

class AdsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = ads
    success_url = '/'
    def test_func(self):
        ad = self.get_object()
        if self.request.user == ad.user:
            return True
        return False


def about (request):
    return render(request, 'Advertisements/about.html', {'title' : 'About'})

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def searchByCity(request):
	city = request.GET.get('city')
	ad = ads.objects.filter(city=city).first()
	return Response({"title": ad.title})
	
#	return Response({"title": ad.title, "score": ad.score})