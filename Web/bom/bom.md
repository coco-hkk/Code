# BOM
浏览器对象模型 BOM 可使 JavaScript 有能力与浏览器对话。

- [BOM](#bom)
- [Window 对象](#window-对象)
- [window 窗口操作](#window-窗口操作)
- [window 尺寸](#window-尺寸)
- [window 屏幕](#window-屏幕)
- [window location](#window-location)
- [window 历史](#window-历史)
- [window navigator](#window-navigator)
- [window 弹窗](#window-弹窗)
  - [警告框](#警告框)
  - [确认框](#确认框)
  - [提示框](#提示框)
- [window 计时](#window-计时)
- [cookie](#cookie)
  - [创建 cookie](#创建-cookie)
  - [读取 cookie](#读取-cookie)
  - [修改 cookie](#修改-cookie)
  - [删除 cookie](#删除-cookie)

# Window 对象
所有浏览器都支持 window 对象，它表示浏览器窗口。

所有 JavaScript 全局对象、函数以及变量均自动成为 window 对象的成员。

- 全局变量是 window 对象的属性。
- 全局函数是 window 对象的方法。

HTML DOM 的 document 也是 window 对象的属性之一：
```JavaScript
window.document.getElementById("header");
// 等价于
document.getElementById("header");
```

# window 窗口操作
```JavaScript
/** window 操作
 *  window.open()       打开新窗口
 *  window.close()      关闭当前窗口
 *  window.moveTo()     移动当前窗口
 *  window.resizeTo()   调整当前窗口的尺寸
 */
window.close();
```

# window 尺寸
```JavaScript
/** window 尺寸
 *  浏览器窗口的内部高度、宽度（包括滚动条）
 *  window.innerHeight
 *  window.innerWidth
 */
var width = window.innerWidth
         || document.documentElement.clientWidth
         || document.body.clientWidth;

var height = window.innerHeight
          || document.documentElement.clientHeight
          || document.body.clientHeight;
```

# window 屏幕
window.screen 对象包含有关用户屏幕的信息，在编写时可以不使用 window 前缀。

```JavaScript
/** window screen
 *  总宽度/高度     screen.width/screen.height
 *  可用宽度/高度   screen.availWidth/screen.availHeight
 *  色彩深度        screen.colorDepth
 *  色彩分辨率      screen.pixelDepth
 */
document.write("总宽度：" + screen.width + "\n" + "总高度" + screen.height);
```

# window location
window.location 对象用于获得当前页面的地址 URL，并把浏览器重定向到新的页面。可不使用 window 前缀。

```JavaScript
/** window location
 *  location.hostname   返回 web 主机的域名
 *  location.pathname   返回当前页面的路径和文件名
 *  location.port       返回 web 主机的端口
 *  location.protocol   返回所使用的 web 协议
 *  location.href       返回当前页面的 URL
 *  location.assign()   加载新的文档
 */
location.assign("http://www.baidu.com");
```

# window 历史
window.history 对象包含浏览器的历史，可不使用 window 前缀。

```JavaScript
/** window history
 *  history.back()      与在浏览器点击后退按钮相同
 *  history.forward()   向前按钮
 */
history.back();
```

# window navigator
window.navigator 对象包含有关访问者浏览器的信息，可不使用 window 前缀。

navigator 对象的信息具有误导性，不应该被用于检测浏览器版本。

```JavaScript
/** window navigator
 *  navigator.appCodeName       浏览器代号
 *  navigator.appName           浏览器名称
 *  navigator.appVersion        浏览器版本
 *  navigator.cookieEnabled     启用 Cookies
 *  navigator.platform          硬件平台
 *  navigator.userAgent         用户代理
 *  navigator.language          用户代理语言
 */
document.write("语言：" + navigator.language);
```

# window 弹窗
## 警告框
警告框常用于确保用户可以得到某些信息，当警告框出现后，用户需要点击确定按钮才能继续进行操作。

window.alert() 方法可以不带上 window 对象，直接使用 alert() 方法。

```JavaScript
window.alert("sometext");
```

## 确认框
确认框通常用于验证是否接受用户操作。当确认卡弹出时，用户可以点击 "确认" 或者 "取消" 来确定用户操作。

当你点击 "确认", 确认框返回 true， 如果点击 "取消", 确认框返回 false。

```JavaScript
window.confirm("sometext");
```

## 提示框
提示框经常用于提示用户在进入页面前输入某个值。当提示框出现后，用户需要输入某个值，然后点击确认或取消按钮才能继续操纵。

如果用户点击确认，那么返回值为输入的值。如果用户点击取消，那么返回值为 null。

```JavaScript
window.prompt("sometext", "defaultvalue");
```

# window 计时
```JavaScript
/** window.setInterval("JavaScript function", milliseconds)    间隔指定毫秒数不停地执行指定的代码
 *  window.clearInterval(intervalVariable)  停止 setInterval
 *  window.setTimeout("JavaScript function", milliseconds)     指定毫秒数后执行指定代码
 *  window.clearTimeout(intervalVariable)   停止 setTimeout
*/
// 定时每 3 秒弹出 alert
var myVar;
myVar=setTimeout(function(){alert("Hello")},3000);
// 清除定时
clearTimeout(myVar);
```

# cookie
JavaScript 可使用 document.cookie 属性来创建、读取及删除 cookie.

cookie 以 名/值对 形式存储，如 `username=coco-hkk`.

## 创建 cookie
```JavaScript
document.cookie = "username=cooc-hkk";
document.cookie = "username=coco-hkk; expires=Thu, 18 Dec 2013 12:00:00 GMT";
```

## 读取 cookie
```JavaScript
// document.cookie 以字符串的方式返回所有的 cookie，类型格式：cookie1=value; cookie2=value;
var x = document.cookie;
```

## 修改 cookie
```JavaScript
// 类似于创建 cookie，旧的 cookie 将被覆盖
document.cookie = "username=hkk";
```

## 删除 cookie
```JavaScript
// 当删除时不必指定 cookie 的值，expires 参数设置为以前的时间即可
document.cookie = "username=; expires=Thu, 01 Jan 1970 00:00:00 GMT";
```