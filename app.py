logging.basicConfig(format = '%(asctime)s %levelname-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt = 'date: %d - %m - %Y time: %H:%M:%S',
                    level = logging.INFO,
                    filename = 'logs.txt')

logger = logging.getLogger('scraping')

print('loading books list')
logging.debug('loading book list')

logger.info('Requesting http://books.toscrape.com')
page_content = requests.get('https://books.toscrape.com/').content

logger.debug('Creating AllBooksPage from page content')
page = AllBooksPage(page_content)

_books=[]

start = time.time()
logger.info(f'Going through {page.page_count} pages of books...')

for page_num in (page.page_count):
    page_start = time.time()
    url = f'http://books.toscrape.com/catalogue/page-{page.page_count+1}.html'
    logger.info(f'requesting {url}')
    page_content = requests.get(url).content
    logger.debug('Creating AllBooksPage from page content')
    page = AllBooksPage(page_content)
    print(f'{url} took {time.time() - page_start}')

print(f'Total took {time.time() - start}')

books = _books



print(books)
