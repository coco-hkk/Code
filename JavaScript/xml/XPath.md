XPath 是一门在 XML 文档中查找信息的语言。

- [XPath](#xpath)
- [XPath 节点](#xpath-节点)
  - [XPath 术语](#xpath-术语)
  - [节点关系](#节点关系)
- [XPath 语法](#xpath-语法)
  - [选取节点](#选取节点)
  - [选取未知节点](#选取未知节点)
  - [选取若干路径](#选取若干路径)
  - [谓语(Predicates)](#谓语predicates)

# XPath
#### XPath 路径表达式
XPath 使用路径表达式来选取 XML 文档中的节点或者节点集。这些路径表达式和我们在常规的电脑文件系统中看到的表达式非常相似。

#### XPath 标准函数
XPath 含有超过 100 个内建的函数。这些函数用于字符串值、数值、日期和时间比较、节点和 QName 处理、序列处理、逻辑值等等。

#### XPath 在 XSLT 中使用
XPath 是 XSLT 标准中的主要元素。

#### XPath 是 W3C 标准
XPath 被设计为供 XSLT、XPointer 以及其他 XML 解析软件使用。

# XPath 节点
## XPath 术语
#### 节点
在 XPath 中，有七种类型的节点：元素、属性、文本、命名空间、处理指令、注释以及文档（根）节点。

XML 文档是被作为节点树来对待的。树的根被称为文档节点或者根节点。

```XML
<!-- 例一 -->
<?xml version="1.0" encoding="UTF-8"?>

<bookstore>
  <book>
    <title lang="en">Harry Potter</title>
    <author>J K. Rowling</author>
    <year>2005</year>
    <price>29.99</price>
  </book>
</bookstore>
```

XML 文档中的节点例子：
```text
<bookstore> (文档节点)

<author>J K. Rowling</author> (元素节点)

lang="en" (属性节点)
```

#### 原子值(Atomic value)
原子值是无父或无子的节点。

#### 项目(Item)
项目是原子值或者节点。

## 节点关系
#### 父(Parent)
每个元素以及属性都有一个父。

例一中，book 元素是 title、author、year 以及 price 元素的父。

#### 子(Children)
元素节点可有零个、一个或多个子。

例一中，title、author、year 以及 price 元素都是 book 元素的子。

#### 同胞(Sibling)
拥有相同的父的节点。

例一中，title、author、year 以及 price 元素都是同胞。

#### 先辈(Ancestor)
某节点的父、父的父，等等。

例一中，title 元素的先辈是 book 元素和 bookstore 元素。

#### 后代(Descendant)
某个节点的子，子的子，等等。

例一中，bookstore 的后代是 book、title、author、year 以及 price 元素。

# XPath 语法
```xml
<!-- 例二 -->
<?xml version="1.0" encoding="UTF-8"?>
 
<bookstore>
 
<book>
  <title lang="eng">Harry Potter</title>
  <price>29.99</price>
</book>
 
<book>
  <title lang="eng">Learning XML</title>
  <price>39.95</price>
</book>
 
</bookstore>
```

## 选取节点
XPath 使用路径表达式来选取 XML 文档中的节点或节点集。节点是通过沿着路径 (path) 或者步 (steps) 来选取的。

|  表达式  | 描述                                                                     |
| :------: | ------------------------------------------------------------------------ |
| nodename | 选取此节点的所有子节点。                                                 |
|    /     | 从根节点选取（取子节点）。                                               |
|    //    | 从匹配选择的当前节点选择文档中的节点，而不考虑它们的位置（取子孙节点）。 |
|    .     | 选取当前节点。                                                           |
|    ..    | 选取当前节点的父节点。                                                   |
|    @     | 选取属性。                                                               |

例二中的路径表达式及其结果：
| 路径表达式      | 结果                                                                                     |
| --------------- | ---------------------------------------------------------------------------------------- |
| bookstore       | 选取 bookstore 元素的所有子节点。                                                        |
| /bookstore      | 选取根元素 bookstore，假如路径起始于正斜杠( / )，则此路径始终代表到某元素的绝对路径！    |
| bookstore/book  | 选取属于 bookstore 的子元素的所有 book 元素。                                            |
| //book          | 选取所有 book 子元素，而不管它们在文档中的位置。                                         |
| bookstore//book | 选择属于 bookstore 元素的后代的所有 book 元素，而不管它们位于 bookstore 之下的什么位置。 |
| //@lang         | 选取名为 lang 的所有属性。                                                               |

## 选取未知节点
XPath 通配符可用来选取未知的 XML 元素。

| 通配符 | 描述                 |
| ------ | -------------------- |
| *      | 匹配任何元素节点。   |
| @*     | 匹配任何属性节点。   |
| node() | 匹配任何类型的节点。 |

例二中的路径表达式及其结果：
| 路径表达式   | 结果                              |
| ------------ | --------------------------------- |
| /bookstore/* | 选取 bookstore 元素的所有子元素。 |
| //*          | 选取文档中的所有元素。            |
| //title[@*]  | 选取所有带有属性的 title 元素。   |

## 选取若干路径
通过在路径表达式中使用"|"运算符，您可以选取若干个路径。

例二中的路径表达式及其结果：
| 路径表达式                   | 结果                                       |
| ---------------------------- | ------------------------------------------ |
| //book/title \| //book/price | 选取 book 元素的所有 title 和 price 元素。 |
| //title      \| //price      | 选取文档中的所有 title 和 price 元素。     |

## 谓语(Predicates)
谓语用来查找某个特定的节点或者包含某个指定的值的节点。

谓语被嵌在方括号中。

| 路径表达式                          | 结果                                                                                      |
| ----------------------------------- | ----------------------------------------------------------------------------------------- |
| /bookstore/book[1]                  | 选取属于 bookstore 子元素的第一个 book 元素。                                             |
| /bookstore/book[last()]             | 选取属于 bookstore 子元素的最后一个 book 元素。                                           |
| /bookstore/book[last()-1]           | 选取属于 bookstore 子元素的倒数第二个 book 元素。                                         |
| /bookstore/book[position() < 3]     | 选取最前面的两个属于 bookstore 元素的子元素的 book 元素。                                 |
| //title[@lang]                      | 选取所有拥有名为 lang 的属性的 title 元素。                                               |
| //title[@lang='eng']                | 选取所有 title 元素，且这些元素拥有值为 eng 的 lang 属性。                                |
| /bookstore/book[price>35.00]        | 选取 bookstore 元素的所有 book 元素，且其中的 price 元素的值须大于 35.00。                |
| /bookstore/book[price>35.00]//title | 选取 bookstore 元素中的 book 元素的所有 title 元素，且其中的 price 元素的值须大于 35.00。 |