from tkinter import *
from time import *
from math import *
from random import *
myInterface = Tk()
screen = Canvas(myInterface, width = 1000, height = 800, background = "#C0E1F3")
screen.pack()

##BACKGROUND
#Grass
screen.create_polygon(0,775,265,0,0,0, fill="#157E0D", outline="#157E0D")
screen.create_polygon(1000,775,735,0,1000,0, fill="#157E0D", outline="#157E0D") 

for grass1 in range(1,8000):
    x = randint(0,265)
    y = randint(0,775)
    deltaX = randint(-3,3)
    deltaY = randint(0,10)
    screen.create_line(x,y,x+deltaX,y-deltaY, fill="#0F5D0A")

for grass2 in range(1,8000):
    x = randint(735,1000)
    y = randint(0,775)
    deltaX = randint(-3,3)
    deltaY = randint(0,10)
    screen.create_line(x,y,x+deltaX,y-deltaY, fill="#0F5D0A")

#Road
screen.create_polygon(0,800,275,0,725,0,1000,800, fill="#303030", outline="#303030")
screen.create_line(0,800,275,-3, fill="#A2A4A2", width=25)
screen.create_line(1000,805,725,-3, fill="#A2A4A2", width=25)

#Road Lines
screen.create_polygon(515,750,535,750,534,625,516,625,  fill="white", outline="white")
screen.create_polygon(516,500,534,500,533,388,517,388,  fill="white", outline="white")
screen.create_polygon(517,275,533,275,532,175,518,175,  fill="white", outline="white")
screen.create_polygon(518,80,532,80,531,5,519,5,  fill="white", outline="white")

#Sidewalk
screen.create_polygon(62,0,165,0,0,315,0,85, fill="#BEBEBE", outline="#BEBEBE")
screen.create_polygon(938,0,835,0,1000,315,1000,85, fill="#BEBEBE", outline="#BEBEBE")


##VARIABLES
#Bottom Left Corner of Car Front
Rx1 = 425
Ry1 = -725
Bx1 = 500
By1 = -200
Ox1 = 500
Oy1 = -950
LGx1 = 550
LGy1 = -1175
WHx1 = 275
WHy1 = -1560
#Snail Shell
a1 = -45
b1 = 275
#Snake Tail
c1 = -350
d1 = 275

for f in range(350):

    ##SNAIL
    a2 = a1 + 32 
    b2 = b1 + 34
    a3 = a1 - 10
    b3 = b1 + 17
    a4 = a2 + 11

    trail = screen.create_polygon(a3,b3+10,a4,b3+5,a4,b3-3,a1,b3, fill="#b3d8b5", smooth="true")
    body = screen.create_polygon(a3,b3+10,a4,b3+5,a4,b3-3,a1,b3, fill="#7cad7f", smooth="true")
    tentacleL = screen.create_line(a4-6,b3,a4-9,b1+4, fill="#75a578", width=2)
    tentacleR = screen.create_line(a4-4,b3,a4-1,b1+4, fill="#75a578", width=2)
    eyeL = screen.create_oval(a4-3,b3-15,a4+1,b3-12, fill="#75a578", outline="#75a578")
    eyeR = screen.create_oval(a4-11,b3-15,a4-7,b3-12, fill="#75a578", outline="#75a578")
    shell = screen.create_arc(a1,b1,a2,b2, start=0, extent=195, fill="#bf8c39", outline="#bf8c39")
    swirl = screen.create_line(a1+25,b3,a1+20,b3-11,a1+5,b3-9,a1+6,b3-1,a1+12,b3-3, fill="#a3772f", width=2, smooth="true")

    ##SNAKE
    snakeBody = screen.create_polygon(c1,d1,c1+5,d1+5,c1+50,d1-10,c1+90,d1-5,c1+115,d1-45,c1+130,d1-45,c1+130,d1-55,c1+115,d1-60,c1+90,d1-15,c1+50,d1-20, fill="#97c15d", smooth="true")
    snakeEye = screen.create_oval(c1+119,d1-55,c1+123,d1-51, fill="black")
    
    #RED CAR
    #Rest of Car Front
    xx1 = Rx1 - 5 
    yy1 = Ry1 - 10 
    x2 = Rx1 + 5 
    y2 = Ry1 - 45 
    xx2 = x2 + 5 
    yy2 = y2 - 10
    x3 = Rx1 + 120
    xx3 = x3 - 5 
    x4 = x3 + 5 
    xx4 = x3 + 10 
    x5 = Rx1 + 66 
    y5 = Ry1 + 10 
    #Hood
    Hx1 = Rx1 - 15 
    Hy1 = Ry1 + 35 
    Hxx1 = Hx1 + 1
    Hyy1 = Hy1 + 5
    Hy2 = Hy1 + 25 
    Hy3 = Hy2 + 10 
    Hx4 = x4 - 2 
    Hx5 = x4 + 16 
    Hxx5 = Hx5 - 2 
    #Top
    Tx1 = x3 - 24 
    Ty1 = y2 - 45 
    Txx1 = Tx1 - 5 
    Tyy1 = Ty1 - 7 
    Tx2 = x2 + 24 
    Txx2 = Tx2 + 5 
    #Bumper
    By1 = Hy1 + 35
    Byy1 = By1 + 5
    By2 = Hy2 + 30
    By3 = Hy3 + 30
    #Grille
    Gx1 = xx2 + 25
    Gy1 = Hy2 + 12 
    Gxx1 = Gx1 + 1
    Gyy1 = Gy1 - 3 
    Gx2 = Hx4 - 25
    Gy2 = By2 - 6
    Gxx2 = Gx2 - 1 
    Gyy2 = Gy2 + 3
    Gy3 = Hy3 + 5
    Gy4 = By3 - 7
    #Headlights
    Lx1 = Hx1 + 7
    Ly1 = Hy1 + 22
    Lx2 = Hx5 - 7
    Ly2 = Hy1 + 24
    #Tires
    Wy1 = Hy1 + 55
    Wx2 = Hx1 + 29
    Wy3 = Hy1 + 57
    Wx4 = Hx5 - 30
    #Mirrors
    Mx1 = Rx1 - 8
    My1 = Ry1 - 12
    Mx2 = Mx1 - 13
    My2 = My1 - 11
    Mx4 = x4 + 8
    Mx5 = Mx4 + 13

    RmirrorCL = screen.create_line(Rx1,My1,Rx1-12,My1-3, fill="#910101", width=4)
    RmirrorCR = screen.create_line(x4,My1,x4+12,My1-3, fill="#910101", width=4)
    RmirrorL = screen.create_oval(Mx1,My1,Mx2,My2, fill="#f21818", outline="#f21818")
    RmirrorR = screen.create_oval(Mx4,My1,Mx5,My2, fill="#f21818", outline="#f21818")
    Rfront = screen.create_polygon(Rx1,Ry1,xx1,yy1,x2,y2,xx2,yy2,xx3,yy2,x3,y2,xx4,yy1,x4,Ry1,x5,y5, fill="#ff0000", smooth="true")
    Rwindshield = screen.create_polygon(Rx1+5,Ry1-5,xx1+5,yy1-5,x2+5,y2+5,xx2+5,yy2+5,xx3-5,yy2+5,x3-5,y2+5,xx4-5,yy1-5,x4-5,Ry1-5,x5,y5-5, fill="#5d979b", smooth="true")
    RwiperL = screen.create_line(x5-14,y5-10,x5-49,y5-17, fill="black", width=2)
    RwiperR = screen.create_line(x5+25,y5-10,x5-10,y5-15, fill="black", width=2)
    Rhood = screen.create_polygon(xx4,yy1,x4,Ry1,x5,y5,Rx1,Ry1,xx1,yy1,Hx1,Hy1,Hxx1,Hyy1,xx2,Hy2,x5,Hy3,Hx4,Hy2,Hxx5,Hyy1,Hx5,Hy1, fill="#e01111", smooth="true")
    RhoodOutline = screen.create_line(xx4-8,yy1+15,x4-8,Ry1+15,x5,y5+12,Rx1+8,Ry1+15,xx1+8,yy1+15,Hx1+12,Hy1-10,Hxx1+12,Hyy1-10,xx2+5,Hy2-10,x5,Hy3-10,Hx4-5,Hy2-10,Hxx5-12,Hyy1-10,Hx5-12,Hy1-10,xx4-8,yy1+15, fill="#fc1b11", width=3, smooth="true")
    Rtop = screen.create_polygon(x2,y2,xx2,yy2,xx3,yy2,x3,y2,Tx1,Ty1,Txx1,Tyy1,Txx2,Tyy1,Tx2,Ty1, fill="#e01111", smooth="true")
    Rantenna = screen.create_line(x5-3,Ty1-3,x5-3,Ty1-18, fill="black", width=3)
    RwheelL = screen.create_polygon(Hx1,By1,Hxx1,Byy1,Hx1,Wy1,Wx2,Wy1+10,Wx2,By1, fill="#050505", smooth="true")
    RwheelR = screen.create_polygon(Hxx5,Byy1,Hx5,By1,Wx4,By1,Wx4,Wy3+10,Hx5,Wy3, fill="#050505", smooth="true")
    Rbumper = screen.create_polygon(Hx1,Hy1,Hxx1,Hyy1,xx2,Hy2,x5,Hy3,Hx4,Hy2,Hxx5,Hyy1,Hx5,Hy1,Hxx5,Byy1,Hx5,By1,Hx4,By2,x5,By3,xx2,By2,Hx1,By1,Hxx1,Byy1, fill="#fc1b11", smooth="true")
    Rgrille = screen.create_polygon(Gx1,Gy1,Gxx1,Gyy1,x5,Gy3,Gxx2,Gyy1,Gx2,Gy1,Gx2,Gy2,Gxx2,Gyy2,x5,Gy4,Gxx1,Gyy2,Gx1,Gy2, fill="#515050", smooth="true")
    RheadlightR1 = screen.create_arc(Lx1+13,Ly1+15,Lx1,Ly1, start=260, extent=180, fill="#edebda", outline="#edebda")
    RheadlightL1 = screen.create_arc(Lx1,Ly1,Lx1+11,Ly1+15, start=70, extent=180, fill="#ffcf70", outline="#ffcf70")
    RheadlightL2 = screen.create_arc(Lx2,Ly2,Lx2-13,Ly2+15, start=105, extent=180, fill="#edebda", outline="#edebda")
    RheadlightR2 = screen.create_arc(Lx2-11,Ly2+15,Lx2,Ly2, start=290, extent=180, fill="#ffcf70", outline="#ffcf70")
    

    ##BLUE CAR
    xx1 = Bx1 - 5 
    yy1 = By1 - 10 
    x2 = Bx1 + 5 
    y2 = By1 - 45 
    xx2 = x2 + 5 
    yy2 = y2 - 10
    x3 = Bx1 + 120
    xx3 = x3 - 5 
    x4 = x3 + 5 
    xx4 = x3 + 10 
    x5 = Bx1 + 66 
    y5 = By1 + 10 

    Hx1 = Bx1 - 15 
    Hy1 = By1 + 35 
    Hxx1 = Hx1 + 1
    Hyy1 = Hy1 + 5
    Hy2 = Hy1 + 25 
    Hy3 = Hy2 + 10 
    Hx4 = x4 - 2 
    Hx5 = x4 + 16 
    Hxx5 = Hx5 - 2 

    Tx1 = x3 - 24 
    Ty1 = y2 - 45 
    Txx1 = Tx1 - 5 
    Tyy1 = Ty1 - 7 
    Tx2 = x2 + 24 
    Txx2 = Tx2 + 5
    
    Buy1 = Hy1 + 35
    Buyy1 = Buy1 + 5
    Buy2 = Hy2 + 30
    Buy3 = Hy3 + 30

    Gx1 = xx2 + 25
    Gy1 = Hy2 + 12 
    Gxx1 = Gx1 + 1
    Gyy1 = Gy1 - 3 
    Gx2 = Hx4 - 25
    Gy2 = Buy2 - 6
    Gxx2 = Gx2 - 1 
    Gyy2 = Gy2 + 3
    Gy3 = Hy3 + 5
    Gy4 = Buy3 - 7
    
    Lx1 = Hx1 + 7
    Ly1 = Hy1 + 22
    Lx2 = Hx5 - 7
    Ly2 = Hy1 + 24
    
    Wy1 = Hy1 + 55
    Wx2 = Hx1 + 29
    Wy3 = Hy1 + 57
    Wx4 = Hx5 - 30
    
    Mx1 = Bx1 - 8
    My1 = By1 - 12
    Mx2 = Mx1 - 13
    My2 = My1 - 11
    Mx4 = x4 + 8
    Mx5 = Mx4 + 13

    BmirrorCL = screen.create_line(Bx1,My1,Bx1-12,My1-3, fill="#002672", width=4)
    BmirrorCR = screen.create_line(x4,My1,x4+12,My1-3, fill="#002672", width=4)
    BmirrorL = screen.create_oval(Mx1,My1,Mx2,My2, fill="#003196", outline="#003196")
    BmirrorR = screen.create_oval(Mx4,My1,Mx5,My2, fill="#003196", outline="#003196")
    Bfront = screen.create_polygon(Bx1,By1,xx1,yy1,x2,y2,xx2,yy2,xx3,yy2,x3,y2,xx4,yy1,x4,By1,x5,y5, fill="#0055ff", smooth="true")
    Bwindshield = screen.create_polygon(Bx1+5,By1-5,xx1+5,yy1-5,x2+5,y2+5,xx2+5,yy2+5,xx3-5,yy2+5,x3-5,y2+5,xx4-5,yy1-5,x4-5,By1-5,x5,y5-5, fill="#5d979b", smooth="true")
    BwiperL = screen.create_line(x5-14,y5-10,x5-49,y5-17, fill="black", width=2)
    BwiperR = screen.create_line(x5+25,y5-10,x5-10,y5-15, fill="black", width=2)
    Bhood = screen.create_polygon(xx4,yy1,x4,By1,x5,y5,Bx1,By1,xx1,yy1,Hx1,Hy1,Hxx1,Hyy1,xx2,Hy2,x5,Hy3,Hx4,Hy2,Hxx5,Hyy1,Hx5,Hy1, fill="#0045d1", smooth="true")
    BhoodOutline = screen.create_line(xx4-8,yy1+15,x4-8,By1+15,x5,y5+12,Bx1+8,By1+15,xx1+8,yy1+15,Hx1+12,Hy1-10,Hxx1+12,Hyy1-10,xx2+5,Hy2-10,x5,Hy3-10,Hx4-5,Hy2-10,Hxx5-12,Hyy1-10,Hx5-12,Hy1-10,xx4-8,yy1+15, fill="#0055ff", width=3, smooth="true")
    Btop = screen.create_polygon(x2,y2,xx2,yy2,xx3,yy2,x3,y2,Tx1,Ty1,Txx1,Tyy1,Txx2,Tyy1,Tx2,Ty1, fill="#0045d1", smooth="true")
    Bantenna = screen.create_line(x5-3,Ty1-3,x5-3,Ty1-18, fill="black", width=3)
    BwheelL = screen.create_polygon(Hx1,Buy1,Hxx1,Buyy1,Hx1,Wy1,Wx2,Wy1+10,Wx2,Buy1, fill="#050505", smooth="true")
    BwheelR = screen.create_polygon(Hxx5,Buyy1,Hx5,Buy1,Wx4,Buy1,Wx4,Wy3+10,Hx5,Wy3, fill="#050505", smooth="true")
    Bbumper = screen.create_polygon(Hx1,Hy1,Hxx1,Hyy1,xx2,Hy2,x5,Hy3,Hx4,Hy2,Hxx5,Hyy1,Hx5,Hy1,Hxx5,Buyy1,Hx5,Buy1,Hx4,Buy2,x5,Buy3,xx2,Buy2,Hx1,Buy1,Hxx1,Buyy1, fill="#0c5afc", smooth="true")
    Bgrille = screen.create_polygon(Gx1,Gy1,Gxx1,Gyy1,x5,Gy3,Gxx2,Gyy1,Gx2,Gy1,Gx2,Gy2,Gxx2,Gyy2,x5,Gy4,Gxx1,Gyy2,Gx1,Gy2, fill="#515050", smooth="true")
    BheadlightR1 = screen.create_arc(Lx1+13,Ly1+15,Lx1,Ly1, start=260, extent=180, fill="#edebda", outline="#edebda")
    BheadlightL1 = screen.create_arc(Lx1,Ly1,Lx1+11,Ly1+15, start=70, extent=180, fill="#ffcf70", outline="#ffcf70")
    BheadlightL2 = screen.create_arc(Lx2,Ly2,Lx2-13,Ly2+15, start=105, extent=180, fill="#edebda", outline="#edebda")
    BheadlightR2 = screen.create_arc(Lx2-11,Ly2+15,Lx2,Ly2, start=290, extent=180, fill="#ffcf70", outline="#ffcf70")


    ##ORANGE CAR
    xx1 = Ox1 - 5 
    yy1 = Oy1 - 10 
    x2 = Ox1 + 5 
    y2 = Oy1 - 45 
    xx2 = x2 + 5 
    yy2 = y2 - 10
    x3 = Ox1 + 120
    xx3 = x3 - 5 
    x4 = x3 + 5 
    xx4 = x3 + 10 
    x5 = Ox1 + 66 
    y5 = Oy1 + 10 

    Hx1 = Ox1 - 15 
    Hy1 = Oy1 + 35 
    Hxx1 = Hx1 + 1
    Hyy1 = Hy1 + 5
    Hy2 = Hy1 + 25 
    Hy3 = Hy2 + 10 
    Hx4 = x4 - 2 
    Hx5 = x4 + 16 
    Hxx5 = Hx5 - 2 

    Tx1 = x3 - 24 
    Ty1 = y2 - 45 
    Txx1 = Tx1 - 5 
    Tyy1 = Ty1 - 7 
    Tx2 = x2 + 24 
    Txx2 = Tx2 + 5
    
    By1 = Hy1 + 35
    Byy1 = By1 + 5
    By2 = Hy2 + 30
    By3 = Hy3 + 30

    Gx1 = xx2 + 25
    Gy1 = Hy2 + 12 
    Gxx1 = Gx1 + 1
    Gyy1 = Gy1 - 3 
    Gx2 = Hx4 - 25
    Gy2 = By2 - 6
    Gxx2 = Gx2 - 1 
    Gyy2 = Gy2 + 3
    Gy3 = Hy3 + 5
    Gy4 = By3 - 7
    
    Lx1 = Hx1 + 7
    Ly1 = Hy1 + 22
    Lx2 = Hx5 - 7
    Ly2 = Hy1 + 24
    
    Wy1 = Hy1 + 55
    Wx2 = Hx1 + 29
    Wy3 = Hy1 + 57
    Wx4 = Hx5 - 30
    
    Mx1 = Ox1 - 8
    My1 = Oy1 - 12
    Mx2 = Mx1 - 13
    My2 = My1 - 11
    Mx4 = x4 + 8
    Mx5 = Mx4 + 13

    OmirrorCL = screen.create_line(Ox1,My1,Ox1-12,My1-3, fill="#ce4100", width=4)
    OmirrorCR = screen.create_line(x4,My1,x4+12,My1-3, fill="#ce4100", width=4)
    OmirrorL = screen.create_oval(Mx1,My1,Mx2,My2, fill="#ff3b00", outline="#ff3b00")
    OmirrorR = screen.create_oval(Mx4,My1,Mx5,My2, fill="#ff3b00", outline="#ff3b00")
    Ofront = screen.create_polygon(Ox1,Oy1,xx1,yy1,x2,y2,xx2,yy2,xx3,yy2,x3,y2,xx4,yy1,x4,Oy1,x5,y5, fill="#ff5000", smooth="true")
    Owindshield = screen.create_polygon(Ox1+5,Oy1-5,xx1+5,yy1-5,x2+5,y2+5,xx2+5,yy2+5,xx3-5,yy2+5,x3-5,y2+5,xx4-5,yy1-5,x4-5,Oy1-5,x5,y5-5, fill="#5d979b", smooth="true")
    OwiperL = screen.create_line(x5-14,y5-10,x5-49,y5-17, fill="black", width=2)
    OwiperR = screen.create_line(x5+25,y5-10,x5-10,y5-15, fill="black", width=2)
    Ohood = screen.create_polygon(xx4,yy1,x4,Oy1,x5,y5,Ox1,Oy1,xx1,yy1,Hx1,Hy1,Hxx1,Hyy1,xx2,Hy2,x5,Hy3,Hx4,Hy2,Hxx5,Hyy1,Hx5,Hy1, fill="#ff1d00", smooth="true")
    OhoodOutline = screen.create_line(xx4-8,yy1+15,x4-8,Oy1+15,x5,y5+12,Ox1+8,Oy1+15,xx1+8,yy1+15,Hx1+12,Hy1-10,Hxx1+12,Hyy1-10,xx2+5,Hy2-10,x5,Hy3-10,Hx4-5,Hy2-10,Hxx5-12,Hyy1-10,Hx5-12,Hy1-10,xx4-8,yy1+15, fill="#ff5000", width=3, smooth="true")
    Otop = screen.create_polygon(x2,y2,xx2,yy2,xx3,yy2,x3,y2,Tx1,Ty1,Txx1,Tyy1,Txx2,Tyy1,Tx2,Ty1, fill="#ff1d00", smooth="true")
    Oantenna = screen.create_line(x5-3,Ty1-3,x5-3,Ty1-18, fill="black", width=3)
    OwheelL = screen.create_polygon(Hx1,By1,Hxx1,Byy1,Hx1,Wy1,Wx2,Wy1+10,Wx2,By1, fill="#050505", smooth="true")
    OwheelR = screen.create_polygon(Hxx5,Byy1,Hx5,By1,Wx4,By1,Wx4,Wy3+10,Hx5,Wy3, fill="#050505", smooth="true")
    Obumper = screen.create_polygon(Hx1,Hy1,Hxx1,Hyy1,xx2,Hy2,x5,Hy3,Hx4,Hy2,Hxx5,Hyy1,Hx5,Hy1,Hxx5,Byy1,Hx5,By1,Hx4,By2,x5,By3,xx2,By2,Hx1,By1,Hxx1,Byy1, fill="#ff5811", smooth="true")
    Ogrille = screen.create_polygon(Gx1,Gy1,Gxx1,Gyy1,x5,Gy3,Gxx2,Gyy1,Gx2,Gy1,Gx2,Gy2,Gxx2,Gyy2,x5,Gy4,Gxx1,Gyy2,Gx1,Gy2, fill="#515050", smooth="true")
    OheadlightR1 = screen.create_arc(Lx1+13,Ly1+15,Lx1,Ly1, start=260, extent=180, fill="#edebda", outline="#edebda")
    OheadlightL1 = screen.create_arc(Lx1,Ly1,Lx1+11,Ly1+15, start=70, extent=180, fill="#ffcf70", outline="#ffcf70")
    OheadlightL2 = screen.create_arc(Lx2,Ly2,Lx2-13,Ly2+15, start=105, extent=180, fill="#edebda", outline="#edebda")
    OheadlightR2 = screen.create_arc(Lx2-11,Ly2+15,Lx2,Ly2, start=290, extent=180, fill="#ffcf70", outline="#ffcf70")

    ##LIGHT GREEN CAR
    xx1 = LGx1 - 5 
    yy1 = LGy1 - 10 
    x2 = LGx1 + 5 
    y2 = LGy1 - 45 
    xx2 = x2 + 5 
    yy2 = y2 - 10
    x3 = LGx1 + 120
    xx3 = x3 - 5 
    x4 = x3 + 5 
    xx4 = x3 + 10 
    x5 = LGx1 + 66 
    y5 = LGy1 + 10 

    Hx1 = LGx1 - 15 
    Hy1 = LGy1 + 35 
    Hxx1 = Hx1 + 1
    Hyy1 = Hy1 + 5
    Hy2 = Hy1 + 25 
    Hy3 = Hy2 + 10 
    Hx4 = x4 - 2 
    Hx5 = x4 + 16 
    Hxx5 = Hx5 - 2 

    Tx1 = x3 - 24 
    Ty1 = y2 - 45 
    Txx1 = Tx1 - 5 
    Tyy1 = Ty1 - 7 
    Tx2 = x2 + 24 
    Txx2 = Tx2 + 5
    
    By1 = Hy1 + 35
    Byy1 = By1 + 5
    By2 = Hy2 + 30
    By3 = Hy3 + 30

    Gx1 = xx2 + 25
    Gy1 = Hy2 + 12 
    Gxx1 = Gx1 + 1
    Gyy1 = Gy1 - 3 
    Gx2 = Hx4 - 25
    Gy2 = By2 - 6
    Gxx2 = Gx2 - 1 
    Gyy2 = Gy2 + 3
    Gy3 = Hy3 + 5
    Gy4 = By3 - 7
    
    Lx1 = Hx1 + 7
    Ly1 = Hy1 + 22
    Lx2 = Hx5 - 7
    Ly2 = Hy1 + 24
    
    Wy1 = Hy1 + 55
    Wx2 = Hx1 + 29
    Wy3 = Hy1 + 57
    Wx4 = Hx5 - 30
    
    Mx1 = LGx1 - 8
    My1 = LGy1 - 12
    Mx2 = Mx1 - 13
    My2 = My1 - 11
    Mx4 = x4 + 8
    Mx5 = Mx4 + 13

    LGmirrorCL = screen.create_line(LGx1,My1,LGx1-12,My1-3, fill="#0aaa00", width=4)
    LGmirrorCR = screen.create_line(x4,My1,x4+12,My1-3, fill="#0aaa00", width=4)
    LGmirrorL = screen.create_oval(Mx1,My1,Mx2,My2, fill="#21c417", outline="#21c417")
    LGmirrorR = screen.create_oval(Mx4,My1,Mx5,My2, fill="#21c417", outline="#21c417")
    LGfront = screen.create_polygon(LGx1,LGy1,xx1,yy1,x2,y2,xx2,yy2,xx3,yy2,x3,y2,xx4,yy1,x4,LGy1,x5,y5, fill="#00ff08", smooth="true")
    LGwindshield = screen.create_polygon(LGx1+5,LGy1-5,xx1+5,yy1-5,x2+5,y2+5,xx2+5,yy2+5,xx3-5,yy2+5,x3-5,y2+5,xx4-5,yy1-5,x4-5,LGy1-5,x5,y5-5, fill="#5d979b", smooth="true")
    LGwiperL = screen.create_line(x5-14,y5-10,x5-49,y5-17, fill="black", width=2)
    LGwiperR = screen.create_line(x5+25,y5-10,x5-10,y5-15, fill="black", width=2)
    LGhood = screen.create_polygon(xx4,yy1,x4,LGy1,x5,y5,LGx1,LGy1,xx1,yy1,Hx1,Hy1,Hxx1,Hyy1,xx2,Hy2,x5,Hy3,Hx4,Hy2,Hxx5,Hyy1,Hx5,Hy1, fill="#0dcc00", smooth="true")
    LGhoodOutline = screen.create_line(xx4-8,yy1+15,x4-8,LGy1+15,x5,y5+12,LGx1+8,LGy1+15,xx1+8,yy1+15,Hx1+12,Hy1-10,Hxx1+12,Hyy1-10,xx2+5,Hy2-10,x5,Hy3-10,Hx4-5,Hy2-10,Hxx5-12,Hyy1-10,Hx5-12,Hy1-10,xx4-8,yy1+15, fill="#00ff08", width=3, smooth="true")
    LGtop = screen.create_polygon(x2,y2,xx2,yy2,xx3,yy2,x3,y2,Tx1,Ty1,Txx1,Tyy1,Txx2,Tyy1,Tx2,Ty1, fill="#0dcc00", smooth="true")
    LGantenna = screen.create_line(x5-3,Ty1-3,x5-3,Ty1-18, fill="black", width=3)
    LGwheelL = screen.create_polygon(Hx1,By1,Hxx1,Byy1,Hx1,Wy1,Wx2,Wy1+10,Wx2,By1, fill="#050505", smooth="true")
    LGwheelR = screen.create_polygon(Hxx5,Byy1,Hx5,By1,Wx4,By1,Wx4,Wy3+10,Hx5,Wy3, fill="#050505", smooth="true")
    LGbumper = screen.create_polygon(Hx1,Hy1,Hxx1,Hyy1,xx2,Hy2,x5,Hy3,Hx4,Hy2,Hxx5,Hyy1,Hx5,Hy1,Hxx5,Byy1,Hx5,By1,Hx4,By2,x5,By3,xx2,By2,Hx1,By1,Hxx1,Byy1, fill="#1be80d", smooth="true")
    LGgrille = screen.create_polygon(Gx1,Gy1,Gxx1,Gyy1,x5,Gy3,Gxx2,Gyy1,Gx2,Gy1,Gx2,Gy2,Gxx2,Gyy2,x5,Gy4,Gxx1,Gyy2,Gx1,Gy2, fill="#515050", smooth="true")
    LGheadlightR1 = screen.create_arc(Lx1+13,Ly1+15,Lx1,Ly1, start=260, extent=180, fill="#edebda", outline="#edebda")
    LGheadlightL1 = screen.create_arc(Lx1,Ly1,Lx1+11,Ly1+15, start=70, extent=180, fill="#ffcf70", outline="#ffcf70")
    LGheadlightL2 = screen.create_arc(Lx2,Ly2,Lx2-13,Ly2+15, start=105, extent=180, fill="#edebda", outline="#edebda")
    LGheadlightR2 = screen.create_arc(Lx2-11,Ly2+15,Lx2,Ly2, start=290, extent=180, fill="#ffcf70", outline="#ffcf70")

    ##WHITE CAR
    xx1 = WHx1 - 5 
    yy1 = WHy1 - 10 
    x2 = WHx1 + 5 
    y2 = WHy1 - 45 
    xx2 = x2 + 5 
    yy2 = y2 - 10
    x3 = WHx1 + 120
    xx3 = x3 - 5 
    x4 = x3 + 5 
    xx4 = x3 + 10 
    x5 = WHx1 + 66 
    y5 = WHy1 + 10 

    Hx1 = WHx1 - 15 
    Hy1 = WHy1 + 35 
    Hxx1 = Hx1 + 1
    Hyy1 = Hy1 + 5
    Hy2 = Hy1 + 25 
    Hy3 = Hy2 + 10 
    Hx4 = x4 - 2 
    Hx5 = x4 + 16 
    Hxx5 = Hx5 - 2 

    Tx1 = x3 - 24 
    Ty1 = y2 - 45 
    Txx1 = Tx1 - 5 
    Tyy1 = Ty1 - 7 
    Tx2 = x2 + 24 
    Txx2 = Tx2 + 5
    
    By1 = Hy1 + 35
    Byy1 = By1 + 5
    By2 = Hy2 + 30
    By3 = Hy3 + 30

    Gx1 = xx2 + 25
    Gy1 = Hy2 + 12 
    Gxx1 = Gx1 + 1
    Gyy1 = Gy1 - 3 
    Gx2 = Hx4 - 25
    Gy2 = By2 - 6
    Gxx2 = Gx2 - 1 
    Gyy2 = Gy2 + 3
    Gy3 = Hy3 + 5
    Gy4 = By3 - 7
    
    Lx1 = Hx1 + 7
    Ly1 = Hy1 + 22
    Lx2 = Hx5 - 7
    Ly2 = Hy1 + 24
    
    Wy1 = Hy1 + 55
    Wx2 = Hx1 + 29
    Wy3 = Hy1 + 57
    Wx4 = Hx5 - 30
    
    Mx1 = WHx1 - 8
    My1 = WHy1 - 12
    Mx2 = Mx1 - 13
    My2 = My1 - 11
    Mx4 = x4 + 8
    Mx5 = Mx4 + 13

    WHmirrorCL = screen.create_line(WHx1,My1,WHx1-12,My1-3, fill="#cccccc", width=4)
    WHmirrorCR = screen.create_line(x4,My1,x4+12,My1-3, fill="#cccccc", width=4)
    WHmirrorL = screen.create_oval(Mx1,My1,Mx2,My2, fill="#f4eded", outline="#f4eded")
    WHmirrorR = screen.create_oval(Mx4,My1,Mx5,My2, fill="#f4eded", outline="#f4eded")
    WHfront = screen.create_polygon(WHx1,WHy1,xx1,yy1,x2,y2,xx2,yy2,xx3,yy2,x3,y2,xx4,yy1,x4,WHy1,x5,y5, fill="#d8d8d8", smooth="true")
    WHwindshield = screen.create_polygon(WHx1+5,WHy1-5,xx1+5,yy1-5,x2+5,y2+5,xx2+5,yy2+5,xx3-5,yy2+5,x3-5,y2+5,xx4-5,yy1-5,x4-5,WHy1-5,x5,y5-5, fill="#5d979b", smooth="true")
    WHwiperL = screen.create_line(x5-14,y5-10,x5-49,y5-17, fill="black", width=2)
    WHwiperR = screen.create_line(x5+25,y5-10,x5-10,y5-15, fill="black", width=2)
    WHhood = screen.create_polygon(xx4,yy1,x4,WHy1,x5,y5,WHx1,WHy1,xx1,yy1,Hx1,Hy1,Hxx1,Hyy1,xx2,Hy2,x5,Hy3,Hx4,Hy2,Hxx5,Hyy1,Hx5,Hy1, fill="#f2f2f2", smooth="true")
    WHhoodOutline = screen.create_line(xx4-8,yy1+15,x4-8,WHy1+15,x5,y5+12,WHx1+8,WHy1+15,xx1+8,yy1+15,Hx1+12,Hy1-10,Hxx1+12,Hyy1-10,xx2+5,Hy2-10,x5,Hy3-10,Hx4-5,Hy2-10,Hxx5-12,Hyy1-10,Hx5-12,Hy1-10,xx4-8,yy1+15, fill="#dbd4d4", width=3, smooth="true")
    WHtop = screen.create_polygon(x2,y2,xx2,yy2,xx3,yy2,x3,y2,Tx1,Ty1,Txx1,Tyy1,Txx2,Tyy1,Tx2,Ty1, fill="#f2f2f2", smooth="true")
    WHantenna = screen.create_line(x5-3,Ty1-3,x5-3,Ty1-18, fill="black", width=3)
    WHwheelL = screen.create_polygon(Hx1,By1,Hxx1,Byy1,Hx1,Wy1,Wx2,Wy1+10,Wx2,By1, fill="#050505", smooth="true")
    WHwheelR = screen.create_polygon(Hxx5,Byy1,Hx5,By1,Wx4,By1,Wx4,Wy3+10,Hx5,Wy3, fill="#050505", smooth="true")
    WHbumper = screen.create_polygon(Hx1,Hy1,Hxx1,Hyy1,xx2,Hy2,x5,Hy3,Hx4,Hy2,Hxx5,Hyy1,Hx5,Hy1,Hxx5,Byy1,Hx5,By1,Hx4,By2,x5,By3,xx2,By2,Hx1,By1,Hxx1,Byy1, fill="#dbd4d4", smooth="true")
    WHgrille = screen.create_polygon(Gx1,Gy1,Gxx1,Gyy1,x5,Gy3,Gxx2,Gyy1,Gx2,Gy1,Gx2,Gy2,Gxx2,Gyy2,x5,Gy4,Gxx1,Gyy2,Gx1,Gy2, fill="#515050", smooth="true")
    WHheadlightR1 = screen.create_arc(Lx1+13,Ly1+15,Lx1,Ly1, start=260, extent=180, fill="#ffffff", outline="#edebda")
    WHheadlightL1 = screen.create_arc(Lx1,Ly1,Lx1+11,Ly1+15, start=70, extent=180, fill="#ffcf70", outline="#ffcf70")
    WHheadlightL2 = screen.create_arc(Lx2,Ly2,Lx2-13,Ly2+15, start=105, extent=180, fill="#ffffff", outline="#edebda")
    WHheadlightR2 = screen.create_arc(Lx2-11,Ly2+15,Lx2,Ly2, start=290, extent=180, fill="#ffcf70", outline="#ffcf70")
    
    screen.update()
    sleep(0.03)
    screen.delete(RmirrorCL,RmirrorCR,RmirrorL,RmirrorR,Rfront,Rwindshield,RwiperL,RwiperR,Rhood,RhoodOutline,Rtop,Rantenna,RwheelL,RwheelR,Rbumper,Rgrille,RheadlightL1,RheadlightR1,RheadlightL2,RheadlightR2,
                  BmirrorCL,BmirrorCR,BmirrorL,BmirrorR,Bfront,Bwindshield,BwiperL,BwiperR,Bhood,BhoodOutline,Btop,Bantenna,BwheelL,BwheelR,Bbumper,Bgrille,BheadlightL1,BheadlightR1,BheadlightL2,BheadlightR2,
                  OmirrorCL,OmirrorCR,OmirrorL,OmirrorR,Ofront,Owindshield,OwiperL,OwiperR,Ohood,OhoodOutline,Otop,Oantenna,OwheelL,OwheelR,Obumper,Ogrille,OheadlightL1,OheadlightR1,OheadlightL2,OheadlightR2,             
                  LGmirrorCL,LGmirrorCR,LGmirrorL,LGmirrorR,LGfront,LGwindshield,LGwiperL,LGwiperR,LGhood,LGhoodOutline,LGtop,LGantenna,LGwheelL,LGwheelR,LGbumper,LGgrille,LGheadlightL1,LGheadlightR1,LGheadlightL2,LGheadlightR2,
                  WHmirrorCL,WHmirrorCR,WHmirrorL,WHmirrorR,WHfront,WHwindshield,WHwiperL,WHwiperR,WHhood,WHhoodOutline,WHtop,WHantenna,WHwheelL,WHwheelR,WHbumper,WHgrille,WHheadlightL1,WHheadlightR1,WHheadlightL2,WHheadlightR2,
                  body,tentacleL,tentacleR,eyeL,eyeR,shell,swirl,snakeBody,snakeEye)
                  
    Rx1 = Rx1 - 1
    Ry1 = Ry1 + 6
    Bx1 = Bx1 + 1
    By1 = By1 + 5
    Ox1 = Ox1 - 1
    Oy1 = Oy1 + 6
    LGx1 = LGx1 - 1
    LGy1 = LGy1 + 6
    WHx1 = WHx1 + 1
    WHy1 = WHy1 + 5
    a1 = a1 + 3
    b1 = b1 + 0.1
    c1 = 5*f - 1050
    d1 = 275 + 25*sin(0.2*f)

##AFTER ANIMATION
#Dead Snake
c1 = 5*f - 1050
d1 = 275 + 25*sin(0.2*f)
screen.create_polygon(c1,d1,c1+5,d1+5,c1+50,d1-10,c1+90,d1-5,c1+115,d1-45,c1+130,d1-45,c1+130,d1-55,c1+115,d1-60,c1+90,d1-15,c1+50,d1-20, fill="#97c15d", smooth="true")
screen.create_line(c1+119,d1-55,c1+125,d1-49, fill="black", width=2)
screen.create_line(c1+125,d1-55,c1+118,d1-49, fill="black", width=2)

##Text
screen.create_text(c1+165,d1-52, text="R I P", font="Calibri 15", fill="white")

#White Car
WHx1 = 625
WHy1 = 190
xx1 = WHx1 - 5 
yy1 = WHy1 - 10 
x2 = WHx1 + 5 
y2 = WHy1 - 45 
xx2 = x2 + 5 
yy2 = y2 - 10
x3 = WHx1 + 120
xx3 = x3 - 5 
x4 = x3 + 5 
xx4 = x3 + 10 
x5 = WHx1 + 66 
y5 = WHy1 + 10 
Hx1 = WHx1 - 15 
Hy1 = WHy1 + 35 
Hxx1 = Hx1 + 1
Hyy1 = Hy1 + 5
Hy2 = Hy1 + 25 
Hy3 = Hy2 + 10 
Hx4 = x4 - 2 
Hx5 = x4 + 16 
Hxx5 = Hx5 - 2 
Tx1 = x3 - 24 
Ty1 = y2 - 45 
Txx1 = Tx1 - 5 
Tyy1 = Ty1 - 7 
Tx2 = x2 + 24 
Txx2 = Tx2 + 5
y1 = Hy1 + 35
Byy1 = By1 + 5
By2 = Hy2 + 30
By3 = Hy3 + 30
Gx1 = xx2 + 25
Gy1 = Hy2 + 12 
Gxx1 = Gx1 + 1
Gyy1 = Gy1 - 3 
Gx2 = Hx4 - 25
Gy2 = By2 - 6
Gxx2 = Gx2 - 1 
Gyy2 = Gy2 + 3
Gy3 = Hy3 + 5
Gy4 = By3 - 7
Lx1 = Hx1 + 7
Ly1 = Hy1 + 22
Lx2 = Hx5 - 7
Ly2 = Hy1 + 24
Wy1 = Hy1 + 55
Wx2 = Hx1 + 29
Wy3 = Hy1 + 57
Wx4 = Hx5 - 30
Mx1 = WHx1 - 8
My1 = WHy1 - 12
Mx2 = Mx1 - 13
My2 = My1 - 11
Mx4 = x4 + 8
Mx5 = Mx4 + 13

screen.create_line(WHx1,My1,WHx1-12,My1-3, fill="#cccccc", width=4)
screen.create_line(x4,My1,x4+12,My1-3, fill="#cccccc", width=4)
screen.create_oval(Mx1,My1,Mx2,My2, fill="#f4eded", outline="#f4eded")
screen.create_oval(Mx4,My1,Mx5,My2, fill="#f4eded", outline="#f4eded")
screen.create_polygon(WHx1,WHy1,xx1,yy1,x2,y2,xx2,yy2,xx3,yy2,x3,y2,xx4,yy1,x4,WHy1,x5,y5, fill="#d8d8d8", smooth="true")
screen.create_polygon(WHx1+5,WHy1-5,xx1+5,yy1-5,x2+5,y2+5,xx2+5,yy2+5,xx3-5,yy2+5,x3-5,y2+5,xx4-5,yy1-5,x4-5,WHy1-5,x5,y5-5, fill="#5d979b", smooth="true")
screen.create_line(x5-14,y5-10,x5-49,y5-17, fill="black", width=2)
screen.create_line(x5+25,y5-10,x5-10,y5-15, fill="black", width=2)
screen.create_polygon(xx4,yy1,x4,WHy1,x5,y5,WHx1,WHy1,xx1,yy1,Hx1,Hy1,Hxx1,Hyy1,xx2,Hy2,x5,Hy3,Hx4,Hy2,Hxx5,Hyy1,Hx5,Hy1, fill="#f2f2f2", smooth="true")
screen.create_line(xx4-8,yy1+15,x4-8,WHy1+15,x5,y5+12,WHx1+8,WHy1+15,xx1+8,yy1+15,Hx1+12,Hy1-10,Hxx1+12,Hyy1-10,xx2+5,Hy2-10,x5,Hy3-10,Hx4-5,Hy2-10,Hxx5-12,Hyy1-10,Hx5-12,Hy1-10,xx4-8,yy1+15, fill="#dbd4d4", width=3, smooth="true")
screen.create_polygon(x2,y2,xx2,yy2,xx3,yy2,x3,y2,Tx1,Ty1,Txx1,Tyy1,Txx2,Tyy1,Tx2,Ty1, fill="#f2f2f2", smooth="true")
screen.create_line(x5-3,Ty1-3,x5-3,Ty1-18, fill="black", width=3)
screen.create_polygon(Hx1,By1,Hxx1,Byy1,Hx1,Wy1,Wx2,Wy1+10,Wx2,By1, fill="#050505", smooth="true")
screen.create_polygon(Hxx5,Byy1,Hx5,By1,Wx4,By1,Wx4,Wy3+10,Hx5,Wy3, fill="#050505", smooth="true")
screen.create_polygon(Hx1,Hy1,Hxx1,Hyy1,xx2,Hy2,x5,Hy3,Hx4,Hy2,Hxx5,Hyy1,Hx5,Hy1,Hxx5,Byy1,Hx5,By1,Hx4,By2,x5,By3,xx2,By2,Hx1,By1,Hxx1,Byy1, fill="#dbd4d4", smooth="true")
screen.create_polygon(Gx1,Gy1,Gxx1,Gyy1,x5,Gy3,Gxx2,Gyy1,Gx2,Gy1,Gx2,Gy2,Gxx2,Gyy2,x5,Gy4,Gxx1,Gyy2,Gx1,Gy2, fill="#515050", smooth="true")
screen.create_arc(Lx1+13,Ly1+15,Lx1,Ly1, start=260, extent=180, fill="#ffffff", outline="#edebda")
screen.create_arc(Lx1,Ly1,Lx1+11,Ly1+15, start=70, extent=180, fill="#ffcf70", outline="#ffcf70")
screen.create_arc(Lx2,Ly2,Lx2-13,Ly2+15, start=105, extent=180, fill="#ffffff", outline="#edebda")
screen.create_arc(Lx2-11,Ly2+15,Lx2,Ly2, start=290, extent=180, fill="#ffcf70", outline="#ffcf70")

