import allure
import pytest


class Test02:
    # 最严重BLOCKER
    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    def test001(self):
        print("test001被执行")

    # 紧要的 critical
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    # @allure.severity(allure.severity_level.TRIVIAL)
    def test002(self):
        print("test002被执行")

    # 次要 minor
    @pytest.allure.severity(pytest.allure.severity_level.MINOR)
    def test003(self):
        print("test003被执行")