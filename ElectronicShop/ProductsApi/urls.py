from django.urls import path
from .views import ElectProducts, ElectProductsUpdate

urlpatterns = [
    path('electronic-items/', ElectProducts.as_view(), name='view'),
    path('electronic-items/<int:item_id>', ElectProductsUpdate.as_view(), name='update'),
]
