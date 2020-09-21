import time
import os
import unittest
from appium import webdriver
import logging
from appium.common.exceptions import NoSuchContextException

# 写入数据的函数进行封装
class Auto_execise(unittest.TestCase):
    def device(self):
        d = {
            "deviceName": "CN42195G00019",
            "platformName": "Android",
            "platformVersion": "5.0",
            "appPackage": "com.himirror.mirrorxsmax",
            "appActivity": "com.himirror.mirrorxsmax.CustomerHome.HomeActivity",
            "unicodeKeyboard": True,  # 使用unicode编码方式发送字符串
            "resetKeyboard": True,  # 屏蔽软键盘
            # "automationName": "UiAutomator1" # 设备版本比较低的情况下  需要加上
        }
        self.dr = webdriver.Remote("http://localhost:4723/wd/hub", d)  # 开启appium 启动设备
        return self.dr

    def wirte_value(self, way, element, value):
        error_message = ""
        try:
            if way == "id":
                self.dr.find_element_by_id(element).send_keys(value)
            if way == "xpath":
                self.dr.find_element_by_xpath(element).send_keys(value)
        except NoSuchContextException as e:
            logging.error("找不到这个元素%s" % e)
            error_message = str(e)
        except Exception as e:
            logging.error("出现错误%s" % e)
            error_message = str(e)
        finally:
            return error_message

        # 断言实际字符串相等的函数封装

    def Assert_Equal(self, way, element, expect_value):
        result = {"status": "", "error_message": ""}
        try:
            if way == "id":
                self.assertEqual(self.dr.find_element_by_id(element).text, expect_value)
            result["status"] = "PASS"
            if way == "xpath":
                self.assertEqual(self.dr.find_element_by_xpath("element").text, expect_value)
                result["status"] = "PASS"
        except NoSuchContextException as e:
            logging.error("没有找到这个元素 %s" % e)
            result["status"] = "unfind"
            result["error_message"] = str(e)
        except AssertionError as e:
            logging.error("断言错误 %s" % e)
            result["status"] = "Assert_error"
            result["error_message"] = str(e)
        except Exception as e:
            logging.error("出现其他的错误 %s" % e)
            result["status"] = "fail"
            result["error_message"] = str(e)
        finally:
            return result

        #  断言字符串是否包含于的函数封装

    def Assert_Notequal(self, way, element, expect_value):
        result = {"status": "", "error_message": ""}
        try:
            if way == "id":
                self.assertIn(expect_value, self.dr.find_element_by_id(element).text)
            result["status"] = "PASS"
            if way == "xpath":
                self.assertEqual(expect_value, self.dr.find_element_by_xpath("element").text)
                result["status"] = "PASS"

        except NoSuchContextException as e:
            logging.error("没有找到这个元素 %s" % e)
            result["status"] = "unfind"
            result["error_message"] = str(e)
        except AssertionError as e:
            logging.error("断言错误 %s" % e)
            result["status"] = "Assert_error"
            result["error_message"] = str(e)
        except Exception as e:
            logging.error("出现其他的错误 %s" % e)
            result["status"] = "fail"
            result["error_message"] = str(e)
        finally:
            return result
