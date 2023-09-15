'''
print(100>30)
a_name='小明'
b_name='小花'
print(a_name+b_name)
'''
# sentense="my name's 'lihua'"
# print(sentense.title())
'''
print(sentense.upper())
a=int(input('input the first num:'))#input 输入的为字符串
print(type(a))
b=int(input('input the second num:'))
print(a+b)
'''
'''
for value in range(1,5):
    print(value)
cars=['a','b','c','d','e']
for a in cars:
    print(a.title()+' that is great!')
print("i like them")
'''
'''
squares=[]
for value in range(1,11):
    squares.append(value**2)
print(squares)
'''
'''
player=['a','b','c','d']
print(player[1:2])
print(player[:])
'''
'''
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
'''
#banned_users = ['andrew', 'carolina', 'david']
#user = 'marie'
#if user not in banned_users:
#   print(user.title() + ", you can post a response if you wish.")
'''
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))
# 向右移动外星人
# 据外星人当前速度决定将其移动多远
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
# 新位置等于老位置加上增量
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))
print(type(x_increment))
'''
user_0 = {
'username': 'efermi',
'first': 'enrico',
'last': 'fermi',
}
for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)