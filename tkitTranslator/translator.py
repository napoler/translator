# -*- coding: utf-8 -*-
"""
一个爬取翻译结果的类

"""
import requests
import json

class Translator:
    """
    一个爬取deepl翻译结果的类
    需要安在splash使用，建议使用docker
    
    >>> from tkitTranslator import  Translator
    >>> T = Translator()

    """
    def __init__(self,hosts="http://localhost:8050",proxy=None):
        """
        预定义服务器数据
        proxy 为sudo docker run -d --name splash -p 8050:8050 -v /mnt/data/dev/github/translator/proxy:/etc/splash/proxy-profiles -p 5023:5023  scrapinghub/splash --max-timeout 3600 
        /mnt/data/dev/github/translator/proxy里的配置文件名称
        更多资料查看：
        https://github.com/napoler/napoler.github.io/blob/master/_posts/2020-12-10-slpash%E5%90%AF%E7%94%A8tor%E4%BB%A3%E7%90%86.md
        """
        self.hosts=hosts
        self.proxy=proxy
    def E_trans_to_C(self,string):
        """英文标点转换微中文标点
        
        """
        E_pun = u',.!?[]()<>"\''
        C_pun = u'，。！？【】（）《》“‘'
        table= {ord(f):ord(t) for f,t in zip(E_pun,C_pun)}
        return string.translate(table)
    def render(self,text='hello word'):
        """
        解析数据函数
        这里只需要传入text需要翻译的数据即可
        """
        api=self.hosts+"/execute"
        text=self.E_trans_to_C(text)
        #这里写lua脚本
        if len(text)==0:
            print("翻译内容为空")

            return {}
        lua_source='''function main(splash, args)
	  splash:set_custom_headers({
	   ["Accept-Language"] = "zh,zh-CN;q=0.5"
		})
	  assert(splash:go(args.url))
	  assert(splash:wait(0.5))
	  local input = splash:select('.lmt__source_textarea')
	  input:mouse_click()
	  input:send_text([[ '''+text+''' ]])
	  input:mouse_click()
      local data = splash:select('#target-dummydiv')
     --循环最多一百次
        for i=1000,1,-1 do
            splash:wait(0.5)
            --如果获取到数据则退出
            if data.node.innerHTML~= nil then
                break
            end
        end

	  --assert(splash:wait(25.5))
	  --local data = splash:select('#target-dummydiv')
	  --return data.node.innerHTML

	  return {
	    --html = splash:html(),
	    --html = data.node.innerHTML,
        data = data.node.innerHTML,
	    --png = splash:png(),
	    --har = splash:har(),
	  }
	  --]]
	end'''
        # print(lua_source)
        #exit();


        args={
            "url":"https://www.deepl.com/translator",
            "timeout":360,
           #"html":1,
            #"wait":0.5,
            "lua_source":lua_source

        }
        if self.proxy!=None:
            args["proxy"]=self.proxy

        # response =requests.get(api,params=args)
        response =requests.post(api,json= args)
        try:
            return response.json()
        except:
            return response.text



        pass
    def fun(self):
        print("fun run!")
        pass
