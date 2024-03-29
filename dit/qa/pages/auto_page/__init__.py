from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component
from coms.qa.frontend.pages.component.button import Button
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.components.header import Header
from dit.qa.pages.start_page.components.auth_form import AuthForm
from dit.qa.pages.start_page.components.menu import Menu

__all__ = ['AutoPage']


class AutoPage(Page):
    header = Header(id="ui-app")
    footer = Component(css='[class="the-footer"]')
    new_systems = Component(xpath="//span[text()='Функциональные подсистемы']")
    menu_news = Component(css='[class="header-menu__news"] ')
    menu_notifications = Component(css='[class="header-menu-item header-menu__notifications"] ')
    systems = Component(class_name='new-systems-systems')
    analytics = Button(css='[href="/analytics"]')
    news_analytics = Component(xpath="//div[text()='Новости']")

    def analytics_page(self) -> None:
        self.analytics.click()
        assert self.news_analytics.visible

    def wait_for_loading(self, is_authorize: bool = False) -> None:
        def condition() -> bool:
            try:
                if is_authorize:
                    assert self.header.profile_name.visible

                assert self.header.logo.visible
                assert self.new_systems.visible
                assert self.menu_news.visible
                assert self.menu_notifications.visible
                assert self.systems.visible

                return self.footer.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()
