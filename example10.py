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

#真實邏輯運算實際案例
while True:
    a = int(input('請輸入數字'))
    if a == 0:
        break
    x1 = a > 50
    x2 = a % 4 == 0
    x3 = a ** 2 > 3000
    x4 = (x1 and x2)
    x5 = (x1 or x2)
    x6 = (not x2)
    x7 = (not x3)
    x8 = (not x6 and not x7)
    print(x1, x2, x3, x4, x5, x6, x7, x8)
