from django.conf.urls import include, url
from django.contrib import admin
from beeApp import views
from bee import urls_tag, urls_badge, urls_comment

urlpatterns = [
    # Examples:
    # url(r'^$', 'bee.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^tag/', include(urls_tag)),
    url(r'^badge/', include(urls_badge)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^comment/', include(urls_comment)),
]
