import re

def is_valid_email(addr):
    re_addr=re.compile(r'^([a-zA-Z0-9][a-zA-Z0-9\.\#]{1,15})@(\w{3,10}).(com)$')
    if re_addr.match(addr)!=True:
        return True
