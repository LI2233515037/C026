import allure


class Test01:
    @allure.step(title="我测试方法1")
    def test001(self):
        allure.attach("描述：","失败原因")
        print("test001被执行")

    @allure.step(title="我测试方法2")
    def test002(self):
        allure.attach("失败原因：", "断言错误！")
        print("test002被执行")
