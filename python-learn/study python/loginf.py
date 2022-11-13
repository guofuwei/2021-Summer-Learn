# -*- coding: utf-8 -*-
db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}



import hashlib


def login(user,password):
    password_md5=hashlib.md5()
    password_md5.update(password.encode('utf-8'))
    if (db[user]==password_md5.hexdigest()):
        return True
    else:
        return False