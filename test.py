import matplotlib.pyplot as plt
import os
import numpy as np
import pandas as pd
from sklearn.manifold import TSNE
import json
import seaborn as sns

# import numpy as np
# from sklearn.manifold import TSNE
# import matplotlib.pyplot as plt
# plt.style.use('seaborn-whitegrid')
#
# xs = np.array([[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 1], [1,1,1], [1,1,1]]*100)
# xs_embedded = TSNE(n_components=2).fit_transform(xs)
#
# X = list()
# Y = list()
# for x in xs_embedded:
#     X.append(x[0])
#     Y.append(x[1])
#
# plt.scatter(X,Y)
# plt.show()

sourceTitleList = ['HUFFINGTON POST', 'ECONOMIC TIMES', 'DAILY NEWS AND ANALYSIS (DNA)', 'HINDU', 'INDEPENDENT',
                   'DIE WELT', 'FINANCIAL TIMES (FT)', 'ABCNEWS.GO.COM', 'TIME.COM', 'SYDNEY MORNING HERALD',
                   'DAILY TELEGRAPH', 'MOSCOW TIMES', 'DAILY MAIL', 'BBC RADIO LINCOLNSHIRE', 'STERN MAGAZINE',
                   'BLOGS.WSJ.COM', 'EL MUNDO', 'GIZMODO.COM', 'GLOBE AND MAIL', 'BUSINESS INSIDER', 'THENEXTWEB.COM',
                   'ABC', 'WWW.THEGUARDIAN.COM', 'CNN EUROPE', 'BOSTON BUSINESS JOURNAL', 'ONLINE.WSJ.COM',
                   'WWW.FOXNEWS.COM', 'GIGAOM', 'USA TODAY SPORTS WEEKLY', 'WASHINGTON POST']


with open('xs_embedded from TSNE.npy', 'rb') as fl:
    xs_embedded = np.load(fl)
print(xs_embedded)
df = pd.DataFrame(xs_embedded, index=sourceTitleList)
df = df.rename(columns={0 : "X", 1 : "Y"})
print(df.head())