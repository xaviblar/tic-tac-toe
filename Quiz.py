from Tkinter import*

v0=Tk()
matriz=[[0]*3,[0]*3,[0]*3]
matriz2=[[3]*3,[3]*3,[3]*3]
blanco=PhotoImage(file="blanco.gif")
cero=PhotoImage(file="cero.gif")
equis=PhotoImage(file="x.gif")

cont=0
turno=0
def cambiar(y,x):
    global turno
    global cont
    if turno==0:
        if matriz2[y][x]==3:
            matriz[y][x].config(image=cero)
            turno=1
            matriz2[y][x]=0
            cont+=1

        if y==0 and x==0:
            if matriz2[y][x+1]==0 and matriz2[y][x+2]==0:
                print "Gana el Jugador Cero"
                return ""
            elif matriz2[y+1][x]==0 and matriz2[y+2][x]==0:
                print "Gana el jugador Cero"
                return ""
            elif matriz2[y+1][x+1]==0 and matriz2[y+2][x+2]==0:
                print "Gana el Jugador Cero"
                return ""
        elif y==1 and x==0:
            if matriz2[y][x+1]==0 and matriz2[y][x+2]==0:
                print "Gana el Jugador Cero"
                return ""
            elif matriz2[y+1][x]==0 and matriz2[y-1][x]==0:
                print "Gana el jugador Cero"
                return ""
        elif y==2 and x==0:
            if matriz2[y][x+1]==0 and matriz2[y][x+2]==0:
                print "Gana el Jugador Cero"
                return ""
            elif matriz2[y-1][x]==0 and matriz2[y-2][x]==0:
                print "Gana el jugador Cero"
                return ""
            elif matriz2[y-1][x+1]==0 and matriz2[y-2][x+2]==0:
                print "Gana el Jugador Cero"
                return ""
        elif y==0 and x==1:
            if matriz2[y][x+1]==0 and matriz2[y][x-1]==0:
                print "Gana el Jugador Cero"
                return ""
            elif matriz2[y+1][x]==0 and matriz2[y+2][x]==0:
                print "Gana el jugador Cero"
                return ""
        elif y==0 and x==2:
            if matriz2[y][x-1]==0 and matriz2[y][x-2]==0:
                print "Gana el Jugador Cero"
                return ""
            elif matriz2[y+1][x]==0 and matriz2[y+2][x]==0:
                print "Gana el jugador Cero"
                return ""
            elif matriz2[y+1][x-1]==0 and matriz2[y+2][x-2]==0:
                print "Gana el Jugador Cero"
                return ""
        elif y==1 and x==1:
            if matriz2[y][x+1]==0 and matriz2[y][x-1]==0:
                print "Gana el Jugador Cero"
                return ""
            elif matriz2[y-1][x]==0 and matriz2[y+1][x]==0:
                print "Gana el jugador Cero"
                return ""
            elif matriz2[y-1][x-1]==0 and matriz2[y+1][x+1]==0:
                print "Gana el Jugador Cero"
                return ""
        elif y==1 and x==2:
            if matriz2[y][x-1]==0 and matriz2[y][x-2]==0:
                print "Gana el Jugador Cero"
                return ""
            elif matriz2[y-1][x]==0 and matriz2[y+1][x]==0:
                print "Gana el jugador Cero"
                return ""
        elif y==2 and x==1:
            if matriz2[y][x+1]==0 and matriz2[y][x-1]==0:
                print "Gana el Jugador Cero"
                return ""
            elif matriz2[y-1][x]==0 and matriz2[y-2][x]==0:
                print "Gana el jugador Cero"
                return ""
        elif y==2 and x==2:
            if matriz2[y][x-1]==0 and matriz2[y][x-2]==0:
                print "Gana el Jugador Cero"
                return ""
            elif matriz2[y-1][x]==0 and matriz2[y-2][x]==0:
                print "Gana el jugador Cero"
                return ""
            elif matriz2[y-1][x-1]==0 and matriz2[y-2][x-2]==0:
                print "Gana el Jugador Cero"
                return ""
        if cont==9:
            print "Empate"
            return ""
        
        
    else:
        if matriz2[y][x]==3:
            matriz[y][x].config(image=equis)
            turno=0
            matriz2[y][x]=1
            cont+=1

        if y==0 and x==0:
            if matriz2[y][x+1]==1 and matriz2[y][x+2]==1:
                print "Gana el Jugador Equis"
                return ""
            elif matriz2[y+1][x]==1 and matriz2[y+2][x]==1:
                print "Gana el jugador Equis"
                return ""
            elif matriz2[y+1][x+1]==1 and matriz2[y+2][x+2]==1:
                print "Gana el Jugador Equis"
                return ""
        elif y==1 and x==0:
            if matriz2[y][x+1]==1 and matriz2[y][x+2]==1:
                print "Gana el Jugador Equis"
                return ""
            elif matriz2[y+1][x]==1 and matriz2[y-1][x]==1:
                print "Gana el jugador Equis"
                return ""
        elif y==2 and x==0:
            if matriz2[y][x+1]==1 and matriz2[y][x+2]==1:
                print "Gana el Jugador Equis"
                return ""
            elif matriz2[y-1][x]==1 and matriz2[y-2][x]==1:
                print "Gana el jugador Equis"
                return ""
            elif matriz2[y-1][x+1]==1 and matriz2[y-2][x+2]==1:
                print "Gana el Jugador Equis"
                return ""
        elif y==0 and x==1:
            if matriz2[y][x+1]==1 and matriz2[y][x-1]==1:
                print "Gana el Jugador Equis"
                return ""
            elif matriz2[y+1][x]==1 and matriz2[y+2][x]==1:
                print "Gana el jugador Equis"
                return ""
        elif y==0 and x==2:
            if matriz2[y][x-1]==1 and matriz2[y][x-2]==1:
                print "Gana el Jugador Equis"
                return ""
            elif matriz2[y+1][x]==1 and matriz2[y+2][x]==1:
                print "Gana el jugador Equis"
                return ""
            elif matriz2[y+1][x-1]==1 and matriz2[y+2][x-2]==1:
                print "Gana el Jugador Equis"
                return ""
        elif y==1 and x==1:
            if matriz2[y][x+1]==1 and matriz2[y][x-1]==1:
                print "Gana el Jugador Equis"
                return ""
            elif matriz2[y-1][x]==1 and matriz2[y+1][x]==1:
                print "Gana el jugador Equis"
                return ""
            elif matriz2[y-1][x-1]==1 and matriz2[y+1][x+1]==1:
                print "Gana el Jugador Equis"
                return ""
        elif y==1 and x==2:
            if matriz2[y][x-1]==1 and matriz2[y][x-2]==1:
                print "Gana el Jugador Equis"
                return ""
            elif matriz2[y-1][x]==1 and matriz2[y+1][x]==1:
                print "Gana el jugador Equis"
                return ""
        elif y==2 and x==1:
            if matriz2[y][x+1]==1 and matriz2[y][x-1]==1:
                print "Gana el Jugador Equis"
                return ""
            elif matriz2[y-1][x]==1 and matriz2[y-2][x]==1:
                print "Gana el jugador Equis"
                return ""
        elif y==2 and x==2:
            if matriz2[y][x-1]==1 and matriz2[y][x-2]==1:
                print "Gana el Jugador Equis"
                return ""
            elif matriz2[y-1][x]==1 and matriz2[y-2][x]==1:
                print "Gana el jugador Equis"
                return ""
                
            elif matriz2[y-1][x-1]==1 and matriz2[y-2][x-2]==1:
                print "Gana el Jugador Equis"
                return ""
                
        if cont==9:
            print "Empate"
            return ""

for y in range(len(matriz)):
    for x in range(len(matriz)):
        obj=Button(v0,text="",image=blanco,command=lambda columna=x, fila=y:cambiar(fila,columna))
        matriz[y][x]=obj
        matriz[y][x].grid(column=x, row=y)


v0.mainloop()
