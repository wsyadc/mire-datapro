file_name=E:\\天池比赛\\tianchi\\train\\train.json
check_class=("实物拍摄" "商品头图" "商品详情页截图" "下单过程中出现异常" "订单详情页面" "支付页面" "评论区截图页面" "物流列表页面" "物流跟踪页面" "物流异常页面" "退款页面" "退货页面" "换货页面" "购物车页面" "店铺页面" "活动页面" "优惠券领取页面" "账户页面" "投诉举报页面" "平台介入页面" "外部APP截图" "其他类别图片")
i=0
for class in "${check_class[@]}";
do
  save_path=E:\\天池比赛\\tianchi\\train\\reasonbyQwen72b\\save_train_${class}.json
  save_path=$(echo "$save_path" | sed 's/[[:space:]]/_/g' | sed 's/(/_/g' | sed 's/)/_/g')
  # 在后台执行每个 Python 程序
  python E:\\天池比赛\\tianchi\\TrainSet_Enhancement\\Qwen_72B_class_reason.py \
        --file_name $file_name \
        --save_path "$save_path" \
        --class_label "$class" &
done

# 等待所有后台任务完成
wait
