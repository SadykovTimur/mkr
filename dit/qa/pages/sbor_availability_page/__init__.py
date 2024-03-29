from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component
from coms.qa.frontend.pages.component.button import Button
from selenium.common.exceptions import NoSuchElementException

__all__ = ['SborAvailabilityPage']


class SborAvailabilityPage(Page):
    data_sbor = Button(css='[href="/data2"]')
    news = Component(xpath="//h1[text()='Новости']")
    warning_text = Component(xpath="//div[contains(text(),'По запросу новостей не найдено.')]")
    search = Component(class_name="search")

    def open_data_sbor(self):
        self.data_sbor.wait_for_clickability()
        self.data_sbor.click()

    def wait_for_loading(self) -> None:

        def condition() -> bool:
            try:
                assert self.news.visible
                assert self.warning_text.visible

                return self.search.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()

