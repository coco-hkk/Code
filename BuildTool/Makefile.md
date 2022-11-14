- [make](#make)
- [Makefile](#makefile)
	- [原理](#原理)
	- [组成部分](#组成部分)
- [Makefile 解析](#makefile-解析)
- [Makefile 规则](#makefile-规则)
	- [伪目标](#伪目标)
	- [命令前缀](#命令前缀)
- [自动推导(隐含规则)](#自动推导隐含规则)
- [变量](#变量)
	- [延迟变量 =](#延迟变量-)
	- [立即变量 :=](#立即变量-)
	- [条件赋值 ?=](#条件赋值-)
	- [追加赋值 +=](#追加赋值-)
	- [make 环境变量](#make-环境变量)
	- [make 自动变量](#make-自动变量)
	- [预定义变量](#预定义变量)
	- [通配符](#通配符)
- [指示符](#指示符)
	- [define 多行定义](#define-多行定义)
	- [条件判断](#条件判断)
	- [包含其它 Makefile](#包含其它-makefile)
	- [override](#override)
	- [export 声明](#export-声明)
	- [目录搜索](#目录搜索)
- [模式规则](#模式规则)
- [函数](#函数)
	- [文本处理](#文本处理)
	- [文件名处理函数](#文件名处理函数)
	- [make 控制函数](#make-控制函数)
- [特别注意](#特别注意)
  
在某方面来说，是一种自动化工具，能够自动化构建代码和日常办公。

# make
make 是一个命令工具，它解释 Makefile 中的规则。

# Makefile
Makefile 是一个文本文件，它描述了整个工程的编译、链接等规则，包括：工程中哪些源文件需要编译以及如何编译、需要创建哪些库文件以及如何创建这些库文件、如何最后产生我们想要的可执行文件。

## 原理
1. 如果这个工程没有被编译过，那么所有的 C 文件都要编译并链接。
2. 如果这个工程的某几个 C 文件被修改，那么我们只编译被修改的 C 文件，并链接目标程序。
3. 如果这个工程的头文件被改变了，那么我们需要编译引用这几个头文件的 C 文件，并链接目标程序。

## 组成部分
完整的 Makefile 包含五部分：显示规则、隐含规则、变量定义、指示符和注释。

#### `显式规则`
显式规则说明了，如何生成一个或多个目标文件。

书写 Makefile 时需要明确地给出目标文件、目标的依赖文件列表以及更新目标文件所需要的命令（有些规则没有命令，这样的规则只是纯粹的描述了文件之间的依赖关系）。

#### `隐式规则`
隐式规则是由 make 能够自动推导的规则。

隐式的规则可以使书写 Makefile 更加简略，这是由 make 所支持的（不同版本的 make 可能不同）。

#### `变量定义`
使用一个字符或字符串代表一段文本串，当定义了一个变量以后，Makefile 后续在需要使用此文本串的地方，通过引用这个变量来实现对文本串的使用。

#### `Makefile 指示符`
指示符指明在 make 程序读取 Makefile 文件过程中所要执行的一个动作。

其中动作包括：
- 读取一个文件。读取给定文件名的文件，将其内容作为 Makefile 文件的一部分。
- 决定（通常是根据一个变量的得值）处理或者忽略 Makefile 中的某一特定部分。
- 定义一个多行变量。

#### `注释`
Makefile 中 ` #` 字符后的内容被作为是注释内容（和 shell 脚本一样）处理。

如果此行的第一个非空字符为 ` #`，那么此行为注释行。注释行的结尾如果存在反斜线 ` \`，那么下一行也被作为注释行。

# Makefile 解析
GNU make 的执行过程分为两个阶段：

#### 第一阶段
1. 依次读取变量 "MAKEFILES" 定义的 Makefile 文件列表。
2. 读取工作目录下的 Makefile 文件。根据命名的查找顺序 "GNUMakefile"，"Makefile"，" makefile"，首先找到哪个就读取哪个。
3. 依次读取工作目录 Makefile 文件中使用指示符 "include" 包含的文件。
4. 查找重建所有已读取的 Makefile 文件的规则。如果存在一个目标是读取某一个 Makefile 文件，则执行此规则重建此 Makefile 文件，完成以后从第一步开始重新执行。
5. 初始化变量值并展开那些需要立即展开的变量和函数，并根据预设条件确定执行分支。
6. 根据 "终极目标" 以及其他目标的依赖关系建立依赖关系链表。

#### 第二阶段
1. 执行除 "终极目标" 以外的所有的目标的规则。规则中如果依赖文件中任一个文件的时间戳比目标文件新，则使用规则所定义的命令重建目标文件。
2. 执行 "终极目标" 所列的规则。

# Makefile 规则
一条简单的 Makefile 规则，如下：

```Makefile
 # 注意 : 使用空格缩进注释，不能使用 <tab>
# 注意 : 使用 <tab> 缩进 command，不能使用空格
target ... : prerequisites ...
	command
	...
```

`target` 规则的目标。目标通常是最后需要生成的 `最终文件名` 或者为了实现这个目的而必需的 `中间过程文件名`，如可执行程序的文件名或 .o 文件等。
另外，目标也可以是一个 make 执行的 `动作的名称`，是一个标签(label)，如目标 "clean"，我们称这样的目标是"伪目标"。

`prerequistites` 规则的依赖、先决条件。生成规则目标所需要的文件名列表。通常一个目标依赖于一个或者多个文件。

`command` 规则的命令行。是规则所要执行的动作（任意的 shell 命令或者是可在shell 下执行的程序）。它限定了 make 执行这条规则时所需要的动作。

这是一个文件的依赖关系，即 target 这一个或多个的目标文件依赖于 prerequisites 中的文件，其生成规则定义在 command 中。依赖关系的实质就是说明目标文件是由哪些文件生成的，换言之，目标文件是哪些文件更新的。在描述依赖关系行之下通常就是规则的命令行（存在一些些规则没有命令行），命令行定义了规则的动作（如何根据依赖文件来更新目标文件）。

命令行必需以 [Tab] 键开始，以和 Makefile 其他行区别。就是说所有的命令行必需以 [Tab] 字符开始，但并不是所有的以 [Tab] 键出现行都是命令行。 但 make 程序会把出现在第一条规则之后的所有以 [Tab] 字符开始的行都作为命令行来处理。

即 prerequisites 中如果有一个以上的文件比 target 文件要新的话（依据时间戳判断），command 所定义的命令就会被执行。
这就是 makefile 的规则，最核心的内容。

如果 make 不带任何⽬标，那么规则中的第⼀个⽬标将被视为是 `缺省⽬标`。

## 伪目标
Makefile 中把那些没有任何依赖只有执行动作的目标称为 `伪目标`(phony targets)。

```makefile
.PHONY : clean
clean :
	-rm edit $(objects)
```

通过 `.PHONY` 特殊目标将 clean 目标声明为伪目标：
- 避免当前目录存在 clean 同名文件，导致命令执行错误 
- 提高执行 make 时的效率

clean 的规则不要放在文件的开头，不然变成 make 的默认目标。不成文的规则是：clean 从来都是放在文件的最后。

## 命令前缀
- `@` 关闭当前行命令回显，只输出命令执行的结果, 出错的话停止执行
- `-` 命令执行有错的话, 忽略错误, 继续执行

# 自动推导(隐含规则)
make 可以自动推导文件以及文件依赖关系后面的命令。

如，编译 C 时，*.o 的目标会自动推导为 *.c.

# 变量
赋值方式，主要有一下四种：

```makefile
IMMEDIATE = DEFERRED
IMMEDIATE := IMMEDIATE
IMMEDIATE ?= DEFERRED
IMMEDIATE += DEFERRED
```

- 变量没有数据类型，可看作字符串
- 变量名可由字母、数字和下划线构成，可以数字开头
- 变量大小写敏感
- 等号两边的空白符无明确要求，make 在执行时会将多余空白符自动删除
- 变量值既可以是零项，一项或多项
- 变量一般都在 makefile 头部定义
- 变量几乎可在 makefile 任何地方使用

使用变量的方法： `$(变量)` 或 `${变量}`.

注意：美元符号 `$` 在 Makefile 中有特殊的含义，因此，在命令或者文件名中使用 `$` 时，需用两个美元符号 `$$` 来代替。

变量引用的展开过程是严格的文本替换，即变量的字符串被精确的展开在变量被引用的地方，如：

```makefile
foo = c
prog.o : prog.$(foo)
	$(foo)$(foo) -$(foo) prog.$(foo)
```

展开后就是：

```makefile
prog.c : prog.c
	cc -c prog.c
```

## 延迟变量 =
变量采用递归展开方式。变量的引用采用严格的文本替换方式，如果此变量定义在其他变量的引用，这些被引用的变量会在它被展开的同时被展开。

```makefile
foo = $(bar)
bar = $(ugh)
ugh = Huh?
all:
	@echo $(foo)
```

输出结果为 'Huh?'，且输出结果与变量定义的位置无关。

## 立即变量 :=
变量采用直接展开方式。变量值中对其他量或者函数的引用在定义变量时被展开，所以变量定义后就是一个实际需要的文本串，其中不再包含变量的引用。

```makefile
x := foo
y := $(x) bar
x := later

# 等价于：
y := foo bar
x := later
```

和递归展开不同，变量在定义时就完成了对所有变量和函数的展开，因此若将 x 定义在 y 之后，则得到 "y := bar"。

## 条件赋值 ?=
变量在之前没有赋值的情况下才会对这个变量进行赋值。

```makefile
FOO ?= bar

# 等价于：
ifeq ($(origin FOO), undefined)
	FOO = bar
endif
```

## 追加赋值 +=
```makefile
objects += another.o
```
把字符串 "another.o" 添加到变量 "objects" 原有值的末尾，使用 `空格` 和原有值分开。

## make 环境变量
#### MAKEFILES
如果当前环境定义了一个 "MAKEFILES" 环境变量，make 执行时首先将变量的值作为需要读入的 Makefile 文件，多个文件之间使用空格分开。

类似使用指示符 "include" 包含其它 Makefile 文件一样。

#### MAKEFILES_LIST
make 在读取多个 Makefile 文件时，包括由环境变量 "MAKEFILES" 指定、命令行指定、当前工作下默认以及使用指示符 "include" 指定包含的，在对这些文件进行解析执行之前 make 读取的文件名将会被自动依次追加到变量 "MAKEFILES_LIST" 的定义域中。

#### VPATH
指定依赖文件的搜索路径，当规则的依赖文件在当前目录不存在时，make 会在此变量所指定的目录下去寻找这些依赖文件。其实，"VPATH" 变量所指定的是 Makefile 中所有文件的搜索路径，包括了规则的依赖文件和目标文件。

定义变量 "VPATH" 时，使用空格或者冒号（:）将多个需要搜索的目录分开。例如：

```makefile
VPATH = src:../headers
```
这样，就为所有规则的依赖指定了两个搜索目录，"src" 和 "../headers"。

#### SHELL
make 对所有规则命令的解析使用环境变量 "SHELL" 所指定的那个程序，在 GNU make 中，默认的程序是 "/bin/sh"。

#### MAKE
在使用 make 的递归调用时，在 Makefile 规则的命令行中应该使用变量 "MAKE" 来代替直接使用 "make"。例如：

```makefile
subsystem:
	cd subdir && $(MAKE)
```

变量 "MAKE" 的值是 "make"。如果其值为 "/bin/make" 那么上边规则的命令就是 "cd subdir && /bin/make"。
好处是，当我们使用一个其它版本的 make 程序时，可以保证最上层使用的 make 程序和其子目录下执行的 make 程序保持一致。

#### MAKELEVEL
在多级递归调用的 make 执行过程中，变量 "MAKELEVEL" 代表了调用的深度。在 make 一级级的执行过程中变量 "MAKELEVEL" 的值不断发生变化。

最上一级 "MAKELEVEL" 的值是 "0"、下一级是 "1"，再下一级是 "2"。

#### MAKEFLAGS
在 make 的递归过程中，最上层 make 的命令行选项如 "-k"、"-s" 等会被自动的通过环境变量 "MAKEFLAGS" 传递给子 make 进程。

传递过程中变量 "MAKEFLAGS" 的值会被主控 make 自动的设置为包含执行 make 时的命令行选项的字符串。

执行多级的 make 调用时，当不希望传递 "MAKEFLAGS" 给子 make 时，需要再调用子程序 make 对这个变量进行赋空，例如：

```makefile
subsystem:
	cd subdir && $(MAKE) MAKEFLAGS=
```

#### MAKECMDGOALS
make 在执行时，设置一个特殊变量 "MAKECMDGOALS"，此变量记录了命令行参数指定的终极目标列表，没有通过参数指定终极目标时，此值为空。

例如，使用变量 "MAKECMDGOALS" 来判断命令行参数是否指定终极目标为 "clean"，如果不是才包含。

```makefile
sources = foo.c bar.c
ifneq($(MAKECMDGOALS),clean)
	include $(sources:.c=.d)
endif
```

#### CURDIR
在 make 递归调用中，变量 "CURDIR" 代表 make 的工作目录。当使用 "-C" 选项进入一个子目录后，此变量将被重新赋值。

#### .SUFFIXES
特殊目标 `.SUFFIXES` 的所有依赖指出了一系列在后缀规则中需要检查的后缀名。例如，把后缀 ".hack" 和 ".win" 加入到可识别后缀列表的末尾。

```makefile
.SUFFIXES:.hack .win
```

若需要重设置默认的可识别后缀，如下

```makefile
.SUFFIXES            #删除所有已定义的可识别后缀
.SUFFIXES:.c .o .h   #重新定义
```

#### .LIBPATTERNS
变量 `.LIBPATTERNS` 就是告诉链接器在执行链接过程中，对于出现 `-INAME` 的文件如何展开。

".LIBPATTERNS" 的值一般是多个包含模式字符（%）的字（一般不包含空格的字符串），多个字之间使用空格分开。

也可以将此变量置空，取消链接器对 "-INAME" 格式的展开。

## make 自动变量
#### $@
表示规则的目标文件名。如果目标是一个文档文件（linux下，一般称.a文件为文档文件，也称为静态库文件），那么它代表这个文档的文件名。在多目标模式规则中，它代表的是那个触发规则被执行的目标文件名。

#### $%
当规则的目标文件是一个静态库时，代表静态库的一个成员名。例如，规则的目标是 `foo.a(bar.o)`，那么， `$%` 的值就为 "bar.o"，`$@` 的值就是 "foo.a"。如果目标文件不是静态库文件，其值为空。

#### $<
目标依赖列表中的第一个依赖文件名。如果是一个目标文件使用隐含规则来重建，则它代表由隐含规则加入的第一个依赖文件。

#### $?
所有比目标文件更新的依赖文件列表，即最新被修改过的文件。空格分割。如果目标是静态库文件名，代表的是库成员(.o 文件)。

#### $^
规则的所有依赖文件列表，使用空格分隔。如果目标是静态库文件，它所代表的只能是所有库成员(.o 文件)名。一个文件可重复的出现在目标的依赖中，变量 `$^` 只记录它的一次引用情况。就是说变量 `$^` 会去掉重复的依赖文件。

#### $+
类似 `$^`，但是它保留了依赖文件中重复出现的文件。主要用在程序链接时库的交叉引用场合。

#### $*
在模式规则和静态模式规则中，代表“茎”。“茎”是目标模式中“%”所代表的部分（当文件名中存在目录时，“茎”也包含目录（斜杠之前）部分），例如：文件 "dir/a.foo.b"，当目标的模式是 “a.%.b” 时，`$*` 的值为 "dir/a.foo"。“茎” 对于构造相关文件名非常有用。

#### $(@D)
表示目标文件的目录部分（不包括斜杠）。如果 `$@` 是 "dir/foo.o"，那么 `$(@D)` 的值为 "dir"。如果 `$@` 不存在斜杠，其值就是 "."（当前目录）。

#### $(@F)
目标文件的完整文件名中除目录以来的部分（实际文件名）。如果 `$@` 为 "dir/foo.o"，那么 `$(@F)` 只就是 "foo.o"

#### $(*D)
#### $(*F)
分别代表目标 "茎" 中的目录部分和文件名部分。

#### $(%D)
#### $(%F)
当以如 "archive(member)" 形式静态库为目标时，分别表示库文件成员 "member" 名中的目录部分和文件名部分。它仅对这种形式的规则目标有效。

#### $(<D)
#### $(<F)
分别表示规则中第一个依赖文件的目录部分和文件名部分。

#### $(^D)
#### $(^F)
分别表示所有依赖文件的目录部分和文件部分（不存在同一文件）。

#### $(+D)
#### $(+F)
分别表示所有依赖文件的目录部分和文件部分（可存在重复文件）。

#### $(?D)
#### $(?F)
分别表示被更新的依赖文件的目录部分和文件部分。

## 预定义变量
- `RM` => `rm -f`
- `AR` => `ar`
- `CC` => `cc`
- `CXX` => `g++`
- `CPPFLAGS` => C 预处理器选项
- `CFLAGS` => C 编译器选项
- `LDFLAGS` => 链接器选项
- `ARFLAGS` => AR 命令选项
- `CXXFLAGS` => C++ 编译器选项

## 通配符
- `*` 表示任意一个或多个字符
- `?` 表示任意一个字符
- `[abcd]` 表示 a,b,c,d 中任意一个字符 
- `[^abcd]` 表示除 a,b,c,d 以外的字符
- `[0-9]` 表示 0~9 中任意一个数字

# 指示符
## define 多行定义
定义一个包含多行字符串的变量，利用这个特点，可以实现一个完整命令包的定义。
```makefile
bar = abcd
define two-lines
	@echo foo
	@echo $(bar)
endef
all:
	@$(two-lines)
```

## 条件判断
所有使用条件语句在产生分支的地方，make 程序会根据预设条件将正确的分支展开，就是说条件分支展开是"立即"的。其中包含：ifdef、ifeq、ifndef 和 ifneq 所确定的所有分支命令。

其中，有三个关键字：ifeq、else 和 endif。具体说明如下：
- `ifeq` 表示条件语句的开始，并指定一个比较条件（相等）。括号和关键字之间要使用空格分隔，两个参数之间要使用逗号分隔。参数中的变量引用在进行变量值比较时被展开。ifeq 之后是当条件满足时，make 需要执行的部分，条件不满足时忽略。
- `else` 之后是当条件不满足时的执行部分，不是所有的条件语句都要执行此部分。
- `endif` 是条件语句的结束标志，任何一个条件表达式都必须以 endif 结束。

条件判断语句（包含 else 和 endif）可以以若干空格开始，make 处理时会忽略这些空格。但不能以 [Tab] 字符作为开始，否则就被认为是命令。

#### ifeq
此关键字用来判断参数是否相等，格式如下：
```makefile
ifeq (A, B)
ifeq 'A' 'B'
ifeq "A" "B"
	TEXT-IF-TRUE
else
	TEXT-IF-FALSE
endif
```

#### ifneq
此关键字实现的条件判断语句和 ifeq 相反，格式如下：
```makefile
ifneq (A, B)
ifneq 'A' 'B'
	TEXT-IF-TRUE
else
	TEXT-IF-FALSE
endif
```

#### ifdef
此关键字用来判断一个变量是否已定义，格式如下：
```makefile
ifdef VARIABLE
	TEXT-IF-TRUE
else
	TEXT-IF-FALSE
endif
```

#### ifndef
此关键字实现功能和 ifdef 相反，格式如下：
```makefile
ifndef VARIABLE
	TEXT-IF-TRUE
else
	TEXT-IF-FALSE
endif
```

## 包含其它 Makefile
Makefile 中包含其它文件所需要使用的关键字是 `include`。

```makefile
include FILENAMES
```

"include" 指示符告诉 make 暂停读取当前的 Makefile，而转去读取 "include"指定的一个或者多个文件，读取完成后，再继续当前 Makefile 的读取。

FILENAMES 可以是当前操作系统 shell 的文件模式（可以包含路径和通配符）。

在 include 前面可以有若干空格，但是绝不能以 [Tab] 开始。

如果文件都没有指定绝对路径或相对路径，make 会在当前目录下首先查找，如果当前目录没有，make 还会在下面的几个目录下找：
- 如果 make 执行时，有 `-I` 或 `--include-dir` 参数，那么 make 就会出现在这个参数所指定的目录去寻找。
- 如果目录 prefix/include （一般为：usr/local/bin 或 usr/include）存在的话，make 也会去找。

如果没找到文件，make 会生成一条警告信息，但不会马上出现致命错误。它会继续载入其它文件，一旦完成 Makefile 的读取，make 会重新载入读取失败的文件，如果还是不行，make 才会出现一条致命信息。

## override
通常在执行 make 时，如果通过命令行定义了一个变量，那么它将替代在 Makefile 中出现的同名变量的定义。如果不希望命令行指定的变量值替代在 Makefile 中的变量定义，那么就需要在 Makefile 中使用指示符 `override` 来对变量进行声明。

## export 声明
上层 make 过程要将所执行的 Makefile 中的变量传递给子 make 过程，需要明确地指出。

在 GNU make 中，实现此功能的指示符是 `export`。当一个变量使用 `export` 进行声明后，变量和它的值将被加入到当前工作的环境变量中，以后在 make 执行的所有规则的命令都可以使用这个变量。

当没有使用指示符 export 对任何变量进行声明的情况下，上层 make 只将那些已经初始化的环境变量（在执行 make 之前已经存在的环境变量）和使用命令行指定的变量（如："make CFLAGS +=-g" 或者 "make -e CFLAGS +=-g"）传递给子 make 程序，通常这些变量由字符、数字和下划线组成。

在没有使用关键字 export 声明变量，make 执行时它们不会被自动传递给子make，因此下层 Makefile 中可以定义和上层同名的变量，不会引起变量定义冲突。

需要将一个在上层定义的变量传递给子 make，应该在上层 Makefile 中使用指示符 `export` 对此变量进行声明。格式如下：

```makefile
export VARIABLE ...
```

当不希望将一个变量传递给子 make 时，可以使用指示符 `unexport` 来声明这个变量。格式如下：

```makefile
unexport VARIABLE ...
```

## 目录搜索
一般搜索，采用变量 `VAPTH` 来完成。

另一个设置文件搜索路径的方法是使用 make 的 `vpath` 关键字（全小写）。它不是一个变量，而是一个 make 的关键字，它所实现的功能和 VPATH 类似，但是更为灵活。

它可以为不同类型的文件（由文件名区分）指定不同的搜索目录。使用方法有以下三种：

```makefile
# 为所有符合模式 "PATTERN" 的文件指定搜索目录 "DIRECTORIES"。多个目录使用空格或者冒号（:）分开。
vpath PATTERN DIRECTORIES

# 清除之前为符合模式 "PATTERN" 的文件设置的搜索路径。
vpath PATTERN

# 清除所有已被设置的文件搜索路径。
vpath
```

`PATTERN` 表示了具有相同特征的一类文件，而 `DIRECTORIES` 则指定了搜索此类文件目录。当规则的依赖文件列表中的文件不能在当前目录下找到时，make 程序将依次在 `DIRECTORIES` 所描述的目录下找此文件。

# 模式规则
模式字符 `%` 表示匹配一个或者多个字符。

在 Makefile 中，所有的模式匹配中使用 `%` 替代 `*`。

```makefile
.PHONY: clean
CC = gcc
RM = rm
EXE = simple
OBJS = main.o foo.o
$(EXE): $(OBJS)
	$(CC) -o $@ $^
%.o: %.c
	$(CC) -o $@ -c $^
clean:
	$(RM) $(EXE) $(OBJS)
```

# 函数
## 文本处理
#### 字符串替换函数 subst
```makefile
# 语法：$(subst FROM, TO, text)
# 功能：把 text 中的 FROM 替换为 TO
# 返回：替换后的新字符串
TEST = "feet on the street"
all:
	@echo $(TEST)
	@echo $(subst ee, EE, $(TEST))
```

#### 模式替换函数 patsubst
```makefile
# 语法：$(patsubst PATTERN, REPLACEMENT, TEXT)
# 功能: 把 TEXT 中的的每个满足 PATTERN 字符串的替换为 REPLACEMENT
# 返回：替换后的新字符串
all:
	@echo $(patsubst %.c, %.o, programA.c programB.c)
```

搜索 TEXT 中以空格分开的单词，将符合模式 PATTERN 替换为 REPLACEMENT。参数 PATTREN 中可以使用模式通配符 `%` 来代表一个单词中的若干字符。

在 PATTREN 和 REPLACEMENT 中，只有第一个 `%` 被称为模式字符来处理，之后出现的不再作为模式字符（作为一个字符）。

在参数中如果需要将第一个出现的 `%` 作为字符本身而不作为模式字符时，可使用反斜杠 `\` 进行转义处理。

#### 去空格函数 strip
```makefile
# 语法：$(strip STRING)
# 功能: 去掉 STRING 字符串中开头和结尾的空字符，并将其中多个连续空字符合并为一个字符
# 返回：无前导和结尾空字符、使用单一空格分割的多单词字符串
VAL := "    aa   b  cc "
all:
	@echo "去除空格前: " $(VAL)
	@echo "去除空格后: " $(strip $(VAL))
```

#### 查找字符串函数 findstring
```makefile
# $(findstring FIND, TEXT)
# 功能: 搜索字符串 TEXT 中查找 FIND 字符串，TEXT 中可以包含空格、[TAB]
# 返回: 如果找到, 返回 FIND 字符串, 否则返回空字符串
VAL := "   aa  bb cc "

all:
	@echo $(findstring aa,$(VAL))
```

#### 过滤函数 filter
```makefile
# 语法：$(filter PATTERN..., TEXT)
# 功能：保留符合此模式的字符串，可以使用多个模式，模式表达式之间使用空格分割
# 返回：空格分割的 TEXT 字符串中所有符合模式 PATTERN 的字符串
cc = gcc
sources := test1.c test2.c test3.s test4.h
all: $(sources)
	$(cc) $(filter %.c %.s, $(sources)) -o test
```

#### 反过滤函数 filter-out
```makefile
# 语法：$(filter-out PATTERN..., TEXT)
# 功能：和 filter 实现功能相反。保留所有不符合此模式的字符串
# 返回：空格分割的 TEXT 字符串中所有不符合模式 PATTERN 的字符串
	@echo $(filter-out %.o %.a,program.c program.o program.a)
```

#### 排序函数 sort
```makefile
# 语法：$(sort LIST)
# 功能：给 LIST 中的字符串以字母为准进行排序（升序），并去掉重复的单词
# 返回：空格分割的没有重复单词的字符串
list = foo bar lose foo
all:
	@echo $(sort $(list))
```

#### 取单词函数 word
```makefile
# 语法：$(word N,LIST)
# 功能：取字符串 LIST 中第 N 个字符串，N 从 1 开始
# 返回：返回字符串 LIST 中第 N 个字符串
# 说明：如果 N 值大于字串 LIST 中字符串的数目，返回空字符串。如果 N 为 0，出错。
list = foo bar lose foo
all:
	@echo $(word 2, $(list))
```

#### 统计单词数目函数 words
```makefile
# 语法：$(words LIST)
# 功能：计算 LIST 中单词的数目
# 返回：LIST 中的单词数
list = foo bar lose foo
all:
	@echo $(words $(list))
```

#### 取字符串函数 wordlist
```makefile
# 语法：$(wordlist S,E,TEXT)
# 功能：从 TEXT 中取出从 S 开始到 E 的单词串。S 和 E 表示单词在字串中位置的数字。
# 返回：字串 TEXT 中从第 S 到 E（包括 E）的单词字串。
# 说明：S 和 E 都是从 1 开始的数字。如果 E 大于 TEXT 的数字，则返回从 S 开始，到 TEXT 结束的单词串；如果 S 大于 E 的数字，返回空。
list = foo bar lose foo
all:
	@echo $(wordlist 2,3, $(list))
```

#### 取首单词函数 firstword
```makefile
# 语法：$(firstword NAMES...)
# 功能：取字符串 NAMES 中的第一个单词
# 返回：字符串 NAMES 的第一个单词
list = foo bar lose foo
all:
	@echo $(firstword $(list))
```

## 文件名处理函数
#### 取目录函数 dir
```makefile
# 语法：$(dir NAMES...)
# 功能: 取出各个文件名的目录部分
# 返回: 空格分割的文件名序列 NAMES... 中每一个文件的目录部分
# 说明：如果文件名中没有斜线，认为此文件为当前目录（"./"）下的文件。
# 输出：/home ./ ../ ./
	@echo $(dir /home/a.c ./bb.c ../c.c d.c)
```

#### 取文件名函数 notdir
```makefile
# 语法：$(notdir NAMES...)
# 功能: 删除所有文件名中的目录部分，只保留非目录部分
# 返回: 文件名序列 NAMES... 中每一个文件的非目录部分
all:
# 输出 a.c bb.c c.c d.c
	@echo $(notdir /home/a.c ./bb.c ../c.c d.c)
```

#### 取前缀函数 basename
```makefile
# 语法：$(basename NAMES...)
# 功能: 从文件名序列 NAMES... 中取出各个文件名的前缀部分。前缀部分指的是文件名中最后一个点号之前的部分。
# 返回: 空格分割的文件名序列 NAMES... 中各个文件的前缀序列。如果文件没有前缀，则返回空字符串。
# 输出：/home/a ./b ../c /home/
	@echo $(basename /home/a.c ./b.o ../c.a /home/.d .e)
```

#### 取后缀函数 suffix
```makefile
# 语法：$(suffix NAMES...)
# 功能: 从文件名序列 NAMES... 中取出各个文件名的后缀。后缀是文件名中最后一个以点 "." 开始的（包含点号）部分，如果文件名中不包含一个点号，则为空。
# 返回: 以空格分割的文件名序列 NAMES... 中每一个文件的后缀序列。
all:
# 输出: .c .o .a
	@echo $(suffix /home/a.c ./b.o ../c.a d)
```

#### 加前缀函数 addprefix
```makefile
# 语法：$(addprefix PREFIX, NAMES...)
# 功能: 为 NAMES... 中的每一个文件名添加前缀 PREFIX。参数 NAMES... 是空格分割的文件名序列，将 SUFFIX 添加到此序列的每一个文件名之前。
# 返回: 以单空格分割的添加了前缀 PREFIX 的文件名序列。
# 输出：test_/home/a.c test_b.c test_./d.c
	@echo $(addprefix test_,/home/a.c b.c ./d.c)
```

#### 加后缀函数 addsuffix
```makefile
# 语法：$(addsuffix SUFFIX,NAMES...)
# 功能: 为 NAMES... 中的每一个文件名添加后缀 SUFFIX。参数 NAMES... 为空格分割的文件名序列，将 SUFFIX 追加到此序列的每一个文件名的末尾。
# 返回: 以单空格分割的添加了后缀 SUFFIX 的文件名序列。
# 输出：/home/a.c b.c ./c.o.c ../d.c.c
all:
	@echo $(addsuffix .c,/home/a b ./c.o ../d.c)
```

#### 单词连接函数 join
```makefile
# 语法：$(join LIST1,LIST2)
# 功能: 将字符串 LIST1 和字串 LIST2 各单词进行对应连接。
# 返回: 单空格分割的合并后的字（文件名）序列。
# 说明：如果 LIST1 和 LIST2 中的字数目不一致时，两者中多余部分将被作为返回序列的一部分。
# 输出：a.c b.o c
all:
	$(join a b c,.c .o)
```

#### 获取匹配模式文件名函数 wildcard
```makefile
# 语法：$(wildcard PATTERN)
# 功能：列出当前目录下所有符合模式 PATTERN 的文件名
# 返回：空格分割的、存在当前目录下的所有符合模式 PATTREN 的文件名。
	@echo $(wildcard *.c)
```

## make 控制函数
#### foreach 函数
```makefile
# 语法：$(foreach VAR, LIST, TEXT)
# 功能：把 list 中的单词逐一取出放到 var 变量中，然后再执行 text 表达式。
#       每次 text 会返回一个字符串，循环过程中，text 所返回的每个字符串会以空格分隔。
#       当循环结束时，返回的每个字符串所组成的整个字符串（以空格分隔）
# 返回：空格分割的多次表达式 TEXT 的计算的结果。
name := a b c d
files:= $(foreach n,$(names),$(n).o)
all:
# 输出：a.o b.o c.o d.o
	@echo $(files)
```

如果需要（存在变量或函数的引用），首先展开变量 VAR 和 LIST 的引用；而表达式 TEXT 中的变量引用不展开。
执行时把 LIST 中使用空格分割的单词依次取出赋值给变量 VAR，然后执行 TEXT 表达式。重复直到 LIST 的最后一个单词（为空时结束）。

TEXT 中的变量或者函数引用在执行时才被展开，因此如果在 TEXT 中存在对 VAR 引用，那么 VAR 的值在每一次展开式将会得到不同的值。

#### if 函数
```makefile
# 语法：$(if CONDITION, THEN-PART[,ELSE-PART])
# 功能：如果 CONDITION 非空，条件为真，执行 THEN-PART，否则执行 ELSE-PART
# 返回：根据条件决定函数的返回值是第一个或者第二个参数表达式的计算结果。当不存在第三个参数 ELSE-PART ，并且 CONDITION 展开为空，函数返回空。
SUBDIR += $(if $(SRC_DIR) $(SRC_DIR), /home/src)
```

#### call 函数
`call` 函数是唯一一个可以创建定制化参数函数的引用函数。使用这个函数可以实现对用户自己定义函数引用。可以将一个变量定义为一个复杂的表达式，用 call 函数根据不同的参数对它进行展开开获得不同的结果。

```makefile
# 语法：$(call VARIABLE,PARAM,PARAM,...)
# 功能：在执行时，将它的参数 PARAM 依次赋值给临时变量 $(1)、$(2)……（这些临时变量定义在 VARIABLE 的值中）。call 函数对参数的数目没有限制，也可以没有参数值，没有参数值的 call 没有任何实际存在的意义。变量 $(0) 代表变量 VARIABLE 本身。
# 返回：参数值 PARAM 依次替换 $(1)、$(2)... 之后变量 VARIABLE 定义的表达式的计算值。
# 输出：b a
reverse = $(2) $(1)
all:
	@echo $(call reverse,a,b)
```

1. 函数中 VARIABLE 是一个变量名，而不是变量引用。因此，通常 call 函数中的 VARIABLE 中不包含 `$`（当然，除非此变量名是一个计算的变量名）。
2. 当变量 VARIABLE 是一个 make 内嵌的函数名时（如 "if"、"foreach"、"strip" 等），对 PARAM 参数的使用需要注意，因为不合适或者不正确的参数将会导致函数的返回值难以预料。
3. 函数中多个 PARAM 之间使用逗号分隔。
4. 变量 VARIABLE 在定义时不能定义为直接展开式，只能定义为递归展开式。

#### value 函数
提供一种在不对变量进行展开的情况下获取变量值的方法。

```makefile
# 语法：$(value VARIABLE)
# 功能：不对变量 VARIABLE 进行任何展开操作，直接返回变量 VARIABLE 的值。这里 VARIABLE 是一个变量名，一般不包含 $（除非计算的变量名）。
# 返回：变量 VARIABLE 所定义文本值。如果变量定义为递归展开式，其中包含对其他变量或者函数的引用，那么函数不对这些引用进行展开。函数的返回值是包含有引用值。
FOO = $PATH
all:
    # ATH ($P 为空)
	@echo $(FOO)
    # $PATH
	@echo $(value FOO)
```

#### eval 函数
函数 eval 是一个比较特殊的函数。使用它可以在 Makefile 中构造一个可变的规则结构关系（依赖关系链），其中可以使用其他变量和函数。

函数 eval 对它的参数进行展开，展开的结果作为 Makefile 的一部分，make 可以对展开内容进行语法解析。展开的结果可以包含一个新变量、目标、隐含规则或者是明确规则等。

也就是说，此函数的功能主要是：根据其参数的关系、结构，对它们进行替换展开。

eval 函数执行时会对它的参数进行两次展开。第一次展开过程是由函数本身完成的，第二次是函数展开后的结果被称作为 Makefile 内容时由 make 解析时展开的。

```makefile
PROGRAMS = server client
server_OBJS = server.o server_priv.o server_access.o
server_LIBS = priv protocol
client_OBJS = client.o client_api.o client_mem.o
client_LIBS = protocol
 
# Everything after this is generic
.PHONY: all
all: $(PROGRAMS)
 
define PROGRAM_template
$(1): $$($(1)_OBJ) $$($(1)_LIBS:%=-l%)
ALL_OBJS += $$($(1)_OBJS)
endef
 
$(foreach prog,$(PROGRAMS),$(eval $(call PROGRAM_template,$(prog))))
 
$(PROGRAMS):
	$(LINK.o) $^ $(LDLIBS) -o $@
 
clean:
	rm -f $(ALL_OBJS) $(PROGRAMS)
```

它实现的功能是完成 PROGRAMS 的编译链接。例子中，$(LINK.o) 为 $CC $(LDFLAGS)，意思是对所有的 .o 文件和指定的库文件进行链接。

```makefile
$(foreach prog,$(PROGRAMS),$(eval $(call PROGRAM_template,$(prog))))
 
# 展开为：
 
server : $(server_OBJS) –l$(server_LIBS)
client : $(client_OBJS) –l$(client_LIBS)
```

#### origin 函数
```makefile
# 语法：$(origin VARIABLE)
# 功能：查询参数 VARIABLE 的出处
# 返回：返回 VARIABLE 的定义方式，用字符串表示
```

返回值类型：
- `undefined` 变量 VARIABLE 没被定义。
- `default` 变量是默认定义（内嵌变量），如：CC、MAKE、RM等变量。如果在 Makefile 中重新定义这些变量，函数返回值将相应发生变化。
- `environment` 变量是一个系统环境变量，并且 make 没有使用命令行选项 -e
- `environment override` 变量是一个系统变量，并且 make 使用了命令行选项 -e
- `file` 变量是在某个 makefile 文件中定义
- `command line` 变量是在命令行中定义
- `override` 变量是在 makefile 文件中定义并使用 override 指示符声明
- `automatic` 变量是自动化变量

#### shell 函数
函数 `shell` 所实现的功能和 shell 中的引用（``）相同。

进行函数展开式时，它所调用的命令（它的参数）得到执行；除对它的引用出现在规则的命令行和递归变量的定义中之外，其它绝大多数情况下，make 是读取解析 Makefile 时完成对函数 shell 的展开。

```makefile
# 语法：$(shell <shell command>)
# 返回：函数 shell 的参数（一个 shell 命令）在 shell 环境中的执行结果。
contents := $(shell cat test1.c)
all:
	echo $(contents)
```

#### $(error TEXT...)
产生致命错误，并提示 TEXT... 信息给用户，并退出 make 的执行。

说明：error 函数是在函数展开式（函数被调用时）才提示信息并结束 make 进程。因此，如果函数出现在命令中或者一个递归的变量定义时，在读取 Makefile 时不会出现错误，而只有包含 error 函数的引用的命令被执行，或者定义中引用此函数的递归变量被展开时，才会提示致命信息 TEXT... 同时退出 make。

```makefile
ERROR1 = 'test'
 
ifdef ERROR1
contents = $(error error is $(ERROR1))
endif
```
make 读取解析 Makefile 时，如果已经定义变量 ERROR1，make 将会提示致命错误信息 $(ERROR1)，并退出。

#### $(warning TEXT...)
函数 warning 类似于函数 error，区别在于它不会导致致命错误（make 不会退出），而只是提示 TEXT...，make 的执行过程继续。

# 特别注意
1. 一行 command 启动一个 sub shell，前一行命令导致环境的变化在下一行重置。