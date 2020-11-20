python��������sort,sorted���б�������ֵ������е�Ӧ�����;���
 python �б�list��������һ��ʮ�����õ�������sort,sorted�������������б���������������ӡ�
a = [5,2,1,9,6]        
 
>>> sorted(a)                  #��a��С��������,��Ӱ��a����ṹ 
[1, 2, 5, 6, 9] 
 
>>> sorted(a,reverse = True)   #��a�Ӵ�С����,��Ӱ��a����ṹ 
[9, 6, 5, 2, 1] 
 
>>> a.sort()                   #��a��С��������,Ӱ��a����ṹ 
>>> a 
[1, 2, 5, 6, 9] 
 
>>> a.sort(reverse = True)     #��a�Ӵ�С����,Ӱ��a����ṹ 
>>> a 
[9, 6, 5, 2, 1] 
 
ע�⣬a.sort() �Ѹı���ṹ��b = a.sort() �Ǵ����д��! 

>>> b = ['aa','BB','bb','zz','CC'] 
>>> sorted(b) 
['BB', 'CC', 'aa', 'bb', 'zz']    #���б���Ԫ��ÿ����ĸ��ascii���С��������,���Ҫ�Ӵ�С,����sorted(b,reverse=True)��ͬ 
 
>>> c =['CCC', 'bb', 'ffff', 'z']  
>>> sorted(c,key=len)             #���б��Ԫ�صĳ������� 
['z', 'bb', 'CCC', 'ffff'] 
 
>>> d =['CCC', 'bb', 'ffff', 'z'] 
>>> sorted(d,key = str.lower )    #���б��е�ÿ��Ԫ�ر�ΪСд���ٰ�ÿ��Ԫ���е�ÿ����ĸ��ascii���С�������� 
['bb', 'CCC', 'ffff', 'z'] 
 
>>> def lastchar(s): 
       return s[-1] 
>>> e = ['abc','b','AAz','ef'] 
>>> sorted(e,key = lastchar)      #�Զ��庯������,lastcharΪ��������������������б�e��ÿ��Ԫ�ص����һ����ĸ 
['b', 'abc', 'ef', 'AAz']         #sorted(e,key=lastchar)���þ��� ���б�e��ÿ��Ԫ�ص����һ����ĸ��ascii���С�������� 
 
>>> f = [{'name':'abc','age':20},{'name':'def','age':30},{'name':'ghi','age':25}]     #�б��е�Ԫ��Ϊ�ֵ� 
>>> def age(s): 
       return s['age'] 
>>> ff = sorted(f,key = age)      #�Զ��庯�����б�f���ֵ��age��С��������  
 
[{'age': 20, 'name': 'abc'}, {'age': 25, 'name': 'ghi'}, {'age': 30, 'name': 'def'}] 
 
>>> f2 = sorted(f,key = lambda x:x['age'])    #����������涨��һ���������벻���ۣ�������lambda����ʽ�����庯��,Ч��ͬ�� 