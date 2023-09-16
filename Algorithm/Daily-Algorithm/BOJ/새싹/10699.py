'''
https://www.acmicpc.net/problem/10699
'''

import datetime


KST = datetime.timezone(datetime.timedelta(hours=9))
print(datetime.datetime.now(KST).strftime('%Y-%m-%d'))
