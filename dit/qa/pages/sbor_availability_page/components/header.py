from coms.qa.frontend.pages.component import Component, ComponentWrapper

__all__ = ['Header']


class HeaderWrapper(ComponentWrapper):
    logo = Component(id="h-logo")
    user_name = Component(id="userName")
    user_menu = Component(id="userMenu")
    registry_menu = Component(xpath='//a[text()="Реестры"]')
    import_menu = Component(xpath='//a[text()="Импорт"]')
    report_menu = Component(xpath='//a[text()="Отчёты"]')


class Header(Component):
    def __get__(self, instance, owner) -> HeaderWrapper:
        return HeaderWrapper(instance.app, self.find(instance), self._locator)
