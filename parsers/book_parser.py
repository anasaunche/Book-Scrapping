import re

from locators.book_locators import BookLocators

class BookParser:

    RATINGS = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }

    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f'Book: {self.name}, ${self.price}, ({self.rating} stars)'

    @property
    def name(self):
        locator = BookLocators.NAME
        item_name = self.parent.select_one(locator).attrs['title']
        return item_name

    def link(self):
        locator = BookLocators.LINK
        item_link = self.parent.select_one(locator).attrs['href']
        return item_link

    def price(self):
        locator = BookLocators.PRICE
        item_price = self.parent.select_one(locator).string

        pattern = '£([0-9]+\.[0-9]+)'
        matcher = re.search(pattern, item_price)
        price = float(matcher.group(1))
        return price

    def rating(self):
        locator = BookLocators.RATING
        item_rating = self.parent.select_one(locator)
        classes = item_rating.attrs['class']
        rating_classes = [r for r in classes if r != 'star-rating']
        rating = BookParser.RATINGS.get(rating_classes[0])
        return rating
