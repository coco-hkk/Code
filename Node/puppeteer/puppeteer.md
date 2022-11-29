# puppeteer
[Puppeteer](https://github.com/puppeteer/puppeteer) 是一个 Node 库，它提供了一整套高级 API，通过 DevTools 协议控制 Chromium 或 Chrome。

## puppeteer-core VS puppeteer
1. puppeteer 安装时会下载 Chromium，而 puppeteer-core 不会。
2. puppeteer-core 会忽略所有 puppeteer_* 环境变量，同时使用时需要提前保证环境中已经具有可执行的 Chromium.

## 防止自动化方式被检测
chrome 属性 `navigator.webdriver` 值为 `true` 表示浏览器正在由自动化程序操作。

```javascript
// 启动 chrome 时添加参数 --enable-automation
const browser = await puppeteer.launch({ignoreDefaultArgs: ["--enable-automation"]});
```

## 浏览器启动参数
参考[这里](https://peter.sh/experiments/chromium-command-line-switches/).
```js
const browser = await puppeteer.launch({
    headless: false, // 开启界面
    executablePath,  // 浏览器路径

    defaultViewport: null,                  // 设置视口尺寸
    args: ['--start-maximized',             // 浏览器最大化
           '--disable-notifications=true',  // 关闭浏览器弹出通知提示框
           '--window-size=1920, 1080',      // 设置浏览器窗口尺寸
           '--user-agent=xxx',              // 设置 UA
           '--blink-settings=imagesEnabled=false',  // 浏览器层面禁用图片加载
    ],

    ignoreDefaultArgs: ['--enable-automation'], // 防自动化被检测
  });
```

## 超时设置
默认时间为 30s.

```js
// 影响所有导航功能以及所有等待功能
// page.waitForFunction/waitForRequest/waitForResponse/waitForSelector/waitForXpath
page.setDefaultTimeout(60 * 1000);  // 默认单位为 ms，下同

// 影响所有导航功能
// page.goBack/goForward/goto/reload/setContent/waitForNavigation
page.setDefaultNavigationTimout(60 * 1000)
```

## cookie 登录及代理设置
```js
const dotenv = require('dotenv');

// 在当前目录中创建一个 .env 文件，将用户 session 粘贴到 .env 中
// 格式：SESSION='粘贴内容'
dotenv.config();

const {SESSION} = process.env;
page.setCookie({
    url: "URL",
    name: 'session',
    value: SESSION,
});

// 代理设置
page.setUserAgent("用户代理");
```

# 错误处理
1. Node is either not clickable or not an HTMLElement
- 使用参考不存在元素的脚本（错误的选择器）
- 使用参考不可见元素的脚本（正确的选择器但元素不可见）