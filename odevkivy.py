from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.lang import Builder
from random import choice

Builder.load_file("odevkivy.kv")

class Manager(ScreenManager):
    pass

class Screen_1(Screen):
    pass

class Screen_2(Screen):
    gizli_kelime = list(choice(["LAMBA", "PORTAKAL", "ELMA", "BARDAK", "PENCERE", "DEMOKRASI", "KALEMLIK"]))
    cizgili_list =["_" for i in range(len(gizli_kelime))]
    cizgili=""
    for i in cizgili_list:
        cizgili+=i
    hak = 6
    puan = 5
    kullanilan_harf = "Kullanilan harfler: "
    havuz = []
    uyari = ""
    def oyuncalistir(self,harf):
        label_kullanilanharf=self.ids["text_1"]
        label_hak=self.ids["text_2"]
        label_puan=self.ids["text_3"]
        label_kelime=self.ids["kelime"]
        text_durum=self.ids["durum"]
        label_kullanilanharf.text=self.kullanilan_harf
        label_hak.text="Kalan hak:"+str(self.hak)
        label_puan.text="Puan:"+str(self.puan)
        label_kelime.text=self.cizgili
        text_durum.text=self.uyari

        if harf in self.havuz:
            self.uyari="Bu harf daha once kullanilmistir"
        else:
            if harf not in self.gizli_kelime:
                self.uyari="Yanlis Tahmin"
                self.hak-=1
                self.kullanilan_harf+=harf
                self.havuz.append(harf)
                if self.hak==0:
                    self.uyari="OYUNU KAYBETTINIZ"
                    self.puan=0
                    self.hak=0
            else:
                self.havuz.append(harf)
                for i in range(len(self.gizli_kelime)):
                    if harf==self.gizli_kelime[i]:
                        self.cizgili_list[i]=harf
                        self.cizgili = ""
                        for i in self.cizgili_list:
                            self.cizgili += i
                        self.puan+=10
                        self.uyari="Dogru Tahmin"
                        if self.cizgili_list==self.gizli_kelime:
                            self.uyari="TEBRIKLER OYUNU KAZANDINIZ"



        label_kullanilanharf.text = self.kullanilan_harf
        label_hak.text = "Kalan hak:" + str(self.hak)
        label_puan.text = "Puan:" + str(self.puan)
        label_kelime.text = self.cizgili
        text_durum.text = self.uyari
        label_hak.setter("text")
        label_puan.setter("text")
        label_kullanilanharf.setter("text")
        label_kelime.setter("text")
        text_durum.setter("text")

class feedback(Screen):
    uyari=Screen_2.uyari

    pass



class AdamAs(App):
    def build(self):
        return Manager()

if __name__=="__main__":
    AdamAs().run()