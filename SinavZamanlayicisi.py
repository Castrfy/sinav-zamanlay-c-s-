import math
from sys import platform
from tkinter import PhotoImage
import customtkinter as tk
import time
import datetime
import _tkinter
import os
import platform
import PIL
from tkinter import *
var = 0
def getColors():
    global backColor,foreColor
    if tk.get_appearance_mode() == "Light":
        backColor = "#a0a8ba"
        foreColor = "#d1d5df"
    elif tk.get_appearance_mode() == "Dark":
        backColor = "#555555"
        foreColor = "#908f8f"
getColors()
def round_rectangle(x1, y1, x2, y2,canvas, radius=25, **kwargs): # Creating a rounded rectangle
    
    points = [x1+radius, y1,
                   x1+radius, y1,
                    x2-radius, y1,
                    x2-radius, y1,
                    x2, y1,
                    x2, y1+radius,
                    x2, y1+radius,
                    x2, y2-radius,
                    x2, y2-radius,
                    x2, y2,
                    x2-radius, y2,
                    x2-radius, y2,
                    x1+radius, y2,
                    x1+radius, y2,
                    x1, y2,
                    x1, y2-radius,
                    x1, y2-radius,
                    x1, y1+radius,
                    x1, y1+radius,
                    x1, y1]
    return canvas.create_polygon(points, **kwargs, smooth=True)

class get_win(tk.CTk):
    def __init__(self, screenName: str | None = None, baseName: str | None = None, className: str = "Tk", useCTk: bool = True, sync: bool = False, use: str | None = None) -> None:
        super().__init__()
        if self.winfo_screenwidth() == 1368 and self.winfo_screenheight() == 768:
            self.width = 700
            self.height = 700
        elif self.winfo_screenwidth() == 3840 and self.winfo_screenheight() == 2160:
            self.width = 2000
            self.height = 2000
        else:
            self.width = 1000
            self.height = 1000
        self.iconbitmap("icon.ico")
        self.x = int((self.winfo_screenwidth()/2)-(self.width/2))
        self.y = int((self.winfo_screenheight()/2)-(self.height/2))-(20)
        self.geometry(f"{self.width}x{self.height}+{self.x}+{self.y}")
        self.title("Sınav Zamanlayıcısı")
        self.canvas = tk.CTkCanvas(self,width=self.width,height=self.height,bg="grey",highlightthickness=0)
        self.canvas.place(x=0,y=0)
        self.overrideredirect(True)
        self.canvas.config(bg="grey")
        self.config(background='grey')
        self.attributes("-transparentcolor", "grey")
        '''
            tasarım 1
        self.clockLabel = tk.CTkLabel(self.canvas,font=("Yu Gothic Bold",90),text="",bg_color="#908f8f",text_color="black")
        self.clockLabel.place(x=310,y=805)
        round_rectangle(50,0,950,900,self.canvas,radius=100,fill="#908f8f")
        self.draw_circle(color="#555555",canvas=self.canvas,radius=400,centerx=500,centery=405)
        '''
        self.name = "[süreyi ayarlayın]"
        self.time_started = False
        self.time_finished = False
        self.stopanim = False
        self.t = 0
        self.finishTime = 0
        self.clockTime = 0
        self.sumTime = 0
        self.turn = 0

        self.animt = 0
        self.animspeed = 1
        self.animpoints = []
        
        x = 100*math.cos((470+(100*630))/100)+500
        y = 100*math.sin((470+(100*630))/100)+500
        self.animpoints.append(x)
        self.animpoints.append(y)
        print(self.animpoints)
        self.dersIndex = -1
        delta = datetime.datetime.now()
        self.dersSaatleri = [[(9,0),(9,40)],[(9,50),(10,30)],[(10,40),(11,20)],[(11,30),(12,10)],[(12,50),(13,30)],[(13,40),(14,20)],[(14,30),(15,10)],[(15,20),(16,0)]]
        
        self.settingsWinON = False
        
        for ders in self.dersSaatleri:
            if ders[1][0] >= delta.hour >= ders[0][0]:
                if delta.hour == ders[1][0]:
                    if ders[1][1] > delta.minute >= 0:self.dersIndex = self.dersSaatleri.index(ders)+1
                        
                elif delta.hour == ders[0][0]:
                    if 59 >= delta.minute >= ders[0][1]:
                        if 59 >= delta.second:self.dersIndex = self.dersSaatleri.index(ders)+1
                            
                        
        if self.width == 700 and self.height == 700:
            self.settingsButton = tk.CTkButton(self.canvas,width=25,height=25,image=PhotoImage(file="settings.png"),corner_radius=10,bg_color=foreColor,fg_color=foreColor,text="",hover_color="#858585",text_color="black",font=("Yu Gothic Bold",20),command=self.settingsCommand)        
            self.exitButton = tk.CTkButton(self.canvas,height=20,fg_color=foreColor,text="Masaüstüne dön",corner_radius=10,bg_color=foreColor,hover_color="#858585",text_color="black",font=("Yu Gothic Bold",15),command=self.myexit)
            self.dersLabel = tk.CTkLabel(self.canvas,font=("Yu Gothic",40),text=f"{self.dersIndex}. Ders",width=400,bg_color=foreColor,text_color="black")
            self.dateLabel = tk.CTkLabel(self.canvas,font=("Yu Gothic",40),text="Tarih\nPerş.",width=400,bg_color=foreColor,text_color="black")
            self.clockLabel = tk.CTkLabel(self.canvas,font=("Yu Gothic",40),text="",width=300,bg_color=foreColor,text_color="black")                
            self.nameLabel = tk.CTkLabel(self.canvas,font=("Yu Gothic Bold",40),text=self.name,width=300,anchor="center",bg_color=foreColor,text_color="black")
            self.sumLabel = tk.CTkLabel(self.canvas,font=("Yu Gothic Bold",70),text="",bg_color=foreColor,text_color="black")
        elif self.width == 2000 and self.height == 2000:
            self.settingsButton = tk.CTkButton(self.canvas,width=100,height=100,image=PhotoImage(file="settings.png"),corner_radius=20,bg_color=foreColor,fg_color=foreColor,text="",hover_color="#858585",text_color="black",font=("Yu Gothic Bold",20),command=self.settingsCommand)        
            self.exitButton = tk.CTkButton(self.canvas,height=50,fg_color=foreColor,text="Masaüstüne dön",corner_radius=10,bg_color=foreColor,hover_color="#858585",text_color="black",font=("Yu Gothic Bold",40),command=self.myexit)
            self.dersLabel = tk.CTkLabel(self.canvas,font=("Yu Gothic",100),text=f"{self.dersIndex}. Ders",width=800,bg_color=foreColor,text_color="black")
            self.dateLabel = tk.CTkLabel(self.canvas,font=("Yu Gothic",100),text="Tarih\nPerş.",width=600,bg_color=foreColor,text_color="black")
            self.clockLabel = tk.CTkLabel(self.canvas,font=("Yu Gothic",100),text="",width=600,bg_color=foreColor,text_color="black")                
            self.nameLabel = tk.CTkLabel(self.canvas,font=("Yu Gothic Bold",100),text=self.name,width=1000,anchor="center",bg_color=foreColor,text_color="black")
            self.sumLabel = tk.CTkLabel(self.canvas,font=("Yu Gothic Bold",200),text="",bg_color=foreColor,text_color="black")
        else:
            self.settingsButton = tk.CTkButton(self.canvas,width=50,height=50,image=PhotoImage(file="settings.png"),corner_radius=10,bg_color=foreColor,fg_color=foreColor,text="",hover_color="#858585",text_color="black",font=("Yu Gothic Bold",20),command=self.settingsCommand)        
            self.exitButton = tk.CTkButton(self.canvas,height=28,fg_color=foreColor,text="Masaüstüne dön",corner_radius=2,bg_color=foreColor,hover_color="#858585",text_color="black",font=("Yu Gothic Bold",20),command=self.myexit)
            self.dersLabel = tk.CTkLabel(self.canvas,font=("Yu Gothic",50),text=f"{self.dersIndex}. Ders",width=400,bg_color=foreColor,text_color="black")
            self.dateLabel = tk.CTkLabel(self.canvas,font=("Yu Gothic",50),text="Tarih\nPerş.",width=400,bg_color=foreColor,text_color="black")
            self.clockLabel = tk.CTkLabel(self.canvas,font=("Yu Gothic",50),text="",width=300,bg_color=foreColor,text_color="black")                
            self.nameLabel = tk.CTkLabel(self.canvas,font=("Yu Gothic Bold",50),text=self.name,width=500,anchor="center",bg_color=foreColor,text_color="black")
            self.sumLabel = tk.CTkLabel(self.canvas,font=("Yu Gothic Bold",100),text="",bg_color=foreColor,text_color="black")
        
        if self.dersIndex == -1:
            self.dersLabel.configure(text="Teneffüs")
            if delta.hour < 9 or delta.hour > 17:
                self.dersLabel.configure(text="Okul Saati Değil")
                
        if self.width == 700 and self.height == 700:
            self.settingsButton.place(x=320,y=560)
            self.exitButton.place(x=285,y=615)
            self.dersLabel.place(x=150,y=400)
            self.dateLabel.place(x=150,y=450)
            self.clockLabel.place(x=190,y=500)
            self.nameLabel.place(x=180,y=150)
            self.sumLabel.place(x=90,y=210)
        elif self.width == 2000 and self.height == 2000:
            self.settingsButton.place(x=940,y=1600)
            self.exitButton.place(x=820,y=1720)
            self.dersLabel.place(x=600,y=1160)
            self.dateLabel.place(x=700,y=1300)
            self.clockLabel.place(x=700,y=1440)
            self.nameLabel.place(x=520,y=660)
            self.sumLabel.place(x=260,y=800)
        else:
            self.settingsButton.place(x=470,y=800)
            self.exitButton.place(x=420,y=860)
            self.dersLabel.place(x=300,y=580)
            self.dateLabel.place(x=300,y=650)
            self.clockLabel.place(x=350,y=720)
            self.nameLabel.place(x=260,y=330)
            self.sumLabel.place(x=130,y=400)

        if self.width == 700 and self.height == 700:
            self.draw_circle(color=backColor,canvas=self.canvas,radius=350,centerx=350,centery=350)
            self.draw_circle(color=foreColor,canvas=self.canvas,radius=300,centerx=350,centery=350)
        elif self.width == 2000 and self.height == 2000:
            self.draw_circle(color=backColor,canvas=self.canvas,radius=1000,centerx=1000,centery=1000)
            self.draw_circle(color=foreColor,canvas=self.canvas,radius=800,centerx=1000,centery=1000)
        else:
            self.draw_circle(color=backColor,canvas=self.canvas,radius=500,centerx=500,centery=500)
            self.draw_circle(color=foreColor,canvas=self.canvas,radius=400,centerx=500,centery=500)
       


    def create_polygon(self,points, **kwargs):
        if 'alpha' in kwargs:
            alpha = int(kwargs.pop('alpha') * 255)
            fill = kwargs.pop('fill')
            fill = self.winfo_rgb(fill) + (alpha,)
            
            pim = PIL.Image.new('RGBA', (400,400), fill)
            photo = PIL.ImageTk.PhotoImage(pim)
            self.transparentlabel= tk.CTkLabel(self.canvas,text="",image=photo,width=400,height=400)
            self.transparentlabel.place(x=300,y=300)
            print(fill)
        #self.canvas.create_polygon(points, **kwargs)
    
    #animasyon deneme    
    def mainAnimation(self):
        

        if self.animt == 0:
            points = list()
            for i in range(628+1):
                konum = (390*math.cos(i/100)+500,390*math.sin(i/100)+500)
                points.append(konum[0])
                points.append(konum[1])
            for i in range(628+1):
                konum = (385*math.cos(629-i/100)+500,385*math.sin(629-i/100)+500)
                points.append(konum[0])
                points.append(konum[1])
        
            self.create_polygon(points, fill=backColor,alpha=.5,tags="x")
            self.animt += 1

        if self.animt < 10000:
            self.animt += 1

    def myexit(self):
        global On
        On = False
        self.destroy()
        
    def settingsCommand(self):
        global var
        if self.settingsWinON:
            try:
                self.settingsWin.focus()
            except _tkinter.TclError:
                print("İptal Ediliyor...")
                
                self.time_started = False
                self.t = 0
                self.finishTime = 0
                self.clockTime = 0
                self.sumTime = 0
                self.stopanim = True 
                self.settingsButton.configure(text="")
                if self.width == 700 and self.height == 700:
                    self.settingsButton.place(x=320,y=560)
                if self.width == 2000 and self.height == 2000:
                    self.settingsButton.place(x=940,y=1600)
                else:
                    self.settingsButton.place(x=470,y=800)
                self.nameLabel.configure(text="[süreyi ayarlayın]")
                self.sumLabel.configure(text="")
                self.canvas.delete("s")
                self.canvas.delete("x")

                self.settingsWinON = False
        else:
            self.settingsWinON = True
            self.settingsWin = tk.CTkToplevel(self)
            self.settingsWin.geometry(f"700x700+{int((self.winfo_screenwidth()/2)-(700/2))}+{int((self.winfo_screenheight()/2)-(700/2))}")
            self.settingsWin.protocol("WM_DELETE_WINDOW",self.settingsExit)
            self.settingsWin.title("Ayarlar")
            
            self.hourEntry = tk.CTkEntry(self.settingsWin,width=35,height=28,placeholder_text="00",font=("Yu Gothic",20),border_width=1)
            self.hourEntry.place(x=120,y=250)
            self.minuteEntry = tk.CTkEntry(self.settingsWin,width=35,height=28,placeholder_text="00",font=("Yu Gothic",20),border_width=1)
            self.minuteEntry.place(x=190,y=250)
            self.sepLabel = tk.CTkLabel(self.settingsWin,font=("Yu Gothic Bold",20),text=":",width=35,bg_color="transparent",text_color="gray")
            self.sepLabel.place(x=155,y=250)
            self.nameEntry = tk.CTkEntry(self.settingsWin,width=140,height=28,placeholder_text="Sınav adı",font=("Yu Gothic",20),border_width=1)
            self.nameEntry.place(x=100,y=290)
            
            self.dersVariable = tk.StringVar()
            self.dersComboBox = tk.CTkComboBox(self.settingsWin,variable=self.dersVariable,width=100,height=28,corner_radius=2,font=("Yu Gothic",15),dropdown_font=("Yu Gothic",15),values=["Bu dersin","1. dersin","2. dersin","3. dersin","4. dersin","5. dersin","6. dersin","7. dersin","8. dersin"],border_width=1)
            self.dersComboBox.set("Bu dersin")
            self.dersComboBox.place(x=280,y=250)
            self.sonbasVariable = tk.StringVar()
            self.sonbasComboBox = tk.CTkComboBox(self.settingsWin,variable=self.sonbasVariable,width=100,height=28,corner_radius=2,font=("Yu Gothic",15),dropdown_font=("Yu Gothic",15),values=["sonuna","başına"],border_width=1)
            self.sonbasComboBox.set("sonuna")
            self.sonbasComboBox.place(x=390,y=250)
            self.ayarladersButton = tk.CTkButton(self.settingsWin,text="Ayarla",font=("Yu Gothic Bold",15),command=lambda : self.ayarla(ders = self.dersVariable.get(), sonu = self.sonbasVariable.get()))
            self.ayarladersButton.place(x=500,y=250)

            self.sureVariable = tk.StringVar()
            self.sureComboBox = tk.CTkComboBox(self.settingsWin,variable=self.sureVariable,width=100,height=28,corner_radius=2,font=("Yu Gothic",15),dropdown_font=("Yu Gothic",15),values=["1 dk","3 dk","5 dk","10 dk","15 dk","30 dk","40 dk","1 sa","1 sa 20 dk","1 sa 40 dk","2 sa","2 sa 30 dk","3 sa","4 sa"],border_width=1)
            self.sureComboBox.set("40 dk")
            self.sureComboBox.place(x=280,y=290)
            self.sonrayaLabel = tk.CTkLabel(self.settingsWin,font=("Yu Gothic",15),text="sonraya",width=60,height=28,bg_color="transparent")
            self.sonrayaLabel.place(x=390,y=290)
            self.ayarlasureButton = tk.CTkButton(self.settingsWin,text="Ayarla",font=("Yu Gothic Bold",15),command=lambda : self.sureayarla(self.sureVariable.get()))
            self.ayarlasureButton.place(x=500,y=290)
            
            self.themeButton = tk.CTkButton(self.settingsWin,text=f"Tema: {tk.get_appearance_mode()}",font=("Yu Gothic Bold",20),command=self.changeTheme)
            self.themeButton.place(x=550,y=50)
            self.timeStartButton = tk.CTkButton(self.settingsWin,text="Saati Başlat",font=("Yu Gothic Bold",20),command=self.startTime)
            self.timeStartButton.place(x=300,y=500)
            var = 1

    def ayarla(self,ders:str,sonu:str):
        if len(self.hourEntry.get()) != 0:self.hourEntry.delete(0,len(self.hourEntry.get()))
        if len(self.minuteEntry.get()) != 0:self.minuteEntry.delete(0,len(self.minuteEntry.get()))
        if len(self.nameEntry.get()) != 0:self.nameEntry.delete(0,len(self.nameEntry.get()))
        match sonu:
            case "sonuna":
                if ders == "Bu dersin":
                    if self.dersIndex != -1:
                        saat = str(self.dersSaatleri[self.dersIndex-1][1][0]).zfill(2)
                        dk = str(self.dersSaatleri[self.dersIndex-1][1][1]).zfill(2)
                        self.hourEntry.insert(0,saat)
                        self.minuteEntry.insert(0,dk)
                        self.nameEntry.insert(0,"Sınav")
                else:
                    saat = str(self.dersSaatleri[int(ders[0])-1][1][0]).zfill(2)
                    dk = str(self.dersSaatleri[int(ders[0])-1][1][1]).zfill(2)
                    self.hourEntry.insert(0,saat)
                    self.minuteEntry.insert(0,dk)
                    self.nameEntry.insert(0,"Sınav")
            case "başına":
                if ders == "Bu dersin":
                    if self.dersIndex != -1:
                        saat = str(self.dersSaatleri[self.dersIndex-1][0][0]).zfill(2)
                        dk = str(self.dersSaatleri[self.dersIndex-1][0][1]).zfill(2)
                        self.hourEntry.insert(0,saat)
                        self.minuteEntry.insert(0,dk)
                        self.nameEntry.insert(0,"Sınav")
                else:
                    saat = str(self.dersSaatleri[int(ders[0])-1][0][0]).zfill(2)
                    dk = str(self.dersSaatleri[int(ders[0])-1][0][1]).zfill(2)
                    self.hourEntry.insert(0,saat)
                    self.minuteEntry.insert(0,dk)
                    self.nameEntry.insert(0,"Sınav")
                    
    def sureayarla(self,sure:str):
        if sure != "":
            if len(self.hourEntry.get()) != 0:self.hourEntry.delete(0,len(self.hourEntry.get()))
            if len(self.minuteEntry.get()) != 0:self.minuteEntry.delete(0,len(self.minuteEntry.get()))
            if len(self.nameEntry.get()) != 0:self.nameEntry.delete(0,len(self.nameEntry.get()))
            dakikalar = ["1 dk","3 dk","5 dk","10 dk","15 dk","30 dk","40 dk","1 sa","1 sa 20 dk","1 sa 40 dk","2 sa","2 sa 30 dk","3 sa","4 sa"]
            dakikalarint = [1,3,5,10,15,30,40,60,80,100,120,150,180,240]
            dakika = dakikalarint[dakikalar.index(sure)]

            delta = datetime.datetime.now()
            Fsaat, Fdk = divmod(dakika,60)
            dk = delta.minute +Fdk
            saat, dk = divmod(dk,60)
            saat += delta.hour + Fsaat
            gün, saat = divmod(saat,24)
        
            self.hourEntry.insert(0,saat)
            self.minuteEntry.insert(0,dk)
            self.nameEntry.insert(0,"Sınav")

    def startTime(self):
        if self.nameEntry.get() != "" and self.hourEntry.get() != "" and self.minuteEntry.get() != "":
            self.name = self.nameEntry.get()
            self.nameLabel.configure(text= self.name)
            delta = datetime.datetime.now()
            self.finishTime = datetime.datetime(delta.year,delta.month,delta.day,int(self.hourEntry.get()),int(self.minuteEntry.get()),0)
            
            self.settingsButton.configure(text="İptal et")
            
            if self.width == 700 and self.height == 700:
                self.settingsButton.place(x=280,y=560)
            if self.width == 2000 and self.height == 2000:
                self.settingsButton.place(x=890,y=1600)
            else:
                self.settingsButton.place(x=430,y=800)
            self.time_started = True
            self.settingsWin.destroy()

    def changeTheme(self):
        global var
        if tk.get_appearance_mode() == "Light":
            tk.set_appearance_mode("Dark")
            getColors()
            self.canvas.delete("daire")
            if self.width == 700 and self.height == 700:
                self.draw_circle(color=backColor,canvas=self.canvas,radius=350,centerx=350,centery=350)
                self.draw_circle(color=foreColor,canvas=self.canvas,radius=300,centerx=350,centery=350)
            elif self.width == 2000 and self.height == 2000:
                self.draw_circle(color=backColor,canvas=self.canvas,radius=1000,centerx=1000,centery=1000)
                self.draw_circle(color=foreColor,canvas=self.canvas,radius=800,centerx=1000,centery=1000)
            else:
                self.draw_circle(color=backColor,canvas=self.canvas,radius=500,centerx=500,centery=500)
                self.draw_circle(color=foreColor,canvas=self.canvas,radius=400,centerx=500,centery=500)
       
            self.dersLabel.configure(bg_color=foreColor)
            self.dateLabel.configure(bg_color=foreColor)
            self.clockLabel.configure(bg_color=foreColor)
            self.nameLabel.configure(bg_color=foreColor)
            self.sumLabel.configure(bg_color=foreColor)
            self.settingsButton.configure(fg_color=foreColor,bg_color=foreColor)
            self.exitButton.configure(fg_color=foreColor,bg_color=foreColor)
            
            config = open("config.txt","w")
            config.write("Dark")
            config.close()
        elif tk.get_appearance_mode() == "Dark":
            tk.set_appearance_mode("Light")
            getColors()
            self.canvas.delete("daire")
            if self.width == 700 and self.height == 700:
                self.draw_circle(color=backColor,canvas=self.canvas,radius=350,centerx=350,centery=350)
                self.draw_circle(color=foreColor,canvas=self.canvas,radius=300,centerx=350,centery=350)
            elif self.width == 2000 and self.height == 2000:
                self.draw_circle(color=backColor,canvas=self.canvas,radius=1000,centerx=1000,centery=1000)
                self.draw_circle(color=foreColor,canvas=self.canvas,radius=800,centerx=1000,centery=1000)
            else:
                self.draw_circle(color=backColor,canvas=self.canvas,radius=500,centerx=500,centery=500)
                self.draw_circle(color=foreColor,canvas=self.canvas,radius=400,centerx=500,centery=500)
       
            self.dersLabel.configure(bg_color=foreColor)
            self.dateLabel.configure(bg_color=foreColor)
            self.clockLabel.configure(bg_color=foreColor)
            self.nameLabel.configure(bg_color=foreColor)
            self.sumLabel.configure(bg_color=foreColor)
            self.settingsButton.configure(fg_color=foreColor,bg_color=foreColor)
            self.exitButton.configure(fg_color=foreColor,bg_color=foreColor)
            
            config = open("config.txt","w")
            config.write("Light")
            config.close()
        self.themeButton.configure(text=f"Tema: {tk.get_appearance_mode()}")

    def settingsExit(self):
        self.settingsWin.destroy()
        self.settingsWinON = False

    def draw_circle(self,canvas, radius:int = 500, color:str = "white",centerx:int=500,centery:int=500,**kwargs):    
        
        points = list()

        for i in range(628+1):
            konum = (radius*math.cos(i/100)+centerx,radius*math.sin(i/100)+centery)
            points.append(konum[0])
            points.append(konum[1])
        
        return canvas.create_polygon(points , **kwargs, smooth=True, fill=color,tags="daire")
       
    def geriSayma(self):
        
        delta = self.finishTime - datetime.datetime.now()
        saat , kalan = divmod(delta.seconds,3600)
        dakika , saniye = divmod(kalan,60)
        if self.sumTime == 0: self.clockTime = (delta.seconds*1000000) + delta.microseconds
        self.sumTime = (delta.seconds*1000000) + delta.microseconds
        text = str(saat).zfill(2) +"sa "+str(dakika).zfill(2) +"dk "+str(saniye).zfill(2)+"sn"
        self.sumLabel.configure(text=text)

    def main(self):
        global points,var
        
        delta = datetime.datetime.now()
        self.clockLabel.configure(text=str(delta.hour).zfill(2) +":"+str(delta.minute).zfill(2) +":"+str(delta.second+1).zfill(2))
        self.dateLabel.configure(text=str(delta.day).zfill(2) +"/"+str(delta.month).zfill(2) +"/"+str(delta.year).zfill(2))
        
        if var > 0:
            self.settingsCommand()
            var -= 1
        if self.time_started:
            self.geriSayma()
            #self.mainAnimation()


            if self.t == 0:
                points = list()
                if self.width == 700 and self.height == 700:
                    points.append(350)
                    points.append(350)
                elif self.width == 2000 and self.height == 2000:
                    points.append(1000)
                    points.append(1000)
                else:
                    points.append(500)
                    points.append(500)
                self.canvas.delete("s")
                if self.width == 700 and self.height == 700:
                    konum = (350*math.cos((470)/100)+350,350*math.sin((470)/100)+350)
                elif self.width == 2000 and self.height == 2000:
                    konum = (1000*math.cos((470)/100)+1000,1000*math.sin((470)/100)+1000)
                else:
                    konum = (500*math.cos((470)/100)+500,500*math.sin((470)/100)+500)
                points.append(konum[0])
                points.append(konum[1])
                if self.width == 700 and self.height == 700:
                    points.append(350)
                    points.append(350)
                elif self.width == 2000 and self.height == 2000:
                    points.append(1000)
                    points.append(1000)
                else:
                    points.append(500)
                    points.append(500)
                self.canvas.create_polygon(points, smooth=False, fill=foreColor,tags="s")
                self.update()
                time.sleep(60/630)
                points.pop(len(points)-1)
                points.pop(len(points)-1)
            
            
            if self.t < 0.99:
                self.t = ((self.clockTime-self.sumTime)/self.clockTime)
                #print(f"{self.t} = {self.clockTime} - {self.sumTime}")
                self.canvas.delete("s")
                if self.width == 700 and self.height == 700:
                    konum = (350*math.cos((470+(self.t*630))/100)+350,350*math.sin((470+(self.t*630))/100)+350)
                elif self.width == 2000 and self.height == 2000:
                    konum = (1000*math.cos((470+(self.t*630))/100)+1000,1000*math.sin((470+(self.t*630))/100)+1000)
                else:
                    konum = (500*math.cos((470+(self.t*630))/100)+500,500*math.sin((470+(self.t*630))/100)+500)
                points.append(konum[0])
                points.append(konum[1])
                if self.width == 700 and self.height == 700:
                    points.append(350)
                    points.append(350)
                elif self.width == 2000 and self.height == 2000:
                    points.append(1000)
                    points.append(1000)
                else:
                    points.append(500)
                    points.append(500)
                self.canvas.create_polygon(points, smooth=False, fill=foreColor,tags="s")
                self.update()
                time.sleep(60/630)
                points.pop(len(points)-1)
                points.pop(len(points)-1)
            
            if self.t < 0:
                self.t = 1.0

            if self.t >= 0.99:
                self.canvas.delete("s")
                if self.width == 700 and self.height == 700:
                    konum = (350*math.cos((470+(630))/100)+350,350*math.sin((470+(630))/100)+350)
                elif self.width == 2000 and self.height == 2000:
                    konum = (1000*math.cos((470)+(630)/100)+1000,1000*math.sin((470)+(630)/100)+1000)
                else:
                    konum = (500*math.cos((470+(630))/100)+500,500*math.sin((470+(630))/100)+500)
                points.append(konum[0])
                points.append(konum[1])
                points.append(500)
                points.append(500)
                self.canvas.create_polygon(points, smooth=False, fill=foreColor,tags="s")
                self.update()
                points.pop(len(points)-1)
                points.pop(len(points)-1)
                self.time_started = False
                self.stopanim = False
                self.time_finished = True
                self.t = 0
                self.finishTime = 0
                self.clockTime = 0
                self.sumTime = 0
                self.sumLabel.configure(text="00sa 00dk 00sn")
                self.settingsButton.configure(text="Bitir")
        
        if self.time_finished:
            if self.stopanim == False:
                self.canvas.delete("s")
                match self.turn:
                    case 0:
                        print(0)
                        self.canvas.create_polygon(points, smooth=False, fill=foreColor,tags="s")
                        self.dersLabel.configure(bg_color=foreColor)
                        self.dateLabel.configure(bg_color=foreColor)
                        self.clockLabel.configure(bg_color=foreColor)
                        self.nameLabel.configure(bg_color=foreColor)
                        self.sumLabel.configure(bg_color=foreColor)
                        self.settingsButton.configure(fg_color=foreColor,bg_color=foreColor)
                        self.exitButton.configure(fg_color=foreColor,bg_color=foreColor)
                        self.update()
                        time.sleep(.3)
                        self.turn = 1
                    case 1:
                        print(1)
                        self.canvas.create_polygon(points, smooth=False, fill=backColor,tags="s")
                        self.dersLabel.configure(bg_color=backColor)
                        self.dateLabel.configure(bg_color=backColor)
                        self.clockLabel.configure(bg_color=backColor)
                        self.nameLabel.configure(bg_color=backColor)
                        self.sumLabel.configure(bg_color=backColor)
                        self.settingsButton.configure(fg_color=backColor,bg_color=backColor)
                        self.exitButton.configure(fg_color=backColor,bg_color=backColor)
                        self.update()
                        time.sleep(.3)
                        self.turn = 0
            else:
                self.time_finished = False
                self.canvas.delete("s")
                self.canvas.delete("x")
                self.dersLabel.configure(bg_color=foreColor)
                self.dateLabel.configure(bg_color=foreColor)
                self.clockLabel.configure(bg_color=foreColor)
                self.nameLabel.configure(bg_color=foreColor)
                self.sumLabel.configure(bg_color=foreColor)
                self.settingsButton.configure(fg_color=foreColor,bg_color=foreColor)
                self.exitButton.configure(fg_color=foreColor,bg_color=foreColor)
                self.update()

        


        self.update()
            

On = True
match platform.system():
    case "Windows":
        username = os.getlogin()
        lastpath = os.getcwd()
        try:
            os.chdir(f"C:\\Users\\{username}\\AppData\\Roaming\\Sınav Zamanlayıcısı")
        except FileNotFoundError:
            os.mkdir(f"C:\\Users\\{username}\\AppData\\Roaming\\Sınav Zamanlayıcısı")
        os.chdir(lastpath)
        try:
            os.system(f'copy "files\\icon.ico" "C:\\Users\\{username}\\AppData\\Roaming\\Sınav Zamanlayıcısı\\icon.ico"')
            os.system(f'copy "files\\settings.png" "C:\\Users\\{username}\\AppData\\Roaming\\Sınav Zamanlayıcısı\\settings.png"')
        except FileNotFoundError:
            psuccess = 0
            for i in os.listdir(f"C:\\Users\\{username}\\AppData\\Roaming\\Sınav Zamanlayıcısı\\"):
                if i == "icon.ico":
                    psuccess += 1
                if i == "settings.png":
                    psuccess += 1
            if psuccess < 2:
                print("Files Doesn't Exist.")
                time.sleep(5)
        except FileExistsError:
            pass
        os.chdir(f"C:\\Users\\{username}\\AppData\\Roaming\\Sınav Zamanlayıcısı")
        try:
            config = open("config.txt","r")
        except FileNotFoundError:
            config = open("config.txt","w")
            config.close()
            config = open("config.txt","r")
        tk.set_appearance_mode(config.read())
        config.close()
    case "Linux":
        username = os.getlogin()
        lastpath = os.getcwd()
        try:
            os.chdir("/home/Sınav Zamanlayıcısı")
        except FileNotFoundError:
            os.mkdir("/home/Sınav Zamanlayıcısı")
        os.chdir(lastpath)
        try:
            os.rename("files/icon.ico","/home/Sınav Zamanlayıcısı/icon.ico")
            os.rename("files/settings.png","/home/Sınav Zamanlayıcısı/settings.png")
        except FileNotFoundError:
            psuccess = 0
            for i in os.listdir("/home/Sınav Zamanlayıcısı"):
                if i == "icon.ico":
                    psuccess += 1
                if i == "settings.png":
                    psuccess += 1
            if psuccess < 2:
                print("Files Doesn't Exist.")
                time.sleep(5)
                On = False
        os.chdir("/home/Sınav Zamanlayıcısı")
        try:
            config = open("config.txt","r")
        except FileNotFoundError:
            config = open("config.txt","w")
            config.close()
            config = open("config.txt","r")
        tk.set_appearance_mode(config.read())
        config.close()

getColors()
win = get_win()

while On:
    win.main()