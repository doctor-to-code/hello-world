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
x = int(input('輸入整數下限值'))
y = int(input('輸入整數上限值'))
#引入random概念
#random.randrange ([start,] stop [,step]) 分別為下限值, 上限值(不包含, 差值
#random.randint(start, stop)相當於random.randrange (start, stop + 1),
#random randint 不建議使用因為跟我們一般認知不同
import random
r = random. randrange(x, y)

i = 0
# 引入while True因為需要多次進入迴圈
while True:
    i += 1
    a = int(input('請輸入數字猜猜看'))
    if a == r:
        print('nice play')
        break
    elif a > r:
        print('smaller please')
    else:
        print('bigger please')
    print(f'this is {i} run')
if i > 7:
    print('you foolish')

