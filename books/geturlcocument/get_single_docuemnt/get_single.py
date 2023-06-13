from geturlcocument.get_document import get_page
import re
# 初始数据
pictures=[]
names=[]
authors=[]
prices=[]
scores=[]
sums=[]
def get_single():
    # 网址地址
    urls = [f"https://book.douban.com/top250?start={num}" for num in range(0,250,25)]
    for url in urls:
        # 获取对应的网页文本
        text = get_page.get_page(url)
        # 所有数据的集合
        all_tr = text.find_all(name="tr", attrs={"class": "item"})
        # 查找每个单项
        for tr in all_tr:
            # 数据类型：图片，书名，作者，价格，评分，简介
            # 图片
            picture = tr.find(name="img")
            picture = picture.get('src')
            # print(picture)
            # 书名
            div = tr.find(name='div', attrs={'class': 'pl2'})
            name = div.find('a').text
            name = re.sub(r'\s+', '', name)
            # 作者
            author = tr.find(name='p', attrs={'class': 'pl'}).text
            author = author.split('/')[0]
            # 价格
            price = author.split('/')[-1]
            price = re.sub(r'元', '', price)
            # 评分
            score = tr.find(name='span', attrs={'class': 'rating_nums'}).text
            try:
                sum = tr.find(name='span', attrs={'class': 'inq'}).text
            except AttributeError:
                sum = ''
            pictures.append(picture)
            names.append(name)
            authors.append(author)
            prices.append(price)
            scores.append(score)
            sums.append(sum)
    data = {
        "picture": pictures,
        "name": names,
        "author": authors,
        "price": prices,
        "score": scores,
        "sum": sums
    }
    return data

