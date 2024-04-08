from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages.component import Component, ComponentWrapper
from selenium.common.exceptions import NoSuchElementException
from coms.qa.frontend.pages.component.text import Text

__all__ = ['ProblemDetails']


class ProblemDetailsWrapper(ComponentWrapper):
    title = Text(tag="strong")
    page_footer = Component(class_name="ui-page-footer")
    total_prefecture = Component(xpath="//div[text()='Итого по префектурам'] ")
    department_housing = Component(xpath="//a[text()='ДЖКХ']")
    department_health = Component(xpath="//a[text()='ДепЗдрав']")
    complex = Component(xpath='//div[text()="Комплексы"]')
    gp = Component(xpath='//div[text()="ГП"]')
    grbs = Component(xpath='//div[text()="ГРБС"]')

    def wait_for_loading(self, name: str) -> None:
        def condition() -> bool:
            try:
                assert self.title == name
                assert self.total_prefecture.visible
                assert self.department_health.visible
                assert self.department_housing.visible
                assert self.complex.visible
                assert self.gp.visible
                assert self.grbs.visible

                return self.page_footer.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()


class ProblemDetails(Component):
    def __get__(self, instance, owner) -> ProblemDetailsWrapper:
        return ProblemDetailsWrapper(instance.app, self.find(instance), self._locator)
