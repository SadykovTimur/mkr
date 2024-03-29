from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component
from coms.qa.frontend.pages.component.button import Button
from selenium.common.exceptions import NoSuchElementException

__all__ = ['AnalyticSupportPage']


class AnalyticSupportPage(Page):
    menu_analytic = Component(css='[href="index.php?show=rep_01"]')
    analytics = Button(id="sub_main_menu")
    panel_control = Component(xpath="//span[text()='Показатели']")
    panel_header = Component(xpath="//span[text()='Параметры и фильтры']")
    apply_btn = Button(id="btn_apply")
    panel_report = Component(id="c_repPanel")
    title = Component(css='[title="Отчет по мерам социальной поддержки "]')
    grid_container = Component(id="gridOutput")
    body_content = Component(class_name="grid-body-content")

    def open_analytic(self) -> None:
        self.app.move_to_element(self.menu_analytic.webelement)
        self.analytics.click()

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.panel_control.visible

                return self.panel_header.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()

    def open_social_report(self) -> None:
        self.apply_btn.click()

    def wait_for_loading_social_report(self) -> None:
        def condition() -> bool:
            try:
                assert self.panel_report.visible
                assert self.title.visible
                assert self.body_content.visible
                assert self.grid_container.visible

                return self.panel_header.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=60, msg='Page was not loaded')
        self.app.restore_implicitly_wait()
