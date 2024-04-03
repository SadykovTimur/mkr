from coms.qa.frontend.pages.component import Component, ComponentWrapper
from coms.qa.frontend.pages.component.text import Text

__all__ = ['Header']


class HeaderWrapper(ComponentWrapper):
    items_news = Component(xpath="//a[text()='Новости'] ")
    items_data = Component(xpath="//a[text()='Сбор отчетности'] ")
    items_analytica = Component(xpath="//a[text()='Аналитика'] ")
    items_service = Component(xpath="//a[text()='Служебный функционал']")
    title = Text(id="h-logo")
    logo = Component(class_name="mkr-logo-ico")
    name = Text(css='[class="name"]')
    login = Text(css='[class="login"]')


class Header(Component):
    def __get__(self, instance, owner) -> HeaderWrapper:
        return HeaderWrapper(instance.app, self.find(instance), self._locator)
