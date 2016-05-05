from itertools import cycle
import numpy as np
import matplotlib.pyplot as plt

def chunks(_list,size):
    '''Get Chunks of size size from a list _list '''
    for x in xrange(0, len(_list),size):
        yield _list[x:x+size]

def get_windows(no_of_sensors,no_of_cols,budget):    
    '''Get the window indices for each column/each time-stamp'''
    pool = cycle(range(0,no_of_sensors))

    final_list = []

    if budget == 0 :
        
        for _ in range(0,no_of_cols):
            final_list.append([])
            
        return final_list
    
    else:
        
        for _id,x in enumerate(pool):
            if _id == budget * no_of_cols:
                break
            final_list.append(x)

        return list(chunks(final_list, budget))

def mean_abs_error(actual_mat,pred_mat):
    '''Compute the mean absolute error'''
    diff_mat = np.subtract(actual_mat,pred_mat)
    diff_mat = np.fabs(diff_mat)
    
    total_cells = diff_mat.shape[0] * diff_mat.shape[1]
    
    mean_abs_error = float(np.sum(diff_mat))/ total_cells
    
    return mean_abs_error

def autolabel(rects,ax):
    #Courtesy : mathplotlib.org
    for rect in rects:
        height = rect.get_height()        
        
        ax.text(rect.get_x() + float(rect.get_width())/2., 1.09*height,
                '%f' % float(height),
                ha='center', va='bottom')

def top_k_indices(_list,k):
    '''Return the indices of top k elements of the list'''
    return sorted(range(len(_list)), key=lambda i: _list[i], reverse=True)[:k]

def plot(budgets,predictions):
    
    for k1 in predictions.keys(): 
                
        _list = []
        
        for k2,v in predictions[k1].items():
            if v!= []:
                _list.append(v)
                
        ax,rects1,rects2 = get_ax(_list[1],_list[0],budgets)

        autolabel(rects1,ax)
        autolabel(rects2,ax)
        
        plt.title(k1)
        
        plt.show()
