import re
from datetime import datetime,timezone,timedelta

def to_timestamp(dt_str,tz_str):
    re_tz=re.compile(r'(UTC)([+-]\d+):(\d+)')
    if re_tz.match(tz_str)!=None:
        tz=re_tz.match(tz_str).group(2)
    local_time = datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')
    st_time=local_time.replace(tzinfo=timezone(timedelta(hours=int(tz))))
    return st_time.timestamp()


