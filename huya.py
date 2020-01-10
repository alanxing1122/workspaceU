import requests# 
from lxml import etree # 数据预处理
from urllib import request #下载图片
import time #让爬虫不容易被发现，延时

def huya_spider():
    #请求地址
    url = 'https://www.huya.com/g/4079'

    headers = {
        'User-agent' :'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
    }
    response = requests.get(url,headers=headers)
    print(response) 
    #<Response [200]> 请求成功 3开头重定向 4开头请求有错误 5开头服务器端内部有问题
    data_txt = response.text
    #print(data_txt)
    
    data = etree.HTML(data_txt)

    friends_list = data.xpath('//img[@class="pic"]')

    #print(friends_list)
    for friend in friends_list:
        img = friend.xpath('./@data-original')[0]
        #print(img)

        img = img.split('?')[0]
        print(img)
        name = '昱凯喜欢的'+friend.xpath('./@alt')[0]

        request.urlretrieve(img,'E:/python/project/friends/' +name+'.jpg')
        
        print('<%s>下载完毕'%name)

        #防反爬
        time.sleep(2)
huya_spider()