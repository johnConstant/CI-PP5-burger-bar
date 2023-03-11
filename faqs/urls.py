from django.urls import path
from . import views

urlpatterns = [
    path('', views.FAQList.as_view(), name='faqs'),
    path(
         'add/', views.FaqAdd.as_view(), name='add_faq'
    ),
    path('edit/<int:id>', views.FaqUpdate.as_view(),
         name='edit_faq'),
    path(
        'delete/<int:id>',
        views.FaqDelete.as_view(),
        name='delete_faq'
        ),
]
