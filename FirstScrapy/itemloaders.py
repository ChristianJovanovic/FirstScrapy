from bs4 import BeautifulSoup
from itemloaders.processors import TakeFirst, MapCompose
from scrapy.loader import ItemLoader


class FirstScrapyItemLoader(ItemLoader):
    default_output_processor = TakeFirst()
    name_in = MapCompose(lambda x: BeautifulSoup(x, 'html.parser').text.replace('\n', '').strip())
    price_in = MapCompose(lambda x: BeautifulSoup(x, 'html.parser').text.replace('\n', '').strip().replace('€', '').replace(',', '.'))
    strong_in = MapCompose(lambda x: BeautifulSoup(x, 'html.parser').text.replace('\n', '').strip())
    url_in = MapCompose(lambda x: "https://snuzone.com/collections/snus-und-nicotine-pouches" + x)
    details_in = MapCompose(lambda x: BeautifulSoup(x, 'html.parser').text.replace('\n', '').strip())

class ProductDetailsLoader(ItemLoader):
    default_output_processor = TakeFirst()
    marke_in = MapCompose(lambda x: BeautifulSoup(x, 'html.parser').text.replace('\n', '').strip())
    niko_per_gram_in = MapCompose(lambda x: BeautifulSoup(x, 'html.parser').text.replace('\n', '').strip())
    niko_per_piece_in = MapCompose(lambda x: BeautifulSoup(x, 'html.parser').text.replace('\n', '').strip())
    aroma_in = MapCompose(lambda x: BeautifulSoup(x, 'html.parser').text.replace('\n', '').strip())
    format_in = MapCompose(lambda x: BeautifulSoup(x, 'html.parser').text.replace('\n', '').strip())
    pieces_per_pack_in = MapCompose(lambda x: BeautifulSoup(x, 'html.parser').text.replace('\n', '').strip())
    summary_in = MapCompose(lambda x: BeautifulSoup(x, 'html.parser').text)
    review_score_in = MapCompose(lambda x: BeautifulSoup(x, 'html.parser').text)

