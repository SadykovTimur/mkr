from typing import List

from coms.qa.frontend.pages.component import Components, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button

__all__ = ['ProblemCards']


class ProblemCardWrapper(ComponentWrapper):
    problem_value = Button(css='[data-id="problem_value"]')


class ProblemCards(Components):
    def __get__(self, instance, owner) -> List[ProblemCardWrapper]:
        ret: List[ProblemCardWrapper] = []

        for webelement in self.finds(instance):
            ret.append(ProblemCardWrapper(instance.app, webelement, self._locator))

        return ret
