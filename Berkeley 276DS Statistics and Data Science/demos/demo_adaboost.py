import numpy as np
import matplotlib.pyplot as plt
from itertools import islice
from sklearn.datasets import make_gaussian_quantiles, make_moons
import tkinter as tk
from BaseApp import BaseApp
import tkinter.ttk as ttk

np.random.seed(13)

def plot_db_stage(ax,model,X,y,m,xx,yy,plot_type):

    ax[0].clear()
    ax[1].clear()

    if m==0:
        
        idx = y==1
        ax[0].scatter(X[idx, 0],X[idx, 1],marker='x',c='g',s=30,edgecolors=None)

        idx = y==-1
        ax[0].scatter(X[idx, 0],X[idx, 1],marker='o',c='r',s=30,edgecolors=None)

    else:

        # plot background
        if plot_type=='class':
            Z = model.predict(np.c_[xx.ravel(), yy.ravel()], m=m)
        else:
            Z = model.predict_proba(np.c_[xx.ravel(), yy.ravel()], m=m)

        Z = Z.reshape(xx.shape)

        # DB ---------------------------------------------------------
        yhat_model = model.predict(X,m=m)

        ax[0].contourf(xx, yy, Z, cmap=plt.cm.RdYlGn, alpha=0.2)

        # TN
        idx = np.logical_and(y==-1,yhat_model==-1)
        if any(idx):
            ax[0].scatter(X[idx, 0],X[idx, 1],marker='o',c='r',s=50,edgecolors=None)

        # FP
        idx = np.logical_and(y==-1,yhat_model==1)
        if any(idx):
            ax[0].scatter(X[idx, 0],X[idx, 1],marker='o',c='m',s=50,edgecolors=None)

        # TP
        idx = np.logical_and(y==1,yhat_model==1)
        if any(idx):
            ax[0].scatter(X[idx, 0],X[idx, 1],marker='x',c='g',s=50,edgecolors=None)

        # FN
        idx = np.logical_and(y==1,yhat_model==-1)
        if any(idx):
            ax[0].scatter(X[idx, 0],X[idx, 1],marker='x',c='b',s=50,edgecolors=None)

    ax[0].set_xlim(-5, 9)
    ax[0].set_ylim(-5, 9)
    ax[0].set_xticks([])
    ax[0].set_yticks([])
    ax[0].spines[:].set_visible(False)

    # STAGE -------------------------------------------------
    h = model.stumps[m]
    yhat_stump = h.predict(X)

    w = model.whats[m,:]
    w /= w.max()

    # TN
    idx = np.logical_and(y==-1,yhat_stump==-1)
    if any(idx):
        ax[1].scatter(X[idx, 0],X[idx, 1],marker='o',c='r',s=50,alpha=w[idx],edgecolors=None)

    # FP
    idx = np.logical_and(y==-1,yhat_stump==1)
    if any(idx):
        ax[1].scatter(X[idx, 0],X[idx, 1],marker='o',c='m',s=50,alpha=w[idx],edgecolors=None)

    # TP
    idx = np.logical_and(y==1,yhat_stump==1)
    if any(idx):
        ax[1].scatter(X[idx, 0],X[idx, 1],marker='x',c='g',s=50,alpha=w[idx],edgecolors=None)

    # FN
    idx = np.logical_and(y==1,yhat_stump==-1)
    if any(idx):
        ax[1].scatter(X[idx, 0],X[idx, 1],marker='x',c='c',s=50,alpha=w[idx],edgecolors=None)

    if h.d==0:
        ax[1].axvline(h.threshold,c='k')
    else:
        ax[1].axhline(h.threshold,c='k')

    ax[1].text(-5,6,'$\epsilon$ = {:.2f}'.format(sum(y!=yhat_stump)/len(y)),fontsize=36)

    ax[1].set_xlim(-5, 9)
    ax[1].set_ylim(-5, 9)
    ax[1].set_xticks([])
    ax[1].set_yticks([])
    ax[1].spines[:].set_visible(False)

def get_data(datatype,N_per_class, plot_step):
        
        if datatype=='gaussian_quantiles':
            X1, y1 = make_gaussian_quantiles(cov=2.0, n_samples=N_per_class, n_features=2, n_classes=2, random_state=1 )
            X2, y2 = make_gaussian_quantiles(mean=(3, 3), cov=1.5, n_samples=N_per_class, n_features=2, n_classes=2, random_state=1 )
            y1[y1==0] = -1
            y2[y2==0]=-1
            X = np.concatenate((X1, X2))
            y = np.concatenate((y1, -y2))

        elif datatype=='moons': 
            X, y = make_moons(n_samples=2*N_per_class,noise = .2, random_state=1)
            y[y==0]=-1
            X *= 4
        x_min, x_max = X[:, 0].min() - 2, X[:, 0].max() + 2
        y_min, y_max = X[:, 1].min() - 2, X[:, 1].max() + 2
        xx, yy = np.meshgrid(
            np.arange(x_min, x_max, plot_step), np.arange(y_min, y_max, plot_step)
        )

        return X, y, xx, yy

class Stump:

    def __init__(self):
        self.polarity = 1
        self.d = None      # feature index
        self.threshold = None

    def fit(self, X, y, w):

        N, D = X.shape

        min_error = np.inf
        for d in range(D):
            Xd = X[:, d]
            Xsorted = np.sort(np.unique(Xd))

            for i in range(len(Xsorted)-1):

                threshold =  (Xsorted[i] +  Xsorted[i+1])/2
                
                yhat = np.ones(N)
                yhat[Xd < threshold] = -1

                # Error = Weight of misclassified samples
                epsilon = sum(w[y!=yhat])

                if epsilon < 0.5:
                    p = 1
                else:
                    p = -1
                    epsilon = 1 - epsilon

                # store the best configuration
                if epsilon < min_error:
                    self.polarity = p
                    self.threshold = threshold
                    self.d = d
                    min_error = epsilon

        return self

    def predict(self, X):
        N = X.shape[0]
        X_column = X[:, self.d]
        yhat = np.ones(N)
        if self.polarity == 1:
            yhat[X_column < self.threshold] = -1
        else:
            yhat[X_column >= self.threshold] = -1

        return yhat

class Adaboost:

    def __init__(self, M=5):
        self.M = M
        self.alpha = np.empty(M,dtype=float)
        self.epsilon = np.empty(M,dtype=float)
        
        self.stumps = []
        self.whats = []

    def fit(self, X, y):
        N, D = X.shape
        self.whats = np.empty((self.M+1,N))
        self.stumps = []

        self.H = np.zeros((self.M+1,N))


        for m in range(self.M):
            
            # update weights
            if m==0:
                self.whats[m,:] = np.ones(N)
            else:
                self.whats[m,misclass]  = self.whats[m-1,misclass] * np.exp(self.alpha[m-1]) 
                self.whats[m,~misclass] = self.whats[m-1,~misclass] * np.exp(-self.alpha[m-1]) 
                
            # normalize weights
            w = self.whats[m,:] / sum(self.whats[m,:])

            # train decision stump
            h = Stump().fit(X, y, w)
            self.stumps.append(h)

            # compute misclassification error
            yhat = h.predict(X)
            misclass = yhat != y
            self.epsilon[m] = sum(w[misclass])

            # compute step size
            self.alpha[m] = 0.5 * np.log((1.0 - self.epsilon[m]) / self.epsilon[m])

            # self.H[m+1,:] = self.H[m,:] + self.alpha[m] * yhat

    def predict(self, X, m=None):
        return np.sign(self.predict_proba(X, m))

    def predict_proba(self, X, m=None):
        if m==None:
            m=len(self.stumps)
        return sum([self.alpha[mu]*self.stumps[mu].predict(X) for mu in range(m)])
        # return self.H[m,:]
       
class TkContainer(BaseApp):
    
    plot_types = ['probability','class']
    data_types = ['gaussian_quantiles','moons']
    maxTrees = 100
    plot_step = 0.05
    N_per_class = 100

    def __init__(self):
        super(TkContainer, self).__init__(
            title="Adaboost demo",
            geometry="1500x500",
            figsize=(12, 4),
            subplots=(1,2) )

    def initialize_parameters(self):
        self.numtrees = tk.IntVar(master=self.root, value=0)
        self.plot_type = tk.StringVar(master=self.root, value='class')
        self.data_type = tk.StringVar(master=self.root, value='moons')

    def initialize_data(self):
        self.X, self.y, self.xx, self.yy = get_data(self.data_type.get(),self.N_per_class, self.plot_step)
        self.model = Adaboost(M=self.maxTrees)
        self.model.fit(self.X, self.y)

    def add_widgets(self):

		# select data type combo box ........................................
        self.get_combobox(self.root,
						  	text='Data',
							textvariable = self.data_type,
							values = self.data_types,
							command = self.select_data_type)\
			.pack(side=tk.TOP, fill=tk.X)
        

		# select plot type combo box ........................................
        self.get_combobox(self.root,
						  	text='Plot',
							textvariable = self.plot_type,
							values = self.plot_types,
							command = self.select_plot_type)\
			.pack(side=tk.TOP, fill=tk.X)


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

        
    def initialize_fig(self):
        plot_db_stage(self.ax,self.model,
                      self.X,self.y,self.numtrees.get(),
                      self.xx,self.yy,
                      plot_type=self.plot_type.get())

    def update_fig(self,notused=None):
        plot_db_stage(self.ax,self.model,
                      self.X,self.y,
                      self.numtrees.get(),
                      self.xx,self.yy,
                      plot_type=self.plot_type.get())
        plt.draw()
        
    def Fwd_pressed(self):
        numtrees = self.numtrees.get()
        self.numtrees.set(min(self.maxTrees-1,numtrees+1))
        self.update_fig()

    def Rev_pressed(self):
        numtrees = self.numtrees.get()
        self.numtrees.set(max(0,numtrees-1))
        self.update_fig()
        
    def select_plot_type(self,event):
        plot_db_stage(self.ax,self.model,
                        self.X,self.y,self.numtrees.get(),
                        self.xx,self.yy,
                        plot_type=self.plot_type.get())
        plt.draw()
        
    def select_data_type(self,event):

        self.initialize_data()
        self.numtrees.set(0)

        plot_db_stage(self.ax,self.model,
                        self.X,self.y,self.numtrees.get(),
                        self.xx,self.yy,
                        plot_type=self.plot_type.get())
        plt.draw()

    def format_text(self,y,yhat):
        return'$\epsilon$ = {:.2f}'.format(sum(y!=yhat)/len(y))
    
if __name__ == "__main__":
    app = TkContainer()
    tk.mainloop()