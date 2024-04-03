from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.sbor_availability_page.components.header import Header

__all__ = ['SborAvailabilityPage']


class SborAvailabilityPage(Page):
    header = Header(id="h-content")
    news = Component(xpath="//h1[text()='Новости']")
    warning_text = Component(css="[class='empty-report']")
    search = Component(class_name="search")

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.header.logo.visible
                assert self.header.user_name.visible
                assert self.header.user_menu.visible
                assert self.header.registry_menu.visible
                assert self.header.import_menu.visible
                assert self.header.report_menu.visible

                assert self.news.visible
                assert self.warning_text.visible

                return self.search.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()
