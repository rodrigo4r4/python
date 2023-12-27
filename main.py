from tkinter import *
from PIL import Image, ImageTk
import speedtest

co0 = "#f0f3f5"
co1 = "#feffff"
co2 = "#3fb5a3"
co3 = "#fc766d"
co4 = "#403d3d"
co5 = "#4a88e8"



janela = Tk()
janela.title("SpeedTest")
janela.geometry('350x200')
janela.configure(background=co1)
janela.resizable(False, False)


#Frames
frame_logo = Frame(janela, width=350, height=60, bg=co1)
frame_logo.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

frame_corpo = Frame(janela, width=350, height=140, bg=co1)
frame_corpo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

#Configurando o fram_logo

imagem = Image.open('speed.png')
imagem = imagem.resize((55,55))
imagem = ImageTk.PhotoImage(imagem)

l_logo_imagem = Label(frame_logo, height=60, image=imagem, compound=LEFT, padx=10, anchor='nw', bg=co1, fg=co3)
l_logo_imagem.place(x=20, y=0)
label_logo = Label(frame_logo, text='Internet Speed Test', font='Times 18 bold', padx=10, bg=co1)
label_logo.place(x=80, y=13)
label_linha = Label(frame_logo, width=50, bg=co2)
label_linha.place(x=0,y=57)

def start():
    test = speedtest.Speedtest()
    test.get_servers()
    best = test.get_best_server()
    download_result = test.download()
    upload_result = test.upload()
    ping_result = test.results.ping
    down = download_result / 1024 / 1024
    up = upload_result / 1024 / 1024
    print(ping)
    label_download['text'] = int(down)
    label_upload['text'] = int(up)
    label_ping['text'] = int(ping)

label_download = Label(frame_corpo, text='0,0', font='Arial 28 bold', bg=co1, fg=co4)
label_download.place(x=55, y=20)
label_ping = Label(frame_corpo, text='0', font='Arial 28 bold', bg=co1, fg=co4)
label_ping.place(x=165, y=20)
label_upload = Label(frame_corpo, text='0,0', font='Arial 28 bold', bg=co1, fg=co4)
label_upload.place(x=235, y=20)
label_down = Label(frame_corpo, text='Download Speed', font='Arial 8', bg=co1, fg=co4)
label_down.place(x=42, y=70)
label_ping1 = Label(frame_corpo, text='Ping', font='Arial 8', bg=co1, fg=co4)
label_ping1.place(x=164, y=70)
label_up = Label(frame_corpo, text='Upload Speed', font='Arial 8', bg=co1, fg=co4)
label_up.place(x=228, y=70)
btn_teste = Button(frame_corpo, text='Start', width=15, relief=RAISED, overrelief=RIDGE, bg=co5, fg=co1, command=start)
btn_teste.place(x=118, y=100)



janela.mainloop()