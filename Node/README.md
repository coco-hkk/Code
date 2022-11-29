# JavaScript
JavaScript 是一种轻量级的编程语言，可插入 HTML 页面的编程代码。

# Nodejs
[node.js](https://nodejs.org/en/) 是一个基于 Chrome V8 引擎的 JavaScript 运行环境，
使用事件驱动、非阻塞式 I/O 模型，让 JavaScript 运行在服务端的开发平台。

# 库模块
## lodash
## nodemon

## log4js
[log4js](https://github.com/log4js-node/log4js-node) 是 Node.js 日志管理工具。log4js分为6个输出级别，从低到高分别为trace、debug、info、warn、error、fatal。

## dotenv

## node-xlsx
[node-xlsx](https://www.npmjs.com/package/node-xlsx) 操作 Excel 文件。

```javascript
// npm 安装
npm install node-xlsx --save
// yarn 安装
yarn add node-xlsx
```

## tesseract.js
[tesseract.js](https://github.com/naptha/tesseract.js) 图片识别。
需要配合语言训练库，如 [eng](https://github.com/naptha/tessdata).

```js
// 代码地址: https://github.com/naptha/tesseract.js/blob/master/docs/examples.md#with-detailed-progress
const { createWorker } = require('tesseract.js');

const worker = createWorker({
    // 将语言训练库下载到目录 lang 中，这样避免 tesseract.js 联网下载
    langPath: './lang',
});

(async () => {
  await worker.load();
  await worker.loadLanguage('eng');
  await worker.initialize('eng');
  const { data: { text } } = await worker.recognize('./0.png');
  // text 即为识别内容
  console.log(text);
  await worker.terminate();
})();
```

# 日志模块
## logger-line-number
输出时间、文件名和行号。

安装 `yarn add logger-line-number`.

```js
const logger = require('logger-line-number')

logger.log('test')
//2021-02-03 13:28:30 test.js:3:8 [INFO] test

logger.error('error')
2021-02-03 13:28:30 test.js:3:8 [ERROR] error

logger.debug('debug')
//2021-02-03 13:28:30 test.js:3:8 [DEBUG] debug

logger.setLogType(logger.LOG_TYPES.NONE)  //禁用打印日志
logger.setLogType(logger.LOG_TYPES.ERROR)  //打印 错误 日志
logger.setLogType(logger.LOG_TYPES.NORMAL)  //打印 错误 消息 日志
logger.setLogType(logger.LOG_TYPES.DEBUG)  //打印 错误 消息 调试 日志
```