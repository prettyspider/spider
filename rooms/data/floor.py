import getdata
import time
import re
import random
import csv
import savedata
title=''
price=''
src=''
area=''
address=''
direction=''
condition=''
hall=''
bathroom=''
buildingheight=''
rooms=''
room=''
directions=['东','西','南','北']
# 1.获取网页数据
# url='https://bj.lianjia.com/zufang/'
urls = [f'https://bj.lianjia.com/zufang/pg{i}/#contentList'  for i in range(100)]

for url in urls:
    soup = getdata.get_data(url)
    # 2.解析数据
    div_all = soup.find_all(name='div', attrs={"class": "content__list--item"})  # 获取数据的大盒子
    for item in div_all:
        try:
            # 房子字
            title = item.find(name='a', attrs={'class': 'twoline'}).text
            # 规则
            title = re.sub(r'\s+', '', title)
        except AttributeError:
            title=item.find(name='p',attrs={'class':'twoline'}).text
            title=re.sub(r'\s+',"",title)
        #    价格
        price = item.find(name='span', attrs={'class': 'content__list--item-price'}).text
        price = re.split(r" ", price)[0]
        #     房子的图片
        img = item.find(name='a', attrs={'class': 'content__list--item--aside'}).find(name='img',attrs={'class': 'lazyload'})
        # http: // image1.ljcdn.com /
        src = img.get('data-src')
        src=src.replace('https://image1.ljcdn.com/','')
        if '!' in src:
            print(src)
        complex = item.find(name='p', attrs={'class': 'content__list--item--des'})
        # 地址
        addresses = complex.find_all(name='a')
        temp_str = ''
        for address in addresses:
            temp = address.text
            temp_str += temp + '-'
        address = temp_str[:len(temp_str) - 1]
        # print(address)
        # 面积area,方位direction,房子书rooms，楼高buildingheight
        i_all = complex.find_all(name='i')
        if len(i_all) == 5:
            area = i_all[1].next_sibling
            area = re.sub(r'\s+', '', area)
            area = re.split(r'㎡', area)[0]
            direction = i_all[2].next_sibling
            direction=re.sub(r'\s+','',direction)
            if len(direction) > 2:
                num = random.randint(0, 3)
                direction = directions[num]
            rooms = i_all[len(i_all) - 2].next_sibling
            rooms = re.sub(r'\s+', '', rooms)
            # temp_str2 = rooms
            # if '房间' in rooms:
            #     temp_str2 = temp_str2.split('房间')
            #     num = int(temp_str2[0])
            #     temp_hide = temp_str2[1]
            #     flag = 1
            #     num1 = random.randint(1, 4)
            #     num2 = random.randint(1, 2)
            #
            #     while num1 + num2 != num:
            #         rooms = f'{num1}室{num2}厅' + temp_hide
            # # 室room 厅hall 浴室 bathroom
            # rooms = re.split(r'室', rooms)
            # room = rooms[0]
            # rooms = re.split(r'厅', rooms[1])
            # hall = rooms[0]
            # bathroom = rooms[1].split('卫')[0]
            buildingheight = i_all[len(i_all) - 1].next_sibling.replace(' ', '')
            buildingheight = buildingheight.split('（')[1].replace("）", '')
            # print(buildingheight)
        elif len(i_all)==4:
            area = complex.find(name='i').next_sibling
            area = re.sub(r'\s+', '', area)
            area = re.split(r'㎡', area)[0]
            direction = i_all[1].next_sibling
            direction=re.sub(r'\s+','',direction)
            if len(direction)>2:
                num=random.randint(0,3)
                direction=directions[num]
            rooms = i_all[len(i_all) - 2].next_sibling
            rooms = re.sub(r'\s+', '', rooms)
            print(rooms)
            # temp_str2 = rooms
            # if '房间' in rooms:
            #     temp_str2 = temp_str2.split('房间')
            #     num = int(temp_str2[0])
            #     temp_hide = temp_str2[1]
            #     flag = 1
            #     num1 = random.randint(1, 4)
            #     num2 = random.randint(1, 2)
            #
            #     while num1 + num2 != num:
            #         rooms = f'{num1}室{num2}厅' + temp_hide
            # # 室room 厅hall 浴室 bathroom
            # rooms = re.split(r'室', rooms)
            #
            # room = rooms[0]
            # print(rooms)
            # rooms = re.split(r'厅', rooms[1])
            # hall = rooms[0]
            # bathroom = rooms[1].split('卫')[0]
        else:
            area = complex.find(name='i').next_sibling
            area = re.sub(r'\s+', '', area)
            area = re.split(r'㎡', area)[0]
        try:
            buildingheight = i_all[len(i_all) - 1].next_sibling.replace(' ', '')
            buildingheight = buildingheight.split('（')[1].split('）')[0]
        except IndexError:
            buildingheight='10层'
        # 优势advantage
        advantage = item.find(name='p', attrs={'class': 'content__list--item--bottom oneline'})
        # 住宿条件   housecondition,condition
        houseconditions = advantage.find_all(name='i')
        condition = ''
        for housecondition in houseconditions:
            # 个体 individual
            for individual in housecondition:
                condition += individual.text
        houseconditions=condition
        # print(direction,buildingheight,condition)
        header=['title','price','src','address','area','direction','buildingheight','condition','rooms']
        data=[title,price,src,address,area,direction,buildingheight,condition,rooms]
        with open('data.txt','a+',encoding='utf-8',newline='') as f:
            writer=csv.writer(f)
            writer.writerow(data)
        # # sql='insert into lianjia(title,price,img,address,area,direction,buildingheight,conditions) values({},{},{},{},{},{},{},{})'.format(title,price,src,address,area,direction,buildingheight,condition)
        # savedata.db_insert(sql)

    # 3.数据预处理
    # 4.保存数据
    time.sleep(10)
time.sleep(3)