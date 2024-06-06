from random import randint
from PIL import Image
import customtkinter as ctk
from customtkinter import(
    CTkButton,
    CTkLabel,
    CTkEntry,
    CTkImage
)
trys = 3
num = randint(1,15)
mau = None
print(num)
class App():
    def __init__(self):   
        global num,mau

        self.sus = ctk.CTk()

        self.sus.geometry("800x600")
        self.sus.title("Đoán số")
        self.sus.resizable(False, False)

        # self.sus.bg_image = CTkImage(Image.open("bg.png"),size=(800,600))
        # self.sus.bg_image_label = CTkLabel(self.sus, image=self.sus.bg_image,text = "")
        # self.sus.bg_image_label.place(x=0, y=0)

        self.sus.label = CTkLabel(self.sus,text = "Đoán số (1 - 15)", font = ("Consolas",18))
        self.sus.label.pack(padx = 10, pady = 10)

        self.sus.textbox = CTkEntry(self.sus, font = ("Consolas",20), width = 100, height = 10,justify='center')
        self.sus.textbox.pack(padx = 10,pady = 10)

        self.sus.ans = CTkEntry(self.sus,font = ("Consolas",20), state = "disable", height= 10, width= 500,justify='center')
        self.sus.ans.pack(padx = 10, pady = 10)
        mau = self.sus.ans.cget("fg_color")

        self.sus.submit = CTkButton(self.sus, text = "Gửi", font = ("Consolas", 20), command = self.process_button)
        self.sus.bind('<Return>',self.process_button)
        self.sus.submit.pack(padx = 10, pady = 10)


        self.sus.mainloop()

    def process_button(self,*args):
        global trys,num
        check = False
        try:
            nums = int(self.sus.textbox.get())
        except:
            check = True
        if check == False and trys != 0 and (nums >= 1 and nums <= 15):
            trys -= 1
            if nums < num:
                self.trakq(f"Số cần tìm lớn hơn {nums}!","red")  
                if trys == 0:
                    self.hetluot()
            elif nums > num:
                self.trakq(f"Số cần tìm nhỏ hơn {nums}!","red")  
                if trys == 0:
                    self.hetluot()
            elif nums == num:
                self.trakq(f"Số bạn vừa tìm được là {nums}!","green")  
                self.thang()
            
        else:
            if trys == 0:
                self.hetluot()
            else:
                self.sus.ans.configure(state = "normal")
                self.trakq("Vui lòng nhập đúng định dạng!","red") 

    def hetluot(self):
        global num
        self.trakq(f"Bạn đã hết lượt chơi! Số cần tìm là: {num}","red")  
        self.thua()

    def trakq(self,msg:str,mau:str):
        self.sus.ans.configure(state = "normal")
        self.sus.ans.delete("0","end")
        self.sus.ans.insert("0",msg)
        self.sus.ans.configure(state = "disabled",fg_color = mau)

    def thang(self):
        self.win = ctk.CTk()
        self.win.geometry("250x250")
        self.win.resizable(False, False)

        self.sus.submit.configure(state = "disabled")

        self.sus.textbox.configure(state = "disabled")

        self.win.label = CTkLabel(self.win, text = "Bạn đã chiến thắng!", font = ("Consolas",20))

        self.win.label.pack(padx = 10,pady = 10)

        self.win.conti = CTkButton(self.win, text = "Chơi tiếp", font = ("Consolas",20),command = self.conti2).pack(padx = 10,pady = 10)
        self.win.close = CTkButton(self.win, text = "Dừng lại", font = ("Consolas",20),command = self.close2).pack(padx = 10,pady = 10)

        self.win.mainloop()

    def thua(self):
        self.dia = ctk.CTk()
        self.dia.geometry("250x250")
        self.dia.resizable(False, False)

        self.sus.submit.configure(state = "disabled")

        self.sus.textbox.configure(state = "disabled")

        self.dia.label = CTkLabel(self.dia, text = "Bạn đã hết lượt chơi!", font = ("Consolas",20))

        self.dia.label.pack(padx = 10,pady = 10)

        self.dia.conti = CTkButton(self.dia, text = "Chơi tiếp", font = ("Consolas",20),command = self.conti).pack(padx = 10,pady = 10)
        self.dia.close = CTkButton(self.dia, text = "Dừng lại", font = ("Consolas",20),command = self.close).pack(padx = 10,pady = 10)

        self.dia.mainloop()

    def close(self):
        self.sus.destroy()
        self.dia.destroy()

    def close2(self):
        self.sus.destroy()
        self.win.destroy()

    def conti(self):
        global trys,mau,num
        num = randint(1,15)
        trys = 3
        self.dia.destroy()
        self.sus.submit.configure(state = "normal")
        self.sus.textbox.configure(state = "normal")
        self.sus.textbox.delete("0","end")
        self.sus.ans.configure(state = "normal")
        self.sus.ans.delete("0","end")
        self.sus.ans.configure(state = "disabled",fg_color = mau)

    def conti2(self):
        global trys,mau,num
        num = randint(1,15)
        trys = 3
        self.win.destroy()
        self.sus.submit.configure(state = "normal")
        self.sus.textbox.configure(state = "normal")
        self.sus.textbox.delete("0","end")
        self.sus.ans.configure(state = "normal")
        self.sus.ans.delete("0","end")
        self.sus.ans.configure(state = "disabled",fg_color = mau)

App()