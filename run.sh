#! /usr/bin/bash
#"""
#使用docker运行splash

#https://splash-cn-doc.readthedocs.io/zh_CN/latest/faq.html?highlight=timeout#i-m-getting-lots-of-504-timeout-errors-please-help

#"""


sudo docker run -p 8050:8050 -p 5023:5023 scrapinghub/splash --max-timeout 3600 
