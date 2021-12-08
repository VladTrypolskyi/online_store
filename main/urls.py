from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='main'),
    path('support', views.about),
    # path('index', views.index, name='index'),
    path('login_page', views.LoginView.as_view(), name='login_page'),
    path('category/<slug>', views.CategoryView.as_view(), name='category'),
    path('all_products', views.AllProductsView.as_view(), name='all_products'),
    path('log_out', views.logout_user, name='logout'),

]
