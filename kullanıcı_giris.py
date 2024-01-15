print("""*******************************
Kullanıcı Giriş Programı
*******************************
""")

sys_kullanici_adi= "zafomastik"
sys_parola= "12345"
giris_hakki= 3


while True:
        kullanıcı_adı= input("Kullanıcı adı:")
        parola = input("Parola:")
        if (kullanıcı_adı==sys_kullanici_adi and parola!=sys_parola):
            print("Parola hatalı.")
            giris_hakki-=1
        elif (kullanıcı_adı!=sys_kullanici_adi and parola==sys_parola):
            print("kullanıcı adı hatalı.")
            giris_hakki-=1
        elif (kullanıcı_adı!=sys_kullanici_adi and parola!=sys_parola):
            print("ikisi de hatalı.")
            giris_hakki-=1
        else:
            print("Başarıyla giriş yaptınız.")
            break
        if (giris_hakki==0):
            print("Hakkınız doldu.")
            break