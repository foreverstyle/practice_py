# -*- coding: utf-8 -*-
# Author: style_forever
# Date: 14
# Description: 获取昨天日期

import datetime

def get_yesterday():
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)
    return yesterday.strftime('%Y-%m-%d')

if __name__ == '__main__':
    print(get_yesterday())