from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component
from coms.qa.frontend.pages.component.text import Text
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.analytic_support_page.components.panel_report import PanelReport
from dit.qa.pages.analytic_support_page.components.settings_panel import SettingsPanel
from dit.qa.pages.availability_support_page.components.header import Header

__all__ = ['AnalyticSupportPage']


class AnalyticSupportPage(Page):
    header = Header(id="main-menu")
    breadcrumbs = Text(id="breadcrumbs-menu")
    settings_panel = SettingsPanel(id="c_settingsPanel")
    panel_control = Component(id="c_poksPanel")
    panel_text = Component(xpath="//span[text()='Показатели']")
    panel_report = PanelReport(id="c_repPanel")
    grid_container = Component(id="gridOutput")

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.header.logo.visible
                assert self.header.title == 'ИАС МКР'
                assert self.header.items_analytics.visible
                assert self.header.items_reference.visible
                assert self.header.items_data.visible
                assert self.header.items_news.visible
                assert self.header.items_statistics.visible
                assert self.header.name == 'Вершинин А. Ю.'
                assert self.header.login == 'FTest'

                assert self.panel_control.visible
                assert self.panel_text.visible
                assert self.settings_panel.visible
                assert self.settings_panel.title.visible
                assert "МСП" in self.breadcrumbs

                return 'Аналитика' in self.breadcrumbs

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()

    def wait_for_loading_social_report(self) -> None:
        def condition() -> bool:
            try:
                assert self.panel_report.visible
                assert self.panel_report.title.visible
                assert self.panel_report.body_content.visible
                assert self.grid_container.visible

                return self.settings_panel.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=60, msg='Report was not loaded')
        self.app.restore_implicitly_wait()
