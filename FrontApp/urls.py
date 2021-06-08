from django.urls import path
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import include, path
from django.views.generic.base import RedirectView
from django.conf import settings

from . import views

urlpatterns = [

    path('',views.home, name = 'home'),
    path("favicon.jpg",RedirectView.as_view(url=staticfiles_storage.url("favicon.jpg")), ),
    path('next',views.next, name = 'next'),
    path('style.css',RedirectView.as_view(url=staticfiles_storage.url("style.css")), ),
    path('do.jpg',RedirectView.as_view(url=staticfiles_storage.url("do.jpg")), ),
    path('file.png',RedirectView.as_view(url=staticfiles_storage.url("file.png")), ),
    path('import.png',RedirectView.as_view(url=staticfiles_storage.url("import.png")), ),
    path("upload.html",RedirectView.as_view(url=staticfiles_storage.url("upload.html")), ),
    path("download.html",RedirectView.as_view(url=staticfiles_storage.url("download.html")), ),
    path('360.jpg',RedirectView.as_view(url=staticfiles_storage.url("360.jpg")), ),
    

]

