#coding=utf-8
from PIL import Image
import numpy as np
import random
#import turtle
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.gridspec as gridspec
#plt.switch_backend('agg')

class image:
    def __init__(self,width,hight,pdata=None):
        self.shape=(width,hight)
        self.result=[]
        self.result_beauty=[]
        
        if len(pdata)>0:
            self.loaddata(pdata)
            #self.reshapeRGB(hight,width) 
    def loaddata(self,data): 
        if len(data) == self.shape[0]*self.shape[1]:
            self.data = data
        else:
            print("data length cannot match the image shape\n image shape is :{wi}*{hi}\n but data length is {len}".format(wi=self.shape[0],hi=self.shape[1],len=len(data)))
         
    def reshapeRGB(self):
        x=self.shape[0]
        y=self.shape[0]
        ori=np.array(self.data)
        self.numpy=np.reshape(ori,(x,y,3))
        #print(np.shape(x))
    def anylyze(self,l):
        self.debug=l
        self.category=list(l.keys())
        result={}
        value = np.array(list(self.debug.values()))
        value_p = value/value.sum()*100
        beauty  = value/value.sum()*100
        while beauty.min()<10.0:
            for i,num in enumerate(list(beauty)):
                if num<10.0:
                    beauty += [10.0,10.0,10.0,10.0]
            beauty = beauty/beauty.sum()*100
        
        self.result.append(value_p)
        self.result_beauty.append(beauty)

    def survey(self,G,draw_num):
        labels = range(draw_num)
        data=np.array(self.result)
        beauty_result=np.array(self.result_beauty)
        data_cum =beauty_result.cumsum(axis=1)
        category_colors = plt.get_cmap('RdYlGn')(
            np.linspace(0.15, 0.85, data.shape[1]))

        ax = plt.subplot(G[25:,:])
        ax.invert_yaxis()
        ax.xaxis.set_visible(False)
        ax.set_xlim(0, np.sum(data,axis=1).max())

        for i, (colname, color) in enumerate(zip(self.category, category_colors)):
            rel_val = data[:,i]
            widths = beauty_result[:,i]
            starts = data_cum[:,i] - widths
            
            ax.barh(labels, widths, left=starts, height=0.5,
                    label=colname, color=color)
            xcenters = starts + widths / 2

            r, g, b, _ = color
            text_color = 'white' if r * g * b < 0.5 else 'darkgrey'
            for y, (x, c) in enumerate(zip(xcenters, rel_val)):
                ax.text(x, y, '%.2f'%c+'%', ha='center', va='center',
                        color=text_color,fontsize=8)
        ax.legend(ncol=len(self.category), bbox_to_anchor=(0, 1),
                  loc='lower left', fontsize='x-small')

        return ax

    def print(self,draw_num):
        fig = plt.figure()
        G = gridspec.GridSpec(25+draw_num*2, 20)
        self.reshapeRGB()
        plt.subplot(G[:20,:])
        plt.imshow(self.numpy)
        plt.axis('off') 
        self.survey(G,draw_num)
        #plt.legend()
        #plt.yticks([]) 
        plt.show()

    def export2ppm(self,file ):
        with open("images/{file}.ppm".format(file=file),"w") as ppmwrite:
            ppmwrite.write("P6\n")
            ppmwrite.write("{weight} {height}\n".format(weight=self.shape[0],height=self.shape[1]))
            ppmwrite.write("255\n")
        with open("images/{file}.ppm".format(file=file),"ab") as ppmwrite:
            for pixel in self.data:
                 #ppmwrite.write("{r} {g} {b}".format(r=str(pixel[0]),g=str(pixel[1]),b=str(pixel[2])))
                 ppmwrite.write(pixel[0].to_bytes(1,'little'))
                 ppmwrite.write(pixel[1].to_bytes(1,'little'))
                 ppmwrite.write(pixel[2].to_bytes(1,'little'))   
    def printaction(self,func,args,time):
        fig = plt.figure()
        image_ani,=plt.imshow(self.numpy)
        
        plt.axis('off') 
        ani = animation.FuncAnimation(fig, func, np.arange(0, 100), interval=100, blit=True)
        plt.show()

    def savejpg(self):
        self.export2ppm("temp")
        self.showjpgimage("temp")
                 
    def showjpgimage(self,file):
        img = Image.open("images/{file}.ppm".format(file=file))
        img.save("JPGimg/{file}.jpg".format(file=file))
        img.show()

if __name__=="__main__":
    
    test=[]
    i=0
    #turtle.colormode(255)
    while i<250000:
        test.append([random.randint(0,255),random.randint(0,255),random.randint(0,255)])
        #test.append([0,0,random.randint(0,255)])
        i+=1
    
    imag = image(500,500,test)
    #print(x.shape)
    imag.print()
    #print (x)