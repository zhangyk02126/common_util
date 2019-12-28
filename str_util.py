def str_to_unicode(u_or_str, enc='utf-8'):
    if isinstance(u_or_str, str):
        u_or_str = u_or_str.decode(enc)
    return u_or_str

def is_chineses(s):
    s = str_to_unicode(s)
    if u'\u4e00' <= s <= u'\u9fff':
        return True
    else:
        return False
