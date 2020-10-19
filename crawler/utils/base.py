import os
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import pickle

def get_all_date(start_date, end_date):
    d1 = datetime.strptime(start_date, '%Y%m%d').date()
    d2 = datetime.strptime(end_date, '%Y%m%d').date()
    date_list = [str(d1 + timedelta(days=x)).replace('-', '') for x in range((d2 - d1).days + 1)]
    return date_list

def get_url_list(main_url):
    ua = UserAgent()
    headers = {'User-Agent': ua.random}
    main_url = requests.get(main_url, headers=headers)
    soup = BeautifulSoup(main_url.text, "html.parser")
    title_url_pair_list = [
        (a.text.strip(), str(a).split('href="')[1].split('"')[0].replace('amp;', '')) if a.find('img') is None
        else (a.find('img').get('alt').strip(), str(a).split('href="')[1].split('"')[0].replace('amp;', ''))
        for a in soup.select('dt > a')]
    return title_url_pair_list


def remove_duplicate(title_url_pair_list=list):
    my_set = set()
    res = []
    for title, url in title_url_pair_list:
        if url not in my_set:
            res.append((title.strip().replace("\xa0", ' ').replace("\'", ''), url))
            my_set.add(url)

    return res

def load_comments(fname):
    with open(fname, encoding='utf-8') as f:
        docs = [doc.strip() for doc in f]
    if docs[0][-15:] != 'antipathy_count':
        first = docs[0].split('antipathy_count')[0] + 'antipathy_count'
        second = docs[0].split('antipathy_count')[1]
        docs = [first, second] + docs[1:]
    return docs

def mkdir(path: str) -> None:
    """Recursively creates the directory and does not raise an exception

    Args:
      path: A target directory path

    To use:
    >>> mkdir('target_directory_path')
    """
    os.makedirs(path, exist_ok=True)

def load_docs(abs_path):
    try:
        with open(abs_path, 'rb') as f:
            whole_doc = pickle.load(f)
            return whole_doc
    except Exception as ex:
        print(ex)

def dump_docs(crawled_data, output_dir: str, file_name: str):
    """Dump news comments as pickle type

    Args:
        crawled_data: cleaned_news to save
        output_dir: output directory path
        file_name: file name to save

    """
    mkdir(output_dir)
    path = os.path.join(output_dir, f"{file_name}.pkl")
    with open(path, 'wb') as file:
        pickle.dump(crawled_data, file)
    show_stat(path, file_name)

def show_stat(abs_path, file_name):
    doc_len = 0
    comment_len = 0
    with open(abs_path, 'rb') as f:
        whole_doc = pickle.load(f)
    for doc in whole_doc:
        doc_len += 1
        for comment in doc.get('comments'):
            comment_len +=1
    print(f"file name : {file_name}")
    print(f"crawled_news_n : {doc_len}")
    print(f"crawled_comment_n : {comment_len}")
    print('\n')