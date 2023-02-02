customers=[
    {"number":"05333371000"},
    {"number":"05354321938"},
    {"number":"3840812"},
    {"number":"545 12 15"},
    {"number":"0212 512 12 78"},
    {"number":"0312 244 12 45"},
    {"number":"0216 441 45 12"},
    {"number":"0273 574 19 1"},
    {"number":"53534156 43"},
    {"number":"5422388080"},
    {"number":"1111111"},
    {"number":"3121111111"},
    {"number":"+90543 337 91 31"},
    {"number":"272 415 56 58"},
    {"number":"0312 244 12 47"},
    {"number":"0312 244 12 48"},
    {"number":"0315 233 12 33"},
    {"number":"5444321939"},
    {"number":"02164177175"}
]
cities=[
    {"İstanbul (Avrupa Yakası)":"212"},
    {"Ankara":"312"},
    {"İstanbul (Anadolu Yakası)":"216"},
    {"Afyon":"272"},
    {"Adana":"332"},
    {"Adıyaman":"416"},
    {"Ağrı":"472"},
    {"Aksaray":"382"},
    {"Amasya":"358"},
    {"Antalya":"242"},
    {"Ardahan":"478"},
    {"Artvin":"466"},
    {"Aydın":"256"},
    {"Balıkesir":"266"},
    {"Bartın":"378"},
    {"Batman":"488"},
    {"Bayburt":"458"},
    {"Bilecik":"228"},
    {"Bingöl":"426"},
    {"Bitlis":"434"},
    {"Bolu":"374"},
    {"Burdur":"248"},
    {"Bursa":"224"},
    {"Çanakkale":"286"},
    {"Çankırı":"376"},
    {"Çorum":"364"},
    {"Denizli":"258"},
    {"Diyarbakır":"412"},
    {"Düzce":"380"},
    {"Edirne":"284"},
    {"Elazığ":"424"},
    {"Erzincan":"446"},
    {"Erzurum":"442"},
    {"Eskişehir":"222"},
    {"Gaziantep":"342"},
    {"Giresun":"454"},
    {"Gümüşhane":"456"},
    {"Hakkari":"438"},
    {"Hatay":"326"},
    {"Iğdır":"476"},
    {"Isparta":"246"},
    {"İçel(Mersin)":"324"},
    {"İzmir":"232"},
    {"Karabük":"370"},
    {"Karaman":"338"},
    {"Kars":"474"},
    {"Kastamonu":"366"},
    {"Kayseri":"352"},
    {"Kırıkkale":"318"},
    {"Kırklareli":"288"},
    {"Kırşehir":"386"},
    {"Kilis":"348"},
    {"Kahramanmaraş":"344"},
    {"Kocaeli":"262"},
    {"Konya":"332"},
    {"Kütahya":"274"},
    {"Malatya":"422"},
    {"Manisa":"236"},
    {"Mardin":"482"},
    {"Muğla":"252"},
    {"Muş":"436"},
    {"Nevşehir":"384"},
    {"Niğde":"388"},
    {"Ordu":"452"},
    {"Osmaniye":"328"},
    {"Rize":"464"},
    {"Sakarya":"264"},
    {"Samsun":"362"},
    {"Siirt":"484"},
    {"Sinop":"368"},
    {"Sivas":"346"},
    {"Şanlıurfa":"414"},
    {"Şırnak":"486"},
    {"Tekirdağ":"282"},
    {"Tokat":"356"},
    {"Trabzon":"462"},
    {"Tunceli":"428"},
    {"Uşak":"276"},
    {"Van":"432"},
    {"Yalova":"226"},
    {"Yozgat":"354"},
    {"Zonguldak":"372"},
    {"KKTC":"392"},
]
organised=[]
for i in customers:
    i=i["number"].replace(" ","")
    firstNum=i.startswith("0")
    firstChar=i.startswith("+")
    if firstNum==True or firstChar==True:
        if firstNum==True:
            i=i.replace("0","",1)
            organised.append(i)
        if firstChar==True:
            i=i.replace("+90","",3)
            organised.append(i)
    else:
        organised.append(i)
j=0
x=[]
for i in organised:
    j+=1
    if len(i)!=10:
        print(f"Customer{j} : {i} (Eksik veya Hatalı Telefon Numarası)")
        x.append(j)
    else:
        mobile=i.startswith("5")
        if mobile==True:
            print(f"Customer{j} : {i} (Cep Telefonu Numarası)")
            x.append(j)
        else:
            for a in cities:
                for il,kod in a.items():
                    if i[:3] in kod:
                        print(f"Customer{j} : {i} ({il} Şehrine Ait Sabit Hat)")
                        x.append(j)
            if i[:3]!=kod:   
                    if j in x:
                        continue
                    else:    
                        print(f"Customer{j} : {i} (Yurtdışı Tabanlı Telefon Numarası)")
                        x.append(j)