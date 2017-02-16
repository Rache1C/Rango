"""tango_with_django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from rango import views


urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'about/$', views.about, name='about'),
    url(r'^add_category/$', views.add_category, name='add_category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.show_category, name='show_category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$', views.add_page, name='add_page'),
    url(r'search/$', views.search, name='search'),
    url(r'goto/$', views.track_url, name='goto'),
    url(r'like/$', views_ajax.like_category, name='like_category'),
    url(r'^suggest/$', views_ajax.suggest_category, name='suggest_category'),
    url(r'^add/$', views_ajax.auto_add_page, name='auto_add_page'),
    url(r'^register/$', views.register_profile, name='register'),
    url(r'^profile/(?P<username>[\w\-]+)/$', views.profile, name='profile'),
    url(r'^profiles/$', views.list_profiles, name='list_profiles'),
]

# urlpatterns = [
#     url(r'^$', views.index, name='index'),
# ]
