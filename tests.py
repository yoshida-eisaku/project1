import pandas as pd
import sqlite3

# Excelファイルから商品コードを読み込む
df = pd.read_excel(r'C:\Users\222061\Desktop\practice\prac\project1\inspection\testinspection.xlsx')
product_codes = df['商品コード'].astype(str).values

# SQLite3データベースに接続
connect = sqlite3.connect(r'C:\Users\222061\Desktop\practice\prac\project1\db.sqlite3')
cursor = connect.cursor()

# クエリを実行してデータを取得
cursor.execute("SELECT jan FROM app_item")
result = cursor.fetchall()
result_codes = [r[0] for r in result]

# データベース接続をクローズ
connect.close()

# 重複を格納するリスト
duplicates = []

# 商品コードの重複をチェック
for code in product_codes:
    if code in result_codes:
        duplicates.append(code)

# 重複がある場合の処理
if duplicates:
    print("以下のjanコード商品が入荷しますお客様にご連絡をお願いします:")
    for code in duplicates:
        print(code)
    # ここでポップアップを表示するなどの処理を追加してください
else:
    print("重複はありませんでした。")
