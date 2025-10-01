from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from project import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")),
    path("__reload__/", include("django_browser_reload.urls")),
    path("", views.index, name="index"),
]

urlpatterns += [
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("site-admin/", views.siteadmin, name="site-admin"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
