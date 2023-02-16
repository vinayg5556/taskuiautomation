import time
import pytest
from Base.DriverInitiation import Driver


@pytest.fixture(scope="class")
def beforeClass(request):
    driver1 = Driver()
    driver = driver1.getDriverMethod()
    if request.cls is not None:
        request.cls.driver = driver
        driver.implicitly_wait(10)
    yield driver
    time.sleep(5)
    driver.quit()
