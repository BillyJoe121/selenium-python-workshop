from behave import given, when, then
from selenium import webdriver
from pages.login_fbpage import loginPage
from pages.dashboard_page import DashBoardPage

@given('the user is on the moodle page')
def step_given_user_on_login_page(context):
    context.driver = webdriver.Chrome()  # o webdriver.Firefox()
    context.driver.get("https://www.icesi.edu.co/moodle/login/index.php")
    context.login_page = loginPage(context.driver)

@when('the user logs in with valid data')
def step_when_user_logs_in_valid(context):
    context.login_page.login("micedula", "micontraseña")

@then('the user should be redirected to the dashboard')
def step_then_dashboard_page(context):
    dashboardPage = DashBoardPage(context.driver)
    assert dashboardPage.isTopBar()
