from bs4 import BeautifulSoup
import requests
import mysql.connector # MySQL

url = 'https://b.hatena.ne.jp/togetter/bookmark?page={0}'

# DB接続
def data_registration_single(self):
    connection = mysql.connector.connect(
        user = 'kasumidyaya',
        password = 'root',
        host = 'localhost',
        database = 'comment_list',
        charset = 'utf8'
    )
    cursor = connection.cursor()
    cursor.execute("USE comment_list")
    connection.commit()

    for i in range(1,3):
        r = requests.get(url.format(i))
        soup = BeautifulSoup(r.text,'html.parser')
        results = soup.find_all(class_='js-comment')
        for result in results:
            i = i + 1
            print(result.get_text())

            # データ挿入
            cursor.execute("INSERT INTO comment_list(comment) VALUES (%s)", (self['comment']))
            connection.commit()
            printf('---DB登録に成功---')

    cursor.close
    connection.close