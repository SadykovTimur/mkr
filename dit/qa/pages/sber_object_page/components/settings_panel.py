from coms.qa.frontend.pages.component import Component, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button

__all__ = ['SettingsPanel']


class SettingsPanelWrapper(ComponentWrapper):
    filter_options = Component(xpath="//span[text()='Параметры и фильтры']")
    apply_btn = Button(xpath='//div[text()="Применить"]')


class SettingsPanel(Component):
    def __get__(self, instance, owner) -> SettingsPanelWrapper:
        return SettingsPanelWrapper(instance.app, self.find(instance), self._locator)
