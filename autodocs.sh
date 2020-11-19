#! /usr/bin/bash

# 自动构建脚本
# 文档 http://www.pythondoc.com/sphinx/tutorial.html


#安装
pip install -U Sphinx
#安装主题
pip install sphinx_rtd_theme

#
#清理之前生成的文档
rm -rf ./res/
sphinx-apidoc -o ./res ./src

#编译成为html
#make html
sphinx-autobuild ./source ../docs --open-browser
# 推送命令
git add .
git commit -m "auto更新文档"
git pull
git push
