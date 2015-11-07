from scrapy import Item, Field


class ProductRating(Item):
    pub_status = Field()
    rating_only = Field()
    overall_rating = Field()
    review = Field()
    user_id = Field()
    username = Field()


class Author(Item):
    name = Field()
    bio = Field()
    image = Field()
    link = Field()


class Instructor(Item):
    name = Field()
    bio = Field()
    image = Field()
    link = Field()


class Publisher(Item):
    name = Field()
    image = Field()
    link = Field()


class Certificate(Item):
    id = Field()
    name = Field()
    short_name = Field()
    link = Field()


class RawHtml(Item):
    link = Field()
    fields = Field()
    source = Field()


class ProductEvent(Item):
    price_currency = Field()
    price_display_float = Field()
    duration_display = Field()
    duration_filter = Field()
    start_date_local = Field()
    end_date_local = Field()
    tz = Field()
    location_display = Field()
    location_addr = Field()
    location_city = Field()
    location_state = Field()
    location_country = Field()
    location_postal = Field()
    location_name = Field()
    language = Field()
    price_display_text = Field()
    price_filter = Field()


class Product(Item):
    description = Field()
    product_type_id = Field()
    provider_id = Field()
    name = Field()
    short_desc = Field()
    difficulty = Field()
    product_url = Field()
    product_image_url = Field()
    product_video_url = Field()
    partner_prod_id = Field()
    formats = Field()
    published_date = Field()
    authors = Field()
    publisher = Field()
    toc = Field()
    audience = Field()
    requirements = Field()
    prerequisites = Field()
    certificates = Field()
    prod_keywords = Field()
    raw_html = Field()
    pub_status = Field()
    product_events = Field()
    ProductRating = Field()
    price_currency = Field()
    price_display_float = Field()
    duration_display = Field()
    duration_filter = Field()
    start_date_local = Field()
    end_date_local = Field()
    tz = Field()
    instructors = Field()
    location_display = Field()
    location_addr = Field()
    location_city = Field()
    location_state = Field()
    location_country = Field()
    location_postal = Field()
    location_name = Field()
    language = Field()
    price_display_text = Field()
    price_filter = Field()
    space_lock = Field()
    time_lock = Field()




