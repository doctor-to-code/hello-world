"""
Python 課程
Author: PY
Date: 2022/02/08
Location: 板橋
"""

print('hello, world', end='***')
print('goodbye')
print(125 - 5)
print(125 + 5)
print(125 * 5)
print(125 / 5)
print(125 // 6) # //是指整除部分
print(125 % 5) # %是求餘數意思
print(125 ** 5) #求冪次方125之5次方

#int是定義x 為整數，其中input是指讓使用者自訂義輸入數值，'輸入整數'這段是開發者想要給使用者提示
x = int(input('輸入整數'))
y = int(input('輸入整數'))
print(x + y)
print(x - y)
print(x / (y + 5))
print(y / x)
print(y // x)
print(x ** (y + 5))
print(x % (y + 2))
print(x ** y + 5)
student_age = 18
#變量命名有多個單詞連接時候用下滑線分隔，稱作snake case