import pandas as pd

url = 'https://kworb.net/youtube/topvideos2020.html'
yt_2020 = pd.read_html(url, header = 0, index_col = 0)

if yt_2020:
    df = yt_2020[0]
    df.to_csv("youtube2020.csv", encoding= 'utf-8', index_label = 'Video')
    print("Youtube 2020 extracted and saved successfully")
else:
    print("Youtube 2020 not found")