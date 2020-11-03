import tkinter as tk
from PIL import Image ,ImageTk
from bs4 import BeautifulSoup
import urllib.parse
import urllib.request
HEIGHT = 700
WIDTH = 700
screen = tk.Tk()
screen.title('Google Dorker')
screen.iconbitmap(r'web.ico')

def test(entry):
    values = {'q': entry}
    data = urllib.parse.urlencode(values)
    extra = str('&ei=xomrWqLjLcPQ0gS05o_gCA&start=')
    ix = 0
    z = 2
    while ix <= z - 1:
        url = 'https://www.google.com/search?' + data + extra + str(ix) + '0&sa=N'
        ix = ix + 1

        headers = {}
        headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686)"
        req = urllib.request.Request(url, headers=headers)

        resp = urllib.request.urlopen(req)

        resp_data = resp.read()
        soup = BeautifulSoup(resp_data, "lxml")
        clean = soup.prettify()
        for link in soup.find_all('div', {'class': 'BNeawe UPmit AP7Wnd'}):
            x = str(link)

            try:
                y = x.split('<div class="BNeawe UPmit AP7Wnd">')[1].split('›')[0].split('</div>')[0] + '\n'
                text.insert(tk.END, y)

            except Exception:
                pass


canvas = tk.Canvas(screen,height=HEIGHT,width=WIDTH)
canvas.pack()

img = ImageTk.PhotoImage(Image.open("frame.jpg"))
panel = tk.Label(canvas, image = img)
panel.place(x=0,y=0,relwidth=1,relheight=1)

frame = tk.Frame(screen,bg='#33EEFF',bd=5)
frame.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.10)


img2 = ImageTk.PhotoImage(Image.open("bgimg.jpg"))
panel = tk.Label(frame, image = img2)
panel.place(x=0,y=0,relwidth=1,relheight=1)




button = tk.Button(frame,text= "Click Me",bg ='#33EEFF',font=('Courier',10),fg='#ea1253',command=lambda:test(entry.get()))
button.place(relx=0.75,rely=0,relwidth=0.25,relheight=1)



entry = tk.Entry(frame,bg ='#33EEFF',fg='#e2440f',font=('Courier',18))
entry.place(relx=0,rely=0,relwidth=0.40,relheight=1)


lower_frame = tk.Frame(screen,bg='#33EEFF',bd=5)
lower_frame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.60)



text = tk.Text(screen,width=20,height=10,padx=10,pady=10,bg ='#33EEFF',font=('Courier',18),wrap=tk.WORD)
text.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.60)




screen.mainloop()
