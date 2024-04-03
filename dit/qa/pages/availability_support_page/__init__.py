from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component, Components
from coms.qa.frontend.pages.component.button import Button
from coms.qa.frontend.pages.component.text import Text
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.availability_support_page.components.header import Header

__all__ = ['AvailabilitySupportPage']


class AvailabilitySupportPage(Page):
    header = Header(id="main-menu")
    breadcrumbs = Text(id="breadcrumbs-menu")
    news_filter = Component(css='[class="news-filter"]')
    news = Components(class_name='news-line-item ')
    iframe = Component(tag='iframe')
    footer = Component(class_name="the-footer")
    analytics = Button(id="sub_main_menu")

    def open_analytic(self) -> None:
        self.app.move_to_element(self.header.items_analytics.webelement)
        self.analytics.click()

    def wait_for_loading(self) -> None:
        self.driver.switch_to.frame(self.iframe.webelement)

        def condition() -> bool:
            try:
                assert self.news_filter.visible
                assert self.footer.visible

                return self.news[0].visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()

        self.driver.switch_to.default_content()

    def wait_for_loading_header(self) -> None:
        def condition() -> bool:
            try:
                assert self.header.logo.visible
                assert self.header.title == 'ИАС МКР'
                assert self.header.items_analytics.visible
                assert self.header.items_reference.visible
                assert self.header.items_data.visible
                assert self.header.items_news.visible
                assert self.header.items_statistics.visible
                assert self.header.name == 'Вершинин А. Ю.'
                assert self.header.login == 'FTest'
                assert "МСП" in self.breadcrumbs

                return 'Новости' in self.breadcrumbs

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()
