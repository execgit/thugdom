def dom_logging(log, string, *args):
    max_len = log.ThugOpts.max_len
    _data = ''
    for data in args:
        if max_len == 0:
            _data += data
        elif len(data) > max_len:
            _data += data.strip()[:max_len-3] + '...'
        else:
            _data += data
    log.warning("{} {}".format(string, repr(_data)))
    
