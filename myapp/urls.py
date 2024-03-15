from django.urls import path

import myapp.views as myapp_views

urlpatterns = [
    path("", myapp_views.product_list, name="product_list"),
    path("<int:product_id>/", myapp_views.get_product_by_id, name="product_details")
]
