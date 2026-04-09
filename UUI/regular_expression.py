"""
正则表达式：
正则校验器

"""
import re
"""
参数一：匹配规则
参数二：要匹配的字符串
"""
result = re.match('.it', 'ait')
if result:
    print("匹配成功")
else:
    print("匹配失败")