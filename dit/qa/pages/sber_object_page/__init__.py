from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component.text import Text
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.availability_sber_page.components.header import Header
from dit.qa.pages.sber_object_page.components.object_panel import ObjectPanel
from dit.qa.pages.sber_object_page.components.settings_panel import SettingsPanel

__all__ = ['SberObjectPage']


class SberObjectPage(Page):
    header = Header(class_name="header")
    breadcrumbs = Text(css='[class="ui-breadcrumb"] ')
    settings_panel = SettingsPanel(css='[class*="ui-panel--allocated"]')
    object_panel = ObjectPanel(css='[class="ui-panel object-list ui-panel--collapse"]')

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.object_panel.object_list.visible

                return self.settings_panel.filter_options.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()

    def wait_for_loading_object(self) -> None:
        def condition() -> bool:
            try:
                assert self.object_panel.id_object.visible
                assert self.object_panel.category_object.visible
                assert self.object_panel.address_object.visible

                return self.object_panel.archive_object.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()
