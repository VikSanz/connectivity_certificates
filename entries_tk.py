# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 11:38:45 2020
@author: Víctor Sánchez
"""

import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import tkinter as tk
import networkx as nx
from tkinter import *
import time

import grafica
from grafica import *

#----- ROOT -----#
root = tk.Tk()
root.wm_title("Certificados de k-conexidad")
root.geometry('700x700')
root.resizable(False, False)

# Quit when the window is done
root.wm_protocol('WM_DELETE_WINDOW', root.quit)

# Matplotlib
f = plt.figure(figsize=(7,5))
a = f.add_subplot(111)
plt.axis('off')

# Creamos la gráfica G
G = Grafica()

#----- Variables -----#
edge_aVar=tk.StringVar()
edge_bVar=tk.StringVar()
bttn_clicks = 0
xlim=a.get_xlim()
ylim=a.get_ylim()

# Canvas
canvas = FigureCanvasTkAgg(f, master=root)
canvas.draw()
canvas.get_tk_widget().grid(row=2,columnspan=4)

#--- FUNCIONES ---#
def add_edge():

    edge_a=int(edge_aVar.get())
    edge_b=int(edge_bVar.get())
    
    G.agregar_vertice(edge_a)
    G.agregar_vertice(edge_b)

    G.agregar_arista(edge_a,edge_b, 0)

    edge_aVar.set("")
    edge_bVar.set("")

    print(G.aristas())


def crear_grafica():
    # the networkx part
    H = nx.Graph()
    H.add_edges_from(G.aristas())
    pos=nx.circular_layout(H)
    nx.draw_networkx(H,pos=pos,ax=a)
    xlim=a.get_xlim()
    ylim=a.get_ylim()

    # a tk.DrawingArea
    canvas = FigureCanvasTkAgg(f, master=root)
    canvas.draw()
    canvas.get_tk_widget().grid(row=2,columnspan=4)


def ni_search_button():
        
        global bttn_clicks
        a.cla()
        G.ni_search(1)  
        busqueda_ni = G.ni_edges()

        J= nx.Graph()
        for i in range(0,len(busqueda_ni),2):
            J.add_edge(busqueda_ni[i][0], busqueda_ni[i][1], weight=busqueda_ni[i+1])

        pos1 = nx.circular_layout(J)

        edges,weights = zip(*nx.get_edge_attributes(J,'weight').items())
        
        lista1=[]
        
        for e,w in zip(edges,weights):
            
            if w <= bttn_clicks:
                
                a.cla()
                lista1.append(e)
                lista1.append(w)

                K=nx.Graph()
                for i in range(0,len(lista1),2):
                    K.add_edge(lista1[i][0], lista1[i][1], weight=lista1[i+1])

                edges1,weights1 = zip(*nx.get_edge_attributes(K,'weight').items())
                
                nx.draw_networkx(K, pos1, edgelist=edges1, edge_color=weights1, edge_cmap=plt.cm.cool,ax=a)
                #a.set_xlim(xlim)
                #a.set_ylim(ylim)
                plt.axis('off')
            
                canvas = FigureCanvasTkAgg(f, master=root)
                canvas.draw()
                canvas.get_tk_widget().grid(row=2,columnspan=4)

        bttn_clicks += 1
        if bttn_clicks <= max(weights) + 1:
            label1.config(text=f'Certificado ralo de {bttn_clicks-1}-conexidad')

def limpiar_ventana():
    #Removemos el widget anterior
    a.cla()

    plt.axis('off')
    canvas = FigureCanvasTkAgg(f, master=root)
    canvas.draw()
    canvas.get_tk_widget().grid(row=2,columnspan=4)

    G.reiniciar_grafica()

    print("G tiene las siguientes aristas"+str(G.aristas()))

instrucciones= ("""Instrucciones \n 1. Agrega las aristas de la gráfica de la forma (a,b) una por una \n 2. Presiona Dibujar gráfica \n 3. Selecciona el algoritmo que deseas visualizar \n 4. Presiona varias veces el botón y verás la ejecución paso a paso del algoritmo""")

#----- WIDGETS -----#
edge_a = tk.Entry(root,textvariable = edge_aVar,width=10)
edge_b = tk.Entry(root,textvariable = edge_bVar,width=10)
add_edge=tk.Button(root,text = 'Agregar arista',command= add_edge)

draw_graph=tk.Button(root,text = 'Dibujar gráfica',command= crear_grafica)
instructions = tk.Label(root,text=instrucciones,justify= LEFT)

button_ni = tk.Button(root, text="Búsqueda-NI",command=ni_search_button)
label1 = tk.Label(root, text="Elige el algoritmo que quieres ver 🙂")
limpiar = tk.Button(root, text='Limpiar',command=limpiar_ventana)
button_sfs=tk.Button(root, text='Scan-first Search')

instructions.grid(row=0,columnspan=3)
edge_a.grid(row=1,column=0)
edge_b.grid(row=1,column=1)
add_edge.grid(row=1,column=2)
draw_graph.grid(row=1,column=3)
button_ni.grid(row=4, column=0)
button_sfs.grid(row=4,column=2)
label1.grid(row=3,column=1)
limpiar.grid(row=4,column=1)


root.mainloop()