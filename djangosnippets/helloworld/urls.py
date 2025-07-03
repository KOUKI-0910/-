# helloworld/urls.py

from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from helloworld import views
from helloworld.views import snippet_new, snippet_edit, snippet_detail, shop_new
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

urlpatterns = [
    path('new/', views.snippet_new, name='snippet_new'),
    path('<int:snippet_id>/', views.snippet_detail, name='snippet_detail'),
    path('<int:snippet_id>/edit/', views.snippet_edit, name='snippet_edit'),
    path('shop/new/', views.shop_new, name='shop_new'),  # ★ これを追加
    path('login/', LoginView.as_view(redirect_authenticated_user=True,
                                     template_name='snippets/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', CreateView.as_view(template_name='snippets/signup.html',
                                       form_class=UserCreationForm, success_url='/'), name='signup'),
    path('<int:snippet_id>/sighting/new/', views.sighting_new, name='sighting_new'),
    path('sighting/<int:pk>/', views.sighting_detail, name='sighting_detail'),
path('<int:snippet_id>/resolve/', views.toggle_resolved, name='toggle_resolved'),
]
