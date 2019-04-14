itertools模块
=== 
_**返回的应该是个迭代器**_
>https://docs.python.org/2/library/itertools.html

- product('ABCD', repeat=2)  
AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
***
- permutations('ABCD', 2)	  
AB AC AD BA BC BD CA CB CD DA DB DC  
***
- combinations('ABCD', 2)  
AB AC AD BC BD CD  
***
- combinations_with_replacement('ABCD', 2)  	 
AA AB AC AD BB BC BD CC CD DD
***
- zip_longest(*iterables, fillvalue=None)  
一般的zip是最少原则，即有的列表迭代完了，就停止。但这个是最大原则，其他的不够，则用fillvalue来凑  
***
bisect模块（进行一些二分插入）
===
>https://docs.python.org/3.7/library/bisect.html  
- 只寻找插入位置

  - 返回一个仍保持有序的插入位置，尽可能靠左，即插入位置将有序列表分成两部分  
     all of the left item < target <= all of the right item  
     ```bisect.bisect_left(sorted_list, target, lo=0, hi=len(a))```
     -----
  - 返回一个仍保持有序的插入位置，尽可能靠左，即插入位置将有序列表分成两部分  
      all of the left item <= target < all of the right item
  ```
  bisect.bisect_right(sorted_list, target, lo=0, hi=len(a))   
  bisect.bisect(a, x, lo=0, hi=len(a))
  ```
---

- 二分寻找插入位置，线性进行插入操作

```
bisect.insort_left(a, x, lo=0, hi=len(a))
```
---
```
bisect.insort_right(a, x, lo=0, hi=len(a))    
bisect.insort(a, x, lo=0, hi=len(a))
```
---
上述只是查找插入位置，对于常见的二分查找还得进行封装（还是解装，这谁知道）
---
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
1. reduce(function, iterable[, initializer])
   - function是一个二2一的函数，然后在iterable上一直迭代至结束即可，initializer是一个初始化参数，可以没有
   - example：
   ```python
   def mul(a,b):
       return a*b
   reduce(mul,range(1,6))
   
   out: 120 # 即5的阶乘
   ```
   `reduce(mul,range(1,6),5) # out: 600`  
2. cmp_to_key(func)  
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
              
3. lru_cache(maxsize=128, typed=False) 
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
    
   out:略
   ```
   ```
       fib.cache_info()
   out:CacheInfo(hits=36, misses=20, maxsize=None, currsize=20) #显示命中，未命中，maxsize以及currsize
   ``` 
   `fib.cache_clearn()    #清空缓存`
 
            