import pandas as pd
import numpy as np

from datetime import datetime


def read_fight_data(month):
    print('读取航班数据')
    fight_data = pd.read_csv('input/train/fights-%s.csv' % month)
    print('共%s条数据' % len(fight_data))
    return fight_data


def find_pre_fight(data):
    min_timestamp = data['PDepartureTime'].min()
    max_timestamp = data['PDepartureTime'].max()
    print(datetime.fromtimestamp(min_timestamp).strftime('%Y-%m-%d %H:%M:%S'))
    print(datetime.fromtimestamp(max_timestamp).strftime('%Y-%m-%d %H:%M:%S'))


fight_data = read_fight_data('2017-05')
print(fight_data.info())

# 找出前序航班是否延误(最多4个前序航班)
find_pre_fight(fight_data)
