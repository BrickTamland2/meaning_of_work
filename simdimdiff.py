
# debug: title of graph should inlude key name

# define similarity function for n dimensions

import matplotlib.pyplot as plt
from matplotlib.pyplot import cm
import pandas as pd
import numpy as np
from scipy.interpolate import interp1d


def simdim(models, keywords, key, *dims, trend=3, rangelow=1850, rangehigh=2000, rangestep=10):

    data = pd.DataFrame()
    data['year'] = range(rangelow, rangehigh, rangestep)

    for dim in dims:
        d = []
        for year, model in models.items():
            if year in range(rangelow, rangehigh, rangestep):
                d.append(model.n_similarity(keywords[key], keywords[dim]))
        data[dim] = d

    if len(dims)==2:
        data['diff'] = data.iloc[:, 1]-data.iloc[:, 2]

    # the trendline

    if trend == 3:

        x = data['year'].tolist()
        xnew = np.linspace(rangelow, (rangehigh - 10), 100)

        n = len(dims)
        colors = iter(cm.rainbow(np.linspace(0, 1, n)))

        y = data['diff'].tolist()
        fun = interp1d(x, y, kind='cubic')
        plt.plot(xnew, fun(xnew), "-", label='diff')
        plt.plot(x, y, 'o')



    elif trend == 2:

        n = len(dims)
        colors = iter(cm.rainbow(np.linspace(0, 1, n)))

        z = np.polyfit(data['year'], data['diff'], 2)
        p = np.poly1d(z)
        plt.plot(data['year'], p(data['year']), label='diff')


    elif trend == 1:

        n = len(dims)
        colors = iter(cm.rainbow(np.linspace(0, 1, n)))

        z = np.polyfit(data['year'], data['diff'], 1)
        p = np.poly1d(z)
        plt.plot(data['year'], p(data['year']), label='diff')


    #show plot
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.title(f'Association of dimension(s) with {key=}')
    plt.tight_layout()
    plt.show()
    plt.close()
