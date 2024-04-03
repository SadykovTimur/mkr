from coms.qa.frontend.pages.component import Component, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button

__all__ = ['SettingsPanelWrapper']


class SettingsPanelWrapper(ComponentWrapper):
    show_btn = Button(id="btn_apply")


class SettingsPanel(Component):
    def __get__(self, instance, owner) -> SettingsPanelWrapper:
        return SettingsPanelWrapper(instance.app, self.find(instance), self._locator)
