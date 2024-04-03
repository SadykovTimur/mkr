from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component
from coms.qa.frontend.pages.component.text import Text
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.analytics_page.components.header import Header
from dit.qa.pages.analytics_reports_page.components.settings_panel import SettingsPanel

__all__ = ['AnalyticReportsPage']


class AnalyticReportsPage(Page):
    header = Header(id="main-menu")
    breadcrumbs = Text(id="breadcrumbs-menu")
    settings_panel = SettingsPanel(id="c_settingsPanel")
    structure_panel = Component(id="c_structurePanel")
    rep_panel = Component(id="c_repPanel")
    table_report = Component(class_name='grid-table-wrap')
    general_result = Component(xpath="//th[text()='Общий итог'] ")
    total = Component(xpath="//th[text()='Итого']")
    loader = Component(id="nprogress")

    @property
    def is_loader_hide(self) -> bool:
        try:
            return not self.loader.visible
        except NoSuchElementException:
            return True

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.header.logo.visible
                assert self.header.title == 'ИАС МКР'
                assert self.header.items_analytics.visible
                assert self.header.items_gbrs.visible
                assert self.header.items_data.visible
                assert self.header.items_news.visible
                assert self.header.items_control.visible
                assert self.header.name == 'Вершинин А. Ю.'
                assert self.header.login == 'FTest'

                assert self.settings_panel.visible
                assert self.structure_panel.visible
                assert 'Контрольный отчет' in self.breadcrumbs
                assert 'Аналитика' in self.breadcrumbs

                return self.rep_panel.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()

    def wait_for_loading_report(self) -> None:
        def condition() -> bool:
            try:
                assert self.is_loader_hide
                assert self.general_result.visible
                assert self.table_report.visible

                return self.total.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Report was not loaded')
        self.app.restore_implicitly_wait()
