import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import tkinter as tk
from BaseApp import BaseApp
from sklearn import svm

class TkContainer(BaseApp):

    theta0_init, theta1_init = 0, 1
    theta0, theta1 = None, None
    stddev, showmodel, DE = None, None, None
    line_model, marker_model, txt = None, None, None
    line_db, marker_db, marker_P = None, None, None
    marker_N, line_xi = None, None

    def __init__(self):
        super(TkContainer, self).__init__(
            title="SVM demo",
            geometry="1500x600",
            figsize=(12, 4),
            subplots=None )
        self.update()

    def initialize_parameters(self):
        self.theta0 = tk.DoubleVar(master=self.root,value=0.0)
        self.theta1 = tk.DoubleVar(master=self.root,value=1.0)
        self.stddev = tk.DoubleVar(master=self.root, value=1.0)
        self.stddevstr = tk.StringVar(master=self.root, value='1.0')
        self.showmodel = tk.BooleanVar(master=self.root,value=False)

    def initialize_data(self):
        self.DE = DataAndEstimate(self,self.stddev.get())

    def add_widgets(self):

        # theta0 scale ..............................................
        self.get_scale(self.root,
                 variable=self.theta0,
                 command=self.update,
                 from_=-4,
                 to=4,
                 length=300,
                 resolution=.05,
                 text='theta0')\
            .pack(side=tk.TOP)

        # theta1 scale ..............................................
        self.get_scale(self.root,
                 variable=self.theta1,
                 command=self.update,
                 from_=-10,
                 to=10,
                 length=300,
                 resolution=.05,
                 text='theta1')\
            .pack(side=tk.TOP)

        # resample button ..............................................
        self.get_button(self.root, text="Resample", command=self.resample) \
            .pack(side=tk.TOP, fill=tk.X)

        # stddev ..............................................
        self.get_entry_label(self.root,
                        text="stddev",
                        textvariable=self.stddevstr,
                        validatecommand=self.set_stddev)\
            .pack(side=tk.TOP, fill=tk.X)

        # show solution ..............................................
        self.get_checkbox(self.root, text='Show solution', variable=self.showmodel,
                          command=self.showmodel_clicked) \
            .pack(side=tk.TOP, fill=tk.X)

    def initialize_fig(self):

        DE=self.DE
        theta0 = self.theta0_init
        theta1 = self.theta1_init

        self.ax.clear()

        self.line_model = plt.plot(DE.xx, DE.model_th0 + DE.model_th1 * DE.xx,
                                   color='magenta',
                                   alpha=0.5,
                                   linewidth=3)
        self.marker_model = plt.plot(-DE.model_th0 / DE.model_th1, 0, 'o',
                                     color='magenta',
                                     alpha=0.5,
                                     markersize=20)

        self.line_model[0].set_visible(self.showmodel.get())
        self.marker_model[0].set_visible(self.showmodel.get())

        self.txt = plt.text(0.2, 0.8, self.format_string(),
                       horizontalalignment='right',
                       verticalalignment='center',
                       transform=self.ax.transAxes,
                       fontsize=30)

        self.line_db = plt.plot(DE.xx, theta0 + theta1 * DE.xx, 'k', linewidth=2)
        self.marker_db = plt.plot(-theta0 / theta1, 0, 'ko', markersize=20)
        self.marker_P = plt.plot(DE.x[DE.indP], DE.y[DE.indP] - DE.xi[DE.indP],
                                 'gx',
                                 markersize=8,
                                 markeredgewidth=2)
        self.marker_N = plt.plot(DE.x[DE.indN], DE.y[DE.indN] + DE.xi[DE.indN],
                                 'ro',
                                 markersize=8,
                                 markeredgewidth=2,
                                 markerfacecolor='none')
        self.line_xi = []
        for i in range(len(DE.x)):
            if DE.y[i] == 1:
                line = plt.plot((DE.x[i], DE.x[i]), (DE.y[i] - DE.xi[i], 1.0), 'g', linewidth=5)
                self.line_xi.append(line[0])
            else:
                line = plt.plot((DE.x[i], DE.x[i]), (-1.0, DE.y[i] + DE.xi[i]), 'r', linewidth=5)
                self.line_xi.append(line[0])

        plt.xticks([])
        plt.yticks([-1, 0, 1], fontsize=0)
        plt.grid(':')
        plt.ylim(-3,5)

    def update(self,notused=None):

        if np.isclose(self.theta1.get(),0.0):
            self.theta1.set(1e-4)
        self.DE.update_estimate()
        self.update_fig()

    def update_fig(self):

        DE = self.DE

        theta0 = self.theta0.get()
        theta1 = self.theta1.get()

        self.txt.set_text(self.format_string())
        self.line_db[0].set_ydata(theta0 + theta1 * DE.xx)
        self.marker_db[0].set_xdata([-theta0 / theta1])
        self.marker_P[0].set_ydata(DE.y[DE.indP] - DE.xi[DE.indP])
        self.marker_N[0].set_ydata(DE.y[DE.indN] + DE.xi[DE.indN])
        for i in range(len(DE.x)):
            if DE.y[i] == 1:
                self.line_xi[i].set_ydata((DE.y[i] - DE.xi[i], 1.0))
            else:
                self.line_xi[i].set_ydata((-1.0, DE.y[i] + DE.xi[i]))

        plt.draw()

    def resample(self):
        self.DE = DataAndEstimate(self,self.stddev.get())
        self.initialize_fig()
        self.update()

        self.update(None)

    def set_stddev(self):
        try:
            self.stddev.set(float(self.stddevstr.get()))
            self.resample()
            return True
        except ValueError:
            return

    def showmodel_clicked(self):
        self.line_model[0].set_visible(self.showmodel.get())
        self.marker_model[0].set_visible(self.showmodel.get())
        plt.draw()

    def format_string(self):
        C = self.DE.C
        xi = self.DE.xi
        model_J = self.DE.model_J
        theta1 = self.theta1.get()

        return '|theta1|={:.2f}\nsum(xi)={:.2f}\nJ={:.2f}\nJ*={:.2f}'.format(
            abs(theta1), xi.sum(), abs(theta1) + C * xi.sum(), model_J)

class DataAndEstimate:

    C = 1
    muN = -1
    muP = 1
    N = 20

    def __init__(self, myapp, stddev):
        self.app = myapp

        self.xN = stats.norm(loc=self.muN,scale=stddev).rvs(self.N)
        self.xP = stats.norm(loc=self.muP,scale=stddev).rvs(self.N)
        self.x = np.concatenate((self.xN, self.xP))
        self.y = np.concatenate((-1 * np.ones(self.N), np.ones(self.N)))

        self.model = svm.LinearSVC(C=self.C,loss='hinge').fit(self.x[:, np.newaxis], self.y)

        self.model_th0 = self.model.intercept_[0]
        self.model_th1 = self.model.coef_[0, 0]
        self.model_alpha = self.model_th0 + self.model_th1 * self.x
        self.model_xi = np.maximum(0, 1 - self.y * self.model_alpha)
        self.model_J = abs(self.model_th1) + self.C * self.model_xi.sum()

        self.xx = np.linspace(min(self.x), max(self.x))

        ind = np.argsort(self.x)
        self.x = self.x[ind]
        self.y = self.y[ind]

        self.indP = self.y == 1
        self.indN = self.y == -1

        self.alpha = np.empty(self.x.shape)
        self.xi = np.empty(self.x.shape)

    def update_estimate(self):
        theta0 = self.app.theta0.get()
        theta1 = self.app.theta1.get()
        self.alpha = theta0+ theta1 * self.x
        self.xi = np.maximum(0, 1 - self.y * self.alpha)

if __name__ == "__main__":
    app = TkContainer()
    tk.mainloop()
