import re
import logging

from locators.page_locators import PageLocators
from parsers.book_parser import BookParser
from bs4 import BeautifulSoup

logger = logging.getLogger('scraping.all_books_page')

class AllBooksPage:
    def __init__(self, page):
        logger.debug(f'parsing page with BS HTML parser')
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def books(self):
        logger.debug(f'Finding all books in the page using -{PageLocators.BOOKS}-')
        return [BookParser(e) for e in self.soup.select(PageLocators.BOOKS)]

    @property
    def page_count(self):
        logger.debug('finding all number of cataloge pages available')
        content = self.soup.select_one(PageLocators.PAGER).string
        logger.info(f'Found number of pages available -{content}')
        pattern = 'Page [0-9]+ of [0-9]+' \
                  ''
        matcher = re.search(pattern, content)
        pages = int(matcher.group(1))
        logger.info(f'Extracted number of pages as integer: {pages}')
        return pages
