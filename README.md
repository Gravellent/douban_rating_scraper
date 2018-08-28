# Douban Movie Rating Spider

## Purpose

The spider aims to crawl as many movie raings as possible from Douban. Ratings will mainly consist of a user_id, a movie_id, and a score. With those things, we can intialized a machine learning task based on collaborative filtering algorithm. 

Personally, I took Andrew Ng's course on Coursera, https://www.coursera.org/learn/machine-learning/home/welcome. The data set obtianed from the code here and can be used for Week 9's course. 

### Framework

The spider is built upon scrapy. 

### Douban Anti-crawling measurement

There are a known things that Douban blocks.
- You must set the "User-Agent" header to a browser. Douban will block requests with User-Agent of "scrapy" or "python"
- Douban will require a captcha if they identified too many requests from a cookie. Not sure which part of cookie, but this can be avoided by not storing the cookie.
- Douban will block based on IP after ~1000 requests too frequently. IP rotation can get around it. 


### Note
Note that middlewares.py and settings.py has been removed from the repo since it contains credentials. Specfically, since IP rotation is require for this crwaler to work, you would need to set up some kind of http proxy in order to get around the anti-crawling.