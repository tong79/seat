# -*- coding: utf-8 -*-
# @Time : 2019/5/12 13:32
# @Author : Shilida
# @Site : 
# @File : view_main.py
# @Software: PyCharm
from Tkinter import *
import SeatFree

class SearchView(object):

    statuLabel1Color = 'brown'
    statuLabel2Color = 'brown'
    statuLabel3Color = 'brown'
    statuLabel4Color = 'brown'
    labelColor1 = 'green'
    labelColor2 = 'gray'
    labelColor3 = 'orange'
    selectYear = 2018
    selectMonth = 1
    selectDay = 1
    selectHour = '00:00'
    yearArr = [2018, 2019]
    selectYearVarGe = 0
    monthArr2018 = [9, 10, 11, 12]
    monthArr2019 = [1, 2]
    monthArr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    dayArr31 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
                29, 30, 31]
    dayArr30 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
                29, 30]
    dayArr2 = [1]
    hourArr = ['06:00', '07:00', '08:00', '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00',
               '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00', ]
    roomHeightArr = ['一层', '二层', '三层', '四层', '五层', '六层', '七层', '八层']
    roomRoomArr = ['图书空间 A', '图书空间 B', '图书空间 C', '图书空间 D', '图书空间 E', '图书空间 F', '图书空间 G', '图书空间 H']
    searchValue = [-1, -1, -1, -1, -1, -1]  # 年,月,日,时刻,楼层数,区域
    # def printOption(self,event):
    #     if (self.selectYearVar.get() == '2018'):
    #         menuButtonMonth = OptionMenu(self.frameTime,self. selectMonthVar, *self.monthArr2018)
    #     else:
    #         menuButtonMonth = OptionMenu(self.frameTime, self.selectMonthVar, *self.monthArr2019)
    #     menuButtonMonth.place(x=150, y=50)
    #     self.selectMonthVar.set('月份')
    #     print self.selectYearVar.get()
    # self.selectYearVarGet = v.get()
    def callback(self):
        self.searchValue[0] = self.selectYearVar.get()
        self.searchValue[1] = self.selectMonthVar.get()
        self.searchValue[2] = self.selectDayVar.get()
        self.searchValue[3] = self.selectHourVar.get()
        self.searchValue[4] = self.selectHeightVar.get()
        self.searchValue[5] = self.selectRoomVar.get()
        print u"{} {}".format(self.searchValue[4], self.searchValue[5])
        fileName_course = u"课程总表.xls"
        fileName_seat = u"座位表.xlsx"

        # time1 = '2018-09-24 10:21'  # 输入查询的时间
        time1 = '{}-{}-{} {}'.format(self.searchValue[0], self.searchValue[1], self.searchValue[2], self.searchValue[3])
        # print time1
        # 加一个不合法时间判断，时间限定在，2018-9-3 00:00:00到2019-2-1 23:59:59；同时判断输入格式
        seat_d = SeatFree.read_seat(fileName_seat)
        # seat = u"七层 图书空间 D 座位2"
        seat1 = u"{} {} 座位1".format(self.searchValue[4], self.searchValue[5])
        # print u"{} {} 座位1".format(self.searchValue[4],self.searchValue[5])
        num = seat_d[seat1]  # 输入查询的座位
        print fileName_course
        print num
        print time1
        ava, distance = SeatFree.read_course(fileName_course, num, time1)

        if ava == 0:
            print  seat1 + u"处于占用状态。"
            self.statuLabel1Var = StringVar()
            self.statuLabel1 = Label(self.frameLabel, textvariable=self.statuLabel1Var, width=20, height=5,
                                     bg=self.labelColor3)
            self.statuLabel1.place(x=50, y=100)
            self.statuLabel1Var.set(u"座位1处于占用状态。")
        else:
            if ava == 1:
                print seat1 + u"处于空闲状态，空闲时间为" + str(distance) + u"分钟。"
                self.statuLabel1Var = StringVar()
                self.statuLabel1 = Label(self.frameLabel, textvariable=self.statuLabel1Var, width=20, height=5,
                                         bg=self.labelColor1)
                self.statuLabel1.place(x=50, y=100)
                self.statuLabel1Var.set(u"座位1处于空闲状态\n"
                                        u"空闲时间为" + str(distance) + u"分钟。")
            if ava == 2:
                print seat1 + u"处于未占用状态"
                self.statuLabel1Var = StringVar()
                self.statuLabel1 = Label(self.frameLabel, textvariable=self.statuLabel1Var, width=20, height=5,
                                         bg=self.labelColor2)
                self.statuLabel1.place(x=50, y=100)
                self.statuLabel1Var.set(u"座位1处于未分配状态")
        seat2 = u"{} {} 座位2".format(self.searchValue[4], self.searchValue[5])
        num = seat_d[seat2]  # 输入查询的座位
        ava, distance = SeatFree.read_course(fileName_course, num, time1)
        if ava == 0:
            self.statuLabel2Var = StringVar()
            self.statuLabel2 = Label(self.frameLabel, textvariable=self.statuLabel2Var, width=20, height=5,
                                     bg=self.labelColor3)
            self.statuLabel2.place(x=400, y=100)
            print seat2 + u"处于占用状态。"
            self.statuLabel2Var.set(u"座位2处于占用状态。")
            # self.statuLabel2Color = self.labelColor3
        else:
            if ava == 1:
                self.statuLabel2Var = StringVar()
                self.statuLabel2 = Label(self.frameLabel, textvariable=self.statuLabel2Var, width=20, height=5,
                                         bg=self.labelColor1)
                self.statuLabel2.place(x=400, y=100)
                print seat2 + u"处于空闲状态，空闲时间为" + str(distance) + u"分钟。"
                self.statuLabel2Var.set(u"座位2处于空闲状态\n"
                                        u"空闲时间为" + str(distance) + u"分钟。")
            if ava == 2:
                self.statuLabel2Var = StringVar()
                self.statuLabel2 = Label(self.frameLabel, textvariable=self.statuLabel2Var, width=20, height=5,
                                         bg=self.labelColor2)
                self.statuLabel2.place(x=400, y=100)
                print seat2 + u"处于未分配状态"
                self.statuLabel2Var.set(u"座位2处于未分配状态")

            # self.statuLabel2Color = self.labelColor1

        seat3 = u"{} {} 座位3".format(self.searchValue[4], self.searchValue[5])
        num = seat_d[seat3]  # 输入查询的座位
        ava, distance = SeatFree.read_course(fileName_course, num, time1)
        if ava == 0:
            self.statuLabel3Var = StringVar()
            self.statuLabel3 = Label(self.frameLabel, textvariable=self.statuLabel3Var, width=20, height=5,
                                     bg=self.labelColor3)
            self.statuLabel3.place(x=50, y=300)
            print seat3 + u"处于占用状态。"
            self.statuLabel3Var.set(u"座位3处于占用状态。")
            self.statuLabel3Color = self.labelColor3
        else:
            if ava == 1:
                self.statuLabel3Var = StringVar()
                self.statuLabel3 = Label(self.frameLabel, textvariable=self.statuLabel3Var, width=20, height=5,
                                         bg=self.labelColor1)
                self.statuLabel3.place(x=50, y=300)
                print seat3 + u"处于空闲状态，空闲时间为" + str(distance) + u"分钟。"
                self.statuLabel3Var.set(u"座位3处于空闲状态\n"
                                        u"空闲时间为" + str(distance) + u"分钟。")
            if ava == 2:
                self.statuLabel3Var = StringVar()
                self.statuLabel3 = Label(self.frameLabel, textvariable=self.statuLabel3Var, width=20, height=5,
                                         bg=self.labelColor2)
                self.statuLabel3.place(x=50, y=300)
                print seat3 + u"处于未分配状态"
                self.statuLabel3Var.set(u"座位3处于未分配状态")


        seat4 = u"{} {} 座位4".format(self.searchValue[4], self.searchValue[5])
        num = seat_d[seat4]  # 输入查询的座位
        ava, distance = SeatFree.read_course(fileName_course, num, time1)
        if ava == 0:
            # Label.destroy()
            self.statuLabel4Var = StringVar()
            self.statuLabel4 = Label(self.frameLabel, textvariable=self.statuLabel4Var, width=20, height=5,
                                     bg=self.labelColor3)
            self.statuLabel4.place(x=400, y=300)
            self.statuLabel4Var.set(u"座位4处于占用状态。")
            # self.statu#Label4Color = self.labelColor3
            print seat4 + u"处于占用状态。"
        else:
            if ava == 1:
                self.statuLabel4Var = StringVar()
                # self.statuLabel4Color = self.labelColor1
                self.statuLabel4 = Label(self.frameLabel, textvariable=self.statuLabel4Var, width=20, height=5,
                                         bg=self.labelColor1)
                self.statuLabel4.place(x=400, y=300)

                self.statuLabel4Var.set(u"座位4处于空闲状态\n"
                                        u"空闲时间为" + str(distance) + u"分钟。")

                print seat4 + u"处于空闲状态空闲时间为" + str(distance) + u"分钟。"
            if ava == 2:
                self.statuLabel4Var = StringVar()
                # self.statuLabel4Color = self.labelColor1
                self.statuLabel4 = Label(self.frameLabel, textvariable=self.statuLabel4Var, width=20, height=5,
                                         bg=self.labelColor2)
                self.statuLabel4.place(x=400, y=300)

                self.statuLabel4Var.set(u"座位4处于未分配状态")

                print seat4 + u"处于未分配状态"
        self.statuLabel5Var = StringVar()
        self.statuLabel5 = Label(self.frameLabel, textvariable=self.statuLabel5Var, width=22, height=2, bg='white',
                                 font=30)
        self.statuLabel5.place(x=415, y=440)
        self.statuLabel5Var.set(u"{} {} 区".format(self.searchValue[4], self.searchValue[5]))
        self.switch(self.searchValue[5])
    def yearClick(self,event):
        if(self.selectYearVar.get()== '2018'):
            selectMonthVar = StringVar()
            menuButtonMonth = OptionMenu(self.frameTime, selectMonthVar, *self.monthArr2018, command=self.monthClick)
            menuButtonMonth.place(x=150, y=45)
            selectMonthVar.set('月')
            self.selectMonthVar = selectMonthVar
        if (self.selectYearVar.get() == '2019'):
            selectMonthVar = StringVar()
            menuButtonMonth = OptionMenu(self.frameTime, selectMonthVar, *self.monthArr2019, command=self.monthClick)
            menuButtonMonth.place(x=150, y=45)
            selectMonthVar.set('月')
            self.selectMonthVar = selectMonthVar
    def monthClick(self,event):
        if (self.selectMonthVar.get() == '10'or'12'or'1'):
            selectDayVar = StringVar()
            selectDayVar.set('日')
            menuButtonDay = OptionMenu(self.frameTime, selectDayVar, *self.dayArr31)  # , width=10, height=1)
            menuButtonDay.place(x=205, y=45)
            self.selectDayVar = selectDayVar
        if (self.selectMonthVar.get() == '9'or'11'):
            selectDayVar = StringVar()
            selectDayVar.set('日')
            menuButtonDay = OptionMenu(self.frameTime, selectDayVar, *self.dayArr30)  # , width=10, height=1)
            menuButtonDay.place(x=205, y=45)
            self.selectDayVar = selectDayVar
        if (self.selectMonthVar.get() == '2'):
            selectDayVar = StringVar()
            selectDayVar.set('日')
            menuButtonDay = OptionMenu(self.frameTime, selectDayVar, *self.dayArr2)  # , width=10, height=1)
            menuButtonDay.place(x=205, y=45)
            self.selectDayVar = selectDayVar
    def switch(self,value):

        if(value == u"图书空间 A"):
            self.roomButtonA = Button(self.frameButton, text="图书空间 A区", width=28, height=3,bg = 'powderblue')
            self.roomButtonA.place(x=0, y=0)
            self.roomButtonVarA = StringVar()
            # B button
            self.roomButtonVarB = StringVar()
            self.roomButtonB = Button(self.frameButton, text="图书空间 B区", width=28, height=3)
            self.roomButtonB.place(x=0, y=64)
            # C button
            self.roomButtonVarC = StringVar()
            self.roomButtonC = Button(self.frameButton, text="图书空间 C区", width=28, height=3)
            self.roomButtonC.place(x=0, y=128)
            # D button
            self.roomButtonVarD = StringVar()
            self.roomButtonD = Button(self.frameButton, text="图书空间 D区", width=28, height=3)
            self.roomButtonD.place(x=0, y=192)
            # E button
            self.roomButtonVarE = StringVar()
            self.roomButtonE = Button(self.frameButton, text="图书空间 E区", width=28, height=3)
            self.roomButtonE.place(x=0, y=256)
            # F button
            self.roomButtonVarF = StringVar()
            self.roomButtonF = Button(self.frameButton, text="图书空间 F区", width=28, height=3)
            self.roomButtonF.place(x=0, y=320)
            # G button
            self.roomButtonVarG = StringVar()
            self.roomButtonG = Button(self.frameButton, text="图书空间 G区", width=28, height=3)
            self.roomButtonG.place(x=0, y=384)
            # H button
            self.roomButtonVarH = StringVar()
            self.roomButtonH = Button(self.frameButton, text="图书空间 H区", width=28, height=3)
            self.roomButtonH.place(x=0, y=448)
        if (value == u"图书空间 B"):
            self.roomButtonVarA = StringVar()
            self.roomButtonA = Button(self.frameButton, text="图书空间 A区", width=28, height=3)
            self.roomButtonA.place(x=0, y=0)
            # B button
            self.roomButtonVarB = StringVar()
            self.roomButtonB = Button(self.frameButton, text="图书空间 B区", width=28, height=3,bg = 'powderblue')
            self.roomButtonB.place(x=0, y=64)
            # C button
            self.roomButtonVarC = StringVar()
            self.roomButtonC = Button(self.frameButton, text="图书空间 C区", width=28, height=3)
            self.roomButtonC.place(x=0, y=128)
            # D button
            self.roomButtonVarD = StringVar()
            self.roomButtonD = Button(self.frameButton, text="图书空间 D区", width=28, height=3)
            self.roomButtonD.place(x=0, y=192)
            # E button
            self.roomButtonVarE = StringVar()
            self.roomButtonE = Button(self.frameButton, text="图书空间 E区", width=28, height=3)
            self.roomButtonE.place(x=0, y=256)
            # F button
            self.roomButtonVarF = StringVar()
            self.roomButtonF = Button(self.frameButton, text="图书空间 F区", width=28, height=3)
            self.roomButtonF.place(x=0, y=320)
            # G button
            self.roomButtonVarG = StringVar()
            self.roomButtonG = Button(self.frameButton, text="图书空间 G区", width=28, height=3)
            self.roomButtonG.place(x=0, y=384)
            # H button
            self.roomButtonVarH = StringVar()
            self.roomButtonH = Button(self.frameButton, text="图书空间 H区", width=28, height=3)
            self.roomButtonH.place(x=0, y=448)
        if (value == u"图书空间 C"):
            self.roomButtonVarA = StringVar()
            self.roomButtonA = Button(self.frameButton, text="图书空间 A区", width=28, height=3)
            self.roomButtonA.place(x=0, y=0)
            # B button
            self.roomButtonVarB = StringVar()
            self.roomButtonB = Button(self.frameButton, text="图书空间 B区", width=28, height=3)
            self.roomButtonB.place(x=0, y=64)
            # C button
            self.roomButtonVarC = StringVar()
            self.roomButtonC = Button(self.frameButton, text="图书空间 C区", width=28, height=3,bg = 'powderblue')
            self.roomButtonC.place(x=0, y=128)
            # D button
            self.roomButtonVarD = StringVar()
            self.roomButtonD = Button(self.frameButton, text="图书空间 D区", width=28, height=3)
            self.roomButtonD.place(x=0, y=192)
            # E button
            self.roomButtonVarE = StringVar()
            self.roomButtonE = Button(self.frameButton, text="图书空间 E区", width=28, height=3)
            self.roomButtonE.place(x=0, y=256)
            # F button
            self.roomButtonVarF = StringVar()
            self.roomButtonF = Button(self.frameButton, text="图书空间 F区", width=28, height=3)
            self.roomButtonF.place(x=0, y=320)
            # G button
            self.roomButtonVarG = StringVar()
            self.roomButtonG = Button(self.frameButton, text="图书空间 G区", width=28, height=3)
            self.roomButtonG.place(x=0, y=384)
            # H button
            self.roomButtonVarH = StringVar()
            self.roomButtonH = Button(self.frameButton, text="图书空间 H区", width=28, height=3)
            self.roomButtonH.place(x=0, y=448)
        if (value == u"图书空间 D"):
            self.roomButtonVarA = StringVar()
            self.roomButtonA = Button(self.frameButton, text="图书空间 A区", width=28, height=3)
            self.roomButtonA.place(x=0, y=0)
            # B button
            self.roomButtonVarB = StringVar()
            self.roomButtonB = Button(self.frameButton, text="图书空间 B区", width=28, height=3)
            self.roomButtonB.place(x=0, y=64)
            # C button
            self.roomButtonVarC = StringVar()
            self.roomButtonC = Button(self.frameButton, text="图书空间 C区", width=28, height=3)
            self.roomButtonC.place(x=0, y=128)
            # D button
            self.roomButtonVarD = StringVar()
            self.roomButtonD = Button(self.frameButton, text="图书空间 D区", width=28, height=3,bg = 'powderblue')
            self.roomButtonD.place(x=0, y=192)
            # E button
            self.roomButtonVarE = StringVar()
            self.roomButtonE = Button(self.frameButton, text="图书空间 E区", width=28, height=3)
            self.roomButtonE.place(x=0, y=256)
            # F button
            self.roomButtonVarF = StringVar()
            self.roomButtonF = Button(self.frameButton, text="图书空间 F区", width=28, height=3)
            self.roomButtonF.place(x=0, y=320)
            # G button
            self.roomButtonVarG = StringVar()
            self.roomButtonG = Button(self.frameButton, text="图书空间 G区", width=28, height=3)
            self.roomButtonG.place(x=0, y=384)
            # H button
            self.roomButtonVarH = StringVar()
            self.roomButtonH = Button(self.frameButton, text="图书空间 H区", width=28, height=3)
            self.roomButtonH.place(x=0, y=448)
        if (value == u"图书空间 E"):
            self.roomButtonVarA = StringVar()
            self.roomButtonA = Button(self.frameButton, text="图书空间 A区", width=28, height=3)
            self.roomButtonA.place(x=0, y=0)
            # B button
            self.roomButtonVarB = StringVar()
            self.roomButtonB = Button(self.frameButton, text="图书空间 B区", width=28, height=3)
            self.roomButtonB.place(x=0, y=64)
            # C button
            self.roomButtonVarC = StringVar()
            self.roomButtonC = Button(self.frameButton, text="图书空间 C区", width=28, height=3)
            self.roomButtonC.place(x=0, y=128)
            # D button
            self.roomButtonVarD = StringVar()
            self.roomButtonD = Button(self.frameButton, text="图书空间 D区", width=28, height=3)
            self.roomButtonD.place(x=0, y=192)
            # E button
            self.roomButtonVarE = StringVar()
            self.roomButtonE = Button(self.frameButton, text="图书空间 E区", width=28, height=3,bg = 'powderblue')
            self.roomButtonE.place(x=0, y=256)
            # F button
            self.roomButtonVarF = StringVar()
            self.roomButtonF = Button(self.frameButton, text="图书空间 F区", width=28, height=3)
            self.roomButtonF.place(x=0, y=320)
            # G button
            self.roomButtonVarG = StringVar()
            self.roomButtonG = Button(self.frameButton, text="图书空间 G区", width=28, height=3)
            self.roomButtonG.place(x=0, y=384)
            # H button
            self.roomButtonVarH = StringVar()
            self.roomButtonH = Button(self.frameButton, text="图书空间 H区", width=28, height=3)
            self.roomButtonH.place(x=0, y=448)
        if (value == u"图书空间 F"):
            self.roomButtonVarA = StringVar()
            self.roomButtonA = Button(self.frameButton, text="图书空间 A区", width=28, height=3)
            self.roomButtonA.place(x=0, y=0)
            # B button
            self.roomButtonVarB = StringVar()
            self.roomButtonB = Button(self.frameButton, text="图书空间 B区", width=28, height=3)
            self.roomButtonB.place(x=0, y=64)
            # C button
            self.roomButtonVarC = StringVar()
            self.roomButtonC = Button(self.frameButton, text="图书空间 C区", width=28, height=3)
            self.roomButtonC.place(x=0, y=128)
            # D button
            self.roomButtonVarD = StringVar()
            self.roomButtonD = Button(self.frameButton, text="图书空间 D区", width=28, height=3)
            self.roomButtonD.place(x=0, y=192)
            # E button
            self.roomButtonVarE = StringVar()
            self.roomButtonE = Button(self.frameButton, text="图书空间 E区", width=28, height=3)
            self.roomButtonE.place(x=0, y=256)
            # F button
            self.roomButtonVarF = StringVar()
            self.roomButtonF = Button(self.frameButton, text="图书空间 F区", width=28, height=3,bg = 'powderblue')
            self.roomButtonF.place(x=0, y=320)
            # G button
            self.roomButtonVarG = StringVar()
            self.roomButtonG = Button(self.frameButton, text="图书空间 G区", width=28, height=3)
            self.roomButtonG.place(x=0, y=384)
            # H button
            self.roomButtonVarH = StringVar()
            self.roomButtonH = Button(self.frameButton, text="图书空间 H区", width=28, height=3)
            self.roomButtonH.place(x=0, y=448)
        if (value == u"图书空间 G"):
            self.roomButtonVarA = StringVar()
            self.roomButtonA = Button(self.frameButton, text="图书空间 A区", width=28, height=3)
            self.roomButtonA.place(x=0, y=0)
            # B button
            self.roomButtonVarB = StringVar()
            self.roomButtonB = Button(self.frameButton, text="图书空间 B区", width=28, height=3)
            self.roomButtonB.place(x=0, y=64)
            # C button
            self.roomButtonVarC = StringVar()
            self.roomButtonC = Button(self.frameButton, text="图书空间 C区", width=28, height=3)
            self.roomButtonC.place(x=0, y=128)
            # D button
            self.roomButtonVarD = StringVar()
            self.roomButtonD = Button(self.frameButton, text="图书空间 D区", width=28, height=3)
            self.roomButtonD.place(x=0, y=192)
            # E button
            self.roomButtonVarE = StringVar()
            self.roomButtonE = Button(self.frameButton, text="图书空间 E区", width=28, height=3)
            self.roomButtonE.place(x=0, y=256)
            # F button
            self.roomButtonVarF = StringVar()
            self.roomButtonF = Button(self.frameButton, text="图书空间 F区", width=28, height=3)
            self.roomButtonF.place(x=0, y=320)
            # G button
            self.roomButtonVarG = StringVar()
            self.roomButtonG = Button(self.frameButton, text="图书空间 G区", width=28, height=3,bg = 'powderblue')
            self.roomButtonG.place(x=0, y=384)
            # H button
            self.roomButtonVarH = StringVar()
            self.roomButtonH = Button(self.frameButton, text="图书空间 H区", width=28, height=3)
            self.roomButtonH.place(x=0, y=448)
        if (value == u"图书空间 H"):
            self.roomButtonVarA = StringVar()
            self.roomButtonA = Button(self.frameButton, text="图书空间 A区", width=28, height=3)
            self.roomButtonA.place(x=0, y=0)
            # B button
            self.roomButtonVarB = StringVar()
            self.roomButtonB = Button(self.frameButton, text="图书空间 B区", width=28, height=3)
            self.roomButtonB.place(x=0, y=64)
            # C button
            self.roomButtonVarC = StringVar()
            self.roomButtonC = Button(self.frameButton, text="图书空间 C区", width=28, height=3)
            self.roomButtonC.place(x=0, y=128)
            # D button
            self.roomButtonVarD = StringVar()
            self.roomButtonD = Button(self.frameButton, text="图书空间 D区", width=28, height=3)
            self.roomButtonD.place(x=0, y=192)
            # E button
            self.roomButtonVarE = StringVar()
            self.roomButtonE = Button(self.frameButton, text="图书空间 E区", width=28, height=3)
            self.roomButtonE.place(x=0, y=256)
            # F button
            self.roomButtonVarF = StringVar()
            self.roomButtonF = Button(self.frameButton, text="图书空间 F区", width=28, height=3)
            self.roomButtonF.place(x=0, y=320)
            # G button
            self.roomButtonVarG = StringVar()
            self.roomButtonG = Button(self.frameButton, text="图书空间 G区", width=28, height=3)
            self.roomButtonG.place(x=0, y=384)
            # H button
            self.roomButtonVarH = StringVar()
            self.roomButtonH = Button(self.frameButton, text="图书空间 H区", width=28, height=3,bg = 'powderblue')
            self.roomButtonH.place(x=0, y=448)

    def __init__(self, win):
        self.win = win

    def view1(self):
        frameTime = Frame(self.win, height=100, width=800, )
        frameTime.place(x=0, y=0)
        self.frameTime = frameTime
        # 查询时间button
        textLabel = Label(frameTime, text="查询时间:", width=7, height=1)
        textLabel.place(x=20, y=50)
        # 选择查询时间
        # 选择年份
        selectYearVar = StringVar()
        selectYearVar.set('年')
        menuButtonYear = OptionMenu(frameTime, selectYearVar, *self.yearArr,command=self.yearClick)  # , width=10, height=1)
        self.selectYearVar = selectYearVar
        menuButtonYear.place(x=80, y=45)
        #选择年份
        selectMonthVar = StringVar()
        menuButtonMonth = OptionMenu(frameTime, selectMonthVar, *self.monthArr,command=self.monthClick)
        menuButtonMonth.place(x=150, y=45)
        selectMonthVar.set('月')
        self.selectMonthVar = selectMonthVar
        # 选择日期
        selectDayVar = StringVar()
        selectDayVar.set('日')
        menuButtonDay = OptionMenu(frameTime, selectDayVar, *self.dayArr30)  # , width=10, height=1)
        menuButtonDay.place(x=205, y=45)
        self.selectDayVar = selectDayVar
        # 选择时刻
        selectHourVar = StringVar()
        selectHourVar.set('时刻')
        menuButtonHour = OptionMenu(frameTime, selectHourVar, *self.hourArr)  # , width=10, height=1)
        menuButtonHour.place(x=258, y=45)
        self.selectHourVar = selectHourVar
        # 查询位置button
        textLabel = Label(frameTime, text="查询位置:", width=7, height=1)
        textLabel.place(x=370, y=50)
        # 选择查询的楼层
        selectHeightVar = StringVar()
        selectHeightVar.set('楼层')
        menuButtonRoom = OptionMenu(frameTime, selectHeightVar, *self.roomHeightArr)  # , width=10, height=1)
        menuButtonRoom.place(x=430, y=45)
        self.selectHeightVar = selectHeightVar
        # 选择查询的房间
        selectRoomVar = StringVar()
        selectRoomVar.set('请选择具体区域')
        menuButtonRoom = OptionMenu(frameTime, selectRoomVar, *self.roomRoomArr)  # , width=10, height=1)
        menuButtonRoom.place(x=500, y=45)
        self.selectRoomVar = selectRoomVar
        # 查询button
        searchButton = Button(frameTime, text="查询", width=7, command=self.callback)
        searchButton.place(x=700, y=45)
        # 主体部分框框架
        frameLabel = Frame(self.win, height=700, width=600, bg='white')
        frameLabel.place(x=0, y=100)
        self.frameLabel = frameLabel
        # button部分框架
        self.frameButton = Frame(self.win, height=700, width=200, bg='red')
        self.frameButton.place(x=600, y=100)
        # A button
        self.roomButtonVarA = StringVar()
        self.roomButtonA = Button(self.frameButton, text="图书空间 A区", width=28, height=3)
        self.roomButtonA.place(x=0, y=0)
        # B button
        self.roomButtonVarB = StringVar()
        self.roomButtonB = Button(self.frameButton, text="图书空间 B区", width=28, height=3)
        self.roomButtonB.place(x=0, y=64)
        # C button
        self.roomButtonVarC = StringVar()
        self.roomButtonC = Button(self.frameButton, text="图书空间 C区", width=28, height=3)
        self.roomButtonC.place(x=0, y=128)
        # D button
        self.roomButtonVarD = StringVar()
        self.roomButtonD = Button(self.frameButton, text="图书空间 D区", width=28, height=3)
        self.roomButtonD.place(x=0, y=192)
        # E button
        self.roomButtonVarE = StringVar()
        self.roomButtonE = Button(self.frameButton, text="图书空间 E区", width=28, height=3)
        self.roomButtonE.place(x=0, y=256)
        # F button
        self.roomButtonVarF = StringVar()
        self.roomButtonF = Button(self.frameButton, text="图书空间 F区", width=28, height=3)
        self.roomButtonF.place(x=0, y=320)
        # G button
        self.roomButtonVarG = StringVar()
        self.roomButtonG = Button(self.frameButton, text="图书空间 G区", width=28, height=3)
        self.roomButtonG.place(x=0, y=384)
        # H button
        self.roomButtonVarH = StringVar()
        self.roomButtonH = Button(self.frameButton, text="图书空间 H区", width=28, height=3)
        self.roomButtonH.place(x=0, y=448)

if __name__ == '__main__':
    win = Tk()  # 构造窗体
    win.title("图书馆座位查询系统")  # 设置窗口标题
    win.geometry("800x610")  # 设置窗口大小 注意：是x 不是*
    win.resizable(width=False, height=False)
    searchView = SearchView(win)
    searchView.view1()
    win.mainloop()

