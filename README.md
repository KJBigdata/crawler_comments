## Install

Python 3.7 로 작성되었습니다. 아래의 패키지를 이용합니다.

- beautifulsoup4 >= 4.7.1
- requiests >= 2.14.2

설치는 git clone 으로 코드를 받거나 downloads 를 합니다.

## Usage

실행 코드는 Python 으로 py 파일을 실행합니다. naver_news_search_crawler 폴더로 이동합니다.

    python run_crawling.py --begin_date --end_date --output_dir

run_crawling.py 파일을 실행하면 output 폴더에 댓글이 저장됩니다. 이 파일은 몇 가지 arguments 를 제공합니다.

| argument name | default value | note |
| --- | --- | --- |
| --begin_date | LAST_MONTH| yyyymmdd 형식으로 입력되는 데이터 수집의 첫 날 |
| --end_date | TODAY | yyyymmdd 형식으로 입력되는 데이터 수집의 마지막 날 |
| --output_dir | ./output | 수집된 뉴스와 댓글의 저장 위치 |

## Directory structure

    --| crawler
        --| crawler_base.py
        --| crawler_comments.py
        --| parse_comments.py
        --| run_crawling.py
        --| output
        --| utils
            --| base.py
    --| press_list.txt

## Comments 파일 구조

| column | example | description |
| --- | --- | --- |
| comment_no | 1514778615 | 댓글 고유 아이디 |
| user_id_no | 6EVlK | 댓글 등록자 아이디의 해쉬값 |
| contents | 좋은 방향으로 얘기 잘 되었으면.. | 댓글 내용 |
| reg_time | 2018-10-28T23:41:26+0900 | 댓글 등록 시각 | 
| sympathy_count | 0 | 댓글 공감 수 |
| antipathy_count | 0 | 댓글 비공감 수 |
