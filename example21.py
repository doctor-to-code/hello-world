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
#找出100-999水仙花數有幾個以及總和，例如153= 1 ** 3 + 5 ** 3 + 3 ** 3就是水仙花數
for i in range(100, 1000):
    x = i // 100
    z = i % 10
    y = i // 10 % 10
    if i == x ** 3 + y ** 3 + z ** 3:
        print(i)
