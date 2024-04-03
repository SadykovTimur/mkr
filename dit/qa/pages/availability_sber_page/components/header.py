from coms.qa.frontend.pages.component import Component, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button
from coms.qa.frontend.pages.component.text import Text

__all__ = ['Header']


class HeaderWrapper(ComponentWrapper):
    logo = Component(css="[class*='logo__image']")
    title = Text(css="[class*='logo__title']")
    arm_data = Component(xpath='//a[text()="Формирование данных"]')
    arm_object = Button(xpath='//a[text()="Объекты"]')
    arm_data_lot = Component(xpath='//a[text()="Передача потребностей в ЕАИСТ"] ')
    name = Text(css="[class*='fio']")
    login = Text(css="[class*='login']")


class Header(Component):
    def __get__(self, instance, owner) -> HeaderWrapper:
        return HeaderWrapper(instance.app, self.find(instance), self._locator)
