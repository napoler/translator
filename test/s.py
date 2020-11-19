text="sasasdaijsdjidsuisduisdisd"

lua_source=f'''function main(splash, args)
splash:set_custom_headers({
["Accept-Language"] = "zh,zh-CN;q=0.5"
})
assert(splash:go(args.url))
assert(splash:wait(0.5))
local input = splash:select('.lmt__source_textarea')
input:mouse_click()
input:send_text(" {{text}} ")

end'''
print(lua_source)
