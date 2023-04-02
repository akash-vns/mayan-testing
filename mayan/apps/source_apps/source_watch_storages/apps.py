from django.utils.translation import ugettext_lazy as _

from mayan.apps.common.apps import MayanAppConfig


class SourceWatchStoragesApp(MayanAppConfig):
    app_namespace = 'source_watch_storages'
    app_url = 'source_watch_storages'
    has_rest_api = False
    has_static_media = False
    has_tests = True
    name = 'mayan.apps.source_apps.source_watch_storages'
    verbose_name = _('Watch folders')
