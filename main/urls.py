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
