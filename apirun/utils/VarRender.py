# -*- coding: utf-8 -*-
# @Author : Hami

# 变量渲染
# 字符串模板进行参数渲染
# 使用 jinja2 模板引擎 (类似 flask的模板)
# https://docs.jinkan.org/docs/jinja2/templates.html

from jinja2 import Template


def refresh(target, context):
    """
    把你初始数据中需要渲染的数据变成context当中的值
    :param target: 你的初始数据，用 {{变量名}} -- 请求数据
    :param context: 你的初始数据渲染的值 -- 全局变量
    :return:
    """
    if target is None: return None
    return Template(str(target)).render(context)


# 测试方法
def t_Refresh():
    target = "hello {{name}}, {{niasd}},{{token}}"
    context = {"name": "张三", "token": "3242343242343432432"}
    res = refresh(target, context)
    print(res)


t_Refresh()
