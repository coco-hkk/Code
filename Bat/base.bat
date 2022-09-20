:: 作者：coco-hkk
:: 日期：2022年9月9日

:: 关闭 echo 回显
@echo off

:: 使用 goto 语句实现注释
goto note comment here
= 可以是多行文本，可以是命令
= 可以包含重定向符号和其他特殊字符
= 只要不包含 :note 这一行，就都是注释
=
= 其它注释方法:
= 1. :: 注释内容      =>第一个冒号后也可以跟任何一个非字母数字的字符
= 2. rem 注释内容     =>不能出现重定向符号和管道符号
= 3. echo 注释内容 >nul    =>不能出现重定向符号和管道符号
= 4. :注释内容     =>注释文本不能与已有标签重名
= 5. %注释内容%    =>可以用作行间注释，不能出现重定向符号和管道符号
= 6. if not exist nul 注释内容    =>不能出现重定向符号和管道符号
= 7. goto 标签 注释内容    =>可以用作说明 goto 的条件和执行内容
= 8. :标签 注释内容        =>可以用作标签下方段的执行内容
:note comment here

:: cmd 窗口名称
title BAT base

:: echo 输出信息，并输出时间
echo Begin time: %time%

:: 换行，echo 和 . 之间没有空格
echo.

:: 后台休眠 3s，不向屏幕输出任何内容
timeout 3 > nul

:: 实时显示倒计时
timeout 3

:: 暂停，窗口提示：请按任意键继续……
pause

:: 暂停，无任何输出
pause > nul

:: set 设置变量
set md_file=.\README.md

if not exist %md_file% (
   echo %md_file% not exist
)

:: start 打开一个新的 cmd 窗口，/wait 等待新窗口执行完毕
start /wait ping www.baidu.com

:: 利用 goto 实现循环
:run
echo Drag file here and then press Enter(exit, just press Enter):
echo.

:: 拖拽文件到 cmd 中，保存在 File 变量中
set /p File=

echo %File%

if %File% == "" (
    echo exit program!
    exit
)

set File=""
goto run

:: hkk 功能实现
:: 查看 C 盘剩余空间
for /f "tokens=2 delims==" %%a in ('wmic logicaldisk c: get FreeSpace/value') do set space=%%a
set gbfsize=%space:~0,-7%

if %gbfsize% gtr 500 (
    echo C disk remain %gbfsize%MB, at least 500MB
)

:: 网络状态诊断
:check

ping -n 2 www.baidu.com > nul

:: ERRORLEVEL 判断前一条命令的错误返回值
:: 在 if 后面可以直接使用，其它方式和变量相同
if ERRORLEVEL 1 (
    echo network error!
    timeout 5 > nul
) && goto check

if ERRORLEVEL 0 (echo network ok!)
