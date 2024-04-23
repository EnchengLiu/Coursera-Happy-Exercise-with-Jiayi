# %%
import pandas as pd
import matplotlib.pyplot as plt

def get_param_order(param_grid):
    param0 = [key for key, value in param_grid.items() if len(value) == 2]
    param1 = param_grid.keys() - param0
    return [param0[0],param1.pop()]

def unpack_gridsearch(gs,param_grid,folds):

    result = gs.cv_results_
    
    cols = ['mean_test_accuracy','mean_test_balanced_accuracy']
        
    param_order = get_param_order(param_grid)

    f0 = 'param_{}'.format(param_order[0])
    f1 = 'param_{}'.format(param_order[1])
    f0vals = param_grid[param_order[0]]
    f1vals = param_grid[param_order[1]]
    
    X = dict.fromkeys(f0vals)

    for f0val in f0vals:
        X[f0val] = pd.DataFrame(index=f1vals,columns=cols,dtype=float)

    for f0val in f0vals:
        for f1val in f1vals:
            ind = (result[f0]==f0val) & (result[f1]==f1val)
            for col in cols:
                X[f0val].loc[f1val,col] = float(result[col][ind][0])

    return X, gs.best_params_, gs.best_estimator_, gs.best_score_

def plot_grid_result(X,param_grid,log=True):

    param_order = get_param_order(param_grid)
    cols = ['mean_test_accuracy', 'mean_test_balanced_accuracy']
    labels = ['accuracy', 'balanced_accuracy']
    colors = ['r','b']
    linestyles = ['--', '-']

    f0vals = param_grid[param_order[0]]

    plt.figure(figsize=(14,7))
    for f0ind, f0val in enumerate(f0vals):
        for c, col in enumerate(cols):
            if log:
                plt.semilogx(X[f0val][col],color=colors[c],linestyle=linestyles[f0ind],marker='o',label='{} {}'.format(f0val,labels[c]))
            else:
                plt.plot(X[f0val][col],color=colors[c],linestyle=linestyles[f0ind],marker='o',label='{} {}'.format(f0val,labels[c]))
    plt.legend(fontsize=14)
    plt.grid(':')
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.show()