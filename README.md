# LeetCode
LeetCode 刷题

#### 下面是小技巧整理

#### 1、operator 模块
```python
# 要介绍的三个小函数
from operator import itemgetter, attrgetter, methodcaller
```

(1)、itemgetter
```python
dct = {'B': 2, 'A': 1, 'G': 0}
max(dct)  # 默认按键比较
max(dct.items(), key=lambda x: x[1])  # 如果要比较值通常这样写

# 如果使用itemgetter, 可以用如下方式比较值  
max(dct.items(), key=itemgetter(1))
```

```python
# 另外itemgetter还可以根据给定的下标列表来获取元素
itemgetter(1, 3, 5)('ABCDEFG')  # 返回 ('B', 'D', 'F')
itemgetter(3, 4, 1)(('m0', 'm1', 'm2', 'm3', 'm4', 'm5'))  # 返回 ('m3', 'm4', 'm1')

# 上面写法等同于我们常规如下写法
[('ABCDEFG')[i] for i in (1, 3, 5)]
map(lambda x: ('ABCDEFG')[x], (1, 3, 5))
```

(2)、attrgetter
```python
class MyCls():
    name = 'Alice'
    age = 20
    _class = '计算机科学-172'
    hobby = ['movie', 'music']

attrgetter('name', 'age')(MyCls)  # 返回 ('Alice', 20)
```

(2)、methodcaller
```python
replace = methodcaller('replace', ' ', '-')
print(replace('I am OK!'))  # 返回 I-am-OK!
```