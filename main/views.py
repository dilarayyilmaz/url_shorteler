from django.shortcuts import render, redirect, get_object_or_404
from .models import UrlData
from .forms import UrlForm
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import UrlDataSerializer
import random
import string

def url_shortener_view(request):
    form = UrlForm()
    new_url_data = None
    if request.method == 'POST':
        form = UrlForm(request.POST)
        if form.is_valid():
            original_url = form.cleaned_data['url']

            new_url_data, created = UrlData.objects.get_or_create(url=original_url)


            form = UrlForm()

    all_urls = UrlData.objects.order_by('-id')

    context = {
        'form': form,
        'all_urls': all_urls,
        'new_url_data': new_url_data
    }
    return render(request, 'index.html', context)


def redirect_view(request, slug):
    url_data = get_object_or_404(UrlData, slug=slug)
    return redirect(url_data.url)

@api_view(['GET'])
def get_all_urls(request):
    urls = UrlData.objects.all()
    serializer = UrlDataSerializer(urls, many=True)
    return Response(serializer.data)

@api_view(['DELETE', 'GET'])
def delete_url(request, id):
    url_data = get_object_or_404(UrlData, id=id)
    url_data.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'POST'])
def create_short_url(request, original_url=None):
    if request.method == 'POST':
        original_url = request.data.get('original_url')
    elif request.method == 'GET':
        original_url = original_url  # bu satır gerek bile değil aslında

    if not original_url:
        return Response({"error": "Original URL is required."}, status=400)

    slug = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    new_url = UrlData.objects.create(url=original_url, slug=slug)
    serializer = UrlDataSerializer(new_url)
    return Response(serializer.data)








