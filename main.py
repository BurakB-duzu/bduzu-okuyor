'''
filepath = 'veri2.txt'
bosdict={"key":"value","key2":"vl2"}
bosdict2={"key3":"val3","key4":"val4"}
tum_toplam={"28.11":bosdict,"afsd":bosdict2}
if("28.11" in tum_toplam):
    print(tum_toplam["28.11"])
    if("burak" in tum_toplam["28.11"]):
        print(tum_toplam["28.11"]["burak"])
    else:
        tum_toplam["28.11"]["burak"]= 2
    print(tum_toplam["28.11"]["burak"])
else:
    print("as")
    #tum_toplam["ax"]="yeni"
#print(tum_toplam["ax"])

tum_toplam["Dm Muhammed Seyhan Vakıf"]=bosdict
tum_toplam["D Fikret İnan Yeşil Akasya B1 Bl D:14"]=bosdict
tum_toplam["D Ahmet Çeşmeci"]=bosdict
tum_toplam["Mehmet Karamete"]=bosdict
tum_toplam["D Erol Demir Komşu"]=bosdict
tum_toplam["D Zafer Örsdemir"]=bosdict
tum_toplam["D Dursun Pehlivanlar"]=bosdict
tum_toplam["D Mehmet Şirin Akyol Vanlı Adnan Kahveci Mh Yavuz Sultan Selim Bulvarı Göktürk 2 No:19c D:26"]=bosdict
tum_toplam["D Yusuf Cebir"]=bosdict


if "dene" in tum_toplam:
    if(tum_toplam["dene"]["key"]=="value"):
        print("asd")
    else:
        print("yok")
from collections import namedtuple
'''
from flask import Flask, redirect, url_for, request,render_template
import datetime
import pandas as pd
app = Flask(__name__)

@app.route('/')
def hello():
   return render_template('indexx.html')

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/verii',methods = ['POST'])
def verii():
    if request.method == 'POST':
        yazi = request.form['veri']
    return render_template('indexx.html',table=sonuc_hazirla(yazi)) ##böyle bi fonksiyonla tablo döndür.

def sonuc_hazirla(yazi):
    tum_toplam = {}
    kisiler = []
    for line in yazi.splitlines():#kişileri ekle
        print(line)
        x = line.split("]")
        print(x[0][1:].split()[0] + " ww " + x[1].split(":")[0] + " ww " + x[1].split(":")[1])
        gun = x[0][1:].split()[0]
        kisi = x[1].split(":")[0][1:]
        if kisi not in kisiler:
            kisiler.append(kisi)
        # tikler_str= x[1].split(":")[1]
        tikler = line.count('✅')
    hafta_gunu = datetime.datetime.now() - datetime.timedelta(days=7)
    print(hafta_gunu.weekday())
    while (hafta_gunu.weekday() != 0):
        hafta_gunu = hafta_gunu - datetime.timedelta(days=1)

    for day in range(7):
        tum_toplam[hafta_gunu.strftime("%#d/%#m")] = {}
        for kisi in kisiler:
            tum_toplam[hafta_gunu.strftime("%#d/%#m")][kisi] = 0

        hafta_gunu += datetime.timedelta(days=1)
    haftanin_pazari = hafta_gunu - datetime.timedelta(days=1)

    for line in yazi.splitlines():
        cnt = 1
        print(line)
        x = line.split("]")
        print(x[0][1:].split()[0] + " ww " + x[1].split(":")[0] + " ww " + x[1].split(":")[1])
        gun = x[0][1:].split()[0]
        kisi = x[1].split(":")[0][1:]
        # tikler_str= x[1].split(":")[1]
        tikler = line.count('✅')
        if (gun in tum_toplam):
            tum_toplam[gun][kisi] = tum_toplam[gun][kisi] + tikler
        else:  # eger hafta gunlerinde yoksa son güne koy
            tum_toplam[haftanin_pazari.strftime("%#d/%#m")][kisi] = tum_toplam[haftanin_pazari.strftime("%#d/%#m")][
                                                                        kisi] + tikler
        # tum_toplam[gun][kisi] = tum_toplam[gun][kisi] + tikler
        # kisi={kisi_ismi:tikler}
        '''
       if(gun in tum_toplam):
           if (kisi in tum_toplam[gun]):
               tum_toplam[gun][kisi]=tum_toplam[gun][kisi]+tikler
           else:
               tum_toplam[gun][kisi]=tikler
                #tum_toplam[gun][kisi]=1
       else:
           tum_toplam[gun]={}
           tum_toplam[gun][kisi]=tikler
           if kisi in tum_toplam[gun]:
                tum_toplam[gun][kisi] = tikler
           else:
               kis={}
               print("ds")
        '''
        cnt += 1
    for gun, tik_sayi in tum_toplam.items():
        print("\ntum ID:", gun)

        for key in tik_sayi:
            print(key + ':', tik_sayi[key])
            # if(tik_sayi[key]>1):

    df = pd.DataFrame(tum_toplam)
    df = df.fillna(0)
    for gn in df.axes[1]:
        print(gn + "..")
    sum_row = df.sum(axis=1)
    print(sum_row)
    col_row = df.sum(axis=0)
    print(col_row)
    df_output = pd.DataFrame(columns=df.axes[1])
    df_output.insert(0, "Kisiler", [], True)
    for kisi, sayfa in sum_row.items():
        print(f"Index : {kisi}, Value : {sayfa}")
        if (sayfa >= 7):
            df_output.loc[len(df_output)] = [kisi, "✅", "✅", "✅", "✅", "✅", "✅", "✅"]
        else:
            sonuc = [kisi, "5 tl", "5 tl", "5 tl", "5 tl", "5 tl", "5 tl", "5 tl"]
            for i in range(sayfa):
                sonuc[1 + i] = "✅"
            df_output.loc[len(df_output)] = sonuc

    '''
    for row in df.itertuples():
        for i in range(1,9):
            print(row[i])
            if(row[i]>1):
                for j in range(i,1,-1):
                    if(row[j]==0 and row[i]>1):
                        row[i]=row[i]-1
    '''

    pd.set_option('colheader_justify', 'center')  # FOR TABLE <th>

    html_string = '''
    <html>
    <meta charset="UTF-8">
      <head><title>HTML Pandas Dataframe with CSS</title></head>
      <link rel="stylesheet" type="text/css" href="df_style.css"/>
      <body>
        {table}
      </body>
    </html>
    '''
    print("AAAAAAAAAAA")
    # OUTPUT AN HTML FILE
    #with open('myhtml3.html', 'w+', encoding="utf-8") as f:
    #    f.write(html_string.format(table=df_output.to_html(classes='mystyle')))
    #return html_string.format(table=df_output.to_html(classes='mystyle'))
    return df_output.to_html(classes='mystyle')

if __name__ == '__main__':
   app.run(debug = True)
# TestTuple = namedtuple('TestTuple', ['field1', 'field2', 'field3'],'test2',)
# my_item = TestTuple('a', 'b', [1, 2])
# type(my_item)
from datetime import datetime as dd

filepath = 'veri2.txt'
bosdict = {"key": "value", "key2": "vl2"}
bosdict2 = {"key3": "val3", "key4": "val4"}
# tum_toplam={"28.11":bosdict,"afsd":bosdict2}



'''

import re

string = '[23.11 01:11] D Ahmet Çeşmeci: ✅'

# Three digit number followed by space followed by two digit number
pattern = '([[])\w+([[\]]) \w*:\w'

# match variable contains a Match object.
match = re.search(pattern, string)

if match:
    print(match.group())
else:
    print("pattern not found")
'''
