# HappyMC Random image API Ver1.0 Alpha
该程序主要使用Django框架写成

## 请求方式

Get

## 请求路径
电脑    /img \
手机    /img-phone

## 访问参数
type	填 json则返回一串数组，填img则直接返回一张图片。如果不填写或者填写错误将会返回错误信息（暂不可用） \
token	访问者必须填写程序配置文件内的token，否则将不会返回任何有效信息，将会返回错误信息

## API返回的数据
id  图片 ID（暂不可用） \
url	图床访问url（暂不可用） \
fileName	文件名（暂不可用） \
origin	图片来源（暂不可用） \
image	图片

## 另外
使用前请在```HappyMC_API/settings.py```里的API_TOKEN处添加你的token。token可以使用```Token/token.py```来生成属于你的Token，用法及解释可查看```Token/Readme.md```
