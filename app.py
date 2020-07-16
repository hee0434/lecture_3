import func_module

# func_module.module_show()

nowdate = func_module.date_now()


now_year = nowdate.year
now_month=nowdate.month
now_day = nowdate.day

date_today = '{}년 {}월 {}일'.format(nowdate.year , nowdate.month ,nowdate.day)

#print(nowdate)
print(date_today)

x_mas = nowdate.replace(month=12, day=25)

date_xmas = '{}년 {}월 {}일'.format(nowdate.year , nowdate.month ,nowdate.day)
