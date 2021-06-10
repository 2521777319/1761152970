from urllib.parse import quote
from urllib.parse import urlencode
# urlencode是对 key:vlue 型转码
age = {
    "kw":"你妈的",
    "ie":"what"
    }
print(urlencode(age))
print("==============\n")
# quote是直接对字符串转码
data = '小张'
data = quote(data)
print(data)