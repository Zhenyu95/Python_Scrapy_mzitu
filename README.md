# Python_Scrapy_mzitu
利用scrapy爬取mzitu的图片 （referer反爬）
## Getting started
爬取mzitu制定页面的所有图片

### Prerequisites
需要安装Python3及Scrapy和urllib两个库

### Installing
下载至本地后运行 mzitu_pic/start.py 即可爬取 mzitu 前三页的所有图片及其链接中的图片。下载路径默认为当前路径/images

### Settings
在 settting.py 中设置下载延迟，默认为2秒，速度过快可能会被封ip
```python
DOWNLOAD_DELAY = 2
```
在mzitu_pic/spiders/mzitu.py中设置想要爬取的页面
```python
#设置起始爬取页面，默认为mzitu首页，可以改为想要爬取的特定页面，网址用逗号分开
start_urls = ['https://www.mzitu.com']

    rules = (
    #修改page/[], 中括号中表示想要爬取的页面。1为第一页，2为第二页，多个页面用逗号隔开
        Rule(LinkExtractor(allow=r'page/[1,2,3]',restrict_xpaths='//div[@class="pagination"]//a')),mzi
        Rule(LinkExtractor(allow=r'.+com/\d{6}',restrict_xpaths='//div[@class="postlist"]//li//a'),follow=True,callback='parse_images'),
        Rule(LinkExtractor(allow=r'.+com/\d{6}/\d',restrict_xpaths='//div[@class="pagenavi"]/a'),follow=True,callback='parse_images'),   
    )
```
