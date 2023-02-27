print("Hesap makinesine hoşgeldiniz")
cikis = 0
while cikis == 0:
    print("1-Toplama")
    print("2-Çıkarma")
    print("3-Çarpma")
    print("4-Bölme")
    print("5-Üs alma")
    print("6-Kalan bulma")
    print("Çıkış için -1'e basınız")
    islem = int(input("Yapmak istediğiniz işlemi sayılarla belirtiniz "))
    if islem == 1:
        sayi1 = int(input("Lütfen 1.sayıyı giriniz..."))
        sayi2 = int(input("Lütfen 2.sayıyı giriniz..."))
        sonuc = sayi1+ sayi2
        print(f'"Sonuç :{sonuc}')
    elif islem == 2 :
        sayi1 = int(input("Lütfen 1.sayıyı giriniz..."))
        sayi2 = int(input("Lütfen 2.sayıyı giriniz..."))
        sonuc = sayi1 - sayi2
        print(sonuc)
    elif islem == 3:
        sayi1 = int(input("Lütfen 1.sayıyı giriniz..."))
        sayi2 = int(input("Lütfen 2.sayıyı giriniz..."))
        sonuc = sayi1 * sayi2
        print(sonuc)
    elif islem == 4 :
        sayi1 = input("Lütfen 1.sayıyı giriniz...")
        sayi2 = input("Lütfen 2.sayıyı giriniz...")
        sonuc = sayi1 / sayi2
        print(sonuc)
    elif islem == 5 :
        sayi1 = input("Lütfen tabanını giriniz...")
        sayi2 = input("Lütfen üssünü giriniz...")
        sonuc = sayi1^sayi2
        print(sonuc)
    elif islem == 6 :
        sayi1 = int(input("Lütfen bölününce kalanını bulmak istediğiniz sayıyı giriniz..."))
        sayi2 = int(input("Lütfen böleni giriniz..."))
        sonuc = sayi1 % sayi2
        print(sonuc)
    elif islem == -1 :
        cikis = -1
    else :
        print("Hatalı bir tuşlama yaptınız")
        