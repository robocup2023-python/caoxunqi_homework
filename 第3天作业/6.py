def is_leap_year(year):
    # 判断是否为闰年
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def day_of_year(year, month, day):
    # 每月的天数
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # 如果是闰年，二月天数加1
    if is_leap_year(year):
        days_in_month[2] = 29

    # 计算天数
    total_days = sum(days_in_month[:month]) + day

    return total_days

# 输入年、月、日
year = int(input("请输入年份："))
month = int(input("请输入月份："))
day = int(input("请输入日期："))

day_number = day_of_year(year, month, day)
print(f"{year}年{month}月{day}日是{year}年的第{day_number}天。")