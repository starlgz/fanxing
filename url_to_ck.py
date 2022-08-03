
import os
import sys

env_dist = os.environ
# 变量设置
# export url = 'http://apissl.ksapisrv.com/rest/nebula/system/keyconfig?earphoneMode=0&mod=Xiaomi%28MI%20CC9%20Pro%29&appver=10.6.30.3979&isp=&language=zh-cn'
# export oldCk = 'kpn=NEBULA; kpf=ANDROID_PHONE; userId=169277; did=ANDRO20801af; c=XIAOMI; ver=10.6; appver=10.6.50.4023; languaDK0l8TaNf-yBTpSKEmCp-CBjygFMAE'

url = env_dist.get("url")
oldCk = env_dist.get("oldCk")

if url is None or oldCk is None:
    print("变量没填")
    sys.exit()

def to_new():
    a = url.split('?')[1]
    new_map = to_map(a, '&')
    old_map = to_map(oldCk, ';')
    for k in new_map.keys():
        if k in old_map:
            old_map[k] = new_map[k]
    new_ck = ''
    for k in old_map.keys():
        new_ck += k + '=' + old_map[k]+ '; '
    print(new_ck[0: len(new_ck) - 2])

def to_map(content, split) -> dict:
    cookie_map = {}
    ck_split = content.split(split)
    for entry in ck_split:
        kv = entry.split('=')
        k = kv[0].strip()
        if k == '':
            continue
        v = kv[1].strip()
        cookie_map[k] = v
    return cookie_map


to_new()


