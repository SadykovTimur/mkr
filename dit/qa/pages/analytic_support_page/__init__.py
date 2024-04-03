from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component
from coms.qa.frontend.pages.component.button import Button
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.analytic_support_page.components.panel_report import PanelReport
from dit.qa.pages.analytic_support_page.components.settings_panel import SettingsPanel

__all__ = ['AnalyticSupportPage']


class AnalyticSupportPage(Page):
    settings_panel = SettingsPanel(id="c_settingsPanel")
    menu_analytic = Component(xpath="//a[text()='Аналитика']")
    analytics = Button(id="sub_main_menu")
    panel_control = Component(id="c_poksPanel")
    panel_text = Component(xpath="//span[text()='Показатели']")
    panel_report = PanelReport(id="c_repPanel")
    title = Component(css='[title="Отчет по мерам социальной поддержки "]')
    grid_container = Component(id="gridOutput")

    def open_analytic(self) -> None:
        self.app.move_to_element(self.menu_analytic.webelement)
        self.analytics.click()

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.panel_control.visible
                assert self.panel_text.visible
                assert self.settings_panel.visible

                return self.settings_panel.title.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()

    def wait_for_loading_social_report(self) -> None:
        def condition() -> bool:
            try:
                assert self.panel_report.visible
                assert self.title.visible
                assert self.panel_report.body_content.visible
                assert self.grid_container.visible

                return self.settings_panel.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=60, msg='Page was not loaded')
        self.app.restore_implicitly_wait()
