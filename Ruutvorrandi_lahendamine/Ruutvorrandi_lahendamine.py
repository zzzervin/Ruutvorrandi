from tkinter import *

plan = Tk()

OP=Label(relief="solid").grid(row=0, column=0,sticky=N+S+W+E)
Ep=Label(text="Esmaspäev",height=6,width=15,font="Arial 10",bg="orange",relief="solid")
Ep.grid(row=1, column=0,sticky=N+S+W+E,rowspan=2)
Tp=Label(text="Teisipäev",height=6,width=15,font="Arial 10",bg="orange",relief="solid")
Tp.grid(row=3, column=0,sticky=N+S+W+E,rowspan=2)
Kp=Label(text="Kolmapäev",height=6,width=15,font="Arial 10",bg="orange",relief="solid")
Kp.grid(row=5, column=0,sticky=N+S+W+E,rowspan=2)
Np=Label(text="Neljapäev",height=6,width=15,font="Arial 10",bg="orange",relief="solid")
Np.grid(row=7, column=0,sticky=N+S+W+E,rowspan=2)
Rp=Label(text="Reede",height=6,width=15,font="Arial 10",bg="orange",relief="solid")
Rp.grid(row=9, column=0,sticky=N+S+W+E,rowspan=2)


OP=Label(relief="solid").grid(row=0, column=0,sticky=N+S+W+E)
OP0=Label(text="0",height=4,width=5,font="Arial 20",relief="solid").grid(row=0, column=1,sticky=N+S+W+E)
OP1=Label(text="1",height=4,width=5,font="Arial 20",relief="solid").grid(row=0, column=2,sticky=N+S+W+E)
OP2=Label(text="2",height=4,width=5,font="Arial 20",relief="solid").grid(row=0, column=3,sticky=N+S+W+E)
OP3=Label(text="3",height=4,width=5,font="Arial 20",relief="solid").grid(row=0, column=4,sticky=N+S+W+E)
OP4=Label(text="4",height=4,width=5,font="Arial 20",relief="solid").grid(row=0, column=5,sticky=N+S+W+E)
OP5=Label(text="5",height=4,width=5,font="Arial 20",relief="solid").grid(row=0, column=6,sticky=N+S+W+E)
OP6=Label(text="6",height=4,width=5,font="Arial 20",relief="solid").grid(row=0, column=7,sticky=N+S+W+E)
OP7=Label(text="7",height=4,width=5,font="Arial 20",relief="solid").grid(row=0, column=8,sticky=N+S+W+E)
OP8=Label(text="8",height=4,width=5,font="Arial 20",relief="solid").grid(row=0, column=9,sticky=N+S+W+E)
OP9=Label(text="9",height=4,width=5,font="Arial 20",relief="solid").grid(row=0, column=10,sticky=N+S+W+E)
OP10=Label(text="10",height=4,width=5,font="Arial 20",relief="solid").grid(row=0, column=11,sticky=N+S+W+E)


#EEsmaspäev
Mm=Button(text="Multimeedia",height=4,width=5,font="Arial 10",relief="solid",bg="#abe0ff")
Mm2=Button(text="Multimeedia",height=4,width=5,font="Arial 10",relief="solid",bg="#abe0ff")
Pa=Button(text="Programmeerimise alused",height=4,width=5,font="Arial 10",relief="solid",bg="lightblue")
Pa2=Button(text="Programmeerimise alused",height=4,width=5,font="Arial 10",relief="solid",bg="lightblue")
Rt=Button(text="Rühmajuhataja\ntund",height=4,width=5,font="Arial 10",relief="solid",bg="lightblue")

Mm.grid(row=1, column=2, columnspan=2,sticky=N+S+W+E)
Pa.grid(row=2, column=2, columnspan=3,sticky=N+S+W+E)
Mm2.grid(row=2, column=5, columnspan=2,sticky=N+S+W+E)
Pa2.grid(row=1, column=5, columnspan=3,sticky=N+S+W+E)
Rt.grid(row=1, column=8, columnspan=1,sticky=N+S+W+E,rowspan=2)

#TTeisipäev
ING=Button(text="Inglise keel",height=4,width=5,font="Arial 10",relief="solid",bg="#fffff0")
ING2=Button(text="Inglise keel",height=4,width=5,font="Arial 10",relief="solid",bg="#e0abff")
Oma=Button(text="Operatsioonisüsteemide\nalused",height=4,width=5,font="Arial 10",relief="solid",bg="#e080ff")
Kk=Button(text="Kehaline kasvatus",height=4,width=5,font="Arial 10",relief="solid",bg="#e080c0")
Ek=Button(text="Eesti keel",height=4,width=5,font="Arial 10",relief="solid",bg="#ccb3ff")
Ek2=Button(text="Eesti keel",height=4,width=5,font="Arial 10",relief="solid",bg="#cab4c7")
AAAAA=Button(text="Ajalugu,\ninimgeogr\naafia ja\ninimese\nõpetus\neesti\nkeeles",height=4,width=5,font="Arial 10",relief="solid",bg="#ffe6b3")

ING.grid(row=3, column=2, columnspan=2,sticky=N+S+W+E)
ING2.grid(row=4, column=2, columnspan=2,sticky=N+S+W+E)
Oma.grid(row=3, column=4, columnspan=2,sticky=N+S+W+E,rowspan=2)
Kk.grid(row=3, column=7, columnspan=2,sticky=N+S+W+E,rowspan=2)
Ek.grid(row=3, column=9,sticky=N+S+W+E)
Ek2.grid(row=4, column=9,sticky=N+S+W+E)
AAAAA.grid(row=3, column=10, sticky=N+S+W+E,rowspan=2)

#KKolmapäev
Pa3=Button(text="Programmeerimise alused",height=4,width=5,font="Arial 10",relief="solid",bg="lightblue")
Pa4=Button(text="Programmeerimise alused",height=4,width=5,font="Arial 10",relief="solid",bg="lightblue")
Mm3=Button(text="Multimeedia",height=4,width=5,font="Arial 10",relief="solid",bg="#abe0ff")
Mm4=Button(text="Multimeedia",height=4,width=5,font="Arial 10",relief="solid",bg="#abe0ff")
Ka=Button(text="Multimeedia",height=4,width=5,font="Arial 10",relief="solid",bg="#e080ce")

Mm3.grid(row=6, column=2, columnspan=3,sticky=N+S+W+E)
Mm4.grid(row=5, column=6, columnspan=3,sticky=N+S+W+E)
Pa3.grid(row=6, column=6, columnspan=3,sticky=N+S+W+E)
Pa4.grid(row=5, column=2, columnspan=3,sticky=N+S+W+E)
Ka.grid(row=5, column=9, columnspan=2,sticky=N+S+W+E,rowspan=2)

#NNeljapäev

Bass=Button(text="Andmebaasisüstee\nmide alused (eesti\nkeeles)",height=4,width=5,font="Arial 10",relief="solid",bg="#ff80a1")
Bass2=Button(text="Andmebaasisüsteemide\nalused (eestinkeeles)",height=4,width=5,font="Arial 10",relief="solid",bg="#ff80a1")
AAAAA=Button(text="Ajalugu,\ninimgeogr\naafia ja\ninimese\nõpetus\neesti\nkeeles",height=4,width=5,font="Arial 10",relief="solid",bg="#ffe6b3")
Ek3=Button(text="Eesti keel",height=4,width=5,font="Arial 10",relief="solid",bg="#ccb3ff")
Ek4=Button(text="Eesti keel",height=4,width=5,font="Arial 10",relief="solid",bg="#cab4c7")

Bass.grid(row=7, column=2, columnspan=2,sticky=N+S+W+E,rowspan=2)
Bass2.grid(row=7, column=4, columnspan=3,sticky=N+S+W+E,rowspan=2)
AAAAA.grid(row=7, column=7, sticky=N+S+W+E,rowspan=2)
Ek3.grid(row=7, column=8,sticky=N+S+W+E)
Ek4.grid(row=8, column=8,sticky=N+S+W+E)

#RReede
Kjk=Button(text="Keel ja kirjandus",height=4,width=5,font="Arial 10",relief="solid",bg="#e0ff80")


plan.mainloop()
