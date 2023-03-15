import re
import logging
from locators.book_locator import BookLocators

logger = logging.getLogger('scraping.bookparser')

class BookParser:

    RATINGS = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5}


    def __init__(self, parent):
        logger.debug(f'New book parser created from "{parent}"')
        self.parent = parent

    def __repr__(self):
        return f'Book '

    @property
    def name(self):
        logger.debug('finding book name...')
        locator = BookLocators.NAME
        item_name = self.parent.select_one(locator).attrs['title']
        logger.info(f'Found book name, "{item_name}"')

        return item_name

    @property
    def link(self):
        logger.debug(f'finding book link...')
        locator = BookLocators.LINK
        item_url = self.parent.select_one(locator).attrs['href']
        logger.info(f'found book page link, {item_url} ')
        return item_url

    @property
    def price(self):
        logger.debug(f'finding book price...')
        locator = BookLocators.PRICE
        item_price = self.parent.select_one(locator).string
        logger.info(f'item price element found, {item_price}')
        return item_price

    @property
    def rating(self):
        logger.debug(f'finding book rating...')
        locator = BookLocators.RATING
        item_rating = self.parent.select_one(locator)
        classes = item_rating.attrs['class']
        rating_classes = filter(lambda x: x != star-rating, classes)
        rating_class = next(rating_classes)

        logger.debug(f'found rating class, {rating_class}')
        logger.debug('converting to integer for sorting')
        rating = BookParser.RATINGS.get(rating_class)
        logger.info(f'found book rating, {rating}')
        return rating
