selenium 版本 4.4.3.

- [Selenium 基础](#selenium-基础)
  - [设置 Options](#设置-options)
  - [设置 Service](#设置-service)
  - [获取 webdriver](#获取-webdriver)
  - [打开网页](#打开网页)
  - [打开新的标签页和窗口](#打开新的标签页和窗口)
  - [执行 js 代码](#执行-js-代码)
  - [切换 iframe](#切换-iframe)
  - [模拟按键](#模拟按键)
- [问题集锦](#问题集锦)
  - [异常](#异常)
    - [ElementClickInterceptedException](#elementclickinterceptedexception)
    - [UnexpectedAlertPresentException](#unexpectedalertpresentexception)
- [其它](#其它)

# Selenium 基础
## 设置 Options
```python
options = Options()
# 操作已打开的浏览器
# 启动 chrome 浏览器时，启动参数和配置一致：--remote-debugging-port=9527 --user-data-dir="D:\zidonghua_test"
options.add_experimental_option("debuggerAddress", "127.0.0.1:9527")
```

## 设置 Service
```python
# 设置 chromedriver.exe 路径
chromedriver = "/path/to/chromedriver.exe"
service = Service(chromedriver)

# 隐藏 chromedriver 运行时的黑窗口
service.creationflags = CREATE_NO_WINDOW
```

## 获取 webdriver
```python
browser = webdriver.Chrome(service=service, options=options)
```

## 打开网页
```python
browser.get("www.baidu.com")
```

## 打开新的标签页和窗口
```python
# 打开一个新的 window，并切换过去打开新网页
browser.switch_to.new_window('window')
browser.get('https://opensource.saucelabs.com/')

# 打开一个新的 tab，并切换过去打开新网页
browser.switch_to.new_window('tab')
browser.get('https://opensource.saucelabs.com/')
```

## 执行 js 代码
```python
# 使用 return 获取值 play_speed 为视频播放速度
js_code = "return document.querySelector('video').playbackRate"
play_speed = browser.execute_script(js_code)

# 设置值，将视频播放速度设置为 2 倍
js_code = "document.querySelector('video').playbackRate = 2.0"
browser.execute_script(js_code)

# 点击按钮
button_js = 'document.getElementsByClassName("jbox-button")[0].click()'
browser.execute_script(button_js)
```

## 切换 iframe
```python
# 切换到 iframe
browser.switch_to.frame('jbox-iframe')

# 切换回父 frame
browser.switch_to.default_content()
```

## 模拟按键
```python
webdriver.ActionChains(browser).move_to_element(click_btn).click().perform()
```

# 问题集锦
driver 表示浏览器句柄。

## 异常
### ElementClickInterceptedException
点击元素失败。

```python
# 解决方法一
element = driver.find_element(By.ID, 'id')
driver.execute_script("arguments[0].click();", element)

# 解决方法二
element = driver.find_element(By.ID, 'id')
webdriver.ActionChains(driver).move_to_element(element).click(element).perform()
```

### UnexpectedAlertPresentException
这个异常应该是 alert 一直不出现，导致无法确认 alert。

#### 确认或取消 alert

```python
WebDriverWait(driver, 5).until(EC.alert_is_present()).dismiss()
WebDriverWait(driver, 5).until(EC.alert_is_present()).accept()
```

# 其它
#### 驱动及本地服务类异常
1. 未找到响应的浏览器驱动
```
WebDriverException: Message: 'geckodriver' executable needs to be in PATH.
或
WebDriverException: Message: 'chromedriver' executable needs to be in PATH.

原因:     查找不到对应的浏览器驱动
解决方法: 下载浏览器对应版本的 chromedriver 或 geckodrivergeckodriver
          放到脚本当前文件夹下或将路径配置到环境变量中, 或放到Python目录的scripts下(一般情况下Python的scripts目录在环境变量中), 或使用浏览器选项options指定驱动路径
```

2. 未找到浏览器
```
WebDriverException: Message Can not connect to the Service chromedriver
org.openqa.selenium.WebDriverException: Failed to connect to binary FirefoxBinary

原因:     在默认路径下未找到Firefox浏览器
解决方法: 重新安装Firefox浏览器
```

3. 驱动和浏览器不匹配
```
SessionNotCreatedException: Message: session not created:
this version of ChromeDriver only supports Chrome version 76

原因:     当前使用chromedriver只支持Chrome76版本
解决方法: 查看本地Chrome浏览器的版本, 下载对应的chromedriver
```

4. 驱动被防火墙拦截
```
WebDriverException: Message: Can not connect to the Service IEDriverServer.exe

原因:     iedriverserver.exe 被防火墙拦截
解决方法: 防火墙设置允许
```

5. 连接不上chromedriver服务
```
WebDriverException: Message: Can not connect ot the Service chromedriver

原因:    脚本通过 127.0.0.1 这个 ip 访问本地chromedriver服务, hosts中未配置 127.0.0.1指向localhost
解决办法: 配置本地 hosts, 添加:127.0.0.1 localhost
```

7. 远程服务器异常
```
RemoteDriverServerException:

解决方法: 确认webdriver.Remote()中的远程Webdriver服务是否OK
```

8. Webdriver服务器响应异常
```
ErrorInResponseException: 

解决方法, 根据具体报错信息分析
```

#### 找不到类异常: 定位/获取属性/切换警告框,frame, 窗口
1. NoSuchElementException: 找不到元素, 解决方法: 前面加上sleep等待后重试,或换一种定位方式
2. NoSuchAttributeException: 元素没有这个属性, 解决方法: 确认定位到的元素是否目标元素, 检查属性拼写
3. NoalertPresentException：没有找到alert弹出框, 解决方法: 观察页面,查看是否有弹框出现, 加上等待或作为偶现元素处理
4. NoSuchframeException：没有找到指定的frame或iframe, 解决方法: 查看拼写或切换使用frame的id/name/index/定位到的frame
5. NoSuchWindowException: 没找到窗口句柄指定的窗口, 解决方法: 查看使用的窗口句柄变量拼写
6. UnexpectedalertPresentException: 出现了弹框而未处理, 解决方法: 切换到警告框并处理, 如果偶现,使用try...except处理偶现弹框
7. InvalidSwitchToTargetException: 切换到指定frame或窗口报错, 解决方法: 查看相应的frame或窗口是否能定位到
8. UnexpectedTagNameException: 使用Tag Name不合法, 解决方法: 检查拼写或使用css selector/xpath
9. TimeoutException：查找元素或操作超时, 解决方法, 稍后重试

#### 元素操作异常类: 隐藏/不可操作状态
1. ElementNotVisibleException：元素不可见异常, selenium不能直接操作隐藏元素, 解决方法: 加上等待, 使用正常步骤使元素显示, 或使用js找到该元素的祖先节点的隐藏属性(通常为styple="display: none"), 移除该属性然后定位操作.
2. StaleElementReferenceException: 陈旧元素引用异常, 页面刷新或跳转后使用了之前定位到的元素, 解决方法: 重新定位元素并操作
3. InvalidElementStateException: 元素状态异常 元素只读/不可点击等, 解决方法, 等待或使用js移除元素readonly/disable等限制属性后操作
4. ElementNotSelectableException：元素不可被选中, 解决方法: 确认原始是否为select标签, 是否禁用
5. InvalidSelectorException: 使用的定位方法不支持或xpath语法错误, 未返回元素, 解决方法: 检查使用的元素定位器是否拆包, 使用find_element()方法是, 第一个参数为'class name', 'link text', 'particial link text' 'css selector', 空格分开, 非下划线连接, 建议使用By.CLASS_NAME的方式. 使用chrome开发着工具+Ctrl+F搜索验证自己写的xpath语法.
6. MoveTargetOutOfBoundsException: 使用ActionChains的move方法时移动到的位置不合适

#### cookie 存取相关异常
1. InvalidcookieDomainException: cookie相应的域名无效
2. UnableToSetcookieException: 设置cookie异常

#### IME输入法引擎异常
1. ImeNotAvailableException: 服务器不支持输入法
2. ImeActivationFailedException: 输入法激活异常