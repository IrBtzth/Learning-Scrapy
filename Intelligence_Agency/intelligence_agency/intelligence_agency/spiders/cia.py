from os import link
import scrapy

# Xpath
# links = '//a[starts-with(@href, "collection") and (parent::h3 | parent::h2)]/@href'
# title = '//h1[@class="documentFirstHeading"]/text()'
# paragraph = '//div[@class="field-items"]//p[ not(child::strong and child::i) and not(@class)]/text()'
class SpiderCia(scrapy.Spider):
    name = 'cia'
    start_urls = [
        'https://www.cia.gov/readingroom/historical-collections'
    ]

    custom_settings = {
        'FEED_URI': 'cia.json',
        'FEED_FORMAT': 'json',
        'FEED_EXPORT_ENCODING': 'utf-8',
        'ROBOTSTXT_OBEY': True
    }

    def parse(self, response):
        links_desclassified = response.xpath('//a[starts-with(@href, "collection") and (parent::h3 | parent::h2)]/@href').getall()

        for link in links_desclassified:
            yield response.follow(link, callback = self.parse_links, cb_kwargs={'url': response.urljoin(link)})

    def parse_links(self, response, **kwargs):
        links = kwargs['url']
        title = response.xpath('//h1[@class="documentFirstHeading"]/text()').get()
        paragraph = response.xpath('//div[@class="field-items"]//p[ not(child::strong and child::i) and not(@class)]/text()').getall()

        yield{
            'ur': links,
            'title': title,
            'paragraph': paragraph
        }        