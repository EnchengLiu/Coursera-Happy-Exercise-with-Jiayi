import numpy as np
import matplotlib.pyplot as plt
from BaseApp import BaseApp
import tkinter as tk
from matplotlib.colors import ListedColormap
from sklearn.svm import SVC
from sklearn.datasets import make_classification, make_circles, make_moons

def sampleit(N,noise,dist):
    D = 2
    K = 2
    X = np.zeros((N*K,D)) # data matrix (each row = single example)
    y = np.zeros(N*K) # class labels

    print(noise)
    if dist=='spiral':
        for j in range(K):
            ix = range(N*j,N*(j+1))
            r = np.linspace(0.0,1,N) # radius
            t = np.linspace(j*4,(j+1)*4,N) + np.random.randn(N)*noise # theta
            X[ix] = np.c_[r*np.sin(t), r*np.cos(t)]
            y[ix] = j
    elif dist=='circles':
        X, y = make_circles(n_samples=N*K, noise=noise)
    elif dist=='moons':
        X, y = make_moons(n_samples=N*K,noise=noise)    
    else:
        print("ERROR")

    x0min = X[:,0].min()
    x0max = X[:,0].max()
    d = x0max-x0min
    x0min -= 0.2*d
    x0max += 0.2*d

    x1min = X[:,1].min()
    x1max = X[:,1].max()
    d = x1max-x1min
    x1min -= 0.2*d
    x1max += 0.2*d

    d0_grid, d1_grid = np.meshgrid(np.arange(x0min, x0max, 0.02), np.arange(x1min, x1max, 0.01))
    X0 = d0_grid.ravel()
    X1 = d1_grid.ravel()
    gridshape = d0_grid.shape
    d01_array = np.empty((len(X0),2))
    d01_array[:,0] = X0
    d01_array[:,1] = X1
    
    return X, y, d0_grid, d1_grid, gridshape, d01_array, x0min, x0max, x1min, x1max

def train_model(kernel, C, gamma, degree, Xtrain, ytrain, d12_array, gridshape):
    if kernel=='poly':
        model = SVC(kernel=kernel,C=C,gamma=gamma,degree=degree)
    else:
        model = SVC(kernel=kernel,C=C,gamma=gamma)
        
    model = model.fit(Xtrain, ytrain)
    y_array = model.predict(d12_array)
    y_grid = y_array.reshape(gridshape)
    return model, y_grid

class TkContainer(BaseApp):

    distribution_values = ['spiral','circles','moons']
    degree_values = ['2','3','4','5','6','7','8']
    kernel_values = ['linear', 'poly', 'rbf', 'sigmoid']
    colormap = {0:'black', 1:'red', 2:'blue'}
    bkgrnd_colors = ListedColormap(['#8c8c8c', '#e68e8e', '#e68482'])

    def __init__(self):
        super(TkContainer, self).__init__(
            title="Support Vector Classifier 2D",
            geometry="1300x800",
            figsize=(3, 3),
            subplots=None )
        
    def initialize_data(self):
        N = int(self.Nstr.get())
        noise = float(self.noisestr.get())
        self.X, self.y, self.d0_grid, self.d1_grid, self.gridshape, self.d01_array, self.x0min, self.x0max, self.x1min, self.x1max = sampleit(N,noise,self.distribution_str.get())
        self.scatter_colors_train = [self.colormap[yy] for yy in self.y]

    def initialize_parameters(self):
        self.Nstr = tk.StringVar(master=self.root,value='40')
        self.noisestr = tk.DoubleVar(master=self.root,value='0.5')
        self.distribution_str = tk.StringVar(master=self.root,value=self.distribution_values[0])
        self.kernel_str = tk.StringVar(master=self.root,value=self.kernel_values[0])
        self.C = tk.DoubleVar(master=self.root, value=1)
        self.gamma = tk.DoubleVar(master=self.root, value=0.5)
        self.show_model_bool = tk.BooleanVar(master=self.root, value=False)
        self.degree_str = tk.StringVar(master=self.root,value=self.degree_values[0])

    def add_widgets(self):
        
        header_width = 30

        # Header ------------------------------------------
        self.get_header(self.root,text='Data',char='.',width=header_width)\
            .pack(side=tk.TOP, fill=tk.X)
        
        self.get_combobox(self.root,
                          text='Distribution',
                          textvariable=self.distribution_str,
                          values=self.distribution_values,
                          command=self.update_data)\
            .pack(side=tk.TOP)
        
        self.get_entry_label(self.root,
                        text='samples per class',
                        textvariable=self.Nstr,
                        validatecommand=self.update_data)\
            .pack(side=tk.TOP, fill=tk.X)
        
        self.get_entry_label(self.root,
                        text='noise',
                        textvariable=self.noisestr,
                        validatecommand=self.update_data)\
            .pack(side=tk.TOP, fill=tk.X)


        self.get_button(self.root,text="Resample",command=self.update_data)\
            .pack(side=tk.TOP, fill=tk.X)
        
        # Header ------------------------------------------
        self.get_header(self.root,text='Model',char='.',width=header_width)\
            .pack(side=tk.TOP, fill=tk.X)
        
        self.get_checkbox(self.root, text='Show model',variable=self.show_model_bool, command=self.show_model)\
            .pack(side=tk.TOP, fill=tk.X)

        self.get_combobox(self.root,
                          text='Kernel',
                          textvariable=self.kernel_str,
                          values=self.kernel_values,
                          command=self.update_kernel)\
            .pack(side=tk.TOP)
        
        self.get_scale(self.root,
                        variable=self.C,
                        command=self.update_kernel,
                        from_=0.0,
                        to= 3.0,
                        resolution=.01,
                        length=300,
                        text='C    ') \
            .pack(side=tk.TOP)
        
        self.get_scale(self.root,
                        variable=self.gamma,
                        command=self.update_kernel,
                        from_=0.0,
                        to= 3.0,
                        resolution=.01,
                        length=300,
                        text='gamma') \
            .pack(side=tk.TOP)
        

        self.get_combobox(self.root,
                          text='Poly degree',
                          textvariable=self.degree_str,
                          values=self.degree_values,
                          command=self.update_kernel)\
            .pack(side=tk.TOP)
        

        
    def initialize_fig(self):
        ax = self.ax
        self.scatter = ax.scatter(self.X[:, 0], self.X[:, 1], c=self.scatter_colors_train, s=100)
        ax.set_xlim(self.x0min,self.x0max)
        ax.set_ylim(self.x1min,self.x1max)
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
        ax.spines[:].set_visible(False)

    def update_data(self,notused=None):
        N = int(self.Nstr.get())
        noise = float(self.noisestr.get())
        self.X, self.y, self.d0_grid, self.d1_grid, self.gridshape, self.d01_array, self.x0min, self.x0max, self.x1min, self.x1max  = sampleit(N,noise,self.distribution_str.get())
        self.scatter_colors_train = [self.colormap[yy] for yy in self.y]
        ax = self.ax
        self.scatter.remove()
        self.scatter = ax.scatter(self.X[:, 0], self.X[:, 1], c=self.scatter_colors_train, s=100)
        self.update_kernel()

    def show_model(self):
        if self.show_model_bool.get():
            self.update_kernel(None)
        else:
            for col in self.contour.collections:
                col.remove()
            del self.contour
        plt.draw()

    def update_kernel(self,notused=None):
        
        self.model, y_grid = train_model(self.kernel_str.get(), 
                                         self.C.get(),
                                         self.gamma.get(),
                                         int(self.degree_str.get()),
                                         self.X, 
                                        self.y, 
                                        self.d01_array, 
                                        self.gridshape)
        
        if 'contour' in dir(self):
            for col in self.contour.collections:
                col.remove()

        if self.show_model_bool.get():
            self.contour = self.ax.contourf(self.d0_grid, self.d1_grid, y_grid, cmap=self.bkgrnd_colors,alpha=0.3)
        self.ax.set_xlim(self.x0min,self.x0max)
        self.ax.set_ylim(self.x1min,self.x1max)

        plt.draw()

####################################################
if __name__ == "__main__":
    app = TkContainer()
    tk.mainloop()
