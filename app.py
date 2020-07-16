import func_module
import func_module_as

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

print(date_xmas)

ndate = func_module_as.date_now()

print(ndate)

func_module_as.remain_date_input()

re_date = func_module_as.remain_date_input()

print(re_date)