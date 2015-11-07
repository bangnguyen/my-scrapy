from scrapy_balloons.utils.basefunctions import detect_language

class vrayschool:


    @classmethod
    def not_in_english(cls,response):
        detect_key = response.xpath("//div[@class='course_title']/h1//text()").extract()
        try:
            # import pdb
            # pdb.set_trace()
            title = str(detect_key[0])
            return False
        except:
            return True