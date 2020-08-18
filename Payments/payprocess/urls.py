from django.urls import path,re_path,include
from payprocess import views

app_name = 'payprocess'

urlpatterns=[
    path('ppayment',views.ProcesPayment, name = 'ppayment'),
]
