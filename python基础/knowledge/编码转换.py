unicode_str = "我"

# 先将字符串编码为utf-8
utf8_str = unicode_str.encode("utf-8")
print("我是utf_str:", utf8_str, "type:", type(utf8_str))
# 再按原方式解码为Unicode
unicode_str = utf8_str.decode("utf-8")
print("我是unicode_str:", unicode_str, "type:", type(unicode_str))
# 最后基于uncoide编码再将字符串转为gbk编码
gbk_str = unicode_str.encode("gbk")
print("我是gbk_str:", gbk_str, "type:", type(gbk_str))