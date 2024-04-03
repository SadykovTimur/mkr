from coms.qa.frontend.pages.component import Component, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button

__all__ = ['SubMain']


class SubMainWrapper(ComponentWrapper):
    control_report = Button(xpath="//a[text()='Контрольный отчет']")


class SubMain(Component):
    def __get__(self, instance, owner) -> SubMainWrapper:
        return SubMainWrapper(instance.app, self.find(instance), self._locator)
