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

#如果是float則使用%f當作佔位符號，如果是int則使用%d當作佔位符號
x1 = float(input("請輸入x值="))
y2 = float(input("請輸入y值="))
print('%f + %f = %f' % (x1 , y2, x1 + y2))
print('%f - %f = %f' % (x1 , y2, x1 - y2))
print('%f * %f = %f' % (x1, y2, x1 * y2))
print('%f / %f = %f' % (x1 , y2, x1 / y2))
print('%f // %f = %f' % (x1 , y2, x1 // y2))
print('%f %% %f = %f' % (x1 , y2, x1 % y2))
print('%f ** %f = %f' % (x1 , y2, x1 ** y2))
print('%f %% %f = %f' % (x1 , y2, x1 % y2))

#如果是float則使用%f當作佔位符號，如果是int則使用%d當作佔位符號
x2 = int(input("請輸入x值="))
y3 = int(input("請輸入y值="))
print('%d + %d = %d' % (x2 , y3, x2 + y3))