itertools模块(https://github.com/Rosevil1874/LeetCode/tree/master/Python-Solution)  https://github.com/algorhythms/LeetCode  
=== 

_**返回的应该是个迭代器，每次的都是一个元组**_
>https://docs.python.org/3/library/itertools.html

- product('ABCD', repeat=2)  （放回抽样）  
AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
***
- permutations('ABCD', 2)	 （排列）   
AB AC AD BA BC BD CA CB CD DA DB DC  
***
- combinations('ABCD', 2)  （组合）  
AB AC AD BC BD CD  
***
- combinations_with_replacement('ABCD', 2)  	 
AA AB AC AD BB BC BD CC CD DD
***
- zip_longest(*iterables, fillvalue=None)  
一般的zip是最少原则，即有的列表迭代完了，就停止。但这个是最大原则，其他的不够，则用fillvalue来凑  
***
- accumulate(iterable,func=operator.add)  
    - func是一个二2一的函数，默认为加和函数，对序列进行二元迭代，返回一个迭代器
    - example：
        ```python
        import itertools
        list(itertools.accumulate([2,3,5,8],operator.mul))
        ```
    out:`[2,5,10,18]`
    - 返回的第一个元素为原序列的第一个元素
    -与reduce函数有点类似，但是reduce返回的是最终结果（一个值），而accumulate返回的是迭代器  
---
- count(start, step=1)
    - 返回一个迭代器（这个应该是配合break使用）

bisect模块（进行一些二分插入）
===
>https://docs.python.org/3.7/library/bisect.html  

###**只寻找插入位置**


  - 返回一个仍保持有序的插入位置，尽可能靠左，即插入位置将有序列表分成两部分  
     all of the left item < target <= all of the right item  
     ```python 
     bisect.bisect_left(sorted_list, target, lo=0, hi=len(a))
     ```
     
  - 返回一个仍保持有序的插入位置，尽可能靠右，即插入位置将有序列表分成两部分  
      all of the left item <= target < all of the right item
  ```
  bisect.bisect_right(sorted_list, target, lo=0, hi=len(a))   
  bisect.bisect(a, x, lo=0, hi=len(a))
  ```
***

###**二分寻找插入位置，线性进行插入操作**

```
bisect.insort_left(a, x, lo=0, hi=len(a))
```

```
bisect.insort_right(a, x, lo=0, hi=len(a))    
bisect.insort(a, x, lo=0, hi=len(a))
```
---
###**上述只是查找插入位置，对于常见的二分查找还得进行封装（还是解装，这谁知道）**

```python
def index(sorted_list, target):
    '''
    output:return the left location if find else False
    '''
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    return False
```

字符串的一些操作
===
- split（str,num）
  - 传入两个参数，第一个参数表示分隔符，第二个参数表示分割次数,返回List[str]  
  - 例: 
        `"a.bb.c.d".split(".",2)`  
       返回 ['a', 'bb', 'c.d']，即列表length等于num+1
  - 对于重复的分割，例`"a...b..c.d".split(".")`
    返回 ['a', '', '', 'b', '', 'c', 'd']  
    即默认会在相邻分割字串中添加""这个空字符
  - 对于不填参数，则默认用空白分隔符（不限长度的），所以可用作单词切割  
    例`"  a    bb c   dd     ".split()` 返回['a', 'bb', 'c', 'dd']
    
      
functools模块 
===
>https://docs.python.org/3.7/library/functools.html
1. **reduce(function, iterable[, initializer])**
   - function是一个二2一的函数，然后在iterable上一直迭代至结束即可，initializer是一个初始化参数，可以没有
   - example：
   ```python
   def mul(a,b):
       return a*b
   reduce(mul,range(1,6))
   
   out: 120 # 即5的阶乘
   ```
   `reduce(mul,range(1,6),5) # out: 600` 
    
2. **cmp_to_key(func)** 
   - 接受一个比较函数，返回一个key类型的函数，其实是一个排序参数旧接口与新接口的转换  
   那么问题来了，什么是比较函数：接受两个参数，返回负数（表示小于），零（表示等于）正数（表示大于）  
   - example：  
    ```python
     from math import sin  
     from functools import cmp_to_key
     def my_cmp(a,b):
         return sin(a)-sin(b)  
     iterable=[1,2,3,4,5,6]
     sorted(iterable, key=cmp_to_key(my_cmp))
      
     Out: [5, 4, 6, 3, 1, 2]
   ```
        
     - 个人理解：  
        - 新接口key：将所有元素映射为一个值作为代表，然后对代表进行排序  
        - 旧接口cmp：两两比较，类似于冒泡排序（实际底层应该不是冒泡排序）     
              
3. **lru_cache(maxsize=128, typed=False)** 
    - 一个装饰器，可进行函数结果的缓存，对于会重复调用的函数，可以省大量的时间（比如Fibonacci sequence）  
    - maxsize参数：设置为2的倍数，设置为None，则不限制（应该是直到内存爆），type置True，那么f(3)和f(3.0)会存两个缓存条目
    - example:
    ```python
       @lru_cache(maxsize=None)
       def fib(n):
           if n < 2:
               return n
           return fib(n-1) + fib(n-2)
       [fib(i) for i in range(20)]
    
   out:略略
   ```
   ```
       fib.cache_info()
   out:CacheInfo(hits=36, misses=20, maxsize=None, currsize=20) #显示命中，未命中，maxsize以及currsize
   ``` 
   `fib.cache_clearn()    #清空缓存`
 
读写文件
===
1. 读写pkl  <https://docs.python.org/3/library/pickle.html>
	- 支持python的原生容器和其他（相信自己你用不上的），可嵌套
	- example
		```python
		import pickle

		original_data = [("大江"), (), (), {}, {1: "东去", 3: 4}]

		with open('data.pkl', 'wb') as f:
			pickle.dump(original_data, f)

		with open('data.pkl', 'rb') as f:
			new_data = pickle.load(f)
		print(new_data)
		```
	- 经测试发现，后缀名可以自定义。但是最好规范下使用".pkl" or ".pickle"
2. 读写json文件
	- 其实就是字典文件  
	    ```python
	    # TODO:

        ```        
代码规范
===
1. **TODO and FIXME**
    - TODO注释应该在所有开头处包含”TODO”字符串,
    - 紧跟着是用括号括起来的你的名字, email地址或其它标识符.
    - 然后是一个可选的冒号. 接着必须有一行注释, 解释要做什么. 
    - example:   
         `# TODO(freelikeff): what you want to do `
    - TODO表示未完成准备做，FIXME表示代码有误，需要修改
***
进制转换
===
1. **int(x, base=10)**
	- 将一个base进制的字符串转化为十进制的数
	- example
	`int("20",3)`  意为将三进制数20转化为十进制数返回，即返回6。
	- 注意：
		- 字符串可开始于'+' or '-',前后可以有空格。例 `int(" -20 ",3)`,返回-6
		- 若base进制，那么字符串中的字符必须小于base， 
		其中 a 到 z （或 A 到 Z ）表示 10 到 35，大小写可以混用
		- 2、8、16 进制的数字可以在代码中用 0b/0B 、 0o/0O 、 0x/0X 前缀来表示。
		那么就不要用base参数了（或者置base=0精确解释字符串）。别混用!
		
2. **bin(x),oct(dec)，hex(x)**
	- 将整数x转化为以"0b"('0o','0x')开始的二(八，十六)进制数的字符串形式
	- example `bin(-8)` 返回"-0b1000",只能传入整数
	- 如果要获取浮点数的十六进制字符串形式，请使用 float.hex() 方法。（**别想太多只有十六进制可以**）
	
3. **chr(i)**
	- 传入整数，返回字符。映射关系为Unicode，例如`chr(8364)` 返回'€'(谁知道这是个什么鬼符号)
	- 实参的合法范围是 0 到 1,114,111（16 进制表示是 0x10FFFF）
	
4. **ord(char)** 
	- 对表示单个 Unicode 字符的字符串，返回代表它 Unicode 码点的整数。
	例如 `ord('€')` ）返回 8364 。这是 chr() 的逆函数。
	
5. **exec()**
	- 传入一个字符串，则会当做代码执行
	- example：
	```python
	class A:
    	pass

	exec(r"a=A()")
	print(a)
	```
	out`<__main__.A object at 0x000002534A7AE320>`

6. **eval()**
	- 传入一个字符串，则会当做代码运行并有返回值
	- example：
	```python
	class A:
    	pass

	a=eval(r"A()")
	print(a)
	```
	out`<__main__.A object at 0x000002534A7AE320>`
	
	 _**如果经过以上的对比还看不出差别，我&trade; **_

7. **compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)**
	- 上两个是这个比的情人，我也不想写了

8. **divmod(a, b)**
	- 返回（商，余数）这个元组
	-唉，和我想的有点不一样
	```python
	-4//3
	Out[2]: -2
	```
9. **filter(function, iterable)**
	- function为一个返回T or F的函数，过滤掉iterable中的F，返回一个迭代器
	
random module 
===
1. <https://docs.python.org/zh-cn/3/library/random.html>    

2. **Warning:The pseudo-random generators of this module should not be used for security purposes.  
 For security or cryptographic uses, see the `secrets` module.**(说的我好想用得到似的)

3. **random.randrange(srart,stop,step)**  
	- 在[start,start+step,start+2step,···，且到但是不包含stop的数列中随机取一个数  
	- 只输入一个值，那么相当于传入(srart=0,stop=inpt,step=1)  
	- 只输入两个值，那么就不用多BB了吧。  

4. **random.randint(a:int, b:int)**  
	- 返回[a,b]闭区间的一个随机整数  

5. **random.choice(seq)**  
	- 从序列seq中随机选择一个元素（seq不能为空）  

6. **random.choices(population, weights=None, cum_weights=None, k=1)**  
	- 放回重复抽样  
	- weights为相对权重，cum_weights为累积权重  
	- weights=[5,10,3,2],等价于cum_weights=[5,15,18,20]  

7. **random.sample(population, k)**  
	- 不放回抽样  
	- 结果不一定按照原来的顺序  

8. **random.shuffle(x)**
	- 将序列x就地打乱  
	- 如果对于不可变序列，需要返回一个打乱的副本，那么请使用     
	 `random.sample(x, kx=len(x))`
	 
9. **实值分布**
    - random.random()
        - 返回[0,1)中的均匀分布的浮点数
    - random.gauss(mu, sigma)
        - 高斯分布 mu均值，sigma标准差
---

np.random模块  #TODO
===

    
***
pysnooper模块
===
- 用于debug
- ```python 
    import pysnooper


    @pysnooper.snoop("./snooper.log")
    def numbers2bits(number):
        if number:
            bits = []
            while number:
                number, remainder = divmod(number, 2)
                bits.insert(0, remainder)
            return bits
        return [0]

    numbers2bits(6)
    ```
    out:
    ```
    Starting var:.. number = 4
    08:57:00.991927 call         5 def numbers2bits(number):
    08:57:00.992927 line         6     if number:
    08:57:00.992927 line         7         bits = []
    New var:....... bits = []
    08:57:00.992927 line         8         while number:
    08:57:00.992927 line         9             number, remainder = divmod(number, 2)
    New var:....... remainder = 0
    Modified var:.. number = 2
    08:57:00.992927 line        10             bits.insert(0, remainder)
    Modified var:.. bits = [0]
    08:57:00.992927 line         8         while number:
    08:57:00.992927 line         9             number, remainder = divmod(number, 2)
    Modified var:.. number = 1
    08:57:00.992927 line        10             bits.insert(0, remainder)
    Modified var:.. bits = [0, 0]
    08:57:00.992927 line         8         while number:
    08:57:00.992927 line         9             number, remainder = divmod(number, 2)
    Modified var:.. number = 0
    Modified var:.. remainder = 1
    08:57:00.992927 line        10             bits.insert(0, remainder)
    Modified var:.. bits = [1, 0, 0]
    08:57:00.992927 line         8         while number:
    08:57:00.992927 line        11         return bits
    08:57:00.992927 return      11         return bits
    Return value:.. [1, 0, 0]
    ```
***
#python d的多元赋值
leetcode的206题反转链表，有一段代码
```python 
class Solution3:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp, front = head, None
        while temp:
            front, front.next, temp = temp, front, temp.next
        return front
``` 
倒数第二行
- 个人认为是这样的，先创建右边的临时变量，然后一个一个一个的赋给左边，也就是说，右边的不会变，左边的会变
- 过程：
    - 开始时temp=head,front=None
    - 然后右边为 head(的一个引用)，None，第二个节点的一个引用
    - 一一赋给左边，即front变为head(的一个引用)，然后front.next即head.next变为None，temp又贴到的第二个节点上
    
    	 
# 返回的列表有可能是个引用
```python
def test(nums1, f):
    if f:
        return nums1
    return [2, 3, 4, 5]


a = [1, 2, 3, 4, 5]
ans = test(a,1)
print(ans)
a[1]=9
print(ans)
```
out
```python
[1, 2, 3, 4, 5]
[1, 9, 3, 4, 5]
```
	 
#collections
###ChainMap	 
- 这个类初始化的时候可以传入多个字典，然后会将这些字典依次放入一个列表中
- 也可以当做一个字典来进行增删改查
    - 增：在第一个字典中增
    - 删：在第一个字典中删，如果没有那么会报错
    - 改：第一个字典有，那么就是改，第一个字典没有，那么就是增
    - 查，这个会依次去查，直到找到
- 有一个maps属性,其实就是一个列表，元素是字典
- new_child方法，传入一个字典，放在开头，生成了一个新的ChainMap类
- parents属性，去掉第一个字典，生成了一个新的ChainMap类
- 对于上述，所有相关的字典，全部指向内存的同一块，改一个地方，那么都会进行修改

---
###Counter
- 初始化时候传入一个序列，可以进行技术统计，可以看做是一个字典的子类
    - ```c=Counter(a=2,b=-4)```
    - 这行代码相当于传入{"a":2,"b":-4}
- 当做字典做查询的时候，找不到键会返回0，而不是报错
- elements方法，返回一个迭代器，按照首次出现顺序输出，重复计数次，如果计数小宇1，那么会忽略
- most_common(n)方法，返回一个元组的列表，元组表示元素and计数，按照计数值从大到小的前n个，计数值相等的元素按首次出现的顺序排序
- subtract([iterable-or-mapping]) ，做减法
- update([iterable-or-mapping])，做加法
- 二元运算加减法直接在Counter上做则会忽略掉非正数
- &则会取min(c[x], d[x])，|则会取max(c[x], d[x])，同样忽略掉非正数
---
###Deque(双端队列)
- list也能模拟，但是在左边进行进出则是线性级，但是双端队列是常数级
- 初始化的时候传入一个迭代器，可以指定最大长度，如果添加的时候长度已经满了，那么就会从另一端出队一个元素
- 方法
    - append(x)
    - appendleft(x)
    - clear()
    - copy()创建一份浅拷贝。
    - count(x)
    - extend(iterable)扩展deque的右侧，通过添加iterable参数中的元素。
    - extendleft(iterable)扩展deque的左侧，通过添加iterable参数中的元素。注意，左添加时，在结果中iterable参数中的顺序将被反过来添加。
    - index(x[, start[, stop]])
    - insert(i, x) 在位置 i 插入 x 。如果插入会导致一个限长deque超出长度 maxlen 的话，就升起一个 IndexError 。
    - pop() 移去并且返回一个元素，deque最右侧的那一个。如果没有元素的话，就升起 IndexError 索引错误。
    - popleft() 移去并且返回一个元素，deque最左侧的那一个。如果没有元素的话，就升起 IndexError 索引错误。
    - remove(value) 移去找到的第一个 value。 如果没有的话就升起 ValueError 。
    - reverse() 将deque逆序排列。返回 None 。
    - rotate(n=1) 向右循环移动 n 步。 如果 n 是负数，就向左循环。如果deque不是空的，向右循环移动一步就等价于 d.appendleft(d.pop()) ， 向左循环一步就等价于 d.append(d.popleft()) 。
    - 索引查询（个人推测其实底层是个双向链表，所以在两段索引查询是常数，但是查询中间则是线性）
- 属性
    - 一个只读属性，maxlen
	 
	 
