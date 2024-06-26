from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),  # вывод главной страницы
    path('products/', views.products, name='products'),  # вывод списка всей продукции
    path('product/<int:id_product>', views.product, name='product'),
    # вывод выбранного пользователем продукта по id
    path('clients/', views.clients, name='clients'),  # вывод всех клиентов
    path('orders/', views.orders, name='orders'),  # вывод всех заказов
    path('client_orders/<int:id_client>', views.client_orders, name='client_orders'),
    # все заказы клиента
    path('client_products_sorted/<int:id_client>/<int:days>/', views.client_products_sorted,
         name='client_products_sorted'),
    # вывод всех товаров по клиенту за указанное кол дней
    path('product_form/<int:id_product>/', views.product_form, name='product_form'),
    # форма для изменения выбранного по id продукта + есть возможность загрузки изображения
]