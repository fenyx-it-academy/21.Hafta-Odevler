from kivy import Config
Config.set('graphics', 'multisamples', '0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.pagelayout import PageLayout
import random
country=[]
thing=[]
animal=[]
plant=[]
with open("C:\\Users\\asime\\Desktop\\Programlama\\PYTON program\\pycharm\\kivy\\stickman\\ANIMALS.txt", "r") as anml:
    anml.seek(0)
    animal=[i.upper().split() for i in anml]
    animal=[i[0] for i in animal]
with open("C:\\Users\\asime\\Desktop\\Programlama\\PYTON program\\pycharm\\kivy\\stickman\\ULKELER.txt", "r") as ulk:
    ulk.seek(0)
    country=[i.upper().split() for i in ulk]
    country=[i[0] for i in country]
with open("C:\\Users\\asime\\Desktop\\Programlama\\PYTON program\\pycharm\\kivy\\stickman\\BITKI.txt", "r") as btk:
    btk.seek(0)
    plant=[i.upper().split() for i in btk]
    plant=[i[0] for i in plant]

with open("C:\\Users\\asime\\Desktop\\Programlama\\PYTON program\\pycharm\\kivy\\stickman\\THINGS.txt", "r") as thng:
    thng.seek(0)
    thing=[i.upper().split() for i in thng]
    thing=[i[0] for i in thing]

class Window_Menu(BoxLayout):
    kontrol=False
    #*********************************************************
    def Prepair(self,data):

        if data=="START"and self.kontrol==False:
            self.resim.source = "C:\\Users\\asime\\Desktop\\Programlama\\PYTON program\\pycharm\\kivy\\stickman\\adam_asmagiris.png"

            sec=random.choice((thing,plant,country,animal))
            if sec==country:
                self.dikkat.text = "THIS WORD IS COUNTRY \n\n"
            elif sec==thing:
                self.dikkat.text = "THIS WORD IS GOODS OR THINGS \n\n"
            elif sec==plant:
                self.dikkat.text = "THIS WORD IS PLANT \n\n"
            elif sec == animal:
                self.dikkat.text = "THIS WORD IS ANIMAL \n\n"
            self.choise=random.choice(sec)
            self.R=list(self.choise)
            self.display.text= " --- "*len(self.R)

            self.box = []
            self.depo=[]
            self.sayac=8
            self.dikkat.text += "YOU HAVE "+str(self.sayac)+" ROUND"
            self.kontrol= True
    # *********************************************************
    def game_start(self,item):
        try :

            if self.kontrol==True:

                if len(self.box) == len(self.R):
                    self.dikkat.text = "BRAVOOO....,CONGRATULATIONS YOU ARE WIN  \n"
                    self.dikkat.text += "PLEASE IF YOU WANT PLAY AGAIN  ,PRESS START"
                    self.kontrol = False

                elif item in self.depo:
                    self.dikkat.text ="THIS  "+item+"  LETTER USED AGAIN ,PLEASE ANOTHER LETTER USE "
                elif item not in self.R:
                    self.depo += item
                    self.dikkat.text = "AHH  SORRY....THIS  " +item + "  LETTER IS NOT IN THE WORD\n"
                    self.sayac -= 1
                    self.dikkat.text += "YOU HAVE "+str(self.sayac)+" ROUND"
                    self.resim_goster(self.sayac)
                    if self.sayac == 0:
                        self.dikkat.text = "SOOO SORRY.... YOU ARE LOST \n"
                        self.dikkat.text += "PLEASE IF YOU WANT PLAY AGAIN  ,PRESS START"
                        self.display.text ="**********************"+self.choise+"********************"
                        self.kontrol = False

                else:
                    self.depo += item
                    self.dikkat.text = "VAOOWWW ,CONGRATULATIONS  YOU KNOW "
                    for letter in self.R:
                        if item ==letter:
                            self.box+=item
                    write=""
                    for i in self.R:
                        if i in self.box:
                            write+=i.center(5)
                        else:
                            write+=" --- ".center(5)
                    self.display.text=write
        except:
            print ("dikkat")
    # *********************************************************
    def clear_game(self,clear):

        if clear=="CLEAR":
            self.kontrol = False
            self.resim.source = "C:\\Users\\asime\\Desktop\\Programlama\\PYTON program\\pycharm\\kivy\\stickman\\adam_asmagiris.png"
            self.dikkat.text = "PLEASE PRES START TO START  "
            self.display.text =""
            self.display.text ="                                           WELCOME    "
    def resim_goster(self,sayac):
        if sayac==7:
            self.resim.source="C:\\Users\\asime\\Desktop\\Programlama\\PYTON program\\pycharm\\kivy\\stickman\\adam_asma1.png"
        elif sayac==6:
            self.resim.source="C:\\Users\\asime\\Desktop\\Programlama\\PYTON program\\pycharm\\kivy\\stickman\\adam_asma2.png"
        elif sayac==5:
            self.resim.source="C:\\Users\\asime\\Desktop\\Programlama\\PYTON program\\pycharm\\kivy\\stickman\\adam_asma3.png"
        elif sayac==4:
            self.resim.source="C:\\Users\\asime\\Desktop\\Programlama\\PYTON program\\pycharm\\kivy\\stickman\\adam_asma4.png"
        elif sayac==3:
            self.resim.source="C:\\Users\\asime\\Desktop\\Programlama\\PYTON program\\pycharm\\kivy\\stickman\\adam_asma5.png"
        elif sayac==2:
            self.resim.source="C:\\Users\\asime\\Desktop\\Programlama\\PYTON program\\pycharm\\kivy\\stickman\\adam_asma6.png"
        elif sayac==1:
            self.resim.source="C:\\Users\\asime\\Desktop\\Programlama\\PYTON program\\pycharm\\kivy\\stickman\\adam_asma7.png"
        elif sayac==0:
            self.resim.source="C:\\Users\\asime\\Desktop\\Programlama\\PYTON program\\pycharm\\kivy\\stickman\\adam_asma8.png"



    def Quit_game(self,quit):
        quit()

class HangMan(App):
    def build(self):
        self.s=Window_Menu()
        return self.s

HangMan().run()
