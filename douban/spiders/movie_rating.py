import scrapy
import datetime
import json
from urllib import parse

from ..items import Movie_rating

class QuotesSpider(scrapy.Spider):
    name = "mv_rating"

    def start_requests(self):
        urls = [
            'https://movie.douban.com/people/3872200/collect',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_ratings)


        # test_urls = [
        #     'https://www.httpbin.org/ip'
        # ]
        # for url in test_urls:
        #      yield scrapy.Request(url=url, callback=self.test_parse)
    #

    def test_parse(self, response):
        yield(json.loads(response.body_as_unicode()))
        # yield response.follow('https://www.httpbin.org/ip', callback=self.test_parse, dont_filter=True)
        

    def parse_movie(self, response):
        for people_page in response.css('div.review-list a.avator::attr(href)').extract():
            yield response.follow(people_page.replace('www.douban.com','movie.douban.com') + 'collect', callback=self.parse_ratings)

    def parse_ratings(self, response):
        # page = response.url.split("/")[-2]
        # print(response.headers)
        
        
        urls = []
        items = response.css('div.item')
        for item in items:
            
            
            url = item.css('li.title a::attr(href)').extract_first()
            movie_id = url.split('/')[-2]
            title = item.css('li.title em::text').extract_first()
            
            try:
                rating = item.xpath('.//span[contains(@class, "rating")]/@class').extract_first()[len('rating'):-len('-t')]
            except:
                continue
            date_string = item.xpath('.//span[contains(@class, "date")]/text()').extract_first()
            rating_date = datetime.datetime.strptime(date_string, '%Y-%m-%d')
            rating_ts = int(rating_date.timestamp())
            comment = item.css('span.comment::text').extract_first()
            user = parse.urlparse(response.url).path.split('/')[2]
            rating_id = user + '_' + movie_id
            
            urls.append(url)
            rating = {
                'user': user,
                'rating_id': rating_id,
                'url': url,
                'movie_id': movie_id,
                'title': title,
                'rating': rating,
                'rating_date': rating_date,
                'rating_ts': rating_ts,
                'comment': comment,
            }
        
            yield Movie_rating(rating)
            
        for next_page in response.css('div.paginator a'):
            yield response.follow(next_page, callback=self.parse_ratings)
            
        for movie in urls:
            yield response.follow(url, callback=self.parse_movie)