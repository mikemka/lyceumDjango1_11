from django.conf.urls import url
from django.contrib import admin

from homepage.views import home
from catalog.views import item_list, item_detail
from about.views import description
from users.views import user_list, user_detail, signup, profile


urlpatterns = [
    url(r'^auth/users/(?P<user_id>\d+)/$', user_detail),
    url('auth/users/', user_list),
    url('auth/signup/', signup),
    url('auth/profile/', profile),

    url('about', description),

    url(r'^catalog/(?P<prod_id>\d+)/$', item_detail),
    url('catalog/', item_list),

    url('', home),
]
