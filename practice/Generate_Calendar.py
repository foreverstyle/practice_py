# -*- coding: utf-8 -*-
# Author: style_forever
# Date: 14
# Description:生成日历 ,计算该月天数，并打印日历

import calendar

year = int(input("请输入年份："))
month = int(input("请输入月份："))

# 获取该月天数
num_days = calendar.monthrange(year, month)[1]

print("该月共有{}天".format(num_days))

# 打印日历
cal = calendar.month(year, month)

print(cal)