# -*- coding: utf-8 -*-
"""
一个爬取翻译结果的类

"""
import requests

class Translator:
    def __init__(self,hosts="http://localhost:8050"):
        self.hosts=hosts
    def render(self,text='hello word'):
        api=self.hosts+"/execute"
        #这里写lua脚本

        lua_source="""
	function main(splash, args)
	  splash:set_custom_headers({
	   ["Accept-Language"] = "zh,zh-CN;q=0.5"
		})
	  assert(splash:go(args.url))
	  assert(splash:wait(0.5))
	  local input = splash:select('.lmt__source_textarea')
	  input:mouse_click()
	  input:send_text("n the first example 'main' function returned a Lua table (an associative array similar to JavaScript Object or Python dict). Such results are returned as JSON.")
	  input:mouse_click()
	  assert(splash:wait(25.5))
	  local data = splash:select('#target-dummydiv')
	  --return data.node.innerHTML

	  return {
	    --html = splash:html(),
	    html = data.node.innerHTML,
	    --png = splash:png(),
	    --har = splash:har(),
	  }
	  --]]
	end
	  
         

        """
        args={
            "url":"https://www.deepl.com/translator",
            "timeout":90,
           #"html":1,
            #"wait":0.5,
            "lua_source":lua_source

        }
        response =requests.get(api,params=args)
        try:
            return response.json()
        except:
            return response.text



        pass
    def fun(self):
        print("fun run!")
        pass
