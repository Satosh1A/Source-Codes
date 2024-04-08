import keyword
import pandas as pd

print(len(keyword.kwlist))#36

name = '安藤聡志'
age = 21
height = 172.8
print('私の名前は{}です．年齢は{}歳で，身長は{}cmです．'.format(name,age,height))

scores = {'network':60,'database':80,'security':55}#ディクショナリ
members = ['安藤','石丸','後藤','関口']
print(tuple(members))#('安藤','石丸','後藤','関口')
print(list(scores))#['network','database','security']
print(set(scores.values()))#{80,60,55}
print(scores['database'])#80

# データフレームの作成
df = pd.DataFrame({
    "名前": ["John", "Doe"],
    "年齢": [25, 30],
    "職業": ["教師", "エンジニア"]
})

# データフレームの出力
print(df)
