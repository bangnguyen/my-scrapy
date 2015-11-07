import urllib
from scrapy.http.response.html import HtmlResponse
from scrapy_balloons.utils.html_string import html_to_text
from random import randint
from urlparse import urljoin


class ingram:
    """
    Step 1: Get url
    Step 2: Using urllib,,,,then using HtmlResponse convert text to response scrapy
    """
    box_url = []
    desc_api = 'https://www.im-plus.be/site/?tc=LoadTrainingDetails&trainingid=%s'

    @classmethod
    def get_desc(cls, value):
        try:
            # Step 1
            url_desc = ingram.desc_api % (value)

            # Step 2
            data = urllib.urlopen(url_desc)
            response = HtmlResponse(url=url_desc, body=data.read())

            data = None
            all_xpath = [
                "substring-before(//div[@class='training_details_content'],'Language')",
                "substring-before(//div[@class='training_details_content'],'Please bring your')",
                "//div[@class='training_details_content']/p/text()",
                "//div[@class='training_details_content']/div[1]/text()",
                "//div[@class='training_details_content']/span/text()",
                "//div[@class='training_details_content']//text()"
            ]

            for xpath in all_xpath:
                data = response.xpath(xpath).extract()
                desc = html_to_text(data)
                if desc:
                    return desc

            return None

        except:
            pass

    @classmethod
    def get_prod_id(self, value):
        if 'Webinar' in value:
            return "4"
        else:
            return "1"


    @classmethod
    def get_url(cls, item, spider):
        if item['product_url'] == 'https://www.im-plus.be/site/?id=6572':
            # response = spider.resources_ext[item['product_url']]
            # import pdb
            # pdb.set_trace()
            index =  randint(1,40)
            prod_url = 'https://www.im-plus.be/site/?id=6572#%s' %(index)

            if prod_url not in ingram.box_url:
                item['product_url'] = prod_url
                ingram.box_url.append(prod_url)
            else:
                ingram.get_url(item,spider)




