import tkinter as tk
from PIL import Image, ImageTk
from urllib.request import urlopen
from io import BytesIO
import requests
from bs4 import BeautifulSoup


bg_ = ("white")

class kaop(tk.Tk):
    def get_page(self, page_class):
        return self.frames[page_class]
    
    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (Entrada, Perfil):

            frame = F(container, self, bg=bg_)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Entrada)

    def show_frame(self, cont):
    
        frame = self.frames[cont]
        frame.tkraise()

class Entrada(tk.Frame):

    def __init__(self, parent, controller,bg=None):
        tk.Frame.__init__(self,parent, bg=bg)
        self.controller = controller

        def sea():
            c = tk.Label(self, text="carregando informações...", font="arial 14",bg=bg_)
            c.place(x=330, y=250)


            p = pesq.get()
            
            
            lb = tk.Label(self, text="", font="arial 30 bold",bg=bg_)
            lb.place(x=10, y=150)

            lb["text"] = p

            c.destroy()

            link = f"https://lista.mercadolivre.com.br/{p}"
            get = requests.get(str(link))
            soup = BeautifulSoup(get.text, "html.parser")

            pr = []
            ava = []
            
            for container in soup.findAll('div', class_='ui-search-price__second-line shops__price-second-line'):
                pr.append(container.find('span', class_='price-tag-fraction').text)
                

            for container in soup.findAll('div', class_='ui-search-item__group ui-search-item__group--reviews shops__items-group'):
                ava.append(container.find("span",class_="ui-search-reviews__amount").text)

            
                

            pr1, pr2, pr3, pr4 = pr[0], pr[2], pr[4], pr[6]
            soma = float(pr1) + float(pr2) + float(pr3) + float(pr4)
            som = soma / 4

            av, av2, av3, av4 = ava[0], ava[1], ava[2], ava[3]
            somas = float(av) + float(av2) + float(av3) + float(av4)


            lb = tk.Label(self, text="média:", font="arial 30 bold",bg=bg_)
            lb.place(x=500, y=150)

            lb = tk.Label(self, text=f"R${som}", font="arial 40 bold",bg=bg_)
            lb.place(x=500, y=200)

            lb = tk.Label(self, text="Quantidade de avaliações:", font="arial 20 bold",bg=bg_)
            lb.place(x=500, y=280)

            lb = tk.Label(self, text=f"{somas}", font="arial 15 bold",bg=bg_)
            lb.place(x=500, y=330)


        pesq = tk.Entry(self, width=20,font="arial 32")
        pesq.place(x=330,y=10)

        

        bt = tk.Button(self, text="search",width=39,font="arial 16",command=sea)
        bt.place(x=330,y=70)

        link="https://s.tmimgcdn.com/scr/1200x750/180700/modelo-de-logotipo-automotivo-da-letra-k_180766-original.png"

        u = urlopen(link)
        raw_data = u.read()
        u.close()

        photo = ImageTk.PhotoImage(data=raw_data) # <-----

        label = tk.Label(image=photo,width=300,height=130)
        label.image = photo
        label.place(x=0,y=0)

        

        

        
        


class Perfil(tk.Frame):

    def __init__(self, parent, controller,bg=None):
        tk.Frame.__init__(self,parent, bg=bg)
        self.controller = controller

app = kaop()
app.geometry("900x500")
app.resizable(0, 0)
app.title("KaOp - Mil opções")
#app.iconbitmap("d_icon-icons.com_60501.ico")

app.mainloop()
