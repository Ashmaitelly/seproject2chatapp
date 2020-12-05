from tkinter import *
from tkinter import scrolledtext
import websocket

try:
    import thread
except ImportError:
    import _thread as thread
import time

window = Tk()
window.title("Chat App")

tbr = scrolledtext.ScrolledText(window)
tbr.grid(column=0, row=0, columnspan=2, sticky=W + E + N + S, padx=4, pady=4)

tbs = Entry(window)
tbs.grid(column=0, row=1, sticky=W + E + N + S, padx=4, pady=4)


def clicked(self):
    if tbs.get():
        ws.send(tbs.get())
        tbr.insert(END, 'SENT > ' + tbs.get() + '\n')
        tbs.delete(0, END)


btn = Button(window, text="Send", command=clicked)
btn.grid(column=1, row=1, sticky=W + E + N + S, padx=4, pady=4)

window.bind("<Return>", clicked)


def on_message(ws, message):
    tbr.insert(END, 'RECV > ' + message + '\n')


def on_close(ws):
    tbr.insert(END, "### closed ###\n")


def on_open(ws):
    tbr.insert(END, "### connected ###\n")


def run():
    ws.run_forever()


websocket.enableTrace(True)
ws = websocket.WebSocketApp(
    "ws://localhost:8000/",
    on_message=on_message,
    on_close=on_close)
ws.on_open = on_open

thread.start_new_thread(run, ())

window.mainloop()
