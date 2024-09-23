# vpn/views.py
from urllib.parse import urlparse
import requests
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.views import View
from bs4 import BeautifulSoup
from .models import UserSite


class ProxyView(View):
    def get(self, request, site_name, path):
        user_site = get_object_or_404(UserSite, name=site_name)
        target_url = f"{user_site.url}/{path}"

        response = requests.get(target_url)
        
        if "text/html" in response.headers.get("Content-Type", ""):
            soup = BeautifulSoup(response.content, 'html.parser')
            
            for link in soup.find_all('a', href=True):
                href = link['href']
                if href.startswith('/') or self.is_internal_link(href, user_site.url):
                    link['href'] = f"/{site_name}{href}" if href.startswith('/') else f"/{site_name}/{href[len(user_site.url):]}"

            return HttpResponse(str(soup), content_type="text/html")
        
        return HttpResponse(response.content, content_type=response.headers.get("Content-Type"))
    
    def is_internal_link(self, url, base_url):
        parsed_url = urlparse(url)
        return parsed_url.netloc == '' or parsed_url.netloc == urlparse(base_url).netloc
