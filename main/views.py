# main/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import UrlData
from .forms import UrlForm

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