# a_master_of_go
an iOS App of a strong Go AI

## Downloadable extra weights
Please copy one of URLs below and paste "DL weight from:" field in the setting modal on the app.

<dl>
<dt>https://github.com/new3Rs/a_master_of_go/releases/download/LeelaMaster_GX89/LeelaMaster_GX89_fp16.json (If your internet connection to github is slow, please try https://files.fm/down.php?i=jke8zm7t&n=LeelaMaster_GX89_fp16.json.)</dt>
<dd>[Leela Master](https://github.com/pangafu/LeelaMasterWeight) weight(GX89). This is a 15b weight trained using 80% human style games and 20% Leela Zero games. 章鱼围棋(Octopus Go) & 袁泉(pangafu@github) are making Leela Master.</dd>
<dt>https://github.com/new3Rs/a_master_of_go/releases/download/LeelaZero_226/LeelaZero_226_fp16.json (If your internet connection to github is slow, please try https://files.fm/down.php?i=734d8pyb&n=LeelaZero_226_fp16.json.)</dt>
<dd>[Leela Zero](https://github.com/leela-zero/leela-zero) #226 weight. This is a 40b weight trained by self-plays.</dd>
<dt>https://github.com/new3Rs/a_master_of_go/releases/download/minigo_v17/minigo_v17_fp16.json (If your internet connection to github is slow, please try https://files.fm/down.php?i=9ms8d6kc&n=minigo_v17_fp16.json.)</dt>
<dd>[minigo](https://github.com/tensorflow/minigo) v17 weight(001003-leviathan). WARNING: Version 3.4.0 or later is required. This weight is very heavy even if you use A12 processor (less than 30 nps).</dd>
</dl>

## How to make your own downloadable weights
See https://github.com/new3Rs/a_master_of_go/blob/master/LZ2mlmodel/README.md.