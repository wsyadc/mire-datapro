import os
import dashscope
import json
import argparse
from tqdm import tqdm
import random


# list_class=["实物拍摄","商品头图","商品详情页截图","下单过程中出现异常","订单详情页面","支付页面","评论区截图页面","物流列表页面","物流跟踪页面","物流异常页面","退款页面","退货页面","店铺页面","活动页面","优惠券领取页面","账户页面","投诉举报页面","平台介入页面","其他类别图片"]
# print("总类数{}\n".format(len(list_class)))
# for i in range(len(list_class)):
#     file_name = "E:\\天池比赛\\tianchi\\train\\reasonbyQwen72b\\save_train_{}.json".format(list_class[i])
#     with open(file_name, 'r',encoding="utf-8") as train_file:
#         train_data = json.load(train_file)
#         print("{}推理得到的总数为:{}\n".format(list_class[i],len(train_data)))

list_class=["商品详情页截图"]
print("总类数{}\n".format(len(list_class)))
for i in range(len(list_class)):
    file_name = "E:\\天池比赛\\tianchi\\train\\reasonbyQwen72b\\save_train_{}.json".format(list_class[i])
    with open(file_name, 'r',encoding="utf-8") as train_file:
        train_data = json.load(train_file)
        print("{}推理得到的总数为:{}\n".format(list_class[i],len(train_data)))
    
