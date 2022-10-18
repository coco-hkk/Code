# PowerShell
PowerShell 是一种跨平台的任务自动化解决方案，由命令行 shell、脚本语言和配置管理框架组成。 PowerShell 在 Windows、Linux 和 macOS 上运行。

英文文档：https://learn.microsoft.com/en-us/powershell/module/cimcmdlets/?view=powershell-7.2。
中文文档：https://learn.microsoft.com/zh-cn/powershell/scripting/overview?view=powershell-7.2

PowerShell 随附数百个预安装命令。 PowerShell 命令称为 cmdlet；读作“command-lets”。
每个 cmdlet 的名称都包含一个“谓词-名词”对。 例如 Get-Process。

# Get-ChildItem
获取一个或多个指定位置中的项和子项。类似指令 `ls`。

```powershell
# 显示指定目录中的文件和目录的详细信息
Get-ChildItem -Path C:\Test
# 显示指定目录中的文件和目录名
Get-ChildItem -Path C:\Test -Name
# 显示当前目录和子目录中 .txt 文件
# Recurse 参数搜索路径目录的子目录，Force 参数显示隐藏的文件
Get-ChildItem -Path C:\Test\*.txt -Recurse -Force
```

# Test-Path
确定指定路径是否存在。判断目录或文件是否存在。

```powershell
# 测试路径，用来判断目录或文件是否存在，成功返回 $True，失败返回 $False
Test-Path -Path "C:\Test"
# 测试值为 null
Test-Path $null
```

# New-Item
创建新项。创建新目录或文件。

```powershell
# 在当前目录中创建文件
New-Item -Path . -Name "newfile.txt" -ItemType "file" -Value "This is a text string."
# 创建目录
New-Item -Path . -Name "newdir" -ItemType "directory"
```

# Rename-Item
重命名 PowerShell 提供程序命名空间中的项。重命名文件或目录。

```powershell
# 重命名文件
Rename-Item -Path "old.txt" -NewName "new.txt"
# 移动文件
Rename-Item -Path "project.txt" -NewName "d:\test\project.txt"
# 批量重命名，将当前目录中所有 .txt 替换为 .log
# $_ ，自动变量表示每个文件对象
Get-ChildItem *.txt | Rename-Item -NewName { $_.Name -replace '.txt', '.log'}
```

# Move-Item
将项从一个位置移动到另一个位置。移动文件或重命名文件。

```powershell
# 将 test.txt 移动到另一个目录并将其重命名
Move-Item -Path C:\test.txt -Destination E:\Temp\tst.txt
```

# Remove-Item
删除指定项。删除文件或目录。

```powershell
# 删除当前目录中所有 .txt 文件
Remove-Item *.txt
# 从当前目录中删除 .doc 文件，但不包含 *1* 的名称的所有文件
Remove-Item * -Include *.doc -Exclude *1*
# 删除隐藏和只读的文件，如果没有 Force 则无法删除只读和隐藏的文件。
Remove-Item -Path hidden-RO-file.txt -Force
# 删除非空目录，需要 Recurse 选项
Remove-Item C:\test -Recurse
```

# Copy-Item
将项从一个位置复制到另一个位置。

```powershell
# 将文件 test.txt 复制到指定目录
Copy-Item "test.txt" -Destination "C:\Presentation"
# 将目录和内容复制到新目录
Copy-Item -Path "C:\Test" -Destination "C:\NewTest" -Recurse
```