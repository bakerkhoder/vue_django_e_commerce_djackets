from django.urls import path, include
from product import views

urlpatterns = [
    path('Latest-products/', views.LatestProductsList.as_view()),
    # path('whishlist-products/', views.FavoriteProductsList.as_view()),
    path('products/search/', views.search),
    path('products/<slug:category_slug>/<slug:product_slug>/',
         views.ProductDetail.as_view()),
    path('products/<slug:category_slug>/', views.CategoryDetail.as_view()),
    path('signup/', views.signup),
    path('prof/', views.login),
    path('updateprof/', views.updateprof)
]
