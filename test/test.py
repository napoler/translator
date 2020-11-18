
#encoding=utf-8
from __future__ import unicode_literals
import sys
# 切换到上级目录
sys.path.append("../")
# 引入本地库
import src

Demo =src.Translator()
print(Demo.render("hell word"))

