from coms.qa.frontend.pages.component import Component, ComponentWrapper
from coms.qa.frontend.pages.component.text import Text

__all__ = ['Main']


class MainWrapper(ComponentWrapper):
    editPanel = Component(id="c_editPanel")
    treePanel = Component(id="c_treePanel")
    repPanel = Component(id="c_repPanel")
    program_text = Text(xpath="//span[text()='Программы и подпрограммы']")
    state_program = Text(xpath="//span[text()='Государственные программы']")
    state_program_update = Text(xpath="//span[text()='Актуализация государственных программ']")


class Main(Component):
    def __get__(self, instance, owner) -> MainWrapper:
        return MainWrapper(instance.app, self.find(instance), self._locator)
