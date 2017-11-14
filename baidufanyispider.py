#coding=utf-8
import requests
import json
import sys

class BaiduFanyi:
    def __init__(self,query_string):
        #1.url
        self.query_string = query_string
        self.trans_url = "http://fanyi.baidu.com/v2transapi"
        self.headers= {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"}

    def get_post_data(self): #2.post data
        post_data = {
            "from":"zh",
            "to":"en",
            "query":self.query_string,
            "transtype":"translang",
            "simple_means_flag":"3"
        }
        return post_data

    def parse_url(self,post_data,url="http://fanyi.baidu.com/v2transapi"): #3.发送请求,获取响应
        response = requests.post(url,data=post_data,headers=self.headers)
        return response.content.decode()

    def get_trans_ret(self,json_response):#4.提取数据
        dict_response = json.loads(json_response)
        ret = dict_response["trans_result"]["data"][0]["dst"]
        print(ret)

    def run(self):
        #1.url
        #2.post data
        post_data = self.get_post_data()
        #3.发送请求,获取响应
        json_response = self.parse_url(post_data)
        #4.提取数据
        self.get_trans_ret(json_response)

if __name__ == '__main__':
    query_string = sys.argv[1]
    fanyi = BaiduFanyi(query_string)
    fanyi.run()
