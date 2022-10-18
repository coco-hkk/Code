```bat
:: 初始化 vue 项目，并安装 vue
npm init vue
cd <your-project-name>
npm install

:: 运行 vue 项目，在浏览器打开本地网址查看效果
npm run dev

:: 打包上线，打包文件在 dist 目录中
npm run build

:: 运行打包后的项目
:: 安装 yarn, npm install yarn g
:: yarn 安装全局包 yarn global add express-generator
:: 安装 express-generator
npm install express-generator -g

:: 创建 express 项目
express project_name

:: 安装项目依赖
cd project_name
npm install

:: 将 dist 目录中的内容全部复制到 public 目录下
:: 运行 project_name  项目，打开浏览器访问本地网址，端口号 3000
npm start
```