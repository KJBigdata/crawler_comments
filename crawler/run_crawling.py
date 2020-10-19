import argparse
from datetime import date, timedelta
from crawler_comments import NaverCommentsCrawler
from utils.base import dump_docs, show_stat

def main():

    LAST_MONTH = str(date.today() - timedelta(30)).replace('-', '')
    TODAY = str(date.today()).replace('-','')

    parser = argparse.ArgumentParser()
    parser.add_argument('--begin_date', type=str, default=LAST_MONTH,
                        help='시작 날짜 : yyyymmdd ( default : 30일 전 )')
    parser.add_argument('--end_date', type=str, default=TODAY,
                        help='종료 날짜 : yyyymmdd ( default : 오늘 )')
    parser.add_argument('--output_dir', type=str, default='./output',
                        help='저장 경로 : ./output')

    args = parser.parse_args()
    begin_date = args.begin_date
    end_date = args.end_date

    output_dir = args.output_dir

    comments_crawler = NaverCommentsCrawler()

    for pair in comments_crawler.press_code:
        code, press = pair

        whole_docs = comments_crawler.run_engine(code, begin_date, end_date)

        output_path = output_dir
        file_name = f"{press}_{begin_date}_{end_date}"
        dump_docs(whole_docs, output_path, file_name)

if __name__ == '__main__':
    main()