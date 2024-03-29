from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component
from coms.qa.frontend.pages.component.button import Button
from selenium.common.exceptions import NoSuchElementException

__all__ = ['ReportsPage']


class ReportsPage(Page):
    analytic_report = Component(css='[data-id="133"]')
    control_report = Button(xpath="//a[text()='Контрольный отчет']")
    report_control = Component(xpath="//div[text()='Контрольный отчет']")
    show_btn = Button(css='[id="btn_apply"]')
    table_report = Component(class_name='grid-table-wrap ')
    general_result = Component(xpath="//th[text()='Общий итог'] ")
    total = Component(xpath="//th[text()='Итого']")

    def analytics_reports_page(self) -> None:
        self.app.move_to_element(self.analytic_report.webelement)
        self.control_report.click()
        self.show_btn.click()

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.general_result.visible
                assert self.total.visible

                return self.report_control.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()