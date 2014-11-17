def chunks(l, n):
    """ Yield successive n-sized chunks from l.
    """
    for i in xrange(0, len(l), n):
        yield l[i:i + n]

def is_chinese(string):
    string = string if isinstance(string, unicode) else string.decode('utf-8')
    for c in string:
        if u'\u4e00' <= c <= u'\u9fff':
            return True
    return False
