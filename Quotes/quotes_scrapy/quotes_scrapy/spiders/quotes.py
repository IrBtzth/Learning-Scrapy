import scrapy 

# Next page button = //ul[@class="pager"]//li[@class="next"]/a/@href
class MySpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/'
    ]
    
    custom_settings = {
        'FEED_URI': 'quotes.json',
        'FEED_FORMAT': 'json',
        'CURRRENT_REQUESTS': 24, #Como scrapy es un framework asincrono puede mantener varias peticiones a la vez, sin la necesidad de terminar una para comenzar la otra
        'MEMUSAGE_LIMIT_MB': 2048, #la cantidad de memoria ram que scrapy puede utilizar.
        'MEMUSAGE_NOTIFY_MAIL': ['betzabeth.btzth@gmail.com'], #nos avisa cuando la memoria ram se llena o llega al limite
        'ROBOTSTXT_OBEY': True,
        'USER_AGENT': 'Un ente', #en el sevidor cuando llegue la peticion dira que la hizo un ente
        'FEED_EXPORT_ENCODING': 'utf-8'
    }
    def parse_only_quotes(self, response, **kwargs):
        
        if kwargs:
            quotes = kwargs['quotes'] #Aqui se guardan las citas, inicialmente vacia, es una lista
            authors = kwargs['authors']
       
        quotes.extend(response.xpath(
            "//span[@class = 'text' and @itemprop= 'text']/text()").getall()) #aqui se agregan
        authors.extend(response.xpath('//small[@class="author" and @itemprop = "author"]/text()').getall())
        
        next_page_button_link = response.xpath('//ul[@class="pager"]//li[@class="next"]/a/@href').get()
        
       
        if next_page_button_link:
            yield response.follow(next_page_button_link, 
            callback=self.parse_only_quotes, cb_kwargs= {'quotes': quotes,'authors': authors})
        else:
            for i in range(0, len(quotes)-1):
                quotes[i]= quotes[i]+ " by "+ authors[i] 
            yield {
                'quotes': quotes
                }
    
    def parse(self, response):
        title = response.xpath('//h1/a/text()').get()
  
        quotes = response.xpath("//span[@class = 'text' and @itemprop= 'text']/text()").getall()

        authors = response.xpath('//small[@class="author" and @itemprop = "author"]/text()').getall()

        topTags = response.xpath('//div/span/a[@class="tag"]/text()').getall()
        

        top = getattr(self,'top', None)
        if top:
            top = int(top)
            topTags = topTags[:top]

        yield {
                'titles': title,
                'top tags': topTags
            }

        next_page_button_link = response.xpath('//ul[@class="pager"]//li[@class="next"]/a/@href').get()
    
        if next_page_button_link:
            yield response.follow(next_page_button_link, 
            callback=self.parse_only_quotes, cb_kwargs= {'quotes': quotes, 'authors': authors})
