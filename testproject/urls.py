from django.conf.urls import url, include


urlpatterns = (
    url(r'^auth/', include('djoser.urls.authtoken')),
    url(r'^auth/', include('djoser.urls.base')),
)
