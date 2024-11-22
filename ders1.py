meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "BUG": "Oyundaki sistem hatası",
            "BB" : "BayBay kısaltması Türkçe anlamıda görüşürüz veya hoşçakal",
            "ÇAR":"Oyundaki hesap",
            "AYN":"Aynen kelimesinin kısaltmasıdır"
            }

word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("Kelime sözlükte bulunmuyor veya yanlış yazdınız")
