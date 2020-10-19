from typing import Union, List, Tuple
import time
from utils.base import get_all_date

urlInput = Union[str, List[str], Tuple[str]]

class AbstractCrawler:
    """Base class for all crawler.

    """
    def __init__(self):
        pass

    def crawling(self,
              url : urlInput, **kwargs
              ) -> List[str]:
        """crawling naver news url inputs from a string, a list/tuple of strings

        Args:
            url: a string, a list/tuple of strings

        Returns:
            a list of string(s)

        Raises:
            ValueError: An error occurred cleansing empty list/tuple or not UrlInput

        """

        output = []
        if isinstance(url, str):
            doc = self._crawling(url)
            output.extend(doc)

        elif isinstance(url, (list, tuple)) and len(url) > 0 and (all(isinstance(u, str) for u in url)):
            output = [self._crawling(u) for u in url][0]

        else:
            raise ValueError(
                f"Input {url} is not valid. Should be a string, a list/tuple of strings."
            )

        return output

    def _crawling(self, url, **kwargs):
        """crawling comments in specific url"""

        raise NotImplementedError

    def run_engine(self, code, start_date, end_date, **kwargs):
        """Keep crawling comments by url in url set"""
        date_list = get_all_date(start_date, end_date)
        whole_doc = []
        for date in date_list:
            url_set = self._load_url_set(code, date, **kwargs)
            for title, url in url_set:
                try:
                    comments = self.crawling(url, **kwargs)
                    doc = {'url': url, 'comments': comments}
                    if comments != []:
                        whole_doc.append(doc)
                except Exception as ex:
                    print(ex)
                    print("Let me sleep for 30 seconds")
                    time.sleep(30)
                    continue

        return whole_doc

    def _load_url_set(self, code, date, **kwargs):
        """load url set"""

        raise NotImplementedError
