import smtplib
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

class MySMTP():
    def __init__(self, from_addr, password, smtp_server, to_addr, msg):
        """smtp 配置

        Args:
            from_addr: 发送邮箱
            password: 授权码
            smtp_server: smtp 服务器地址
            to_addr: 接收邮箱
            msg: 邮件内容
        """
        self.from_addr = from_addr
        self.password = password
        self.smtp_server = smtp_server
        self.to_addr = to_addr.copy()
        self.msg = msg

def format_addr(str):
    """格式化字符串"""
    name, addr = parseaddr(str)
    return formataddr((Header(name, 'utf-8').encode(), addr))

def qq_smtp(to_receiver, message):
    """定义 QQ 邮箱的邮件内容"""
    from_sender = "XXX@qq.com"
    # 授权码
    passwd = "XXX"
    smtp_server = "smtp.qq.com"

    # 初始化 QQ 邮箱实例
    info = MySMTP(from_sender, passwd, smtp_server, to_receiver, message)
    return info

def sina_smtp(to_receiver, message):
    """定义 Sina 邮箱的邮件内容"""
    from_sender = "web_msg@sina.com"
    # 授权码
    passwd = "03adcf714fxxxx"
    smtp_server = "smtp.sina.com"

    # 初始化 QQ 邮箱实例
    info = MySMTP(from_sender, passwd, smtp_server, to_receiver, message)
    return info

def mail_content():
    # 通用-定义收件人，以列表形式保存
    receiver = ["hkkdlut@sina.cn"]

    # 通用-定义邮件正文内容
    msg1 = MIMEText("hello, send by Python...", 'plain', 'utf-8')
    msg2 = MIMEText('<html><body><h1>Hello</h1>' +
        '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
        '</body></html>', 'html', 'utf-8')

    # 定义带附件的邮件内容
    msg3 = MIMEMultipart()
    msg3.attach(msg2)

    # 测试文件需修改
    file_name = 'test.jpg'
    with open(file_name, 'rb') as f:
        # 设置附件的MIME和文件名，这里是jpg类型:
        mime = MIMEBase('image', 'jpg', filename=file_name)
        # 加上必要的头信息:
        mime.add_header('Content-Disposition', 'attachment', filename=file_name)
        mime.add_header('Content-ID', '<0>')
        mime.add_header('X-Attachment-Id', '0')
        # 把附件的内容读进来:
        mime.set_payload(f.read())
        # 用Base64编码:
        encoders.encode_base64(mime)
        # 添加到MIMEMultipart:
        msg3.attach(mime)

    # 带附件 TXT
    msg4 = MIMEMultipart()
    msg4.attach(msg1)
    # 测试文件需修改
    file_name = 'test.txt'

    att1 = MIMEText(open(file_name, 'rb').read(), 'base64', 'utf-8')
    att1.add_header('Content-Disposition', 'attachment', filename=file_name)
    att1.add_header('Content-ID', '<0>')
    att1.add_header('Content-Type', 'application/octet-stream')
    att1.add_header('X-Attachment-Id', '0')
    msg4.attach(att1)

    #确定到底使用哪个 msg
    msg = msg4

    info_send = sina_smtp(receiver, msg)

    #通用-定义与发送邮件部分
    msg['From'] = format_addr('Python <%s>' % info_send.from_addr)
    msg['To'] = format_addr('测试 <%s>' % ",".join(info_send.to_addr))
    msg['Subject'] = Header('Python 自动发送', 'utf-8').encode()

    return info_send

def send_email():
    # 获取邮件相关信息
    info_send = mail_content()

    try:
        # 连接 smtp 服务器，25 为 SMTP 端口号
        if info_send.smtp_server == "smtp.qq.com":
            server = smtplib.SMTP_SSL(info_send.smtp_server, 465)
            server.starttls()
        elif info_send.smtp_server == "smtp.sina.com":
            server = smtplib.SMTP(info_send.smtp_server, 25)

        # 打印出和 SMTP 服务器交互的所有信息
        # server.set_debuglevel(1)

        # 登录邮箱
        server.login(info_send.from_addr, info_send.password)

        # 发送邮件
        if type(info_send.msg) == type("string"):
            server.sendmail(info_send.from_addr, info_send.to_addr, info_send.msg)
        elif type(info_send.msg) != type("string"):
            server.sendmail(info_send.from_addr, info_send.to_addr, info_send.msg.as_string())

        print ("邮件发送成功")
        server.quit()
    except smtplib.SMTPException as e:
        print ("Error: 无法发送邮件", e)

if __name__ == '__main__':
    send_email()