Windows bat 批处理文件知识点。

- [BAT](#bat)
- [参数](#参数)
- [字符串](#字符串)
- [基本指令](#基本指令)
- [其它指令](#其它指令)
- [注册表操作](#注册表操作)
- [系统服务](#系统服务)
- [setlocal 与变量延迟](#setlocal-与变量延迟)
- [文件处理](#文件处理)
- [补充](#补充)
  - [命令](#命令)
  - [变量](#变量)
  - [循环](#循环)
- [dos 命令参考](#dos-命令参考)
- [功能](#功能)

# BAT

1. 批处理文件是扩展名为 `.bat` 或 `.cmd` 的纯文本，每一行都是一条 `DOS` 命令。
2. 编写好的批处理文件，可看做一个 DOS 的外部命令。
3. `C:\AUTOEXEC.BAT` 在系统启动时会自动运行，可将启动时需要运行的命令写入。
4. 是一种简单的程序，用 if 和 goto 来控制流程，用 for 循环。
5. 大小写不敏感(命令符忽略大小写)
6. 编程能力弱，编程十分不规范。
7. 双击或在命令行下执行批处理文件，系统会调用 cmd.exe 来执行。

注：批处理文件以 ANSI 格式编码，可解决 bat 中文输出乱码。

# 参数

1. 系统参数

```bat
%SystemRoot%   ==    C:\WINDOWS
%windir%       ==    C:\WINDOWS
%ProgramFiles% ==    C:\Program Files
%USERPROFILE%  ==    C:\Documents and Settings\Administrator  (子目录有“桌面”,“开始菜单”,“收藏夹”等)
%APPDATA%      ==    C:\Documents and Settings\Administrator\Application Data
%TEMP%         ==    C:\DOCUME~1\ADMINI~1\LOCALS~1\Temp  (%TEM% 同样)
%APPDATA%      ==    C:\Documents and Settings\Administrator\Application Data
%OS%           ==    Windows_NT (系统)
%Path%         ==    %SystemRoot%\system32;%SystemRoot%;%SystemRoot%\System32\Wbem  (原本的设置)
%HOMEDRIVE%    ==    C:   (系统盘)
%HOMEPATH%     ==    \Documents and Settings\Administrator

:: 枚举当前的环境变量
setlocal enabledelayedexpansion
FOR /F "usebackq delims==" %%i IN (`set`) DO @echo %%i    !%%i!
```

2. 传递参数给批处理文件

`%[1-9]` 表示参数。变量可以从 %0 到 %9，`%0` 表示批处理命令本身，其它参数字符串
用 %1 到 %9 顺序表示。

```bat
:: 执行同目录下的 test2.bat 文件，并输入两个参数
call test2.bat "hello" "haha"

:: 在 test2.bat 文件里写:
echo %1  (打印: "hello")
echo %2  (打印: "haha")
echo %0  (打印: test2.bat)
echo %19 (打印: "hello"9)
```

# 字符串

1. 分割字符串

```text
%源字符串:~起始值,截取长度%

起始值从 0 开始；截取长度是可选的，如果省略逗号和截取长度，将会从起始值截取到结尾；
截取长度如果是负数，表示截取到倒数第几个。
```

```bat
:: 显示如："11:04:23.03" (完整的时间"hh:mm:ss.tt")
"%time%"

:: 显示"hh:mm"(即"11:04")，其中 0 表示从右向左移位操作的个数，5表示从左向右移位操作的个数
"%time:~0,5%"

:: 显示标准时间格式"hh:mm:ss"(即"11:04:23"，前 8 个字符串)
"%time:~0,8%"

:: 显示"mm:ss"(即从第 4 个开始,截去最后 3 个的字符串)
"%time:~3,-3%"

:: 显示"04:23.03"(即去掉前 4 个字符串)
"%time:~3%"

:: 显示".tt"(即最后 3 个字符串)
"%time:~-3%"
```

2. 替换字符串

```bat
set a="abcd1234"
echo %a%          :: 显示："abcd1234"
set a=%a:1=kk%    :: 替换“1”为“kk”
echo %a%          :: 显示："abcdkk234"
```

3. 字符串合并

```bat
:: 没有直接字符串合并函数
set str1=%str1%%str2%
```

4. 字符串长度

无现成函数。

5. 使用参数截取字符串

```bat
:: 直接 echo %args:~%num%,-5% 没办法想要的字符串，需要如下两步

setlocal enabledelayedexpansion
echo !args:~%num%,-5!
```

# 基本指令

0. help 或 /?

```text
语法：`help command` 或 `command /?`

显示命令的帮助信息。
```

```bat
:: help 命令显示命令 dir 的帮助信息
help dir

:: /? 命令显示命令 dir 的帮助信息，效果和 help 一样
dir /?
```

1. echo

```text
语法：echo [{on|off}] [message]

echo [on|off]     打开回显或关闭回显功能
echo              显示当前回显设置。
echo [message]    显示信息。

默认值为 echo on。
echo off 表示在此语句后所有运行的命令都不显示命令行本身。
```

2. @

```text
不显示 @ 后面的命令。
与 echo off 相象，但它是在行首，表示运行时不显示这一行的命令行（只能影响当前行）。
```

```bat
:: 此语句常用于开头，表示不显示所有的命令行信息，包括此句
@echo off
```

3. goto

```text
语法：goto label

指定跳转到标签 label 行，程序将从下一行命令开始执行。
label 标签的名字可以随便起，但是最好是有意义的，字母前必须加个冒号 `:` 来表示这个字母是标签。
```

4. rem

```text
语法：rem message

行注释。（技巧：用双冒号 :: 替代 rem）
```

5. pause

暂停批处理并在屏幕上显示 `Press any key to continue...` 的提示，等待用户按任意键后继续。

```bat
:: 使用重定向符 `>` 丢弃提示信息
pause > nul
```

6. call

```text
语法: call [[Drive:][Path] FileName [BatchParameters]] [:label [arguments]]

参数: [Drive:][Path] FileName 指定要调用的批处理程序的位置和名称。filename 参数必须具有 .bat 或 .cmd 扩展名。

调用另一个批处理程序，并且不终止父批处理程序。如果不用 call 而直接调用别的批处理文件，那么执行完那个批处理文件后将无法返回当前文件并执行当前文件的后续命令。

call 命令接受用作调用目标的标签。

如果在脚本或批处理文件外使用 Call，它将不会在命令行起作用。

注：可以调用自身(死循环、递归)
```

```bat
:: 调用指定目录下的 test2.bat，且输入 3 个参数给他
call="%cd%\test2.bat" haha kkk aaa

:: 调用同目录下的 test2.bat，且输入 2 个参数给他
call test2.bat arg1 arg2
```

7. start

```text
调用外部程序，所有的 DOS 命令和命令行程序都可以由 start 命令来调用。

常用参数：
    MIN         开始时窗口最小化
    SEPARATE    在分开的空间内开始 16 位 Windows 程序
    HIGH        在 HIGH 优先级类别开始应用程序
    REALTIME    在 REALTIME 优先级类别开始应用程序
    WAIT        启动应用程序并等候它结束
    parameters  这些为传送到命令/程序的参数
```

```bat
:: 调用同目录下的 test2.bat，且输入 2 个参数给他，且本窗口最小化
start /MIN test2.bat arg1 arg2

:: 文件路径名有空格时
e:\"program files"\notepad++\notepad++.exe
```

8. if

- `if`

```bat
:: TEXT
:: 语法: if [not] "参数" == "字符串" 待执行的命令
::
:: 参数如果等于（或 not 不等于）指定的字符串，则条件成立，运行命令，否则运行下一句。
:: 如果待执行命令多于一行，可用括号将它们包起来。

:: CODE
if "%1" == "a" format a:
if {%1} == {} goto noparms
```

- `if exist`

```bat
:: TEXT
:: 语法: if [not] exist [路径\]文件名 待执行的命令
::
:: 如果有指定的文件，则条件成立，运行命令，否则运行下一句。

:: CODE
:: 表示如果存在这文件，则编辑它，用很难看的系统编辑器
if exist config.sys edit config.sys

:: 表示如果存在这文件，则显示它的内容
if exist config.sys type config.sys
```

- `if errorlevel number`

```bat
:: TEXT
:: 语法: if [not] errorlevel <数字> 待执行的命令
::
:: 如果程序返回值等于指定的数字，则条件成立，运行命令，否则运行下一句。(返回值必须按照从大到小的顺序排列)

:: CODE
@echo off

xcopy F:\test.bat D:\

if ERRORLEVEL 1 (echo 文件拷贝失败
) else if ERRORLEVEL 0 echo 成功拷贝文件

pause
```

很多 DOS 程序在运行结束后会返回一个数字值用来表示程序运行的结果(或者状态)，称为
错误码 errorlevel 或称返回码。常见的返回码为 0、1。通过 if errorlevel 命令可以判
断程序的返回值，根据不同的返回值来决定执行不同的命令。


- else

```bat
:: TEXT
:: 语法： if 条件 (成立时执行的命令) else (不成立时执行的命令)
::
:: 如果是多个条件，建议适当使用括号把各条件包起来，以免出错。

:: CODE
if 1 == 0 ( echo comment1 ) else if 1==0 ( echo comment2 ) else (echo comment3 )

:: 如果 else 的语句需要换行，if 执行的行尾需用“^”连接，并且 if 执行的动作需用(括起来)，否则报错
if 1 == 0 ( echo comment1 ) else if 1==0 ( echo comment2 ) ^
else (echo comment3 )
```

- 比较运算符:

EQU - 等于   (一般使用“==”)
NEQ - 不等于 (没有 “!=”,改用“ if not 1==1 ”的写法)
LSS - 小于
LEQ - 小于或等于
GTR - 大于
GEQ - 大于或等于

9. choice

可以让用户输入一个字符(用于选择)，从而根据用户的选择返回不同的 errorlevel，然后
配合 if errorlevel 选择运行不同的命令。

注意：choice 命令为 DOS 或者 Windows 系统提供的外部命令，不同版本的 choice 命令
语法会稍有不同，请用 choice /?查看用法。

choice 使用此命令可以让用户输入一个字符，从而运行不同的命令。

使用时应该加 /c 参数，然后写提示可输入的字符，之间无空格。它的返回码为 1234……

```bat
:: 显示 确认 Y，否定 N，取消 C [Y,N,C]?
choice /c ync /m "确认 Y，否定 N，取消 C"

:: 应先判断数值最高的错误码
choice /c ync /m "确认 Y，否定 N，取消 C"
if errorlevel 3 (echo c
)else if errorlevel 2 (echo n
)else if errorlevel 1 echo y
```

10. for

for 是一个比较复杂的命令，主要用于参数在指定的范围内循环执行命令。

- `for {%variable | %%variable} in (set) do command [command-parameters]`

```text
%variable 指定一个单一字母可替换的参数。变量名称是区分大小写的，所以 %i 不同于 %I.
          在批处理文件中使用 FOR 命令时，指定变量建议用 %%variable 而不要用 %variable。
(set)     指定一个或一组文件。可以使用通配符。
command   指定对每个文件执行的命令。
command-parameters 为特定命令指定参数或命令行开关。
```

如果命令扩展名被启用，下列额外的 for 命令格式会受到支持:

- `FOR /D %variable IN (set) DO command [command-parameters]`

```text
如果集里面包含通配符，则指定与目录名匹配，而不与文件名匹配。
```

- `FOR /R [[drive:]path] %variable IN (set) DO command [command-parameters]`

```text
检查以 [drive:]path 为根的目录树，指向每个目录中的 FOR 语句。
如果在 /R 后没有指定目录，则使用当前目录。如果集仅为一个单点(.)字符，则枚举该目录树。
```

- `FOR /L %variable IN (start,step,end) DO command [command-parameters]`

```text
该集表示以增量形式从开始到结束的一个数字序列。
如：(1,1,5) 将产生序列 1 2 3 4 5；  而(5,-1,1) 将产生序列 (5 4 3 2 1)。
```

- 有或者没有 usebackq 选项:

```text
FOR /F ["options"] %variable IN (file-set) DO command
FOR /F ["options"] %variable IN ("string") DO command
FOR /F ["options"] %variable IN (command)  DO command

参数"options"为:
    eol=c           - 指一个行注释字符的结尾(就一个,如“;”)
    skip=n          - 指在文件开始时忽略的行数。
    delims=xxx      - 指分隔符集。这个替换了空格和跳格键的默认分隔符集。
    tokens=x,y,m-n  - 指每行的哪一个符号被传递到每个迭代的 for 本身。这会导致额外变量名称的分配。
                      m-n 格式为一个范围。通过 nth 符号指定 mth。
          如果符号字符串中的最后一个字符星号，那么额外的变量将在最后一个符号解析之后分配并接受行的保留文本。
    usebackq        - 指定新语法已在下类情况中使用:
                      在作为命令执行一个后引号的字符串并且一个单引号字符为文字字符串命令并允许在 filenameset 中使用双引号扩起文件名称。
```

```bat
:: 如下命令行会显示当前目录下所有以 bat 或者 txt 为扩展名的文件名。
for %%c in (*.bat *.txt) do (echo %%c)

:: 如下命令行会显示当前目录下所有包含有 e 或者 i 的目录名。
for /D %%a in (*e* *i*) do echo %%a

:: 如下命令行会显示 E 盘 test 目录 下所有以 bat 或者 txt 为扩展名的文件名。
for /R E:\test %%b in (*.txt *.bat) do echo %%b

:: 遍历当前目录下所有文件
for /r %%c in (*) do (echo %%c)

:: 如下命令行将产生序列 1 2 3 4 5
for /L %%c in (1,1,5) do echo %%c

:: 以下两句，显示当前的年月日和时间
For /f "tokens=1-3 delims=-/. " %%j In ('Date /T') do echo %%j 年%%k 月%%l 日
For /f "tokens=1,2 delims=: " %%j In ('TIME /T') do echo %%j 时%%k 分

:: 把记事本中的内容每一行前面去掉 8 个字符
setlocal enabledelayedexpansion

for /f %%i in (zhidian.txt) do (
    set atmp=%%i
    set atmp=!atmp:~8!
    if {!atmp!}=={} ( echo.) else echo !atmp!
   )

:: 读取记事本里的内容(使用 delims 是为了把一行显示全,否则会以空格为分隔符)
for /f "delims=" %%a in (zhidian.txt) do echo.%%a
```

- continue 和 break

利用 goto 实现程序中常用的 continue 和 break 命令。

continue: 在 for 循环的最后一行写上一个标签，跳转到这位置即可

break: 在 for 循环的外面的下一句写上一个标签，跳转到这位置即可

```bat
for /F ["options"] %variable IN (command)  DO (
... do command ...
if ... goto continue
if ... goto break
... do command ...
:continue
)
:break
```

# 其它指令
1. ping

```text
测试网络联接状况以及信息包发送和接收状况。但是不能够测试端口。

语法：ping IP 地址或主机名 [-t] [-a] [-n count] [-l size]

参数含义：
-t 不停地向目标主机发送数据；
-a 以 IP 地址格式来显示目标主机的网络地址；
-n count 指定要 Ping 多少次，具体次数由 count 来指定；
-l size 指定发送到目标主机的数据包的大小。
```
```bat
:: 不停的测试 192.168.0.1，按 ctrl+c 停止
ping 192.168.0.1 -t

:: ping 一下所有的局域网电脑
for /L %%a in (0,1,255) do ping 192.168.0.%%a -n 1 >> tmp.txt
```

2. telnet

测试端口。使用 `telnet IP 地址或主机名 端口`，使用 tcp 协议的

```bat
:: 测试 192.168.0.1 的 80 端口
telnet 192.168.0.1 80
```

3. color

```text
设置背景及字体颜色

语法： color bf

b 是指定背景色的十六进制数字； f 指定前景颜色(即字体颜色)。

颜色值: 0:黑色    1:蓝色    2:绿色    3:湖蓝    4:红色    5:紫色    6:黄色    7:白色
        8:灰色    9:淡蓝    A:淡绿    B:浅绿    C:淡红    D:淡紫    E:淡黄    F:亮白

如果没有给定任何参数，该命令会将颜色还原到 CMD.EXE 启动时的颜色。
如果两参数一样，视为无效输入。只有一个参数时，设置字体。
```

4. random

产生随机数（正整数 0~）。

5. exit

结束程序。即时是被调用的程序，结束后也不会返回原程序。

6. shutdown

shutdown -s 关机


10. 所有内置命令的帮助信息

```bat
ver /?
cmd /?
set /?
rem /?
if /?
echo /?
goto /?
for /?
shift /?
call /?

其他需要的常用命令：

type /?
find /?
findstr /?
copy /?
```

# 注册表操作

1. 备份注册表

```bat
:: 将[HKEY_LOCAL_MACHINE ... Run]的内容，备份到“c:\windows\1.reg”
reg export HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run c:\windows\1.reg
reg export HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run c:\windows\2.reg
```

2. 修改/添加注册表内容

- 一般的添加或修改
```bat
:: HKCU 是 “HKEY_CURRENT_USER” 的缩写，用全称也可以
:: 添加名称为“Java_Home”的变量；类型为“reg_sz”，另一种常见类型是“reg_dword”；值为 D:\Java\jdk1.6.0_07
reg add "HKCU\Environment" /v Java_Home /t reg_sz /d "D:\Java\jdk1.6.0_07" /f
```

- 使用变量

```bat
set SoftWareHome=HKEY_LOCAL_MACHINE\SOFTWARE\JavaSoft\Java
reg add "%SoftWareHome%Web Start\1.6.0_07" /v Home /t reg_sz /d "%cd%\jre1.6.0_07\bin" /f
```

- 如果注册表的名称有空格，或者数据用特殊符号时

```bat
:: 传入值为(值用双引号括起来的)："D:\ProgramFiles\1.work_soft\Sybase\PowerDesigner_12\Documentation\Index.htm"
reg add "%SoftWareHome2%\HelpCommands" /v "01:Online Documentation" /t reg_sz /d "\"%cd%\Documentation\Index.htm\"" /f

:: 传入值为(“\”结尾的)： E:\Holemar\1.notes\90. Windows\Resource Files\Report Templates\
reg add "%SoftWareHome2%\Paths" /v ReportTemplates /t reg_sz /d "%cd%\Resource Files\Report Templates\\" /f
```

- 增加空内容

```bat
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Shared Tools\MSConfig\startupreg\IMJPMIG8.1"
```

- 添加或修改默认值

```bat
:: 这里用“/ve”来代替一般修改时的“/v 变量名”，即可修改默认值了
reg add "%vpath%InstallPath" /ve /t reg_sz /d "%cd%" /f
```

3. 删除注册表的内容

```bat
:: 双引号里面的是注册表的目录，下面两句将删除这目录下的所有信息
reg delete "HKEY_CURRENT_USER\Software\RealVNC" /f
reg delete "HKEY_LOCAL_MACHINE\SOFTWARE\RealVNC" /f

:: 双引号里面的是注册表的目录，下面一句将删除这目录下指定的某个信息
reg delete "HKEY_LOCAL_MACHINE\Software\RealVNC" /v VNC_Server /f
```

4. 注册表的常用位置

- 系统启动项

```text
[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run]
[HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run]
```

- 系统环境变量

```text
[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Environment]
```

- 当前用户的环境变量

```text
[HKEY_CURRENT_USER\Environment]
```

5. 修改注册表之后，结束并重新加载 explorer.exe 进程，可刷新注册表，令其生效

```bat
taskkill /f /im explorer.exe >nul
start "" "explorer.exe"
```

# 系统服务

1. 停止服务 `net stop 服务名`
2. 启动服务 `net start 服务名`
3. 设置启动类型

```text
自动：  SC CONFIG 服务名 START= auto
手动：  SC CONFIG 服务名 START= demand
已禁用：SC CONFIG 服务名 START= disabled
附：“START= ”等号后面必须要有一个空格。(start 还有 boot,system 两个值)
```

4. 查看系统服务 `start %SystemRoot%\system32\services.msc /s`

# setlocal 与变量延迟

1. 在没有开启变量延迟的情况下，某条命令行中的变量改变，必须到下一条命令才能体现。
   另外例如 for 命令等，其后用一对圆括号闭合的所有语句也当作一行。

```bat
:: a = 4
set a=4
set a=5 & echo %a%

:: 也可以对这种机制加以利用，如下的变量交换
set var1=abc
set var2=123
echo 交换前： var1=%var1% var2=%var2%
set var1=%var2%& set var2=%var1%
echo 交换后： var1=%var1% var2=%var2%
```

2. 启动批处理文件中环境变量的本地化。本地化将持续到出现匹配的 endlocal 命令或者到达批处理文件结尾为止。

```text
语法: setlocal {enableextension | disableextensions} {enabledelayedexpansion | disabledelayedexpansion}

enableextension: 启用命令扩展，直到出现匹配的 endlocal 命令，无论 setlocal 命令之前的设置如何。
disableextensions: 禁用命令扩展，直到出现匹配的 endlocal 命令，无论 setlocal 命令之前的设置如何。
enabledelayedexpansion: 启用延迟的环境变量扩展，直到出现匹配的 endlocal 命令，无论 setlocal 命令之前的设置如何。
disabledelayedexpansion: 禁用延迟的环境变量扩展，直到出现匹配的 endlocal 命令，无论 setlocal 命令之前的设置如何。
```

3. 为了能够感知环境变量的动态变化，批处理设计了变量延迟。简单来说，在读取了一条
   完整的语句之后，不立即对该行的变量赋值，而会在某个单条语句执行之前再进行赋值，
   也就是说“延迟”了对变量的赋值。

```bat
:: a = 5
setlocal enabledelayedexpansion
set a=4
set a=5 & echo !a!
```

变量延迟的启动语句是 `setlocal enabledelayedexpansion`，并且变量要用一对叹号 `!!` 括起来

由于启动了变量延迟，所以批处理能够感知到动态变化，即不是先给该行变量赋值，而是在
运行过程中给变量赋值，因此此时 a 的值就是 5 了。另外，启动变量延迟，`%` 的变量还是
不变。

```bat
:: 打印从 1 到 5；如果不变量延迟，一个变量也没有打印
setlocal enabledelayedexpansion

for /l %%i in (1,1,5) do (
set a=%%i
echo !a!
)
```

# 文件处理
1. 删除
- 删除一个文件或多个文件

```bat
:: 将直接删除 d:\test\a.bat，没有任务提示
del /s /q /f d:\test\a.bat

:: 将直接删除本目录的 temp 目录的所有文件，没有任务提示
:: 删除文件的时候可以使用 * 作通配符
del temp\* /q /f /s
```

- 删除一个空目录

```bat
:: 将直接删除 d:\test\log 目录，如果 log 目录里面有文件将无法删除
rd /q /s  d:\test\log
```

- 删除一个非空目录 (必须指定目录名称)

```bat
:: 必须指定目录名称，不能使用通配符
:: /S  除目录本身外，还将删除指定目录下的所有子目录
:: /Q  安静模式，带 /S 删除目录树时不要求确认
:: 无论里面是否有文件或文件夹将全部直接删除

rmdir /q /s d:\test\logs
```

2. 创建目录

```bat
:: 路径有空格时，可以用双引号括起来，也可以用 &nbsp; 替代
MKDIR [drive:]path
MD [drive:]path
```

# 补充
## 命令

1. 清屏 `cls`
2. 复制 `copy d:\test\*.* d:\back`，复制 D 盘 test 文件夹的所有文件(不包括文件夹及子文件夹里的东西)到 D 盘的 back 文件夹
3. 目录列表 `dir` 相当于 linux 指令 ls
4. 重定向 `>` 生成文件并写入内容（覆盖方式），`>>` 在文件中追加内容
5. 创建文件夹 `md d:\temp`
6. 屏蔽返回消息 `>nul`，`2>nul`
7. 等待用户输入 `set /p 变量名=屏幕显示信息`
8. 用户按回车退出 `pause`，可在文件最后一行添加 `set /p tmp=操作结束，请按回车键退出...` 替代
9. 设置标题 `title 测试`
10. 设置屏幕显示颜色，如绿色 `color 0a`
11. 修改文件名 `rename test.jpg test2.jpg`
12. 查看 IP 上的共享资源 `net view 192.168.0.1`

## 变量

```bat
:: 给 var 赋值
set var = "abc"

:: 将 1 + 2 的计算结果赋值给 var
set /a var = 1 + 2

:: 等待用户输入，拖拽文件到窗口也可以算输入
set /p var =

:: 访问变量
echo %var%
```

## 循环

```bat
:: for /f ["options"] %%i in (file) do command
:: for /f ["options"] %%i in ("string") do command
:: for /f ["options"] %%i in ('command') do command

:: 显示 a.txt 文件内容
for /f %%i in (a.txt) do (echo %%i)

:: 显示当前目录下文件和目录
:: delims 表示切割内容给的分隔符，默认为空格
:: tokens 表示选中某一列
for /f "tokens=*" %%i in ('dir') do (echo %%i)

:: goto 循环
:circle
echo test
goto circle
```

# dos 命令参考

```text
net use \\ip\ipc$ " " /user:" "            ;建立 IPC 空链接
net use \\ip\ipc$ "passwd" /user:"user"    ;建立 IPC 非空链接
net use h: \\ip\c$ "passwd" /user:"user"   ;直接登陆后映射对方 C：到本地为 H:
net use h: \\ip\c$                         ;登陆后映射对方 C：到本地为 H:
net use \\ip\ipc$ /del                     ;删除 IPC 链接
net use h: /del                            ;删除映射对方到本地的为 H:的映射

net user "user" "passwd" /add              ;建立用户
net user guest /active:yes                 ;激活 guest 用户
net user                                   ;查看有哪些用户
net user "user"                            ;查看帐户的属性
net localgroup administrators "user" /add  ;把“用户”添加到管理员中使其具有管理员权限,注意：administrator 后加 s 用复数

net start                                  ;查看开启了哪些服务
net start "service"　                      ;开启服务；(如:net start telnet， net start schedule)
net stop "service"                         ;停止某服务
net pause "service"                        ;暂停某服务

net time \\"dest_ip"        ;查看对方时间
net time \\"dest_ip" /set   ;设置本地计算机时间与“目标 IP”主机的时间同步,加上参数/yes 可取消确认信息

net view                    ;查看本地局域网内开启了哪些共享
net view \\ip               ;查看对方局域网内开启了哪些共享
net config                  ;显示系统网络设置
net logoff                  ;断开连接的共享

net send ip "message"       ;向对方发信息
net ver                     ;局域网内正在使用的网络连接类型和信息
net share                   ;查看本地开启的共享
net share ipc$              ;开启 ipc$共享
net share ipc$ /del         ;删除 ipc$共享
net share c$ /del           ;删除 C：共享
net user guest 12345        ;用 guest 用户登陆后用将密码改为 12345
net password "passwd"       ;更改系统登陆密码

netstat -a     ;查看开启了哪些端口,常用 netstat -an
netstat -n     ;查看端口的网络连接情况，常用 netstat -an
netstat -v     ;查看正在进行的工作
netstat -p     ;;协议名 例：netstat -p tcq/ip  查看某协议使用情况（查看 tcp/ip 协议使用情况）
netstat -s     ;查看正在使用的所有协议使用情况
nbtstat -A ip  ;对方 136 到 139 其中一个端口开了的话，就可查看对方最近登陆的用户名（03 前的为用户名）-注意：参数-A 要大写

tracert -参数 ip(或计算机名)  ;跟踪路由（数据包），参数：“-w 数字”用于设置超时间隔。
ping ip(或域名)               ;向对方主机发送默认大小为 32 字节的数据，参数：“-l[空格]数据包大小”；“-n 发送数据次数”；“-t”指一直 ping。
ping -t -l 65550 ip           ;死亡之 ping(发送大于 K 的文件并一直 ping 就成了死亡之 ping)
ipconfig (winipcfg)           ;用于 windows NT 及 XP(windows 95 98)查看本地 ip 地址，ipconfig 可用参数“/all”显示全部配置信息

tlist -t            ;以树行列表显示进程(为系统的附加工具，默认是没有安装的，在安装目录的 Support/tools 文件夹内)
kill -F 进程名      ;加-F 参数后强制结束某进程(为系统的附加工具，默认是没有安装的，在安装目录的 Support/tools 文件夹内)
del -F 文件名       ;加-F 参数后就可删除只读文件,/AR、/AH、/AS、/AA 分别表示删除只读、隐藏、系统、存档文件，
                     /A-R、/A-H、/A-S、/A-A 表示删除除只读、隐藏、系统、存档以外的文件。
                     例如 "DEL/AR *.*" 表示删除当前目录下所有只读文件，"DEL/A-S *.*" 表示删除当前目录下除系统文件以外的所有文件

del /S /Q 目录
rmdir /s /Q 目录    ;/S 删除目录及目录下的所有子目录和文件。同时使用参数/Q 可取消删除操作时的系统确认就直接删除。（二个命令作用相同）

move 盘符\路径\要移动的文件名 存放移动文件的路径\移动后文件名  ;移动文件,用参数/y 将取消确认移动目录存在相同文件的提示就直接覆盖

fc one.txt two.txt > 3st.txt   ;对比二个文件并把不同之处输出到 3st.txt 文件中，"> "和"> >" 是重定向命令

at id 号                              ;开启已注册的某个计划任务
at /delete                            ;停止所有计划任务，用参数/yes 则不需要确认就直接停止
at id 号 /delete                      ;停止某个已注册的计划任务
at                                    ;查看所有的计划任务
at \\ip time 程序名(或一个命令) /r    ;在某时间运行对方某程序并重新启动计算机

finger username @host  ;查看最近有哪些用户登陆
telnet ip 端口         ;远和登陆服务器,默认端口为 23
open ip                ;连接到 IP（属 telnet 登陆后的命令）
telnet                 ;在本机上直接键入 telnet 将进入本机的 telnet

copy 路径\文件名 1　路径\文件名 2 /y                 ;复制文件 1 到指定的目录为文件 2，用参数/y 就同时取消确认你要改写一份现存目录文件
copy c:\srv.exe \\ip\admin$                          ;复制本地 c:\srv.exe 到对方的 admin 下
cppy 1st.jpg/b+2st.txt/a 3st.jpg                     ;将 2st.txt 的内容藏身到 1st.jpg 中生成 3st.jpg 新的文件，
                                                      注：2st.txt 文件头要空三排，参数：/b 指二进制文件，/a 指 ASCLL 格式文件
xcopy 要复制的文件或目录树　目标地址\目录名          ;复制文件和目录树，用参数/Y 将不提示覆盖相同文件
copy \\ip\admin$\svv.exe c:\ 或:copy\\ip\admin$\*.*  ;复制对方 admini$共享下的 srv.exe 文件（所有文件）至本地 C：

tftp -i 自己 IP(用肉机作跳板时这用肉机 IP) get server.exe c:\server.exe 登陆后，将“IP”的 server.exe 下载到目标主机 c:\server.exe 参数：-i 指以二进制模式传送，如传送 exe 文件时用，如不加-i 则以 ASCII 模式（传送文本文件模式）进行传送

tftp -i "对方 IP" put c:\server.exe  登陆后，上传本地 c:\server.exe 至主机
ftp ip 端口 用于上传文件至服务器或进行文件操作，默认端口为 21。bin 指用二进制方式传送（可执行文件进）；默认为 ASCII 格式传送(文本文件时)

route print  显示出 IP 路由，将主要显示网络地址 Network addres，子网掩码 Netmask，网关地址 Gateway addres，接口地址 Interface
arp  查看和处理 ARP 缓存，ARP 是名字解析的意思，负责把一个 IP 解析成一个物理性的 MAC 地址。arp -a 将显示出全部信息
start 程序名或命令 /max 或/min  新开一个新窗口并最大化（最小化）运行某程序或命令
mem  查看 cpu 使用情况

attrib 文件名(目录名)  查看某文件（目录）的属性
attrib 文件名 -A -R -S -H 或 +A +R +S +H  去掉(添加)某文件的 存档，只读，系统，隐藏 属性；用＋则是添加为某属性

dir  查看文件，参数：/Q 显示文件及目录属系统哪个用户，/T:C 显示文件创建时间，/T:A 显示文件上次被访问时间，/T:W 上次被修改时间
date /t 、 time /t 使用此参数即“DATE/T”、“TIME/T”将只显示当前日期和时间，而不必输入新日期和时间

set 指定环境变量名称=要指派给变量的字符  设置环境变量
set  显示当前所有的环境变量
set p(或其它字符)  显示出当前以字符 p(或其它字符)开头的所有环境变量

pause  暂停批处理程序，并显示出：请按任意键继续....
if  在批处理程序中执行条件处理（更多说明见 if 命令及变量）
goto 标签  将 cmd.exe 导向到批处理程序中带标签的行（标签必须单独一行，且以冒号打头，例如：“：start”标签）
call 路径\批处理文件名  从批处理程序中调用另一个批处理程序 （更多说明见 call /?）
for  对一组文件中的每一个文件执行某个特定命令（更多说明见 for 命令及变量）

echo on 或 off           ;打开或关闭 echo，仅用 echo 不加参数则显示当前 echo 设置
echo 信息                ;在屏幕上显示出信息
echo 信息 >> pass.txt    ;将"信息"保存到 pass.txt 文件中

findstr "Hello" aa.txt   ;在 aa.txt 文件中寻找字符串 hello
find 文件名              ;查找某文件
title 标题名字           ;更改 CMD 窗口标题名字
color 颜色值             ;设置 cmd 控制台前景和背景颜色；0＝黑、1＝蓝、2＝绿、3＝浅绿、4＝红、5＝紫、6＝黄、7=白、8=灰、9=淡蓝、A＝淡绿、B=淡浅绿、C=淡红、D=淡紫、E=淡黄、F=亮白

prompt 名称       ;更改 cmd.exe 的显示的命令提示符(把 C:\、D:\统一改为：EntSky\ )
print 文件名      ;打印文本文件
2ver              ;在 DOS 窗口下显示版本信息
winver            ;弹出一个窗口显示版本信息（内存大小、系统版本、补丁版本、计算机名）

format 盘符 /FS:类型     ;格式化磁盘,类型:FAT、FAT32、NTFS ,例：Format D: /FS:NTFS
md 目录名 创建目录

replace 源文件 要替换文件的目录   ;替换文件
ren 原文件名 新文件名             ;重命名文件名

type 文件名    ;显示文本文件的内容
more 文件名    ;逐屏显示输出文件
tree           ;以树形结构显示出目录，用参数-f 将列出第个文件夹中文件名称

doskey     ;要锁定的命令＝字符
doskey     ;要解锁命令= 为 DOS 提供的锁定命令(编辑命令行，重新调用 win2k 命令，并创建宏)。
            如：锁定 dir 命令：doskey dir=entsky (不能用 doskey dir=dir)；解锁：doskey dir=
taskmgr    ;调出任务管理器

chkdsk /F D:    ;检查磁盘 D 并显示状态报告；加参数/f 并修复磁盘上的错误

tlntadmn telnt 服务     ;admn,键入 tlntadmn 选择 3，再选择 8,就可以更改 telnet 服务默认端口 23 为其它任何端口

path 路径\可执行文件的文件名    ;为可执行文件设置一个路径。

exit     ;退出 cmd.exe 程序或目前，用参数/B 则是退出当前批处理脚本而不是 cmd.exe
cmd      ;启动一个 win2K 命令解释窗口。参数：/eff、/en 关闭、开启命令扩展；更我详细说明见 cmd /?

regedit /s 注册表文件名  ;导入注册表；参数/S 指安静模式导入，无任何提示；
regedit /e 注册表文件名  ;导出注册表

cacls 文件名 参数     ;显示或修改文件访问控制列表（ACL）——针对 NTFS 格式时。
                       参数：/D 用户名:设定拒绝某用户访问；
                       /P 用户名:perm 替换指定用户的访问权限；
                       /G 用户名:perm 赋予指定用户访问权限；
                       Perm 可以是: N 无，R 读取， W 写入， C 更改(写入)，F 完全控制；例：cacls D:\test.txt /D pub 设定 d:\test.txt 拒绝 pub 用户访问。
cacls 文件名          ;查看文件的访问用户权限列表
REM 文本内容          ;在批处理文件中添加注解
netsh                 ;查看或更改本地网络配置情况
```

# 功能

- 查看 C 盘剩余空间
- 网络状态检查
