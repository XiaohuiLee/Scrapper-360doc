# Scrapper-360doc
tags:
Python3、爬虫、网页、requests、re、正则表达式

## 问题描述
浏览网页的时候遇到这篇笔记：
http://www.360doc.com/content/07/0310/18/17841_392130.shtml，
想要把页面上的书籍全下载下来，一共有80多本，手动点击下载太慢，想要快速批量地把下载链接爬取下来，于是用Python写了一个小程序。

## 爬虫设计
先用requests爬取页面内容，

再用re抽取书名和下载链接，

将结果保存到pandas.DataFrame，

最后保存至csv文件

## 爬取步骤
1、页面抓取

2、正则表达式解析

3、保存到csv文件

4、下载电子书文件

详细的步骤解析参看：
知乎：https://zhuanlan.zhihu.com/p/35292699

简书：https://www.jianshu.com/p/597f1d8a3dce
