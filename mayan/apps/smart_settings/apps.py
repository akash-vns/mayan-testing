from django.utils.translation import ugettext_lazy as _

from mayan.apps.common.apps import MayanAppConfig
from mayan.apps.common.menus import (
    menu_list_facet, menu_object, menu_return, menu_setup
)
from mayan.apps.navigation.classes import SourceColumn
from mayan.apps.views.column_widgets import TwoStateWidget

from .classes import SettingNamespace, Setting
from .column_widgets import WidgetSettingValue
from .links import (
    link_setting_namespace_detail, link_setting_namespace_list,
    link_namespace_root_list, link_setting_edit
)
from .widgets import setting_widget


class SmartSettingsApp(MayanAppConfig):
    app_namespace = 'settings'
    app_url = 'settings'
    has_tests = True
    name = 'mayan.apps.smart_settings'
    verbose_name = _('Smart settings')

    def ready(self):
        super().ready()

        SettingNamespace.load_modules()

        SourceColumn(
            func=lambda context: len(context['object'].settings),
            label=_('Setting count'), include_label=True,
            source=SettingNamespace
        )
        SourceColumn(
            func=lambda context: setting_widget(context['object']),
            label=_('Name'), is_identifier=True, source=Setting
        )
        SourceColumn(
            attribute='serialized_value', include_label=True,
            label=_('Value'), widget=WidgetSettingValue, source=Setting
        )
        SourceColumn(
            attribute='is_overridden', include_label=True, source=Setting,
            widget=TwoStateWidget
        )

        menu_list_facet.bind_links(
            links=(link_setting_namespace_detail,),
            sources=(SettingNamespace,)
        )
        menu_object.bind_links(
            links=(link_setting_edit,), sources=(Setting,)
        )
        menu_return.bind_links(
            links=(link_namespace_root_list,), sources=(
                SettingNamespace, Setting,
                'settings:setting_namespace_list'
            )
        )
        menu_setup.bind_links(
            links=(link_setting_namespace_list,)
        )

        Setting.save_last_known_good()
