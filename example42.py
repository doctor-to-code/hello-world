"""
Python 課程
Author: PY
Date: 2022/02/09
Location: 板橋

//                       _oo0oo_
//                      o8888888o
//                      88" . "88
//                      (| -_- |)
//                      0\  =  /0
//                    ___/`---'\___
//                  .' \\|     |// '.
//                 / \\|||  :  |||// \
//                / _||||| -:- |||||- \
//               |   | \\\  -  /// |   |
//               | \_|  ''\---/''  |_/ |
//               \  .-\__  '-'  ___/-. /
//             ___'. .'  /--.--\  `. .'___
//          ."" '<  `.___\_<|>_/___.' >' "".
//         | | :  `- \`.;`\ _ /`;.`/ - ` : | |
//         \  \ `_.   \_ __\ /__ _/   .-` /  /
//     =====`-.____`.___ \_____/___.-`___.-'=====
//                       `=---='
//
//
//     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//               佛祖保佑         永無BUG

"""
nums = []
for _ in range(10):
    temp = int(input('請輸入數字')) #讓這個自訂義List只能配合輸入10次
    nums.append(temp)
Mean_value = sum(nums) / len(nums)

for num in nums:
    total = 0
    total += (num - Mean_value) ** 2
    variation = total / len(nums)
    standard_variation = variation ** 0.5

Max_Value, Mini_Value = max(nums), min(nums)

print('字串為', nums)
print('平均為', Mean_value)
print('標準差為', standard_variation)
print('最大值為', Max_Value)
print('最小值為', Mini_Value)
