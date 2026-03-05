import os
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.service import Service as EdgeService

# @pytest.fixture(scope="class")
# def setup():
#     print("i will be executing first")
#     yield
#     print("i will be executing last")
#
# @pytest.fixture(scope="class")
# def dataLoad():
#     print("user data profile is created")
#     return ["Vinodh", "Gorla", "rahulshettyacademy.com"]
# @pytest.fixture(params=[("Chrome","Vino"), ("Firefox","Vinu"), ("IE","Sai")])

# def crossBrowser(request):
#     return request.param

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome", help="browser name")

@pytest.fixture(scope="function")
def browserInitiation(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        service_obj = Service()
        driver = webdriver.Chrome(service = service_obj)
    elif browser_name == "firefox":
        service_obj = FirefoxService("C:\\Users\\gvinodh\\Downloads\\geckodriver-v0.36.0-win64\\geckodriver.exe")
        #service_obj = FirefoxService()
        driver = webdriver.Firefox(service = service_obj)
    elif browser_name == "edge":
        service_obj = EdgeService()
        driver = webdriver.Edge(service=service_obj)
    driver.implicitly_wait(5)
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    yield driver
    driver.close()

@pytest.hookimpl( hookwrapper=True )
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin( 'html' )
    outcome = yield
    report = outcome.get_result()
    extra = getattr( report, 'extra', [] )

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr( report, 'wasxfail' )
        if (report.skipped and xfail) or (report.failed and not xfail):
            reports_dir = os.path.join( os.path.dirname( __file__ ), 'reports' )
            file_name = os.path.join( reports_dir, report.nodeid.replace( "::", "_" ) + ".png" )
            print( "file name is " + file_name )
            _capture_screenshot( file_name )
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append( pytest_html.extras.html( html ) )
        report.extras = extra


def _capture_screenshot(file_name):
    driver.get_screenshot_as_file(file_name)
#def _capture_screenshot(file_name):
    #driver.get_full_page_screenshot_as_file(file_name)