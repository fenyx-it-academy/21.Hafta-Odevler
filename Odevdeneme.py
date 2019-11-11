from kivy.app import App
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.core.window import Window
from random import choice

Window.clearcolor = .3,.3,.3,1

kelimeler = ['AFGHANISTAN', 'ALBANIA', 'ALGERIA', 'ANDORRA', 'ANGOLA', 'ARGENTINA', 'ARMENIA', 'AUSTRALIA', 'AUSTRIA',
             'AZERBAIJAN', 'BAHRAIN', 'BANGLADESH', 'BARBADOS', 'BELARUS', 'BELGIUM', 'BELIZE', 'BENIN', 'BHUTAN',
             'BOLIVIA', 'BOTSWANA', 'BRAZIL', 'BRUNEI', 'BULGARIA', 'BURKINA_FASO', 'BURUNDI', 'CAMBODIA', 'CAMEROON',
             'CANADA', 'CHAD', 'CHILE', 'CHINA', 'COLOMBIA', 'COMOROS', 'CONGO', 'COSTA_RICA', 'CROATIA', 'CUBA',
             'CYPRUS', 'CZECH_REPUBLIC', 'DENMARK', 'DOMINICA', 'DOMINICAN_REPUBLIC', 'ECUADOR', 'EGYPT', 'EL_SALVADOR',
             'EQUATORIAL_GUINEA', 'ERITREA', 'ESTONIA', 'ESWATINI', 'ETHIOPIA', 'FINLAND', 'FRANCE', 'GABON', 'GAMBIA',
             'GEORGIA', 'GERMANY', 'GHANA', 'GREECE', 'GRENADA', 'GUATEMALA', 'GUINEA', 'GUYANA', 'HAITI', 'HONDURAS',
             'HUNGARY', 'ICELAND', 'INDIA', 'INDONESIA', 'IRAN', 'IRAQ', 'IRELAND', 'ISRAEL', 'ITALY', 'JAMAICA',
             'JAPAN', 'JORDAN', 'KAZAKHSTAN', 'KENYA', 'KOREA', 'KOSOVO', 'KUWAIT', 'KYRGYZSTAN', 'LAOS', 'LATVIA',
             'LEBANON', 'LIBERIA', 'LIBYA', 'LIECHTENSTEIN', 'LITHUANIA', 'LUXEMBOURG', 'MADAGASCAR', 'MALAWI',
             'MALAYSIA', 'MALDIVES', 'MALI', 'MALTA', 'MAURITANIA', 'MAURITIUS', 'MEXICO', 'MOLDOVA', 'MONACO',
             'MONGOLIA', 'MONTENEGRO', 'MOROCCO', 'MOZAMBIQUE', 'MYANMAR', 'NEPAL', 'NETHERLANDS', 'NEW_ZEALAND',
             'NICARAGUA', 'NIGER', 'NIGERIA', 'NORWAY', 'OMAN', 'PAKISTAN', 'PANAMA', 'PARAGUAY', 'PERU', 'PHILIPPINES',
             'POLAND', 'PORTUGAL', 'QATAR', 'ROMANIA', 'RUSSIA', 'SAN_MARINO', 'YEMEN', 'SAUDI_ARABIA', 'SENEGAL',
             'SERBIA', 'SINGAPORE', 'SLOVAKIA', 'SLOVENIA', 'SOMALIA', 'SOUTH_AFRICA', 'SPAIN', 'SRI_LANKA', 'SUDAN',
             'SURINAME', 'SWEDEN', 'SWITZERLAND', 'SYRIA', 'TAIWAN', 'TAJIKISTAN', 'TANZANIA', 'THAILAND', 'TOGO',
             'TONGA', 'TUNISIA', 'TURKEY', 'TURKMENISTAN', 'TUVALU', 'UGANDA', 'UKRAINE', 'UNITED_ARAB_EMIRATES',
             'UNITED_KINGDOM', 'UNITED_STATES', 'URUGUAY', 'UZBEKISTAN', 'VATICAN_CITY', 'VENEZUELA', 'VIETNAM',
             'ZAMBIA', 'ZIMBABWE']


class Oyunalani(Screen):
    def kelime(self):
        self.seckelime = list(choice(kelimeler))
        self.bulliste = []
        for i in range(len(self.seckelime)):
            self.bulliste.append("_")
        self.display.text = "Kelimeniz {} harfden olusmaktadir. \nLutfen bir harf seciniz. ".format(len(self.seckelime))
        self.sayac = 1
        self.harfler = []
        self.screen.source = "copadam\copadam0.png"

    def tahmin(self,harf):
        if self.bulliste == self.seckelime or self.sayac == 11:
            self.display.text = "Tekrar oynamak icin lutfen Yeni Oyun butonuna basiniz"
            return
        for i in range(len(self.seckelime)):
            if self.seckelime[i] == harf:
                self.bulliste[i] = self.seckelime[i]
            self.display.text = "\n\n\n {}".format("   ".join(self.bulliste).center(70))
            if self.bulliste == self.seckelime:
                self.display.text = "TEBRIKLER: \n\n\n {}".format("   ".join(self.seckelime).center(70))
        if harf not in self.harfler:
            if harf not in self.seckelime:
                self.sayac +=1
                self.resim(self.sayac)
                self.screen1.text += "{}, ".format(harf)
        else:
            self.display.text += "\n\n Bu harfi zaten tahmin ettiniz."
        self.harfler.append(harf)


    def resim(self,sayac):
        if sayac == 2:
            self.screen.source = "copadam\copadam1.png"
        elif sayac == 3:
            self.screen.source = "copadam\copadam2.png"
        elif sayac == 4:
            self.screen.source = "copadam\copadam3.png"
        elif sayac == 5:
            self.screen.source = "copadam\copadam4.png"
        elif sayac == 6:
            self.screen.source = "copadam\copadam5.png"
        elif sayac == 7:
            self.screen.source = "copadam\copadam6.png"
        elif sayac == 8:
            self.screen.source = "copadam\copadam7.png"
        elif sayac == 9:
            self.screen.source = "copadam\copadam8.png"
        elif sayac == 10:
            self.screen.source = "copadam\copadam9.png"
        elif sayac == 11:
            self.screen.source = "copadam\copadam10.png"
            self.display.text = "Oyun Bitti.\nKelimeniz: {}. \nYeni Oyun butonuna basiniz.".format("".join(self.seckelime))


class Window(ScreenManager):
    pass


class Adamasmacadeneme(App):
    def build(self):
        return Window()


if __name__ == "__main__":
    Adamasmacadeneme().run()