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
#三角形形成計算器:
while True:
    a = float(input('三角形邊長a'))
    b = float(input('三角形邊長b'))
    c = float(input('三角形邊長c'))
    x1 = a + b > c
    x2 = b + c > a
    x3 = a + c > b
    y = (x1 and x2 and x3)
    if y == True:
        print('可組成三角形')
    else:
        print('無法組成三角形')

