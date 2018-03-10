import requests
from time import sleep
import csv
import xml.etree.ElementTree as ET
base_url = 'https://www.boardgamegeek.com/xmlapi2'
search_path = '/search?'
thing_path = '/thing?'

array = [
    "AGRICOLA",
    "Aristo・Maze",
    "アン・ギャルド",
    "アンドールの伝説",
    "いかさまゴキブリ",
    "Elfenland",
    "王宮のささやき",
    "Old World And Code Of Nines",
    "お邪魔者 -Saboteur",
    "お邪魔者２",
    "ガイスター",
    "カタンの開拓者たち",
    "カルカソンヌ",
    "狐めくり",
    "CAMEL UP",
    "キングオブトーキョー",
    "キングオブトーキョー -パワーアップ",
    "GET・LUCKY　-キルドクターラッキーカードゲーム",
    "幻影探偵団",
#    "ごきぶりポーカー",
    "COLT EXPRESS",
    "CONCEPT",
    "ザ・ゲーム",
    "桜降る代に決闘を",
    "惨劇ルーパーカイ",
    "Secret Moon",
    "シェフィ",
    "Isle of Skye",
    "SKULL",
    "ZOMBIE TOWER 3D",
    "Ticket To Ride America",
    "チョコボのクリスタルハント",
    "ちろ鈴",
    "Die Staufer",
    "ドブル",
    "NATIONAL ECONOMY",
    "人間ゲーム -コンプレックス人狼-",
    "バトルライン",
    "HANABI",
    "PARANOIA",
    "HANDS",
    "PANDEMIC -パンデミック新たなる試練",
    "Pit",
    "Puerto Rico",
    "フェレータ",
    "フラムルルイエ",
    "Blocks",
    "ペクーニア",
    "ポイズン",
    "宝石の煌めき",
    "街コロ",
    "MANSIONS OF MADNESS",
    "マンマミーア",
    "MYSTERIUM",
    "迷宮キングダム",
    "迷宮キングダム大殺界",
    "ルイナス -Ruinous-",
    "ロビンソン漂流記 -孤島での孤独な冒険",
    "私の世界の見方",
    "WARUMONO2",
    "Once Upon a Time",
    "フルムーン 人狼の森",
    "7 Wonders 世界の七不思議",
    "コヨーテ",
    "インフェルノ",
    "ナンジャモンジャ",
    "マスカレードv",
]
f = open('data.csv','w')
writer = csv.writer(f, lineterminator='\n')
for name in array:
    url = base_url+search_path+'type=boardgame'+'&query='+name
    print(url)
    res = requests.get(url)
    root = ET.fromstring(res.text)
    if (not 'total' in root.attrib.keys()) or root.attrib['total'] == '0':
        print('見つからない')
        continue
    id = root[0].attrib['id']
    data_url = base_url+thing_path+'type=boardgame'+'&id='+id

    sleep(5)
    print(data_url)
    data_response=requests.get(data_url)
    data_xml = ET.fromstring(data_response.text)

    if data_xml.find('.//name') == None:
        print('見つからん')
        continue

    # ゲーム名
    name = data_xml.find('.//name').attrib['value']

    # プレイ最小人数
    min_player = data_xml.find('.//minplayers').attrib['value']

    # プレイ最大人数
    max_player = data_xml.find('.//maxplayers').attrib['value']

    # プレイ時間
    playingtime = data_xml.find('.//playingtime').attrib['value']
    # 画像
    image= data_xml.find('.//image').text
    print([name,min_player,max_player,playingtime,image])
    writer.writerow([name,min_player,max_player,playingtime,image])
    sleep(5)


f.close()
