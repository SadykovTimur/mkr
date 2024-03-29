from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages.component import Component, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button
from coms.qa.frontend.pages.component.text_field import TextField
from selenium.common.exceptions import NoSuchElementException

__all__ = ['AuthForm']


class AuthFormWrapper(ComponentWrapper):
    title = Component(xpath="//div[contains(text(),'Вход в систему')]")
    login = TextField(css='[placeholder="Логин" ]')
    password = TextField(css='[placeholder="Пароль" ]')
    forgot_password = Component(xpath="//a[text()='Забыли пароль?']")
    submit = Button(css='button.ui-button.login-modal__login-button ')

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.title.visible
                assert self.login.visible
                assert self.password.visible
                assert self.forgot_password.visible

                return self.submit.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()


class AuthForm(Component):
    def __get__(self, instance, owner) -> AuthFormWrapper:
        return AuthFormWrapper(instance.app, self.find(instance), self._locator)
