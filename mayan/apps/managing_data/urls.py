from django.conf.urls import url
from .views.base import SampleFormView

urlpatterns = [
    url(
        regex=r'^manage_data/$',
        name='manage_data_sample',
        view=SampleFormView.as_view()
    ),
]
