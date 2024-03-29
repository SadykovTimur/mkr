from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component
from coms.qa.frontend.pages.component.button import Button
from selenium.common.exceptions import NoSuchElementException

__all__ = ['AvailabilityNewPage']


class AvailabilityNewPage(Page):
    arm_lead = Button(xpath="//span[contains(text(),'АРМ Руководителя')]")
    arm_text = Component(xpath="//span[text()='ИАС МКР | АРМ РУКОВОДИТЕЛЯ'] ")
    profile = Component(xpath="//div[text()='Александр Юрьевич Вершинин']")
    filter = Component(class_name='ui-page-sidebar-content__control')
    container = Component(class_name='tile-container ')
    page_tabs = Component(css="[class='ui-page-tabs-header'] ")

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.arm_text.visible
                assert self.profile.visible
                assert self.filter.visible
                assert self.page_tabs.visible

                return self.container.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()
