from django.urls import path

from . import views

app_name = 'ecomockapp'
urlpatterns = [
    path('', views.index, name='index'),
    # path('', views.IndexView.as_view(), name='index'),
    path('plugin', views.plugin, name='plugin'),
]

# Ends here.
