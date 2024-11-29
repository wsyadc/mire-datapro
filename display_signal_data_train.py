#根据输入的id显示图片和instructions

import json
from PIL import Image
import os
import matplotlib.pyplot as plt
def clear_screen():
    # 根据操作系统选择清屏命令
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Unix/Linux/MacOS
        os.system('clear')
file_name = "E:\\天池比赛\\tianchi\\train\\train.json" #改为自己的路径
excel_nums = input("输入需要标注的序号:")
with open(file_name, 'r',encoding="utf-8") as train_file:
    train_data = json.load(train_file)
    for data_i in train_data:
         if data_i['id']==excel_nums:

            print("id:{}\n".format(data_i['instruction']))
            print("训练集标签:{}\n".format(data_i["output"]))
            image_paths = []
            for j in range(len(data_i['image'])):
                    image_paths.append(data_i['image'][j])
            print("有{}张图片:{}\n".format(len(image_paths),image_paths))

            for i in range(len(image_paths)):
                image_path = image_paths[i]
                image = Image.open(image_path)
                image.show()




    
