from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component, Components
from coms.qa.frontend.pages.component.text import Text
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.analytics_page.components.header import Header
from dit.qa.pages.analytics_page.components.sub_main import SubMain

__all__ = ['AnalyticsPage']


class AnalyticsPage(Page):
    header = Header(id="main-menu")
    footer = Component(class_name="the-footer")
    breadcrumbs = Text(id="breadcrumbs-menu")
    menu_news = Component(class_name="news-filter")
    iframe = Component(tag="iframe")
    sub_main = SubMain(id="sub_main_menu")
    news = Components(class_name='news-line-item')

    def open_analytics_reports_page(self) -> None:
        self.app.move_to_element(self.header.items_analytics.webelement)
        self.sub_main.control_report.click()

    def wait_for_loading(self) -> None:
        self.driver.switch_to.frame(self.iframe.webelement)

        def condition() -> bool:
            try:
                assert self.menu_news.visible
                assert self.news[0].visible

                return self.footer.visible

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
                assert self.header.items_gbrs.visible
                assert self.header.items_data.visible
                assert self.header.items_news.visible
                assert self.header.items_control.visible
                assert self.header.name == 'Вершинин А. Ю.'
                assert self.header.login == 'FTest'

                return 'Аналитика' in self.breadcrumbs

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()
