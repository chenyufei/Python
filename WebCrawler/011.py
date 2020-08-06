import requests #导入需要的包
import json

#search = input("请输入你要翻译的内容:")

url = "https://fanyi.baidu.com/#en/zh/desk" #请求的地址
headers = {
    'Referrer Policy': 'no-referrer-when-downgrade',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-Mode': 'navigate',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN, zh;q=0.9',
    'Upgrade_insecure-Requests': str(1),
    'Connection': 'keep-alive',
    'User-Agent': 'Chrome/78.0.3904.97 Safari/537.36'
}

response = requests.get(url=url, headers=headers)#模拟请求

#获取response的数据有2种方式 一种是text获取的直接是文本格式 但是可能有乱码 需要手动设置response.encoding("编码") 解决乱码
#还有一种就是response.content 里面存的是网站直接返回的数据 二进制格式 然后通过decode解码即可
#因为返回的是json对象，所以我们将最后解码后的字符串进行json格式转换 使用json.loads()进行转换
print(response.text)

#然后我们可以通过格式化工具进行json的解析
#print("单词:{0} 翻译:{1}".format(search,json_data["data"]["st_tag"]))