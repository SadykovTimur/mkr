from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component
from coms.qa.frontend.pages.component.button import Button
from selenium.common.exceptions import NoSuchElementException

__all__ = ['AvailabilityEhdPage']


class AvailabilityEhdPage(Page):
    ehd_btn = Button(css='[href="https://ehd.moscow/?auth=mkr&token=rVJe0YWhEN9PkG9gFP%2FSxQ%3D%3D"]')
    user_menu = Component(class_name="userMenu")
    container = Component(id="content-container")
    header_menu = Component(class_name="menuHeader")
    main_toolbar = Component(class_name="mainToolbar")
    main_menu = Component(class_name="mainMenu")
    home_link = Component(class_name="homeLink")

    def open_ehd(self) -> None:
        self.ehd_btn.wait_for_clickability()
        self.ehd_btn.click()

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.user_menu.visible
                assert self.container.visible
                assert self.header_menu.visible
                assert self.main_menu.visible
                assert self.main_toolbar.visible

                return self.home_link.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()
