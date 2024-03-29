from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component
from coms.qa.frontend.pages.component.button import Button
from selenium.common.exceptions import NoSuchElementException

__all__ = ['AvailabilitySupportPage']


class AvailabilitySupportPage(Page):
    social_monitoring = Button(xpath="//span[contains(text(),'Мониторинг реализации мер социальной поддержки')]")
    filter_calendar = Component(css='[class="news-filter-calendar"]')
    calendar = Component(xpath="//span[text()='Календарь событий']")
    news_line = Component(class_name='news-line')

    def open_menu(self) -> None:
        self.social_monitoring.wait_for_clickability()
        self.social_monitoring.click()

    def wait_for_loading(self) -> None:
        self.driver.switch_to.frame('news-body__frame')

        def condition() -> bool:
            try:
                assert self.filter_calendar.visible
                assert self.calendar.visible

                return self.news_line.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()

    def switch_to_default(self) -> None:
        self.driver.switch_to.default_content()
