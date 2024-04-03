from coms.qa.frontend.pages.component import Component, Components, ComponentWrapper

__all__ = ['TreePanel']


class TreePanelWrapper(ComponentWrapper):
    state_program = Component(xpath="//span[text()='Государственные программы']")
    items = Components(css="[id*='lid_gp']")


class TreePanel(Component):
    def __get__(self, instance, owner) -> TreePanelWrapper:
        return TreePanelWrapper(instance.app, self.find(instance), self._locator)
