## 数据结构基本概念

### 什么是数据结构？

1. 数据

> 数据即信息的载体，是能够输入到计算机中并且能被计算机识别、存储和处理的符号总称。

2. 数据元素

> 数据元素是数据的基本单位，又称之为记录（Record）。一般数据元素由若干基本项组成。   

3. 数据结构

> 数据结构指的是数据元素及数据元素之间的相互关系，或组织数据的形式。

### 数据之间的结构关系

1. 逻辑结构

> 表示数据之间的抽象关系（如邻接关系、从属关系等），按每个元素可能具有的直接前趋数和直接后继数将逻辑结构分为“线性结构”和“非线性结构”两大类。

2. 存储结构

> 逻辑结构在计算机中的具体实现方法，分为顺序存储方法、链接存储方法、索引存储方法、散列存储方法。

### 逻辑结构（关系）

1. 特点：

- 只是描述数据结构中数据元素之间的联系规律
- 是从具体问题中抽象出来的数学模型，是独立于计算机存储器的（与机器无关）

2. 逻辑结构分类

- 线性结构

> 对于数据结构课程而言，简单地说，线性结构是n个数据元素的有序（次序）集合。
>
> > - 集合中必存在唯一的一个"第一个元素"；
> > - 集合中必存在唯一的一个"最后的元素"；
> > - 除最后元素之外，其它数据元素均有唯一的"后继"；
> > - 除第一元素之外，其它数据元素均有唯一的"前驱"。

- 树形结构（层次结构）

> 树形结构指的是数据元素之间存在着“一对多”的树形关系的数据结构，是一类重要的非线性数据结构。在树形结构中，树根结点没有前驱结点，其余每个结点有且只有一个前驱结点。叶子结点没有后续结点，其余每个结点的后续节点数可以是一个也可以是多个。

- 图状结构（网状结构）

> 图是一种比较复杂的数据结构。在图结构中任意两个元素之间都可能有关系，也就是说这是一种多对多的关系。

- 其他结构

> 除了以上几种常见的逻辑结构外，数据结构中还包含其他的结构，比如集合等。有时根据实际情况抽象的模型不止是简单的某一种，也可能拥有更多的特征。

![逻辑结构](/home/tarena/leibo/data/img/data1.png)

### 存储结构（关系）

1. 特点：

- 是数据的逻辑结构在计算机存储器中的映象（或表示）
- 存储结构是通过计算机程序来实现的，因而是依赖于具体的计算机语言的。

2. 基础存储结构

- 顺序存储    

> 顺序存储（Sequential Storage）：将数据结构中各元素按照其逻辑顺序存放于存储器一片连续的存储空间中。

- 链式存储

> 链式存储（Linked Storage）：将数据结构中各元素分布到存储器的不同点，用记录下一个结点位置的方式建立它们之间的联系，由此得到的存储结构为链式存储结构。 

## 线性表

线性表的定义是描述其逻辑结构，而通常会在线性表上进行的查找、插入、删除等操作。
线性表作为一种基本的数据结构类型，在计算机存储器中的存储一般有两种形式，一种是顺序存储，一种是链式存储。

### 线性表的顺序存储

1. 定义

> 若将线性表L=(a0,a1, ……,an-1)中的各元素依次存储于计算机一片连续的存储空间，这种机制表示为线性表的顺序存储结构。

2. 特点

> - 逻辑上相邻的元素 ai, ai+1，其存储位置也是相邻的；
> - 存储密度高，方便对数据的遍历查找。
> - 对表的插入和删除等运算的效率较差。

3. 程序实现

> 在Python中，list存放于一片单一连续的内存块，故可借助于列表类型来描述线性表的顺序存储结构，而且列表本身就提供了丰富的接口满足这种数据结构的运算。

```python
>>>L = [1,2,3,4]
>>>L.append(10)      #尾部增加元素
L
[1, 2, 3, 4, 10]

>>>L.insert(1,20)    #插入元素
L
[1, 20, 2, 3, 4, 10]

>>>L.remove(3)       #删除元素
L
[1, 20, 2, 4, 10]     

>>>L[4] = 30         #修改
L
[1, 20, 2, 4, 30]

>>>L.index(2)        #查找
2
```

### 线性表的链式存储

1. 定义

> 将线性表L=(a0,a1,……,an-1)中各元素分布在存储器的不同存储块，称为结点，每个结点（尾节点除外）中都持有一个指向下一个节点的引用，这样所得到的存储结构为链表结构。

![链表结构](/home/tarena/leibo/data/img/data2.png)

2. 特点

> - 逻辑上相邻的元素 ai, ai+1，其存储位置也不一定相邻；
> - 存储稀疏，不必开辟整块存储空间。
> - 对表的插入和删除等运算的效率较高。
> - 逻辑结构复杂，不利于遍历。

3. 程序实现

  ***代码实现：  day1/linklist.py***

![节点](/home/tarena/.cache/.fr-P4aOYj/day01/link.png"链式节点")



```python3
"""
    功能:实现单链表的构建和操作
    重点代码
"""

# 创建节点类
class Node:
    """
    思路:* 自定义类是为节点类,类中的属性数据内容
        * 写一个next属性,用来和下一个节点建立关系
    """
    def __init__(self, val,next = None):
        """
        :param val: 有用数据
        :param next: 下一个节点引用
        """
        self.val = val
        self.next = next


# 链式线性表操作类
class LinkList:
    """
    思路: 生成单链表,通过实例化的对象就代表一个链表
          可以调用具体的操作方法完成各种功能
    """
    def __init__(self):
        # 链表的初始化节点,没有有用的数据,但是便于标记链表的开端.
        self.head = Node(None)
    # 初始化链表,添加一组节点
    def init_list(self, list_):
        p = self.head   # p 作为移动变量
        for i in list_:
            # 遍历到一个值就创建一个节点
            p.next = Node(i)
            p = p.next # 向后移动
    # 遍历链表
    def show(self):
        p = self.head.next
        while p is not None:
            print(p.val)
            p = p.next

    #　判断列表是否为空
    def is_emety(self):
        if self.head.next is None:
            return True # 空的
        return False # 不是空的
    #　清空列表
    def clear(self):
        self.head.next = None
    # 尾部插入
    def append(self,val):
        p = self.head
        # p移动到最后一个节点
        while p.next is not None:
        	p = p.next
        p.next = Node(val)
    # 头部插入
    def head_insert(self,val):
        node = Node(val)
        node.next = self.head.next
        self.head.next = node
    # 指定位置插入
    def insert(self,index,val):
        # 设置个p,移动到指定位置的前一个
        p = self.head
        for i in range(index):
            if p.next is None:
                break
            p = p.next
        #　插入节点
        node = Node(val)
        node.next = p.next
        p.next = node
    # 删除节点
    def remove(self,val):
        p = self.head
        # p移动,待删除节点上一个
        while p.next.val != val and p.next is not None:
            p = p.next
        if p.next is None:
            raise ValueError("x is not linklist")
        else:
            p.next = p.next.next
    # 获取木个节点的值(通过索引获取)
    def search(self, index=0):
        if index < 0:
            raise ValueError("index out of range")
        p = self.head.next
        # 循环移动p
        for i in range(index):
            if p is None:
                raise ValueError("index out of range")
            p = p.next
        return p.val


if __name__ == '__main__':
    # 链表对象
    link = LinkList()
    l = [1,2,3,4]
    link.init_list(l)
    # link.show()
    # link.clear()
    # link.insert(2,"laber")
    # link.show()
    print(link.search(3))
    # link.show()
```

