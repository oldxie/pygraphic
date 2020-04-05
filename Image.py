#coding=utf-8
from PIL import Image
import numpy as np
import random
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import sys
if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk

#import turtle
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.gridspec as gridspec
#plt.switch_backend('agg')
def destroy(e):
    sys.exit()  

class image:
    def __init__(self,width,hight,pdata=None):
        self.shape=(width,hight)
        self.result=[]
        self.result_beauty=[]
        self.imagelist=[]
        if len(pdata)>0:
            self.loaddata(pdata)
            #self.reshapeRGB(hight,width) 
    def loaddata(self,data): 
        if len(data) == self.shape[0]*self.shape[1]:
            self.data = data
            self.add_to_imagelist(data)
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
        value_p = value#/value.sum()*100
        beauty  = value*100#/value.sum()
        #while beauty.min()<10.0:
        #    for i,num in enumerate(list(beauty)):
        #        if num<10.0:
        #            beauty += [10.0,10.0,10.0,10.0]
            #beauty = beauty*100#/beauty.sum()
        
        self.result.append(value_p)
        self.result_beauty.append(beauty)

    def survey(self,G,draw_num,fig):
        labels = ['draw {num}'.format(num=i) for i in range(draw_num)]
        data=np.array(self.result)
        beauty_result=np.array(self.result_beauty)
        data_cum =beauty_result.cumsum(axis=1)
        category_colors = plt.get_cmap('RdYlGn')(
            np.linspace(0.15, 0.85, data.shape[1]))

        ax = fig.add_subplot(G[25:,:])
        ax.invert_yaxis()
        ax.xaxis.set_visible(False)
        limit=np.sum(beauty_result,axis=1).max()
        ax.set_xlim(0, limit)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        ax.spines['left'].set_visible(False)

        for i, (colname, color) in enumerate(zip(self.category, category_colors)):
            rel_val = data[:,i]
            widths = beauty_result[:,i]
            starts = data_cum[:,i] - widths
            
            ax.barh(labels, widths, left=starts, height=0.5,
                    label=colname, color=color)
            xcenters = starts + widths / 2
            r, g, b, _ = color
            text_color = 'white' if r * g * b < 0.5 else 'darkgrey'
            for y, (x, c, w) in enumerate(zip(xcenters, rel_val,widths)):
                rate=w/limit
                if rate<0.05:
                    p=0
                elif rate>0.05 and rate<0.1:
                    p='%.1f'%c
                else:
                    p='%.2f'%c
                ax.text(x, y,p, ha='center', va='center',
                        color=text_color,fontsize=8)
        ax.legend(ncol=len(self.category), bbox_to_anchor=(0, 1),
                  loc='lower left', fontsize='x-small')

        return ax
    def generate(self):
        self.reshapeRGB()
        return self.numpy
    def add_to_imagelist(self,cb):
        self.imagelist.append(self.generate())

    def update(self,n,im):
        im.set_data(self.imagelist[n])
        return im,     
    def print(self,draw_num):
        fig = plt.figure()
        G = gridspec.GridSpec(25+draw_num*2, 20)
        #self.reshapeRGB()
        plt.subplot(G[:20,:])
        plt.imshow(self.numpy)
        plt.axis('off') 
        self.survey(G,draw_num)
        plt.show()
    def printaction(self,draw_num):
        fig = plt.figure()
        G = gridspec.GridSpec(25+draw_num*2, 20)
        ax = plt.subplot(G[:20,:])
        im=ax.imshow(self.numpy)
        ax.axis('off') 
        ani=animation.FuncAnimation(fig, self.update, frames=np.arange(1, draw_num+1),fargs=(im,),interval=100, blit=False)
        self.survey(G,draw_num)
        plt.show()
    def printtk(self,draw_num):
        fig = plt.Figure()
        root = Tk.Tk()
        root.wm_title("Embedding in TK")
        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
        canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
        button = Tk.Button(master=root, text='Quit', command=sys.exit)
        button.pack(side=Tk.BOTTOM)
        G = gridspec.GridSpec(25+draw_num*2, 20)
        ax = fig.add_subplot(G[:20,:])
        im=ax.imshow(self.numpy)
        ax.axis('off') 
        self.survey(G,draw_num,fig)
        ani=animation.FuncAnimation(fig, self.update, frames=np.arange(1, draw_num+1),fargs=(im,),interval=100, blit=False)
        ani.save("dog.gif",writer='pillow')
        Tk.mainloop()

def init():
    #pass
    return im,               

def update(n,x):
    test=[]
    i=0
    print(x)
    while i<2500:
        test.append([random.randint(0,255),random.randint(0,255),random.randint(0,255)])
        #test.append([0,0,random.randint(0,255)])
        i+=1
    imag = image(50,50,test)
    im.set_data(imag.generate())
    return im,
if __name__=="__main__":
    i=0
    j=0
    test=[]
    imag = image(10,10,test)
    #fig, ax = plt.subplots()  
    while j<10:
        test=[]
        while i<100:
            test.append([random.randint(0,255),random.randint(0,255),random.randint(0,255)])
        #test.append([0,0,random.randint(0,255)])
            i+=1
        imag.loaddata(test)
        i=0
        j+=1
    #animation.FuncAnimation(fig, image.update, frames=np.arange(0, 10), blit=True)
    imag.printtk(9)
