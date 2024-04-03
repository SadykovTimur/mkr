from coms.qa.frontend.pages.component import Component, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button

__all__ = ['SettingsPanelWrapper']


class SettingsPanelWrapper(ComponentWrapper):
    filter_options = Component(xpath="//span[text()='Параметры и фильтры']")
    apply_btn = Button(xpath='(//button[@class="ui-button ui-button--color-primary ui-button--size-md"])[1]')


class SettingsPanel(Component):
    def __get__(self, instance, owner) -> SettingsPanelWrapper:
        return SettingsPanelWrapper(instance.app, self.find(instance), self._locator)
