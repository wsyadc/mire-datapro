#共23个类，商品详情页截图推理完成了，商品分类选项不做，剩下21个类

# 选择推理模式
#选择应用的prompt类型(1、模型自由推理(不给模型类别信息)，要求推理格式。2、给出图片类别信息，3、给出图片类别信息并要求模型推理字数在100以内：
infer_model=3
# 0..6  7..13 14..20 
for i in {14..20}
do 

  # 在后台执行每个 Python 程序
  python E:\\天池比赛\\tianchi\\TrainSet_Enhancement\\Qwen_72B_class_reason_para.py \
        --infer_model $infer_model \
        --class_type $i &
done

# 等待所有后台任务完成
wait
