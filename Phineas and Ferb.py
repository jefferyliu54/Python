from tkinter import *
from random import *
myInterface = Tk()
screen = Canvas(myInterface, width=1000, height=700, background="#77DFF1")
screen.pack()

##CLOUDS

#right cloud
for clouds in range(1,26):
    x = randint(600,800)
    y = randint(0,40)
    sizeX = randint(40,60)
    sizeY = randint(20,40)
    screen.create_oval(x,y,x+sizeX,y+sizeY, fill="white", outline="white")
    y2 = randint(30,50)
    screen.create_oval(x,y2,x+sizeX,y2+sizeY, fill="#F7FDFF", outline="#F7FDFF")

#middle cloud
for clouds in range(1,8):
    x = randint(435,500)
    y = randint(75,100)
    sizeX = randint(40,60)
    sizeY = randint(20,40)
    screen.create_oval(x,y,x+sizeX,y+sizeY, fill="white", outline="white")
    y2 = randint(90,125)
    screen.create_oval(x,y2,x+sizeX,y2+sizeY, fill="#F7FDFF", outline="#F7FDFF")

#left cloud
for clouds in range(1,65):
    x = randint(0,250)
    y = randint(90,150)
    sizeX = randint(40,60)
    sizeY = randint(20,40)
    screen.create_oval(x,y,x+sizeX,y+sizeY, fill="white", outline="white")
    y2 = randint(130,200)
    screen.create_oval(x,y2,x+sizeX,y2+sizeY, fill="#F7FDFF", outline="#F7FDFF")

    
##FENCE
x = 0
y = 183
x2 = 75
y2 = 415
for fence in range(1,26):
    screen.create_rectangle(x,y,x2,y2, fill="#EDC69A", outline="black", width=2)
    fenceWidth = randint(62,75)
    x = x + fenceWidth
    x2 = x2 + fenceWidth
    y = randint(183,199)

#darker spots on fence 
for fenceSpots in range(1,25):
    x = randint(0,1000)
    y = randint(199,410)
    deltaX = randint(10,15)
    deltaY = randint(25,45)
    screen.create_rectangle(x,y,x+deltaX,y+deltaY, fill="#E0BF99", outline="#E0BF99")

    
##GRASS
screen.create_rectangle(0,415,1000,700, fill="#6CB06C", outline="#6CB06C")

#grass on lawn
for grass1 in range(1,18):
    x = randint(0,1000)
    y = randint(440,700)
    y2 = y - 16
    screen.create_line(x,y,x+3,y2,x+6,y,x+9,y2,x+12,y,x+15,y2,x+18,y,x+21,y2,x+24,y,x+27,y2,x+30,y, fill="#71D971", width=2, smooth="true")

#grass along fence
x = 0
for grass2 in range(1,700):
    y = randint(419,420)
    y2 = y - 19
    screen.create_line(x,y,x+4,y2,x+8,y, fill="black", width=2, smooth="true")
    x = x + 8

                       
##PHINEAS

#right eye
screen.create_polygon(736,288,746,262,761,255,766,254,771,253,784,257,788,275,783,285,778,292,759,300, fill="white", outline="black", width=2, smooth="true")
screen.create_oval(754,267,768,285, fill="#0D1D69", outline="#0D1D69")
screen.create_oval(762,271,765,274, fill="white", outline="white")

#hair
screen.create_polygon(872,232,857,221,834,212,859,210,866,214,861,207,854,200,849,196,829,185,847,187,854,189,866,197,876,211,
                      870,190,864,181,878,192,885,202,891,213,895,225,900,225,909,228,921,238,910,235,896,234,906,241,910,253,
                      892,242,895,243,892,242,897,245,895,258,891,251,877,237, fill="#FA5643", outline="#DE1D1D", width=2)

#head
screen.create_polygon(878,225,701,320,786,358,788,358,824,372,832,370,840,365,870,269,885,230, fill="#FFD4B0", outline="#DB9370", width=2)

#mouth
screen.create_line(773,354,801,353,826,328, fill="#DB9370", width=2, smooth="true")

#left eye
screen.create_polygon(765,288,775,262,790,255,795,254,800,253,813,257,817,275,812,285,807,292,788,300, fill="white", outline="black", width=2, smooth="true")
screen.create_oval(785,267,801,285, fill="#0D1D69", outline="#0D1D69")
screen.create_oval(795,271,798,274, fill="white", outline="white")

#freckles
screen.create_oval(857,243,861,246, fill="#DB9370", outline="#DB9370")
screen.create_oval(867,249,871,252, fill="#DB9370", outline="#DB9370")
screen.create_oval(871,235,875,238, fill="#DB9370", outline="#DB9370")

#ear
screen.create_arc(848,297,873,317, start=210, extent=270, fill="#FFD4B0", outline="#DB9370", width=2)
screen.create_rectangle(849,300,865,313, fill="#FFD4B0", outline="#FFD4B0")
screen.create_line(861,303,869,305,860,309,867,312,859,313, fill="#DB9370", width=2, smooth="true")

#legs
screen.create_polygon(816,522,815,533,814,551,819,553,823,551,824,533,825,525, fill="#FFD4B0", outline="#DB9370", width=2)
screen.create_polygon(851,525,850,536,850,550,855,552,859,550,859,536,860,526, fill="#FFD4B0", outline="#DB9370", width=2)

#right arm & hand
screen.create_polygon(806,420,806,421,794,482,805,499,812,500,806,475,805,475,802,475,814,420,814,421, fill="#FFD4B0", outline="#DB9370", width=2, smooth="true")
screen.create_line(808,493,804,493,802,482,802,481, fill="#DB9370", width=2, smooth="true")

#shorts
screen.create_polygon(809,475,807,518,806,523,817,525,834,525,837,527,870,527,874,522,871,470, fill="#553BFF", outline="#303030", width=2, smooth="true")
screen.create_line(836,526,832,524,833,510,832,508,821,502, fill="#303030", width=2, smooth="true")
screen.create_line(850,490,846,495,847,512,848,514,861,514,873,511, fill="#303030", width=2, smooth="true")
screen.create_line(847,501,848,503,861,503,873,500, fill="#303030", width=2, smooth="true")

#shirt stripes
screen.create_polygon(840,362,845,372,858,378,866,390,873,415,871,415,868,416,864,417,863,417,866,427,875,492,
                      874,485,868,494,809,494,805,485,804,492,813,421,812,422,808,422,803,421,802,417,801,418,
                      800,417,815,387,819,377,815,369,835,372, fill="#FF9945", outline="#FF9945", smooth="true")
screen.create_polygon(818,382,818,383,835,384,850,374,850,372,867,391,856,397,835,400,822,400,811,397,811,398, fill="blanchedalmond", outline="blanchedalmond", smooth="true")
screen.create_polygon(869,405,870,405,872,414,872,415,850,420,810,422,802,418,800,409,825,413,850,410, fill="blanchedalmond", outline="blanchedalmond", smooth="true")
screen.create_polygon(865,419,811,418,813,429,825,430,838,430,850,429,863,427, fill="blanchedalmond", outline="blanchedalmond")
screen.create_polygon(810,450,838,451,868,448,871,469,838,472,825,472,807,470, fill="blanchedalmond", outline="blanchedalmond")

#shirt outline
screen.create_polygon(840,362,845,372,858,378,866,390,873,415,871,415,868,416,864,417,863,417,866,427,875,492,
                      874,485,868,494,809,494,805,485,804,492,813,421,812,422,808,422,803,421,802,417,801,418,
                      800,417,815,387,819,377,815,369,835,372, fill="", outline="#303030", width=2, smooth="true")
screen.create_line(812,423,816,395, fill="#303030", width=2)
screen.create_line(863,417,855,420,844,419,844,418,845,392, fill="#303030", width=2, smooth="true")

#left arm & hand
screen.create_polygon(854,421,854,422,860,488,868,497,875,495,880,487,880,488,866,478,867,482,862,418,862,419, fill="#FFD4B0", outline="#DB9370", width=2, smooth="true")
screen.create_line(877,491,873,490,869,487, fill="#DB9370", width=2, smooth="true")
screen.create_line(874,495,867,490, fill="#DB9370", width=2, smooth="true")

#shoes
screen.create_polygon(815,550,815,551,820,553,824,550,824,551,823,564,822,565,804,568,805,567,800,561,795,561,805,558,814,560, fill="#553BFF", outline="#303030", width=2, smooth="true")
screen.create_polygon(787,567,788,564,795,560,800,561,805,569, fill="white", outline="#303030", width=2, smooth="true")
screen.create_polygon(787,566,787,568,798,569,823,564,823,565,823,569,823,570,798,574,787,571,787,572, fill="white", outline="#303030", width=2, smooth="true")
screen.create_polygon(802,558,809,564,817,562,812,559, fill="white", outline="#303030", width=2)

screen.create_polygon(850,550,850,551,855,553,859,550,859,551,859,564,858,565,840,568,841,567,836,561,831,561,841,558,850,560, fill="#553BFF", outline="#303030", width=2, smooth="true")
screen.create_polygon(823,567,824,564,831,560,836,561,841,569, fill="white", outline="#303030", width=2, smooth="true")
screen.create_polygon(823,566,823,568,834,569,859,564,859,565,859,569,859,570,834,574,823,571,823,572, fill="white", outline="#303030", width=2, smooth="true")
screen.create_polygon(838,558,845,564,853,562,848,559, fill="white", outline="#303030", width=2)


##FERB

#head
screen.create_polygon(569,145,569,146,647,153,647,154,630,392,630,393,586,392,586,393,582,354,584,350,579,350,574,349,576,344,580,338,583,336,582,304,571,305,
                      564,305,538,305,533,298,531,276,533,255,537,248,549,247,561,247,576,247,577,247, fill="#FFD4B0", outline="#DB9370", width=2, smooth="true")

#mouth
screen.create_line(581,350,587,350, fill="#DB9370", width=2)

#right eye
screen.create_oval(551,185,606,258, fill="white", outline="black", width=2) 
screen.create_oval(572,229,580,238, fill="#05124D", outline="#05124D")
#screen.create_oval(, fill="white", outline="white")

#nose
screen.create_polygon(544,247,556,247,571,247,588,246,589,246,588,255,544,255, fill="#FFD4B0", outline="#DB9370", width=2, smooth="true")
screen.create_polygon(541,249,553,249,571,249,588,249,588,250,588,259,544,259, fill="#FFD4B0", outline="#FFD4B0", width=2, smooth="true")

#left eye
screen.create_oval(583,205,629,264, fill="white", outline="black", width=2) 
screen.create_oval(602,230,610,239, fill="#05124D", outline="#05124D")
#screen.create_oval(, fill="white", outline="white")

#ear
screen.create_arc(613,266,650,287, start=270, extent=165, fill="#FFD4B0", outline="#DB9370", width=2)
screen.create_rectangle(614,268,636,285, fill="#FFD4B0", outline="#FFD4B0")
screen.create_line(638,272,646,274,639,277,644,280,637,282, fill="#DB9370", width=2, smooth="true")

#hair
screen.create_polygon(585,164,567,170,556,175,535,190,535,189,538,157,550,140,579,125,579,125,578,131,566,121,550,114,550,113,562,112,580,112,
                      613,119,629,128,625,132,628,130,630,122,640,114,640,115,638,123,638,132,638,136,640,133,647,132,663,132,679,134,679,135,
                      663,140,653,147,653,148,654,147,668,155,675,177,675,178,650,160,636,156,636,157,642,162,645,180,645,181,633,169,620,159,
                      620,160,613,161,588,177,588,178,604,153,604,154,601,161, fill="#1AAD26", outline="#0A7A13", width=2, smooth="true")

#right arm
screen.create_polygon(570,433,570,432,573,432,577,432,577,433,577,486,577,487,580,486,581,497,588,508,579,503,573,504,570,499,569,489,570,486, fill="#FFD4B0", outline="#DB9370", width=2, smooth="true")

#legs
screen.create_polygon(590,567,598,567,598,585,594,587,590,585, fill="#FFD4B0", outline="#DB9370", width=2) 
screen.create_polygon(620,567,628,567,628,585,624,587,620,585, fill="#FFD4B0", outline="#DB9370", width=2) 

#overalls/pants
screen.create_rectangle(578,430,643,511, fill="#710CB0", outline="#303030", width=2)
screen.create_arc(578,539,643,485, start=180, extent=180, fill="#710CB0", outline="#303030", width=2)
screen.create_polygon(579,519,602,529,601,539,599,569,586,569,587,537,586,519, fill="#710CB0", outline="#303030", width=2, smooth="true")
screen.create_polygon(642,519,619,529,618,539,616,569,629,569,630,537, fill="#710CB0", outline="#303030", width=2, smooth="true")
screen.create_arc(582,500,639,537, start=180, extent=180, fill="#710CB0", outline="#710CB0")
screen.create_rectangle(603,561,584,569, fill="#710CB0", outline="#303030", width=2)
screen.create_rectangle(613,561,633,569, fill="#710CB0", outline="#303030", width=2)

#shirt
screen.create_polygon(640,379,640,380,640,396,649,402,656,410,659,432,656,438,626,438,627,432,627,429,627,427,579,427,579,428,579,432,582,434,
                      561,434,560,431,564,408,575,395,581,379,581,380, fill="#FFFDD0", outline="#303030", width=2, smooth="true")
screen.create_line(627,428,624,406, fill="#303030", width=2)
screen.create_line(579,428,582,408, fill="#303030", width=2)

#shirt collar
screen.create_polygon(570,376,590,394,605,383,619,397,650,377, fill="white", outline="#303030", width=2)
screen.create_oval(601,392,609,400, fill="white", outline="light grey", width=2)

#top of overalls
screen.create_polygon(626,443,625,432,627,419,612,419,605,426,598,419,570,419,578,440, fill="#710CB0", outline="#303030", width=2)
screen.create_rectangle(580,440,641,513, fill="#710CB0", outline="#710CB0")
screen.create_rectangle(596,430,614,439, fill="#7794B5", outline="#303030", width=2)
screen.create_rectangle(578,430,589,439, fill="#7794B5", outline="#303030", width=2)
screen.create_rectangle(621,430,627,439, fill="#7794B5", outline="#303030", width=2)

#left arm
screen.create_polygon(639,440,639,439,642,439,646,439,646,440,646,493,646,494,649,493,650,504,657,515,648,520,642,518,639,509,637,496,639,493, fill="#FFD4B0", outline="#DB9370", width=2, smooth="true")
screen.create_line(652,517,649,509, fill="#DB9370", width=2)
screen.create_line(647,519,644,510, fill="#DB9370", width=2)

#shoes
screen.create_polygon(589,585,589,586,594,588,599,585,599,586,598,599,597,600,579,603,580,602,575,596,570,596,580,593,589,595, fill="white", outline="#303030", width=2, smooth="true")
screen.create_polygon(562,602,563,599,570,595,575,596,580,604, fill="white", outline="#303030", width=2, smooth="true")
screen.create_polygon(562,601,562,603,573,604,598,599,598,600,598,604,598,605,573,609,562,606,562,607, fill="white", outline="#303030", width=2, smooth="true")
screen.create_polygon(570,596,581,603,598,601,587,594, fill="#303030", outline="#303030")

screen.create_polygon(619,585,619,586,624,588,629,585,629,586,629,599,627,600,610,603,611,602,606,596,601,596,608,593,619,595, fill="white", outline="#303030", width=2, smooth="true")
screen.create_polygon(593,602,594,599,601,595,606,596,611,604, fill="white", outline="#303030", width=2, smooth="true")
screen.create_polygon(593,601,593,603,604,604,629,599,629,600,629,604,629,605,604,609,593,606,593,607, fill="white", outline="#303030", width=2, smooth="true")
screen.create_polygon(601,596,612,603,629,601,618,594, fill="#303030", outline="#303030")


##TEXT
screen.create_text(264,235, text="P H I N E A S", font="Calibri 75", fill="#FF0A0A")
screen.create_text(264,300, text="and", font="Calibri 50", fill="#FFC400")
screen.create_text(264,370, text="F E R B", font="Calibri 75", fill="#FF0A0A")
screen.create_text(264,435, text="By  Jeffery Liu", font="Calibri 18", fill="#303030")

screen.update()
