from coms.qa.frontend.pages.component import Component, ComponentWrapper
from coms.qa.frontend.pages.component.text import Text

__all__ = ['Header']


class HeaderWrapper(ComponentWrapper):
    items_news = Component(xpath="//a[text()='Новости'] ")
    items_data = Component(xpath="//a[text()='Данные'] ")
    items_control = Component(xpath="//a[text()='Управление']")
    items_analytics = Component(xpath="//a[text()='Аналитика']")
    items_gbrs = Component(xpath="//a[text()='ГРБС'] ")
    title = Text(id="h-logo")
    logo = Component(class_name="mkr-logo-ico")
    name = Text(class_name="name")
    login = Text(class_name="login")


class Header(Component):
    def __get__(self, instance, owner) -> HeaderWrapper:
        return HeaderWrapper(instance.app, self.find(instance), self._locator)
