from django.urls import path

from .views import ProductView, CategoryView, ItemsSliderView, SubjectsView, MaterialView, SizeView, TagsView


app_name = "products"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('products/', ProductView.as_view()),
    path('categories/', CategoryView.as_view()),
    path('items_slider/', ItemsSliderView.as_view()),
    path('subjects/', SubjectsView.as_view()),
    path('material/', MaterialView.as_view()),
    path('size/', SizeView.as_view()),
    path('tags/', TagsView.as_view()),
]