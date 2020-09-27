from django.urls import path
from . import views
from .views import (
    PostListView
)


urlpatterns = [
	path('', PostListView.as_view(), name='home'),
	path('search/',views.search,name='search' ),
    #path('show/',views.showFac,name='showFac')
]
