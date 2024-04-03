from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component, Components
from coms.qa.frontend.pages.component.text import Text
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.availability_sber_page.components.header import Header

__all__ = ['AvailabilitySberPage']


class AvailabilitySberPage(Page):
    header = Header(class_name="header")
    breadcrumbs = Text(class_name='ui-breadcrumb')
    news_filter = Component(class_name="news-filter")
    news = Components(class_name='news-line-item ')
    iframe = Component(tag='iframe')

    def wait_for_loading(self) -> None:
        self.driver.switch_to.frame(self.iframe.webelement)

        def condition() -> bool:
            try:
                assert self.news_filter.visible

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
                assert self.header.arm_data.visible
                assert self.header.arm_object.visible
                assert self.header.arm_data_lot.visible
                assert self.header.name == 'Вершинин А. Ю.'

                return self.header.login == 'FTest'

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Header was not loaded')
        self.app.restore_implicitly_wait()
