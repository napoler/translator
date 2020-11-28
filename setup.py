# -*- coding: utf-8 -*-
from setuptools import find_packages, setup
from os import path as os_path
import time
this_directory = os_path.abspath(os_path.dirname(__file__))

# 读取文件内容
def read_file(filename):
    with open(os_path.join(this_directory, filename), encoding='utf-8') as f:
        long_description = f.read()
    return long_description

# 获取依赖
def read_requirements(filename):
    return [line.strip() for line in read_file(filename).splitlines()
            if not line.startswith('#')]
# long_description="""

# 这里是说明
# 一个翻译接口
# https://www.terrychan.org/translator/
# """

long_description=read_file("README.md")
setup(
    name='tkitTranslator', #修改包名字
    version='0.1.2',
    description='Terry tkitTranslator 翻译',
    author='Terry Chan',
    author_email='napoler2008@gmail.com',
    url='https://www.terrychan.org/translator/',
    # install_requires=read_requirements('requirements.txt'),  # 指定需要安装的依赖
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        'requests==2.22.0',


    ],
    packages=['tkitTranslator'])

"""
pip freeze > requirements.txt

python3 setup.py sdist
#python3 setup.py install
python3 setup.py sdist upload
"""
