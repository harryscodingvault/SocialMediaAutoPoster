from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from .models import Links

# Create your views here.
def scrape(request):
    page = requests.get('https://www.indeed.com/jobs?q=python&l=Phoenix%2C AZ')
    soup = BeautifulSoup(page.text, 'html.parser')

    link_address = []

    for link in soup.find_all(name='a'):
        print(link)
        link_address = link.get('href')
        link_text = link.string

        if not Links.objects.filter(url=link_address).exists():
            Links.objects.create(url=link_address, name=link_text)

    data = Links.objects.all()

    return render(request, 'myapp/result.html', {'data': data})