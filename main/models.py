from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Customer(models.Model):
    userid = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)
    name = models.CharField(max_length=20, verbose_name='Name')
    address = models.CharField(max_length=20, verbose_name='Address')
    address2 = models.CharField(max_length=20, verbose_name='Address 2')

    def __str__(self):
        return self.name


class Category(models.Model):
    categoryname = models.CharField(max_length=300, verbose_name='Category')
    description = models.CharField(max_length=300, verbose_name='Description', blank=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.categoryname


class Product(models.Model):
    name = models.CharField(max_length=300, verbose_name='Name')
    description = models.CharField(max_length=300, verbose_name='Description', blank=True)
    picture = models.ImageField(verbose_name='Picture', blank=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Price')
    slug = models.SlugField(unique=True)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.name


# class ProductCategory(models.Model):
#     productid = models.ForeignKey(Product, verbose_name='Product', on_delete=models.CASCADE)
#     categoryid = models.ForeignKey(Category, verbose_name='Category', on_delete=models.CASCADE)
#
#     def __str__(self):
#         return f'{self.productid.name}, {self.categoryid.categoryname}'


class Basket(models.Model):
    customer = models.ForeignKey(Customer, verbose_name='Customer', on_delete=models.CASCADE)
    totalprice = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Total Price')
    product = models.ManyToManyField('ProductBasket', verbose_name='Product', related_name='related_basket', blank=True,
                                     )

    def __str__(self):
        return str(self.id)


class ProductBasket(models.Model):
    product = models.ForeignKey(Product, verbose_name='Product', on_delete=models.CASCADE)
    basket = models.ForeignKey(Basket, verbose_name='Basket', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f'{self.product.name}, {self.basket.id}'


class Order(models.Model):
    customer = models.ForeignKey(Customer, verbose_name='Customer', on_delete=models.CASCADE)
    totalprice = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Total Price')
    product = models.ManyToManyField(ProductBasket, verbose_name='Product', related_name='related_order')
    comment = models.TextField(verbose_name='Comment', blank=True)

    def __str__(self):
        return self.customer.userid.username


class Wishlist(models.Model):
    customer = models.ForeignKey(Customer, verbose_name='Customer', on_delete=models.CASCADE)
    product = models.ManyToManyField('ProductWishlist', verbose_name='Product', related_name='related_wishlist',
                                     blank=True)

    def __str__(self):
        return self.customer.userid.username


class ProductWishlist(models.Model):
    Product = models.ForeignKey(Product, verbose_name='Product ID',
                                on_delete=models.CASCADE)
    Wishlist = models.ForeignKey(Wishlist, verbose_name='Wish list ID',
                                 on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.Product.name}, {self.Wishlist.__str__()}'
