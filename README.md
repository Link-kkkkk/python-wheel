# python-wheel

Some python study note

#### virtualenv
virtualenv提供虚拟python环境

生成一个虚拟环境的项目

    virtualenv <project-name>

生成一个python3项目

    virtualenv <project-name> <python3环境路径>

项目不会获取系统中的第三方包

    virtualenv <project-name> --no-site-packages

在项目中执行以下命令即可启用环境
启用之后命令提示符会有一个（venv）的前缀

    source ./bin/activate

退出虚拟环境

    deactivate   