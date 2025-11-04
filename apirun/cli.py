# -*- coding: utf-8 -*-
# @Author : Hami
import os
from core.CasesPlugin import CasesPlugin
# 框架运行的入口

import pytest


# TODO : 1. 最基础的应用，自己找符合规则的测试用例
# pytest.main(["-vs"])

# TODO: 2-1 . 生成测试报告-allure
pytest_args = ["-s", "-v", "--capture=sys",  # 用于显示输出调试信息、 设置级别、打开实时输出
               "./core/ApiTestRunner.py",  # 指定运行文件
               "--clean-alluredir",  # 清空alluredir中的历史数据
               "--alluredir=allure-results",  # 执行过程的数据存放到allure-results中
               "--type=excel",  # 指定文件运行类型
               "--cases=.\examples\examples-dsw",  # 指定运行的路径
               "--reruns=2",  # 重新运行次数
               "--reruns-delay=3"  # 等待运行秒数
               ]

print("run pytest：", pytest_args)
# pytest.main(pytest_args)
pytest.main(pytest_args, plugins=[CasesPlugin()])

# TODO: 2-2 . 基于数据生成测试报告-allure-html
# allure generate -c -o 报告生成的路径
os.system("allure generate -c -o allure-report")

# TODO: 2-3.代码参考如下：生成allure测试报告，双击打开直接查看
# 注意 ： allure报告必须以服务的形式打开，你直接进入到目录是无法打开（没有数据）
from allure_combine import combine_allure

# # combine_allure(测试报告的路径)
combine_allure("./allure-report")
