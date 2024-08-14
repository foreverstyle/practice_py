# -*- coding: utf-8 -*-
# Author: style_forever
# Date: 14
# Description:  获取几天前的时间

import datetime

def get_two_day_delta(__days=2):
    """
    获取几天前的时间
    :param days: 几天前
    :return: 几天前的时间
    """
    today = datetime.date.today()
    delta = datetime.timedelta(days=__days)
    days_ago = today - delta
    return days_ago


if __name__ == '__main__':
    print(get_two_day_delta())
