import allure
from _pytest.fixtures import FixtureRequest
from coms.qa.fixtures.application import Application
from coms.qa.frontend.helpers.attach_helper import screenshot_attach
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.analytic_support_page import AnalyticSupportPage
from dit.qa.pages.analytics_page import AnalyticsPage
from dit.qa.pages.analytics_reports_page import AnalyticReportsPage
from dit.qa.pages.availability_ehd_page import AvailabilityEhdPage
from dit.qa.pages.availability_new_page import AvailabilityNewPage
from dit.qa.pages.availability_sber_page import AvailabilitySberPage
from dit.qa.pages.availability_support_page import AvailabilitySupportPage
from dit.qa.pages.main_page import MainPage
from dit.qa.pages.sber_object_page import SberObjectPage
from dit.qa.pages.sbor_availability_page import SborAvailabilityPage
from dit.qa.pages.start_page import StartPage
from dit.qa.pages.state_program_analytic_page import StateProgramAnalyticPage
from dit.qa.pages.state_program_availability_page import StateProgramAvailabilityPage
from dit.qa.pages.state_program_report_page import StateProgramReportPage

__all__ = [
    'open_start_page',
    'open_auth_form',
    'sign_in',
    'open_start_page',
    'open_analytics_page',
    'open_analytics_reports_page',
    'show_analytics_report',
    'open_availability_hand_new',
    'open_main_page',
    'open_problem_details',
    'open_state_program_analytic_report',
    'open_analytic_support',
    'open_availability_support',
    'show_analytic_report',
    'open_availability_ehd',
    'open_availability_sber',
    'open_reports_ehd',
    'open_sber_objects_section',
    'show_sber_objects',
    'open_sbor_availability',
    'open_state_program_analytic',
    'open_state_program_availability',
    'show_state_program_analytic',
]


def open_start_page(app: Application) -> None:
    with allure.step('Opening Start page'):
        try:
            page = StartPage(app)
            page.open()
            page.wait_for_loading_header()
            page.wait_for_loading()

            screenshot_attach(app, 'start_page')
        except Exception as e:
            screenshot_attach(app, 'start_page_error')

            raise TimeoutError('Start page was not loaded') from e


def open_auth_form(app: Application) -> None:
    with allure.step('Opening Auth form'):
        try:
            page = StartPage(app)
            page.header.login.click()
            page.auth_form.wait_for_loading()

            screenshot_attach(app, 'auth_form')
        except Exception as e:
            screenshot_attach(app, 'auth_form_error')

            raise TimeoutError('Auth form was not loaded') from e


def open_analytics_page(app: Application) -> None:
    with allure.step('Opening analytics page'):
        try:
            MainPage(app).open_page("Аналитика по группам расходов")

            page = AnalyticsPage(app)
            page.wait_for_loading_header()
            page.wait_for_loading()

            screenshot_attach(app, 'analytics_page')
        except Exception as e:
            screenshot_attach(app, 'analytics_page_error')

            raise TimeoutError('Analytics page was not loaded') from e


def open_analytics_reports_page(app: Application) -> None:
    with allure.step('Opening analytics reports'):
        try:
            AnalyticsPage(app).open_analytics_reports_page()
            AnalyticReportsPage(app).wait_for_loading()

            screenshot_attach(app, 'analytics_reports')
        except Exception as e:
            screenshot_attach(app, 'analytics_reports_error')

            raise TimeoutError('Analytics reports was not loaded') from e


def show_analytics_report(app: Application) -> None:
    with allure.step('Show analytics report'):
        try:
            page = AnalyticReportsPage(app)
            page.settings_panel.show_btn.click()
            page.wait_for_loading_report()

            screenshot_attach(app, 'analytics_report')
        except Exception as e:
            screenshot_attach(app, 'analytics_report_error')

            raise TimeoutError('Analytics report was not loaded') from e


def open_availability_hand_new(app: Application) -> None:
    with allure.step('Opening Availability hand new'):
        try:
            MainPage(app).open_page("АРМ Руководителя")
            AvailabilityNewPage(app).wait_for_loading()

            screenshot_attach(app, 'availability_hand_new')
        except Exception as e:
            screenshot_attach(app, 'availability_hand_new_error')

            raise TimeoutError('Availability hand new was not loaded') from e


def open_problem_details(app: Application) -> None:
    with allure.step('Opening problem details detail'):
        try:
            page = AvailabilityNewPage(app)
            problem = page.problems[0]
            name = problem.name
            problem.problem_value.click()
            page.problem_details.wait_for_loading(name)

            screenshot_attach(app, 'problem_details')
        except Exception as e:
            screenshot_attach(app, 'problem_details_error')

            raise TimeoutError('Problem details was not loaded') from e


def open_availability_sber(app: Application) -> None:
    with allure.step('Opening Availability sber'):
        try:
            MainPage(app).open_page("Сбор и актуализация данных по мероприятиям развития")
            page_sber = AvailabilitySberPage(app)
            page_sber.wait_for_loading_header()
            page_sber.wait_for_loading()

            screenshot_attach(app, 'availability_sber')
        except Exception as e:
            screenshot_attach(app, 'availability_sber_error')

            raise TimeoutError('Availability sber was not loaded') from e


def open_sbor_availability(app: Application) -> None:
    with allure.step('Opening Sbor availability'):
        try:
            MainPage(app).open_page("Сбор и актуализация данных  по мероприятиям развития 2011-2013")
            page_sbor = SborAvailabilityPage(app)
            page_sbor.wait_for_loading()

            screenshot_attach(app, 'sbor_availability')
        except Exception as e:
            screenshot_attach(app, 'sbor_availability_error')

            raise TimeoutError('Sbor availability was not loaded') from e


def open_state_program_availability(app: Application) -> None:
    with allure.step('Opening state program availability'):
        try:
            MainPage(app).open_page("Мониторинг и контроль реализации государственных программ")
            page_availability = StateProgramAvailabilityPage(app)
            page_availability.wait_for_loading_header()
            page_availability.wait_for_loading()

            screenshot_attach(app, 'state program')
        except Exception as e:
            screenshot_attach(app, 'state_program_availability_error')

            raise TimeoutError('state program availability was not loaded') from e


def open_state_program_analytic(app: Application) -> None:
    with allure.step('Opening State program analytic'):
        try:
            StateProgramAvailabilityPage(app).open_state_program()
            StateProgramAnalyticPage(app).wait_for_loading()

            screenshot_attach(app, 'state program analytic')
        except Exception as e:
            screenshot_attach(app, 'state_program_analytic_error')

            raise TimeoutError('State program analytic was not loaded') from e


def show_state_program_analytic(app: Application) -> None:
    with allure.step('Show state program analytic'):
        try:
            page = StateProgramAnalyticPage(app)
            page.settings_panel.period_btn.click()
            page.data_btn.click()
            page.wait_for_loading_state_program_table()

            page.settings_panel.show_btn.click()
            page.wait_for_loading_state_table()

            screenshot_attach(app, 'state program analytic')
        except Exception as e:
            screenshot_attach(app, 'state_program_analytic_error')

            raise TimeoutError('Show state program analytic was not loaded') from e


def open_state_program_analytic_report(app: Application) -> None:
    with allure.step('Opening State program analytic report'):
        try:
            StateProgramAvailabilityPage(app).header.items_data.click()
            StateProgramReportPage(app).wait_for_loading()

            screenshot_attach(app, 'state program analytic report')
        except Exception as e:
            screenshot_attach(app, 'state_program_analytic_report_error')

            raise TimeoutError('State program analytic report was not loaded') from e


def open_availability_ehd(app: Application, request: FixtureRequest) -> None:
    with allure.step('Opening Availability ehd'):
        if request.config.option.block_urls:
            app.send_command('Network.setBlockedURLs', {'urls': ['fonts.googleapis.com']})
            app.send_command('Network.enable', {})

        try:
            MainPage(app).open_page("Единое хранилище данных социально-экономических показателей (ЕХД)")
            page_open_ehd = AvailabilityEhdPage(app)
            page_open_ehd.wait_for_loading()

            screenshot_attach(app, 'availability_ehd')
        except Exception as e:
            screenshot_attach(app, 'availability_ehd_error')

            raise TimeoutError('Availability ehd was not loaded') from e


def open_reports_ehd(app: Application) -> None:
    with allure.step('Opening Reports ehd'):
        try:
            page_ehd = AvailabilityEhdPage(app)
            page_ehd.menu.submenu.click()
            page_ehd.wait_for_loading_submenu()

            page_ehd.menu.source_sum.click()
            page_ehd.wait_for_loading_report()

            screenshot_attach(app, 'reports_ehd')
        except Exception as e:
            screenshot_attach(app, 'reports_ehd_error')

            raise TimeoutError('Reports ehd was not loaded') from e


def open_availability_support(app: Application) -> None:
    with allure.step('Opening Availability support'):
        try:
            MainPage(app).open_page("Мониторинг реализации мер социальной поддержки")
            page_support = AvailabilitySupportPage(app)
            page_support.wait_for_loading_header()
            page_support.wait_for_loading()

            screenshot_attach(app, 'availability_support')
        except Exception as e:
            screenshot_attach(app, 'availability_support_error')

            raise TimeoutError('Availability support was not loaded') from e


def open_analytic_support(app: Application) -> None:
    with allure.step('Opening Analytic support'):
        try:
            AvailabilitySupportPage(app).open_analytic()
            AnalyticSupportPage(app).wait_for_loading()

            screenshot_attach(app, 'analytic_support')
        except Exception as e:
            screenshot_attach(app, 'analytic_support_error')

            raise TimeoutError('Analytic support was not loaded') from e


def show_analytic_report(app: Application) -> None:
    with allure.step('Show analytic report'):
        try:
            page = AnalyticSupportPage(app)
            page.settings_panel.apply_btn.click()
            page.wait_for_loading_social_report()

            screenshot_attach(app, 'analytic_report')
        except Exception as e:
            screenshot_attach(app, 'analytic_report_error')

            raise TimeoutError('Analytic report was not loaded') from e


def open_sber_objects_section(app: Application) -> None:
    with allure.step('Opening Sber objects section'):
        try:
            AvailabilitySberPage(app).header.arm_object.click()
            SberObjectPage(app).wait_for_loading()

            screenshot_attach(app, 'sber_objects_section')
        except Exception as e:
            screenshot_attach(app, 'sber_objects_section_error')

            raise TimeoutError('Sber objects section was not loaded') from e


def show_sber_objects(app: Application) -> None:
    with allure.step('Opening Sber objects'):
        try:
            page_sber = SberObjectPage(app)
            page_sber.settings_panel.apply_btn.click()
            page_sber.wait_for_loading_object()

            screenshot_attach(app, 'objects')
        except Exception as e:
            screenshot_attach(app, 'objects__error')

            raise TimeoutError('Objects was not loaded') from e


def sign_in(app: Application, login: str, password: str) -> None:
    with allure.step(f'{login} signing in'):
        try:
            auth_form = StartPage(app).auth_form

            auth_form.login.send_keys(login)
            auth_form.password.send_keys(password)

            screenshot_attach(app, 'auth_data')
        except Exception as e:
            screenshot_attach(app, 'auth_data_error')

            raise NoSuchElementException('Entering data exception') from e

        auth_form.submit.click()


def open_main_page(app: Application) -> None:
    with allure.step('Opening Main page'):
        try:
            MainPage(app).wait_for_loading()

            screenshot_attach(app, 'main_page')
        except Exception as e:
            screenshot_attach(app, 'main_page_error')

            raise TimeoutError('Main page was not loaded') from e
