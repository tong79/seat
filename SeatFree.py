# coding: utf-8
import pandas as pd
import datetime
import time


class Student(object):

    def __init__(self, number, seat, time_list):
        self.number = number
        self.seat = seat
        self.time_list = time_list

    # def check_seat(self):


def read_seat(fileName):
    # type: (object) -> object
    temp = []
    df = pd.read_excel(fileName)
    df = pd.DataFrame(df)
    for index, row in df.iterrows():
        temp.append((row[0], row[1]))
    seat_dic = dict(temp)
    return seat_dic


def get_week(t):
    t = t.split(" ")
    t = t[0].split("-")
    t = [int(t[0]), int(t[1]), int(t[2])]
    week = datetime.datetime(t[0], t[1], t[2]).strftime("%w")
    week = int(week)
    return week


def get_course_n(t):
    distance = 0
    t = t.split(" ")
    t1 = [8, 0]
    t2 = [9, 40]
    t3 = [10, 0]
    t4 = [11, 40]
    t5 = [13, 30]
    t6 = [15, 10]
    t7 = [15, 30]
    t8 = [17, 10]
    t9 = [18, 30]
    t0 = [21, 0]
    temp_list = []
    time = [t1, t2, t3, t4, t5, t6, t7, t8, t9, t0]
    for i in time:
        temp_list.append(i[0]*60+i[1])
    time = temp_list
    t = t[1].split(":")
    t = [int(t[0]), int(t[1])]
    t = t[0]*60+t[1]
    temp = 0
    temp2 = 0
    for i in time:
        temp += 1
        if t - i < 0 and temp2 < 1:
            temp2 = temp
            distance += i - t

    if temp2 == 1 or temp2 == 0:
        return 0, 0
    else:
        if temp2 % 2 == 0:
            return temp2 / 2, distance
        else:
            if temp2 % 2 == 1:
                return 0, 0


def get_week_n(t):
    t = t.split(" ")
    t = t[0]
    n = Caltime("2018-08-27", t)
    n = str(n)
    n = n.split(" days, ")
    n = int(n[0])
    return n / 7 + 1


def Caltime(date1, date2):

    date1 = time.strptime(date1, "%Y-%m-%d")
    date2 = time.strptime(date2, "%Y-%m-%d")

    date1 = datetime.datetime(date1[0], date1[1], date1[2])
    date2 = datetime.datetime(date2[0], date2[1], date2[2])

    return date2-date1


def read_course(fileName, num, time):
    week = get_week(time)  # 输入日期是周几
    if week > 5:
        return 0, 0
    course_n, distance = get_course_n(time)  # 所在时间为第几节课，若不是上课时间则返回0
    if course_n == 0:
        return 0, 0
    week_n = get_week_n(time)  # 输入日期是第几周
    course_list = []
    df = pd.read_excel(fileName)
    df = pd.DataFrame(df)
    for index, row in df.iterrows():
        if row[0] == num:
            temp = -1
            for i in row:
                temp += 1
                if isinstance(i, type(u"unicode")) and temp > 0:
                    weekday = temp / 5 + 1  # 星期几
                    course_num = temp % 5  # 第几节课
                    if course_num == 0:
                        course_num = 5
                    course = i.split("\n")
                    rows_num = 0
                    if weekday == week:
                        for j in course:
                            rows_num += 1
                            if rows_num % 5 == 0:
                                j = j.replace("[", "")
                                j = j.replace("]", "")
                                j = j.replace(u"周", " ")
                                j = j.replace(u"节", " ")
                                j = j.replace(",", " ")

                                if u"单" in j and week_n % 2 == 1:
                                    j = j.replace(u" 单 ", "")
                                    j = j.split(" ")
                                    if "-" not in j[0]:
                                        if week_n == int(j[0]):
                                            course_list.append(course_num)
                                    else:
                                        j = j[0].split("-")
                                        if week_n >= int(j[0]) and week_n <= int(j[1]):
                                            course_list.append(course_num)
                                else:
                                    if u"双" in j and week_n % 2 == 0:
                                        j = j.replace(u" 双 ", "")
                                        j = j.split(" ")
                                        if "-" not in j[0]:
                                            if week_n == int(j[0]):
                                                course_list.append(course_num)
                                        else:
                                            j = j[0].split("-")
                                            if week_n >= int(j[0]) and week_n <= int(j[1]):
                                                course_list.append(course_num)
                                    else:
                                        if u"单" not in j and u"双" not in j:

                                            j = j.split(" ")
                                            if "-" not in j[0]:
                                                if week_n == int(j[0]):
                                                    course_list.append(course_num)
                                            else:
                                                j = j[0].split("-")
                                                if week_n >= int(j[0]) and week_n <= int(j[1]):
                                                    course_list.append(course_num)
            if int(course_n) in course_list:
                return 1, distance
            else:
                return 0, 0

def time_cmp(t1, t2):
    d1 = datetime.datetime.strptime(t1, '%Y-%m-%d %H:%M:%S')
    d2 = datetime.datetime.strptime(t2, '%Y-%m-%d %H:%M:%S')
    delta = d1 - d2
    return delta, delta.days


if __name__ == '__main__':

    fileName_course = u"课程总表.xls"
    fileName_seat = u"座位表.xlsx"
    time1 = '2018-09-24 10:00'  # 输入查询的时间

    # 加一个不合法时间判断，时间限定在，2018-9-3 00:00:00到2019-2-1 23:59:59；同时判断输入格式
    seat_d = read_seat(fileName_seat)
    seat = u"一层 图书空间 A 座位1"
    # seat = u"七层 图书空间 D"
    num = seat_d[seat]   # 输入查询的座位
    ava, distance = read_course(fileName_course, num, time1)
    if ava == 0:
        print seat + u"处于占用状态。"
    else:
        print seat + u"处于空闲状态，空闲时间为" + str(distance) + u"分钟。"
