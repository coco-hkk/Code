# Nodejs
[node.js](https://nodejs.org/en/) 是一个基于 Chrome V8 引擎的 JavaScript 运行环境，
使用事件驱动、非阻塞式 I/O 模型，让 JavaScript 运行在服务端的开发平台。

## yarn
yarn 是 facebook 发布的一款取代 npm 的包管理工具。

### 安装
```bat
: 安装 yarn
npm install -g yarn
: 卸载 yarn
npm uninstall yarn -g
```

### 配置
```bash
# 初始化项目，同 npm init，会生成 package.json 文件
yarn init

# yarn 配置项
yarn config list            # 显示所有配置项
yarn config get <key>       # 显示某配置项
yarn config delete <key>    # 删除某配置项
yarn config set <key> <value> [-g|--global] # 设置配置项

# 安装包
yarn install         # 安装 package.json 里所有包，并将包及它的所有依赖项保存进 yarn.lock
yarn install --flat  # 安装一个包的单一版本
yarn install --force         # 强制重新下载所有包
yarn install --production    # 只安装 dependencies 里的包
yarn install --no-lockfile   # 不读取或生成 yarn.lock
yarn install --pure-lockfile # 不生成 yarn.lock

# 添加包（会更新 package.json 和 yarn.lock）
yarn add [package]              # 在当前的项目中添加一个依赖包，会自动更新到 package.json 和 yarn.lock 文件中
yarn add [package]@[version]    # 安装指定版本，这里指的是主要版本，如果需要精确到小版本，使用-E 参数
yarn add [package]@[tag]        # 安装某个 tag（比如 beta,next 或者 latest）

# 不指定依赖类型默认安装到 dependencies 里，你也可以指定依赖类型
yarn add --dev/-D       # 加到 devDependencies
yarn add --peer/-P      # 加到 peerDependencies
yarn add --optional/-O  # 加到 optionalDependencies

# 默认安装包的主要版本里的最新版本，下面两个命令可以指定版本：
yarn add --exact/-E     # 安装包的精确版本。例如 yarn add foo@1.2.3 会接受 1.9.1 版，但是 yarn add foo@1.2.3 --exact 只会接受 1.2.3 版
yarn add --tilde/-T     # 安装包的次要版本里的最新版。例如 yarn add foo@1.2.3 --tilde 会接受 1.2.9，但不接受 1.3.0

yarn publish            # 发布包
yarn remove <packageName>   # 移除一个包，会自动更新 package.json 和 yarn.lock
yarn upgrade                # 更新一个依赖：用于更新包到基于规范范围的最新版本
yarn run                    # 运行脚本：用来执行在 package.json 中 scripts 属性下定义的脚本
yarn info <packageName>     # 可以用来查看某个模块的最新版本信息

# 缓存
yarn cache 
yarn cache list     # 列出已缓存的每个包 
yarn cache dir      # 返回 全局缓存位置 
yarn cache clean    # 清除缓存
```

`yarn.lock` 不要手动修改，当使用一些操作如 yarn add 时，会自动更新。

### 命令
```bash
yarn -v             # 查看 yarn 版本
yarn config list    # 查看 yarn 配置
yarn config get registry # 查看当前 yarn 源

# 修改 yarn 源
yarn config set registry https://registry.npm.taobao.org

# yarn 安装依赖
yarn add 包名
yarn global add 包名

# yarn 卸载依赖
yarn remove 包名
yarn global remove 包名

# yarn 查看全局安装包
yarn global list
```

## 路径
```javascript
// __dirname：返回被执行的 js 所在目录的绝对路径
console.log(__dirname)
// __filename: 返回被执行的 js 绝对路径
console.log(__filename)
// process.cwd()：返回 js 所在目录的绝对路径
console.log(process.cwd())
// ./ 和 ../ 为相对路径
console.log('./')
// 相对路径可通过 path.resolve 转换为绝对路径
const path = require('path');
console.log(path.resolve('./'))

// 将多个路径片段拼接成完整的路径字符串，可正确识别不同系统路径分隔符
path.join('/a', '/b/c', '..d', 'e');    // \a\b\d\e

// 获取路径中文件名称部分
const fpath = '/a/b/c/index.html';
path.basename(fpath);   // index.html
path.basename(fpath, '.html');  // index

// 获取路径中文件的后缀名
path.extname(fpath); // .html

// 解析对象的路径为组成其的片段
path.parse(fpath);  // 输出一个字典
```

## 进程
Node 是单线程单进程的模式。

严格来说，node 并不是单线程的。node 中存在着多种线程，包括：
- js 引擎执行的线程
- 定时器线程 (setTimeout, setInterval)
- 异步 http 线程 (ajax)

node 的单线程是指 js 的引擎只有一个实例，且在 nodejs 的主线程中执行。

对于 CPU 密集型操作，在 node 中通过 child_process 可以创建独立的子进程。
父子进程通过 IPC 通信。

```js
// 启动子进程来执行 shell 命令，可以通过回调参数来获取脚本 shell 执行结果
// exec() 与 execfile() 在创建的时候可以指定 timeout 属性设置超时时间，一旦超时会被杀死
// 子进程执行的是非 node 程序，传入一串 shell 命令，执行后结果以回调的形式返回，与 execFile 不同的是 exec 可以直接执行一串 shell 命令。
child_process.exec(command[, options][, callback])

// 与 exec 类型不同的是，它执行的不是 shell 命令而是一个可执行文件
// 文件头部一定是 #!/usr/bin/env node
// 子进程中执行的是非 node 程序，提供一组参数后，执行的结果以回调的形式返回。
child_process.execfile(file[, args][, options][, callback])

// 仅仅执行一个 shell 命令，不需要获取执行结果
// 子进程中执行的是非 node 程序，提供一组参数后，执行的结果以流的形式返回。
child_process.spawn(command[, args][, options])

// 可以用 node 执行的。js 文件，也不需要获取执行结果。fork 出来的子进程一定是 node 进程
child_process.fork(modulePath[, args][, options])
```