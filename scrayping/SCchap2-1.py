import requests
from bs4 import BeautifulSoup
import csv
import re
from datetime import datetime, timedelta

# 現在の日付を取得
now = datetime.now()

# CSVファイルを開く（ヘッダーを含めて書き込む）
with open('test.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Data', 'Date'])

    # 各ページにアクセス
# 各ページにアクセス
for i in range(1, 6):
    load_url = f"https://finance.yahoo.co.jp/stocks/ranking/listingDate?market=all&term=daily&page={i}"
    response = requests.get(load_url)

    # レスポンスが成功かどうかチェック
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")

        # tr要素を取得
        rows = soup.find_all('tr', class_="_1GwpkGwB")

        # それぞれの行について処理
        for row in rows:
            # 特定のtdクラスに含まれるspan要素を取得
            date_span = row.select_one('td.P452zeXX.i9grwWp1._2Iu2a9lx span._3rXWJKZF')

            # spanが存在する場合、そのテキストを取得
            if date_span:
                date_text = date_span.text.strip()
                print("Date Text:", date_text)  # 日付テキストを表示

                try:
                    # 日付の形式を解析
                    date_obj = datetime.strptime(date_text, '%Y/%m/%d')

                    # 日付が今日から1年以内であるか確認
                    if now - timedelta(days=365) <= date_obj <= now:
                        # 日付が条件に合う場合、関連するデータを取得
                        data = row.find('li', class_="vv_mrYM6").text.strip()

                        # データが数字の場合のみ書き込み
                        if re.search(r'\d', data):
                            writer.writerow([data, date_text])
                except ValueError:
                    print(f"Date format error: {date_text}")
    else:
        print(f"Failed to get data from page {i}, status code: {response.status_code}")

