from tkinter import*
from math import*

ventana=Tk()
ventana.geometry("400x460")   
ventana.title("   CALCULADORA NIBBLEBOT ") 
ventana.resizable(False,False) 
ventana.configure(bg="GREY") 

operador=""   
texto_pantalla=StringVar() 

def clear ():
    global operador
    operador=""
    texto_pantalla.set("0") 
 
def click(b):     
    global operador
    operador+=str(b)
    texto_pantalla.set(operador)

def resultado(): 
    global operador
    try:
        r=str(eval(operador))
    except:
        r="Syntax ERROR"  
    texto_pantalla.set(r)
    
boton0=Button(ventana,text="0",bg="orange",width=25,height=3,command=lambda:click(0)) 
boton0.grid(row=6,column=0,columnspan=2,padx=10, pady=10)

boton1=Button(ventana,text="1",bg="orange",width=10,height=3,command=lambda:click(1)) 
boton1.grid(row=5,column=0,padx=10, pady=10)

boton2=Button(ventana,text="2",bg="orange",width=10,height=3,command=lambda:click(2)) 
boton2.grid(row=5,column=1,padx=10, pady=10)

boton3=Button(ventana,text="3",bg="orange",width=10,height=3,command=lambda:click(3)) 
boton3.grid(row=5,column=2,padx=10, pady=10)

boton4=Button(ventana,text="4",bg="orange",width=10,height=3,command=lambda:click(4)) 
boton4.grid(row=4,column=0,padx=10, pady=10)

boton5=Button(ventana,text="5",bg="orange",width=10,height=3,command=lambda:click(5)) 
boton5.grid(row=4,column=1,padx=10, pady=10)

boton6=Button(ventana,text="6",bg="orange",width=10,height=3,command=lambda:click(6)) 
boton6.grid(row=4,column=2,padx=10, pady=10)

boton7=Button(ventana,text="7",bg="orange",width=10,height=3,command=lambda:click(7)) 
boton7.grid(row=3,column=0,padx=10, pady=10)

boton8=Button(ventana,text="8",bg="orange",width=10,height=3,command=lambda:click(8)) 
boton8.grid(row=3,column=1,padx=10, pady=10)

boton9=Button(ventana,text="9",bg="orange",width=10,height=3,command=lambda:click(9)) 
boton9.grid(row=3,column=2,padx=10, pady=10)

botonpun=Button(ventana,text=".",bg="red",width=10,height=3,command=lambda:click(".")) 
botonpun.grid(row=6,column=2,padx=10, pady=10)

botonlimpiar=Button(ventana,text="CLEAR",bg="red",width=10,height=8,command=clear) 
botonlimpiar.grid(row=3,column=3,rowspan=2,padx=10, pady=10)

botonsuma=Button(ventana,text="+",bg="red",width=10,height=3,command=lambda:click("+")) 
botonsuma.grid(row=2,column=0,padx=10, pady=10)

botonresta=Button(ventana,text="-",bg="red",width=10,height=3,command=lambda:click("-")) 
botonresta.grid(row=2,column=1,padx=10, pady=10)

botonmul=Button(ventana,text="x",bg="red",width=10,height=3,command=lambda:click("*")) 
botonmul.grid(row=2,column=2,padx=10, pady=10)

botondiv=Button(ventana,text="÷",bg="red",width=10,height=3,command=lambda:click("/")) 
botondiv.grid(row=2,column=3,padx=10, pady=10)

botonigual=Button(ventana,text="=",bg="red",width=10,height=8,command=resultado) 
botonigual.grid(row=5,column=3,rowspan=2,padx=10, pady=10)

pantalla=Entry(ventana,font=("arial",20),fg="black",bg="white",textvariable=texto_pantalla)  
pantalla.grid(row=1,column=0,columnspan=6, padx=5, pady=5)

ventana.mainloop()
#RUBEN JHILMAR LAUREL PLATA