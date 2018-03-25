# Word List
# Kobe Arthur Scofield
# 2018-03-24
# Build 4
# Python: Anaconda3_64 5.0.0.0 (Python 3.6.2)
# IDE: MSVS2017_Community 15.6.4

# =============== WARNING ===============
# The word list below will make you hungry.
# So for the best, don't try to read the whole list.
# You can skip reading it.
# (The author feels hungry when writing the list.)

foodwordlist = {'apple': "苹果",        'banana': "香蕉",       'burger': "汉堡",       'cabbage': "卷心菜",
                'cake': "蛋糕",         'cheese': "奶酪",       'chestnut': "栗子",     'coffee': "咖啡",
                'doughnut': "甜甜圈",   'egg': "鸡蛋",          'fish': "鱼",           'fries': "薯片",
                'garlic': "大蒜",       'ham': "火腿",          'ice-cream': "冰淇淋",  'juice': "果汁",
                'lemon': "柠檬",        'lollipop': "棒棒糖",   'mandarin': "橘子",     'mashmallow': "棉花糖",
                'milk': "牛奶",         'mooncake': "月饼",     'mushroom': "蘑菇",     'mutton': "羊肉",
                'noghut': "牛轧糖",     'onion': "洋葱",        'orange': "橙子",       'peach': "桃子",
                'pear': "梨",           'pepper': "胡椒",       'pork': "猪肉",         'steak': "牛排",
                'strawberry': "草莓",   'tea': "茶",            'water': "水",          'biscuit': "饼干"}

# =========== End of warning ============

import random

question = 10   # Numbers of words to ask

rightcount = 0  # correction counting
usedlist = {}   # Prepare an empty list to store used words
originlist = list(foodwordlist.keys())  # Getting keys and pop in for using
print("A word will display and you'll have to type the meaning of the word.")
print("You'll do it", question, "times.\n")
for mainloop in range(0, question):
    flag = False
    ransel = 0
    while (flag == False):
        ransel = random.randint(0, len(foodwordlist) - 1)   # Lucky number ;-)
        if originlist[ransel] in usedlist:
            flag = False    # loop again if get the used word unluckily
        else:
            usedlist[originlist[ransel]] = "used"   # Throw it in the used list
            flag = True     # Leaving lucky number ;-)
    print(originlist[ransel]+": ", end = '')
    answer = input()        # Type answer
    if (answer == foodwordlist[originlist[ransel]]):
        rightcount = rightcount + 1
        print("Right\n")
    else:
        print("Error\n")
correctrate = rightcount / question * 100   # Calculating the correct rate
print("Correct rate:", correctrate, "%")
