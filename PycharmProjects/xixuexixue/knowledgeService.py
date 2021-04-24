# -*- coding: utf-8 -*- 
# @Time : 2021/4/17 下午11:02 
# @Author : yuxiaoxue
# @File : knowledgeService.py
import re

def getConfig(url):
    configList = []
    configList.append(re.findall('2.*?js',url))
    configList.append(re.findall('2.*?css',url))


if __name__=='__main__':
    url = '文件url: https://cdnbeta.11bee.com/human_resource_betamagic/prd/2.2ff7c8e8.chunk.js 2.2ff7c8e8.chunk.js.map 2.5ef14bb1.chunk.css 2.5ef14bb1.chunk.css.map 3.9acf6afa.chunk.css 3.9acf6afa.chunk.css.map 3.d912754a.chunk.js 3.d912754a.chunk.js.map asset-manifest.json favicon.ico index.html main.538ea224.chunk.js main.538ea224.chunk.js.map main.bf2aed64.chunk.css main.bf2aed64.chunk.css.map manifest.json precache-manifest.6a9845212ae0dc0c8ac6e3fbdb189794.js runtime~main.e9e61789.js runtime~main.e9e61789.js.map service-worker.js'
    #url = '2.2ff7c8e8.chunk.js '
    print(getConfig(url))
