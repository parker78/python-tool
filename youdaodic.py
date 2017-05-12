#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 有道词典脚本的使用：
# youdaodic.py 'apple'
# 苹果
import urllib
import json
import sys
perfix='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessiontype=AUTO&'
postfix='&doctype=json&xmlVersion=1.6&keyfrom=fanyi.web&ue=UTF-8&typoResult=trueFrom=null'
maps={}
def search(word):
    maps['i']=word
    sUrl=perfix+urllib.urlencode(maps)+postfix
    url=urllib.urlopen(sUrl)
    result=url.read()
    url.close()
    resultobj=json.loads(result)
    errorCode=resultobj.get('errorCode')
    if errorCode==0:
        result=resultobj.get('translateResult')
        return result[0][0].get('tgt')
if __name__=='__main__':
#    print sys.argv
    print search(sys.argv[1])
