
#encoding=utf-8
from __future__ import unicode_literals
import sys
# 切换到上级目录
sys.path.append("../")
# 引入本地库
import src
text="""The effect of such changes is unpredictable. If you want to break a for loop before its normal termination, use break."""
Demo =src.Translator()
print(Demo.render(text))


text2="""
本项目每天抓取「阅读」官方微信公众号中分享的优质精品书源，制作成一个单独的书源文件，方便大家一键导入！
彻底解决了「阅读」官方公众号每次更新都需要打开微信手动复制导入的痛点了！现在只需要定期重复导入该书源（二维码或URL）即可，省时省力！

    为了避免阅读作者打爆我的狗头，所以... 「阅读」官方微信公众号：「开源阅读软件」

更新日志：

    更新： 网站域名。
    新增： 阅读3.0书源。
    新增： 校验书源功能。
    —— 脚本会把无法访问的书源网站去除。
    —— 该功能对于那些书源规则失效（而不是书源网站挂了）的书源是无效的，所以依然可能存在小部分失效书源。
    修复： 昨天脚本新抓取的书源有问题，已经修复了格式不对的问题（以后每次更新前会先检查JSON格式是否正确再更新）。
    新增： 历史书源文件：https://yuedu.xiu2.xyz/old
    新增： 网站将显示书源更新时间及数量。

软件介绍：

「阅读」我就不多介绍了，我见过不少人安利，我直接贴酷安的介绍吧。
"""




print(Demo.render(text2))
