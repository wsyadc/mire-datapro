#随机从训练数据中抽取100条数据，看一下正确率有多少
import os
import dashscope
import json
import argparse
from tqdm import tqdm
import random

def parse_args():
    parser = argparse.ArgumentParser(description="Detect span")
    parser.add_argument(
        "--file_name",
        type=str,
        default=''
    )
    parser.add_argument(
        "--save_path",
        type=str,
        default=''
    )
    parser.add_argument(
        "--start_id",
        type=str,
        default=''
    )
    parser.add_argument(
        "--end_id",
        type=str,
        default=''
    )
    args = parser.parse_args()
    return args    

args = parse_args()
file_name = "E:\\天池比赛\\tianchi\\train\\train.json"
save_path="E:\\天池比赛\\tianchi\\train\\save_train_pictureinfo_0_1.json"
start_id = 310
end_id = 400
print("start_id:{},end_id{}".format(start_id,end_id))
with open(file_name, 'r',encoding="utf-8") as train_file:
    train_data = json.load(train_file)

with open(save_path, 'w',encoding="utf-8") as writer:
    acc_nums  = 0
    for i in tqdm(range(int(start_id),int(end_id)+1)):
        prompt ="""
# 你是一个电商领域识图专家,可以理解消费者上传的软件截图或实物拍摄图。

# 你的任务是: 
    首先用一句话概括图片，之后将图片中的文字信息以简洁的描述方式呈现，避免冗长的解释，仅列出最重要和明显的细节。

# 消费者上传的图片如下所示:

"""
        check_str = "现在,请你对消费者上传的图片进行分类。你只需要回答图片分类结果"
        if check_str in train_data[i]['instruction']:    
            messages = [
                {
                    "role": "user",
                    "content": [
                        {"text": prompt}]+
                        [
                        {"image": train_data[i]['image'][j]} for j in range(len(train_data[i]['image']))
                    ]
                }
            ]
            print(train_data[i]["id"])
            print("\n")
            response = dashscope.MultiModalConversation.call(
                # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key="sk-xxx",
                api_key='sk-5db6132db02e4528ad286bbdab49e1d0',
                model='qwen-vl-max',
                messages=messages
                )
            print(response)
            single_json_data = {
                "id": train_data[i]['id'],
                "image": train_data[i]['image'],
                "output": train_data[i]['output'],
                "picture2text": response['output']['choices'][0]['message']['content'][0]['text']
            }
            writer.write(json.dumps(single_json_data, ensure_ascii=False) + ',\n')
            writer.flush()
        else:
            single_json_data = {
                "id": train_data[i]['id'],
                "image": train_data[i]['image'],
                "output": train_data[i]['output'],
                "picture2text": ""

            }
            writer.write(json.dumps(single_json_data, ensure_ascii=False) + ',\n')
            writer.flush()


