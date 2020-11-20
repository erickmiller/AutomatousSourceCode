python的排序函数sort,sorted在列表排序和字典排序中的应用详解和举例
 python 列表list中内置了一个十分有用的排序函数sort,sorted，它可以用于列表的排序，以下是例子。
a = [5,2,1,9,6]        
 
>>> sorted(a)                  #将a从小到大排序,不影响a本身结构 
[1, 2, 5, 6, 9] 
 
>>> sorted(a,reverse = True)   #将a从大到小排序,不影响a本身结构 
[9, 6, 5, 2, 1] 
 
>>> a.sort()                   #将a从小到大排序,影响a本身结构 
>>> a 
[1, 2, 5, 6, 9] 
 
>>> a.sort(reverse = True)     #将a从大到小排序,影响a本身结构 
>>> a 
[9, 6, 5, 2, 1] 
 
注意，a.sort() 已改变其结构，b = a.sort() 是错误的写法! 

>>> b = ['aa','BB','bb','zz','CC'] 
>>> sorted(b) 
['BB', 'CC', 'aa', 'bb', 'zz']    #按列表中元素每个字母的ascii码从小到大排序,如果要从大到小,请用sorted(b,reverse=True)下同 
 
>>> c =['CCC', 'bb', 'ffff', 'z']  
>>> sorted(c,key=len)             #按列表的元素的长度排序 
['z', 'bb', 'CCC', 'ffff'] 
 
>>> d =['CCC', 'bb', 'ffff', 'z'] 
>>> sorted(d,key = str.lower )    #将列表中的每个元素变为小写，再按每个元素中的每个字母的ascii码从小到大排序 
['bb', 'CCC', 'ffff', 'z'] 
 
>>> def lastchar(s): 
       return s[-1] 
>>> e = ['abc','b','AAz','ef'] 
>>> sorted(e,key = lastchar)      #自定义函数排序,lastchar为函数名，这个函数返回列表e中每个元素的最后一个字母 
['b', 'abc', 'ef', 'AAz']         #sorted(e,key=lastchar)作用就是 按列表e中每个元素的最后一个字母的ascii码从小到大排序 
 
>>> f = [{'name':'abc','age':20},{'name':'def','age':30},{'name':'ghi','age':25}]     #列表中的元素为字典 
>>> def age(s): 
       return s['age'] 
>>> ff = sorted(f,key = age)      #自定义函数按列表f中字典的age从小到大排序  
 
[{'age': 20, 'name': 'abc'}, {'age': 25, 'name': 'ghi'}, {'age': 30, 'name': 'def'}] 
 
>>> f2 = sorted(f,key = lambda x:x['age'])    #如果觉得上面定义一个函数代码不美观，可以用lambda的形式来定义函数,效果同上 