#itertools模块 
_**返回的应该是个迭代器**_
>https://docs.python.org/2/library/itertools.html

product('ABCD', repeat=2)  
AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
***
permutations('ABCD', 2)	  
AB AC AD BA BC BD CA CB CD DA DB DC  
***
combinations('ABCD', 2)  
AB AC AD BC BD CD  
***
combinations_with_replacement('ABCD', 2)	 
AA AB AC AD BB BC BD CC CD DD
***

#bisect模块（进行一些二分插入）

>https://docs.python.org/3.7/library/bisect.html  
###只寻找插入位置
 - 返回一个仍保持有序的插入位置，尽可能靠左，即插入位置将有序列表分成两部分  
all of the left item < target <= all of the right item  
`bisect.bisect_left(sorted_list, target, lo=0, hi=len(a))`
-----
 - 返回一个仍保持有序的插入位置，尽可能靠左，即插入位置将有序列表分成两部分  
all of the left item <= target < all of the right item
```
bisect.bisect_right(sorted_list, target, lo=0, hi=len(a))   
bisect.bisect(a, x, lo=0, hi=len(a))
```
---
###二分寻找插入位置，线性进行插入操作
```
bisect.insort_left(a, x, lo=0, hi=len(a))
```
---
```
bisect.insort_right(a, x, lo=0, hi=len(a))    
bisect.insort(a, x, lo=0, hi=len(a))
```
---
###上述只是查找插入位置，对于常见的二分查找还得进行封装（还是解装，这谁知道）
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

