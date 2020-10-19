from crawler_base import AbstractCrawler
from utils.base import get_all_date, get_url_list, remove_duplicate
from parse_comment import get_comments

class NaverCommentsCrawler(AbstractCrawler):
    """Crawler for Naver news comments

    """

    def __init__(self):
        super().__init__()
        self.max_page = 4
        self.base_url = 'https://news.naver.com/main/list.nhn?mode=LPOD&mid=sec&listType=paper'
        self.main_url = ''.join([self.base_url, '&oid={}&date={}&page={}'])
        self.press_code = [('014', '파이낸셜뉴스'), ('018', '이데일리'), ('277', '아시아경제'), ('469', '한국일보'),
                      ('021', '문화일보'), ('023', '조선일보'), ('028', '한겨레'),
                      ('015', '한국경제'), ('011', '서울경제'),
                      ('016', '헤럴드경제'), ('029', '디지털타임스')]

    def _crawling(self, url: str):
        '''

        '''

        return get_comments(url)

    def _load_url_set(self, code, start_date, end_date):
        """

        """
        date_list = get_all_date(start_date, end_date)
        for date in date_list:
            for page in range(1, self.max_page):
                main_url = self.main_url.format(code, date, page)
                title_url_pair_list = remove_duplicate(get_url_list(main_url))

        return title_url_pair_list

