from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.components.header import Header
from dit.qa.pages.start_page.components.auth_form import AuthForm
from dit.qa.pages.start_page.components.menu import Menu

__all__ = ['StartPage']


class StartPage(Page):
    header = Header(id="ui-app")
    footer = Component(css='[class="the-footer"]')
    news_filter = Component(class_name='news-filter')
    news = Component(xpath="//span[text()='Новости']")
    calendar = Component(xpath="//span[text()='Календарь событий']")
    auth_form = AuthForm(css='[class="ui-modal__wrapper"]')

    def wait_for_loading(self, is_authorize: bool = False) -> None:
        def condition() -> bool:
            try:
                if is_authorize:
                    assert self.header.profile_name.visible

                assert self.header.login.visible
                assert self.header.logo.visible
                assert self.news_filter.visible
                assert self.news.visible
                assert self.calendar.visible

                return self.footer.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()
