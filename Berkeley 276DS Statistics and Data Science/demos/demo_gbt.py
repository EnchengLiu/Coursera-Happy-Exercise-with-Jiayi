import numpy as np
import matplotlib.pyplot as plt
from itertools import islice
from sklearn.ensemble import GradientBoostingRegressor
import tkinter as tk
from BaseApp import BaseApp
import tkinter.ttk as ttk

np.random.seed(13)

class TkContainer(BaseApp):

    maxTrees = 500

    def __init__(self):
        super(TkContainer, self).__init__(
            title="Gradient boosted trees demo",
            geometry="1400x1000",
            figsize=(12,8),
            subplots=(3,1) )

    def add_widgets(self):

        self.slider_stage = self.get_scale(self.root,
                       variable=self.numtrees,
                       command=self.update_fig,
                       from_=0,
                       to=self.maxTrees,
                       resolution=1,
                       length=300,
                       text='Stage') \
            .pack(side=tk.TOP, fill=tk.X)

        f = ttk.Frame(self.root)
        f.pack(side=tk.TOP, fill=tk.Y)
        self.get_button(f,text="<",command=self.Rev_pressed).pack(side=tk.LEFT)
        self.get_button(f,text=">",command=self.Fwd_pressed).pack(side=tk.RIGHT)

    def Fwd_pressed(self):
        numtrees = self.numtrees.get()
        self.numtrees.set(min(self.maxTrees,numtrees+1))
        self.update_fig()

    def Rev_pressed(self):
        numtrees = self.numtrees.get()
        self.numtrees.set(max(0,numtrees-1))
        self.update_fig()    

    def initialize_parameters(self):
        self.numtrees = tk.IntVar(master=self.root, value=0)

    def format_text(self,mse):
        return 'MSE = {:.3f}'.format(mse)
    
    def initialize_data(self):

        # Continuous and data axes
        Ncont = 300
        Ndata = 40
        xcont = np.linspace(0.0, 10.0, Ncont,dtype=np.float32)
        Xcont = xcont[:, np.newaxis]

        Xdata = np.random.uniform(0.0, 10.0, size=Ndata)
        Xdata = Xdata.astype(np.float32)
        Xdata.sort()
        Xdata = Xdata.reshape(Ndata,1)

        # Generate the data
        ydata = Xdata[:,0]*np.sin(Xdata[:,0]) + np.sin(2*Xdata[:,0]) + 0.75 * np.random.normal(size=Ndata)
        ydata -= ydata.mean()

        # Train GBT
        gbr = GradientBoostingRegressor(n_estimators=self.maxTrees, 
                                        max_depth=1, 
                                        learning_rate=1.0).fit(Xdata, ydata)

        # Prediction generators
        ycont_gen = gbr.staged_predict(Xcont)
        ydata_gen = gbr.staged_predict(Xdata)

        # Store data
        self.xcont = xcont
        self.Xdata = Xdata
        self.ydata = ydata
        self.yhatcont = np.empty((Ncont,1+self.maxTrees))
        self.yhatdata = np.empty((Ndata,1+self.maxTrees))
        self.ytreecont = np.empty((Ncont,1+self.maxTrees))
        self.ytreecont[:] = np.NAN
        self.residual = np.empty((Ndata,1+self.maxTrees))
        self.mse = np.empty(1+self.maxTrees)

        self.yhatcont[:,0] = np.mean(ydata)*np.ones(Ncont)
        self.yhatdata[:,0] = np.mean(ydata)*np.ones(Ndata)
        self.residual[:,0] = ydata - self.yhatdata[:,0]
        self.mse[0] = np.mean((self.yhatdata[:,0]-ydata)**2)

        for numtrees in range(1,self.maxTrees+1):
            self.yhatcont[:,numtrees] = next(ycont_gen)
            self.yhatdata[:,numtrees] = next(ydata_gen)
            self.ytreecont[:,numtrees] = gbr.estimators_[numtrees-1,0].tree_.predict(Xcont)[:,0]
            self.residual[:,numtrees] = ydata - self.yhatdata[:,numtrees]
            self.mse[numtrees] = np.mean((self.yhatdata[:,numtrees]-ydata)**2)
            
    def initialize_fig(self):

        markersize=12
        fontsize=28
        linewidth=6

        self.ax[0].clear()
        self.ax[1].clear()

        numtrees = self.numtrees.get()

        ax = self.ax[0]
        self.stage_line = ax.plot(self.xcont,self.yhatcont[:,numtrees], 
                                  color='b',linewidth=linewidth,
                                  label='model')
        ax.plot(self.Xdata, self.ydata,'o',
                markersize=markersize,
                c='r',
                label='data')
        ax.grid()
        ax.set_xticks([0,2,4,6,8,10])
        ax.tick_params(axis='both', which='major', labelsize=28)
        ax.tick_params(axis='both', which='minor', labelsize=28)
        ax.spines[['top','right']].set_visible(False)
        ax.legend(fontsize=fontsize,loc='upper left')

        ax = self.ax[1]
        self.tree_line = ax.plot(self.xcont,self.ytreecont[:,numtrees] , 
                                 color='c',
                                 linewidth=linewidth,
                                label='last tree')
        self.residual_plot = ax.plot(self.Xdata, self.residual[:,numtrees],'o',
                                     markersize=markersize,
                                     c='m',
                                     label='residual')
        ax.grid()
        ax.set_xticks([0,2,4,6,8,10])
        ax.tick_params(axis='both', which='major', labelsize=28)
        ax.tick_params(axis='both', which='minor', labelsize=28)
        ax.spines[['top','right']].set_visible(False)
        ax.legend(fontsize=fontsize,loc='upper left')

        ax = self.ax[2]
        ax.semilogy(range(1+self.maxTrees),self.mse,'-',linewidth=4,color='green')
        self.mse_line = ax.plot(np.full(2,self.numtrees.get()),[0, self.mse[self.numtrees.get()]],
                                ':o',linewidth=5,color='r',markersize=16)
                
        ax.grid()
        ax.tick_params(axis='both', which='major', labelsize=28)
        ax.tick_params(axis='both', which='minor', labelsize=28)
        ax.spines[['top','right']].set_visible(False)
        ax.set_xlabel('Number of trees',fontsize=fontsize)
        ax.set_ylabel('MSE',fontsize=fontsize)
        self.error_text = ax.text(350,3,self.format_text(self.mse[numtrees]),fontsize=34)

    def update_fig(self,notused=None):
        numtrees = self.numtrees.get()
        self.residual_plot[0].set_ydata(self.residual[:,numtrees])
        self.tree_line[0].set_ydata(self.ytreecont[:,numtrees])
        self.stage_line[0].set_ydata(self.yhatcont[:,numtrees])
        self.mse_line[0].set_xdata(np.full(2,self.numtrees.get()))
        self.mse_line[0].set_ydata([0, self.mse[self.numtrees.get()]])
        self.error_text.set_text(self.format_text(self.mse[numtrees]))
        plt.draw()
        
if __name__ == "__main__":
    app = TkContainer()
    tk.mainloop()
