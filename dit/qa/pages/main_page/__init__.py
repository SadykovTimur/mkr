from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.constants import WEB_DRIVER_WAIT
from coms.qa.frontend.helpers.custom_wait_conditions import ElementToBeClickable
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component, Components
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from dit.qa.pages.main_page.components.header import Header

__all__ = ['MainPage']


class MainPage(Page):
    header = Header(css="[class*='toolbar']")
    footer = Component(class_name="the-footer")
    title = Component(xpath="//span[text()='Функциональные подсистемы']")
    items = Components(class_name='ag-courses_item')

    def open_page(self, name: str) -> None:
        wait = WebDriverWait(self.driver, WEB_DRIVER_WAIT)
        el = self.driver.find_element(By.XPATH, f'//div[text()="{name}"]')
        wait.until(ElementToBeClickable(element=el))
        el.click()

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.header.is_visible

                assert self.title.visible
                assert self.items[0].visible

                return self.footer.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()
