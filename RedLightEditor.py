##
##
## ################################################
## ###### Please Don't Remove Creator Name #########
## ############# Thanks ###########################
## ################################################
##
##
"""
######################################################
                                            
######################################################

    Arjun.S
     
    Check me out at
	
	arjunsred@gmail.com
	https://arjunsden.wordpress.com/
	https://www.youtube.com/channel/UCmtVqNG1rW7fd0N89GbJeww

     
######################################################
"""
from tkinter import *
import os, subprocess, json, string, tkinter.font as tk_font

font_sizes = ['8','9','10','11','12','14','16','18','20','22', '24','26','28','36','48','72']
font_styles = ['italic','underline','bold']
root = Tk()
font2 = ("Arial", 16)
fontbool = False
wrap_counter = 1

def new_fontwindow():
	global lb
	global lb2
	global lb3
	global nw
	nw = Toplevel(root)
	
	frame1 = Frame(nw)
	frame1.pack(expand=1, fill= BOTH)

	lb = Listbox(nw, selectmode=SINGLE, exportselection=0, height = 5, width = 10) 
	for x in range(0, len(tk_font.families())):
		lb.insert(END, tk_font.families()[x])
	lb.pack(side=LEFT)
	lb2 = Listbox(nw, selectmode=SINGLE, exportselection=0, height = 5, width = 10) 
	for x in range(0, len(font_sizes)):
		lb2.insert(END, font_sizes[x])
	lb2.pack(side=LEFT)
	lb3 = Listbox(nw, selectmode=SINGLE, exportselection=0, height = 5, width = 10) 
	for x in range(0, len(font_styles)):
		lb3.insert(END, font_styles[x])
	lb3.pack()
	button = Button(nw, text = 'Ok', command = ok_fontwindow)
	button.pack(side='bottom')
	nw.mainloop()

def word_wrap():
	global wrap_counter
	wrap_counter += 1
	if wrap_counter%2 == 1:
		editor.config(wrap = "word", 
			undo = True, 
			width = 80, 
			font = font2)     
	else:
		editor.config(wrap="none",
			undo = True, 
			width = 80, 
			font = font2) 



def ok_fontwindow():
	global font2
	global fontbool
	
	fontbool = True
	SelectList = lb.curselection()
	SelectList2 = lb2.curselection()
	SelectList3 = lb3.curselection()

	if SelectList:
		font = [lb.get(i) for i in SelectList]
	if SelectList2:
		font_size2 = [lb2.get(i) for i in SelectList2]
	if SelectList3:
		font_style = [lb3.get(i) for i in SelectList3]
	font2 = (font, font_size2, font_style)
	changefont()
	nw.destroy()

def changefont():
	global font2
	if fontbool:
		editor.config( undo = True, 
			width = 80, 
			font = font2)     

	else:
		editor.config(undo = True, 
				width = 80, 
				font = font2)  

root.iconbitmap('D:\\Python\\Projects\\PythonTextEditor\\red_light7.ico')
root.title('RedLight Editor')
frame = Frame(root)
frame2 = Frame(root)
yscrollbar = Scrollbar(frame, orient="vertical")
xscrollbar = Scrollbar(frame2, orient="horizontal")
editor = Text(frame, yscrollcommand=yscrollbar.set, xscrollcommand=xscrollbar.set)
changefont()
word_wrap()
editor.focus()
editor.pack(side="left", fill="both", expand=1)
yscrollbar.pack(side="right", fill="y")
xscrollbar.pack(side="bottom", fill="x")
yscrollbar.config(command=editor.yview)        
xscrollbar.config(command=editor.xview)  
frame.pack(fill="both", expand=1)
frame2.pack(fill="both", expand=1)
menubar = Menu(root)
filemenu = Menu(menubar, tearoff = 0)
#
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff = 0)
#
menubar.add_cascade(label="Edit", menu=editmenu)
formatmenu = Menu(menubar, tearoff = 0)
#
menubar.add_cascade(label="Format", menu= formatmenu)
formatmenu.add_command(label="Word Wrap", command = word_wrap)
#
viewmenu = Menu(menubar, tearoff = 0)
#
menubar.add_cascade(label="View", menu=viewmenu)
viewmenu.add_command(label="Font", command = new_fontwindow)
helpmenu = Menu(menubar, tearoff = 0)
#
menubar.add_cascade(label="Help", menu=helpmenu)
encodemenu = Menu(menubar, tearoff = 0)
#
menubar.add_cascade(label="Encode", menu=encodemenu)
decodemenu = Menu(menubar, tearoff=0)
#
menubar.add_cascade(label="Decode", menu=decodemenu)
root.config(menu=menubar)


root.mainloop()
