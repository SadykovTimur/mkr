from coms.qa.frontend.pages.component import Component, ComponentWrapper

__all__ = ['TreePanel']


class TreePanelWrapper(ComponentWrapper):
    state_program = Component(xpath="//span[text()='Программы и подпрограммы']")


class TreePanel(Component):
    def __get__(self, instance, owner) -> TreePanelWrapper:
        return TreePanelWrapper(instance.app, self.find(instance), self._locator)
