# wanfangSpider
万方中文期刊爬虫，按年份与期刊名称爬取

### 使用框架： 
python, beautifulsoup4, selenium
### 浏览器版本： 
chrome 89.0.4389.82  
请使用对应的chromedriver 下载地址为 <http://npm.taobao.org/mirrors/chromedriver/>  
### 使用方法
* 首先安装爬虫所需依赖  
  ```pip install -r requirements.txt```

* 使用 `wanfangSpider.py` 对所有中文期刊名称进行爬取，后续需要对期刊数量进行定期修改
    * 一共有8个领域，每个领域使用拼音首字母进行存储，存储格式为`xxxx.csv`，生成的文件在`./periodicalName/`中
* 使用 `periodicalSpider.py` 对所有期刊进行爬取，爬取方式为按照年份如1998-2020与上一步获得的中文期刊名称进行爬取，生成的文件在`./paperDetailed1/`中
* 如果某一页爬取失败，会进行log输出输出到根目录中的`log.txt`中
