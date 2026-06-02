from tkinter.messagebox import showerror
from cryptography.fernet import Fernet
import customtkinter,hashlib
from PIL import ImageTk, Image
from customtkinter import CTkEntry, CTkLabel, CTkCheckBox, CTkComboBox, CTkButton
def clear():
    if Entry_c.get():
        Entry_c.delete(0,'end')
    else:
        showerror('داداشی', '!حالت خوبه ورودی دوم پر نیست')
def clear_2():
    if Entry_Voroodi.get():
        Entry_Voroodi.delete(0,'end')
    else:
        showerror('داداشی', '!حالت خوبه ورودی اول پر نیست')
def Error():
    if Entry_c.get():
        showerror('داداشی', '!تو قرار نیست چیگر جایی که کد میاد چیزی بنویسی')
        return
    if not Entry_Voroodi.get():
        showerror('داداشی','!من چیو کد کنم ورودی اول خالیه')
    if Entry_Voroodi.get():
        if Check_Hash.get():
            if Check_CRypto.get() or Check_Tarkib.get():
                showerror('داداشی', '!نباید گزینه های ئیگه تیک خورده باشد فقط 1 گزینه')
                return
            Entry_c.insert(0,hashlib.sha256().hexdigest())
        if Check_CRypto.get():
            if Check_Hash.get() or Check_Tarkib.get():
                showerror('داداشی', '!نباید گزینه های ئیگه تیک خورده باشد فقط 1 گزینه')
                return
            Entry_c.insert(0,Fernet.generate_key())
        if Check_Tarkib.get():
            if Check_CRypto.get() or Check_Hash.get():
                showerror('داداشی','!نباید گزینه های ئیگه تیک خورده باشد فقط 1 گزینه')
                return
            Entry_c.insert(0, hashlib.sha256().hexdigest())
            Entry_c.insert(0,Fernet.generate_key())
    if Entry_Voroodi.get() and not Check_Hash.get() and not Check_Tarkib.get() and not Check_CRypto.get():
        showerror('داداشی', '!خب یک گزینرو بزن برای کد گزاری')
Root = customtkinter.CTk()
Root.resizable(False,False)
bg_image = Image.open('—Pngtree—a hacker in a hoodie_15877091.jpg')
bg_image = bg_image.resize((1500, 800))
bgg = ImageTk.PhotoImage(bg_image)
bg_Label = customtkinter.CTkLabel(Root, image=bgg, text='')
bg_Label.place(x=0, y=0)
Entry_Voroodi = CTkEntry(Root,300,60,1,None,'#08053d','#08053d',None,'White',None,None,'لطفا متنی که میخواد رمزگذاری بشود را بنویسید',('Calibri',18,'bold'))
Check_Hash = CTkCheckBox(Root,20,20,20,20,2,None,text='Hash Code',font=('Comic Sans Ms',20),bg_color='#08053d',border_color='white',text_color='white')
Check_CRypto = CTkCheckBox(Root,20,20,20,20,2,None,text='Crypto Code',font=('Comic Sans Ms',20),bg_color='#08053d',border_color='white',text_color='white')
Check_Tarkib = CTkCheckBox(Root,20,20,20,20,2,None,text='Tarkiby Code',font=('Comic Sans Ms',20),bg_color='#08053d',border_color='white',text_color='white')
Entry_c = CTkEntry(Root,justify='center',width=300,height=60,corner_radius=1,border_color=None,bg_color='#08053d',fg_color='#08053d',text_color='white',placeholder_text_color=None,textvariable=None,placeholder_text='اینجا جایی است که کد بیرون میاید',font=('Calibri',18,'bold'))
Button_C = CTkButton(Root,width=300,height=60,corner_radius=1,border_color=None,bg_color='#053aaa',fg_color='#053aaa',text_color='white',textvariable=None,text='بزن رو من تا برات کدش کنم',font=('Calibri',18,'bold'),command=Error)
Button_clear = CTkButton(Root,width=30,height=6,corner_radius=1,border_color=None,bg_color='#053aaa',fg_color='#053aaa',text_color='white',textvariable=None,text='بزن رو من تا پاکش کنم',font=('Calibri',18,'bold'),command=clear_2)
Button_clear_2 = CTkButton(Root,width=30,height=6,corner_radius=1,border_color=None,bg_color='#053aaa',fg_color='#053aaa',text_color='white',textvariable=None,text='بزن رو من تا پاکش کنم',font=('Calibri',18,'bold'),command=clear)
Button_clear.place(x=363,y=26)
Button_clear_2.place(x=363,y=396)
Check_CRypto.place(x=180,y=140)
Check_Tarkib.place(x=100,y=190)
Check_Hash.place(x=20,y=140)
Entry_Voroodi.place(x=20,y=10)
Entry_c.place(x=20,y=380)
Button_C.place(x=20,y=280)
Root.geometry('1200x600')
Root.title('DC')
Root.iconbitmap('hacker.ico')
Root.mainloop()