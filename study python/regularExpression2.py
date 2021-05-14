import re

def name_of_email(addr):
    re_name=re.compile(r'^(\<?)([a-zA-Z0-9\.\#\s]{1,15})(\>?)([\w\s]{0,10})@(\w{3,10}).(com|org)$')
    if re_name.match(addr)!=None:
        return re_name.match(addr).group(2)
