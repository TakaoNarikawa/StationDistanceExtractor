# GeoJsonをダウンロード

[国土数値情報　駅別乗降客数データ](http://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-S12-v2_2.html)

上記ページからダウンロード

# geojson形式をcsvに変換

乗客数データが乗っているカラム名を変更

執筆当時は`S12_025`が最新のデータだったのでこれに指定済み

example
`python3 main.py path/to/file.geojson`

変換結果が`output.csv`として出力
