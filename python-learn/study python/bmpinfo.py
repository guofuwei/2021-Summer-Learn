import base64,struct

def bmp_info(data):
    s = struct.unpack('<ccIIIIIIHH',data[0:30])