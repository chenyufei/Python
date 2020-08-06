import re
pattern = re.compile(r'\d+')                     # 用于匹配至少一个数字
m = pattern.match('one12twothree34four')         # 查找头部，没有匹配
print(m)
# None
m = pattern.match('one12twothree34four', 2, 10)  # 从'e'的位置开始匹配，没有匹配
print(m)
# None
m = pattern.match('one12twothree34four', 3, 10)  # 从'1'的位置开始匹配，正好匹配
print(m)                                         # 返回一个 Match 对象
# <_sre.SRE_Match object at 0x10a42aac0>
print(m.group(0))   # 可省略 0
# '12'
print(m.start(0))   # 可省略 0
# 3
print(m.end(0))     # 可省略 0
# 5
print(m.span(0))    # 可省略 0
#(3, 5)


it = re.finditer(r"\d+", "12a32bc43jf3")
for match in it:
    print(match.group())


s = '1102231990xxxxxxxx'
res = re.search('(?P<province>\d{3})(?P<city>\d{3})(?P<born_year>\d{4})', s)
print(res.groupdict())

print(res.group(0))
print(res.group(1))
print(res.group(2))
print(res.group(3))
