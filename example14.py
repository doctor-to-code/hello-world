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

username = input('請輸入使用者名稱:')
password = input('請輸入密碼:')
if username == 'fgdeeerry' and password == 'fgdeerry':
    print('登錄成功，歡迎使用餘額查詢系統，請進行下一步操作')
    x = float(input('請輸入網域密碼'))
    if x != 0:
        print('您的網域密碼為', x, '顯示餘額為', x * 100, '感謝使用餘額查詢系統')
    else:
        print('已退出系統，感謝您的使用')
else:
    print('登錄失敗，請確認帳號密碼是否有誤')
    print('已退出系統，感謝您的使用')
