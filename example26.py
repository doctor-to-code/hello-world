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
#輸入一個數字n，將其重複n次，例如輸入3則得到1, 12, 123
k = int(input('輸入一個正整數'))
for i in range(1, k + 1):
    for num in range(1, i + 1):
        print(num, end='')
    print() #換行

#輸入一個數字n，將其重複n次，例如輸入3則得到1, 22, 333
k = int(input('輸入一個正整數'))
for i in range(k + 1):
    for num in range(1, i + 1):
        print(i, end='')
    print()
'''
print() 相當於 print('') 都是換行意思
print('\n')相當於一次換兩行

'''
k = int(input('輸入一個正整數'))
for i in range(k + 1):
    for num in range(1, i + 1):
        print(i, end='*')
    print('=', i ** i)
    print('\n') #一次換兩行