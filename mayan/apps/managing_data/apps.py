from mayan.apps.common.apps import MayanAppConfig
from django.utils.translation import ugettext_lazy as _


class ManagingDataApp(MayanAppConfig):
    app_namespace = 'managing_data'
    app_url = 'managing_data'
    has_tests = True
    name = 'mayan.apps.managing_data'
    verbose_name = _('Managing data')

    def ready(self):
        super().ready()
