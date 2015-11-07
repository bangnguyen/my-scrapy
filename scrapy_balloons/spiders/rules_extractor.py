from scrapy_balloons.utils.allfunctions import *


class TestRuleSpider(CrawlSpider):
    name = "rules"
    start_urls = ["http://www.measureup.com/"]
    cpt = 0
    rules = [
        Rule(lxml(allow=('\\.aspx$',),restrict_xpaths=("//div[@id='navigation']/ul/li[1]//a")), follow=True),
        Rule(lxml(allow=('\\.aspx$',),restrict_xpaths=("//div[@class='prod-list']/div[@class='prod-item']//a")), callback='parse_product')
    ]
    cpt = 0

    def parse_product(self, response):
        self.cpt += 1
        print self.cpt
        print response.url
        # print self.cpt
        return None

    def passCat(self, response):
        # print "passFollows------------------"
        # self.cpt += 1
        # print self.cpt
        # print response.url
        return None
