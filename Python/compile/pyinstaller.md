# Pyinstaller
Pyinstaller 把 Python 程序打包为一个可执行文件或一个文件夹，Windows 下还可以设置可执行文件的图标！

Pyinstaller 打包时会生成 `build` 和 `dist` 目录，以及一个 `.spec` 配置文件。

- `build` 是打包过程中产生的临时文件，再执行一次会直接使用它作为缓存。
- `dist` 存放最终生成的可执行文件或文件夹。
- `.spec` 执行打包命令后自动创建。可直接修改此文件，此后打包就可直接使用 `pyinstaller xxx.spec`。

实用参数：
- `--clean` 在本次编译开始时，清空上一次编译生成的各种文件。即清空 `build` 目录里的文件。
- `-y` 如果 `dist` 文件夹内已经存在生成文件，则不询问用户直接覆盖。
- `-w`, `--windowed`, `--noconsole` 去掉命令行（只针对 windows 系统）
- `--key` 指定密码来增加反编译难度，需要 `tinyaes`
- `-n` 指定可执行文件名
- `-i` 设置图标，指定图标路径，使用 ico 格式（只针对 windows 系统）
- `-F`, `--onefile` 打包成一个可执行文件
- `-D`, `--onedir` 打包成一个文件夹
- `-p` 搜索导入的路径，指定虚拟环境。允许使用多个路径，以 `;` 分隔（Windows 使用分号，Linux 使用冒号）或使用此选项多次。
- `--add-data` 打包额外资源。对应的是 `.spec` 中 `Analysis` 的 `datas`。
- `--specpath` 指定 `spec` 文件生成路径
- `--dispath` 指定 `dist` 路径
- `--workpath` 指定 `build` 路径
- `upx-dir` 指定 upx 程序的位置

# .spec 详解