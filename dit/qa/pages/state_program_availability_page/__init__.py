from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component, Components
from coms.qa.frontend.pages.component.button import Button
from coms.qa.frontend.pages.component.text import Text
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.state_program_availability_page.components.header import Header

__all__ = ['StateProgramAvailabilityPage']


class StateProgramAvailabilityPage(Page):
    header = Header(id="main-menu")
    news_filter = Component(class_name="news-filter")
    news = Components(class_name='news-line-item ')
    breadcrumbs = Text(id="breadcrumbs-menu")
    iframe = Component(tag='iframe')
    footer = Component(class_name="the-footer")
    state_program_btn = Button(xpath='//a[text()="	Актуализация государственных программ"]')

    def open_state_program(self) -> None:
        self.app.move_to_element(self.header.items_analytica.webelement)
        self.state_program_btn.click()

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
                assert self.header.items_news.visible
                assert self.header.items_data.visible
                assert self.header.items_analytica.visible
                assert self.header.items_service.visible
                assert self.header.title == 'ИАС МКР'
                assert self.header.logo.visible
                assert self.header.name == 'Вершинин А. Ю.'
                assert self.header.login == 'FTest'
                assert "Госпрограммы" in self.breadcrumbs

                return "Новости" in self.breadcrumbs

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()
