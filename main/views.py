from django.views.generic import View
from django.shortcuts import HttpResponseRedirect, render, redirect, get_object_or_404
# Create your views here.
from .models import Category, Product, Basket, ProductBasket, Wishlist
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout


class LoginView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('main')
        form = AuthenticationForm()
        return render(request, 'main/login.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main')
        return redirect('login_page')


class RegisterView(View):
    def get(self, request, *args, **kwargs):
        # if request.user.is_authenticated:
        #     return redirect('main')
        form = UserCreationForm()
        return render(request, 'main/register.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main')
        return render(request, 'main/register.html', context={'form': form})


def logout_user(request):
    logout(request)
    return redirect('main')


class AllProductsView(View):
    def get(self, request, *args, **kwargs):
        category = Category()
        category.categoryname = 'All'
        products = Product.objects.all()
        categorys = Category.objects.all()
        return render(request,
                      'category.html',
                      context={'products': products,
                               'categorys': categorys,
                               'category': category})


class CategoryView(View):
    def get(self, request, slug, *args, **kwargs):
        category = Category.objects.get(slug=slug)
        categorys = Category.objects.all()
        # products_categories = ProductCategory.objects.get(categoryid=category.id)
        products = Product.objects.filter(category=category)
        return render(request, 'category.html',
                      context={'products': products, 'slug': slug, 'categorys': categorys, 'category': category})


class ProductView(View):
    def get(self, request, slug, *args, **kwargs):
        products = Product.objects.get(slug=slug)
        return render(request, 'product_detail.html', context={'product': products})


def index(request):
    categorys = Category.objects.all()
    return render(request, 'main/index.html', context={"categorys": categorys})


def about(request):
    return render(request, 'main/about.html')


def base(request):
    categorys = Category.objects.all()
    return render(request, 'main/base.html', context={"categorys": categorys})
