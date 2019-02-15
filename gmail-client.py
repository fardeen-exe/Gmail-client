
from Tkinter import *
import smtplib
server=smtplib.SMTP("smtp.gmail.com",587)
def mail():
	def send_():
		server.starttls()
		t=toEntry.get()
		m=msgEntry.get()
		fromaddr1=emailEntry.get()
		password=passwordEntry.get()
		server.login(fromaddr1,password)
		server.ehlo()
		server.sendmail(fromaddr1,t,m)
		success=Label(window2,text="msg sent succesfully")
		success.grid(row=4,column=0)
		window1.withdraw()
	window2=Tk()
	fromaddr=emailEntry.get()
	toLabel=Label(window2,text="To")
	toEntry=Entry(window2)
	fromLabel=Label(window2,text="from: "+fromaddr)
	msgLabel=Label(window2,text="Enter your message (no pressing enter)")
	msgEntry=Entry(window2)
	sendButton=Button(window2,text="send",command=send_)
	toLabel.grid(row=0,column=0)
	toEntry.grid(row=0,column=1)
	fromLabel.grid(row=1,column=0)
	msgLabel.grid(row=2,column=0)
	msgEntry.grid(row=2,column=1)
	sendButton.grid(row=3,columnspan=2)
	window2.mainloop()

	

	
	



window1=Tk()
warningLabel=Label(window1,text="please note this works only with gmail --- made by Fardeen ----")
emailLabel=Label(window1,text="E-mail")
emailEntry=Entry(window1)
passwordLabel=Label(window1,text="Password")
passwordEntry=Entry(window1,show='*')
submit1=Button(window1,text="submit",command=mail)
warningLabel.grid(row=0,columnspan=2)
emailLabel.grid(row=1,column=0)
emailEntry.grid(row=1,column=1)
passwordLabel.grid(row=2,column=0)
passwordEntry.grid(row=2, column=1)
submit1.grid(row=3, columnspan=2)
window1.mainloop()


