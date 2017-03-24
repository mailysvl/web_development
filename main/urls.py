from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^basket/', views.basket, name='basket'),
    url(r'^product/', views.product, name='product'),
    url(r'^search/', views.search, name='search'),
    url(r'^login/', views.login, name='login'),
    url(r'^register/', views.register, name='register'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^add_basket/', views.add_to_basket, name='add_basket'),
    url(r'^update_basket/', views.update_basket, name='update_basket'),
    url(r'^remove/', views.remove, name='remove'),

]
