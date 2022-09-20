"""解析 html 页面

作者：coco-hkk
日期：2022年9月9日
"""
from html.parser import HTMLParser

# 需要自定义处理页面流程
class MyHTMLParser(HTMLParser):
    def __init__(self):
        """初始化一些标志位，用于定位具体元素"""
        HTMLParser.__init__(self)
        
        # 标签标志位
        self.in_table = None
        self.in_td = None
        # 保存 table 标签中的内容
        self.table_content = []
        # 保存某个标签的内容
        self.line = []

        self.in_p = None
        self.paragrah = ""


    def _attr(self, attrlist, attrname):
        """获取标签属性值
        
        Args:
            attrlist: 标签的所有属性，一般是 handle_starttag 中的 attrs 参数
            attrname: 指定标签属性
        Returns:
            返回指定属性的值，若没有则返回 None
        """
        for attr in attrlist:
            if attr[0] == attrname:
                return attr[1]
        return None

    def handle_starttag(self, tag, attrs):
        # 改变标签标志位，初始化数据
        if tag == 'p' and self._attr(attrs, 'id') == '1':
            self.in_p = True

        # 开始进入 table 标签，没有其它定位标志(id, class 或其它)，可能会分析不同的 table
        if tag == 'table':
            # 配置标志位
            self.in_table = True

        # 开始进入 td 标签
        if tag == 'td' and self.in_table is True:
            # 配置标志位
            self.in_td = True
            # 数据存储初始化
            self.line = []

    def handle_endtag(self, tag):
        # 这里重置标志位，数据扫尾
        # 退出 td 标签，一定要检查当前 tag 是否是 td
        if self.in_td is True and tag == 'td' and self.line:
            # 重置标志位
            self.in_td = None
            # 数据扫尾工作
            self.table_content.append(self.line)

        # 退出 table 标签
        if self.in_table is True and tag == 'table':
            self.in_table = None

        # 退出 p 标签
        if tag == 'p' and self.in_p is True:
            # 重置标志位
            self.in_p = None 

    def handle_data(self, data):
        # 这里的 data 是标签间的文本内容
        # data 属于哪个标签，需要通过自己配置标志位确定，这个函数本身没有其它参数指定标签
        # 这里还是只处理数据，不要改变标签标志位
        if self.in_td is True:
            data = data.strip()
            self.line.append(data)

        if self.in_p is True:
            data = data.strip()
            self.paragrah = data

    # 自定义函数
    def get_table_content(self):
        return self.table_content

    def get_paragraph(self):
        return self.paragrah

if __name__ == '__main__':
    parser = MyHTMLParser()

    # 打开 html 页面
    with open('test.html', 'r', encoding='utf-8') as f:
        file = f.read()

    # 加载 html 页面
    parser.feed(file)

    content = parser.get_table_content()
    print(content)

    content = parser.get_paragraph()
    print(content)
