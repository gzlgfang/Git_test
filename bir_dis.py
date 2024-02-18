import numpy as np

# 绘图设置
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams["xtick.direction"] = "in"  # 坐标轴上的短线朝内，默认朝外
plt.rcParams["ytick.direction"] = "in"
# 全局设置字体
mpl.rcParams["font.sans-serif"] = ["SimHei"]  # 保证显示中文字
mpl.rcParams["axes.unicode_minus"] = False  # 保证负号显示
mpl.rcParams["font.size"] = 12  # 设置字体大小
mpl.rcParams["font.style"] = "oblique"  # 设置字体风格，倾斜与否
mpl.rcParams["font.weight"] = "normal"  # "normal",=500，设置字体粗细

# fig,ax=plt.subplots(1,3,figsize=(15,4),num="subplot(i,j,**kwargs)布局")
# 绘制三种人数人日分布图


def bir_distr(n):
    bir_month = []
    bir_day = []
    for people in range(n):  ##people为房间人数

        tem_m = np.random.randint(1, 13)  ##1-12中的随机整数
        m_31 = [1, 3, 5, 7, 8, 10, 12]
        if [tem_m in m_31][0] == True:
            tem_day = np.random.randint(1, 32)  ##每月31天中的某1天
        else:
            if tem_m == 2:
                tem_day = np.random.randint(1, 29)  ##2月28天中的某1天
            else:
                tem_day = np.random.randint(1, 31)  ##每月30天中的某1天
        # print(tem_m,tem_day)
        bir_month.append(tem_m)
        bir_day.append(tem_day)
    return [bir_day, bir_month]


people = 10
x = bir_distr(people)[0]
y = bir_distr(people)[1]
# print(x,y)
def draw_dis(people):
    x = bir_distr(people)[0]
    y = bir_distr(people)[1]
    plt.scatter(
        x[0 : int(len(x) / 2)],
        y[0 : int(len(x) / 2)],
        s=200,
        c="b",
        marker="*",
        label="蓝色散点图",
        alpha=0.6,
        clip_on=False,
    )
    plt.scatter(
        x[int(len(x) / 2) :],
        y[int(len(x) / 2) :],
        s=60,
        c="r",
        marker="o",
        label="红色散点图",
        alpha=0.8,
        clip_on=False,
    )
    plt.ylim(0, 12)
    plt.xlim(0, 31)
    plt.xticks(np.arange(0, 32, 1))
    plt.yticks(np.arange(0, 13, 1))
    str1 = "房间人数为" + str(people) + "人时生日分布图"
    plt.title(str1)
    plt.grid()


fig0 = plt.figure(dpi=120)
fig0 = draw_dis(20)
fig1 = plt.figure(dpi=120)
fig1 = draw_dis(50)
fig2 = plt.figure(dpi=120)
fig2 = draw_dis(366)

plt.show()
