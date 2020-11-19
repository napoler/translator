#! /usr/bin/bash

# 自动构建脚本



#
sphinx-apidoc -o ./source ../src

#编译成为html
make html

# 推送命令
git add .
git commit -m "auto更新文档"
git pull
git push
