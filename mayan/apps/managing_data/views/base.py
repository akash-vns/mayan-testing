from mayan.apps.views.generics import FormView
from ..forms import SampleFormClass


class SampleFormView(FormView):
    form_class = SampleFormClass
