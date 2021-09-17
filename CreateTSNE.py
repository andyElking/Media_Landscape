import matplotlib.pyplot as plt
import os
import numpy as np
import pandas as pd
from sklearn.manifold import TSNE
import json
import seaborn as sns

sourceTitleList = ['HUFFINGTON POST', 'ECONOMIC TIMES', 'DAILY NEWS AND ANALYSIS (DNA)', 'HINDU', 'INDEPENDENT',
                   'DIE WELT', 'FINANCIAL TIMES (FT)', 'ABCNEWS.GO.COM', 'TIME.COM', 'SYDNEY MORNING HERALD',
                   'DAILY TELEGRAPH', 'MOSCOW TIMES', 'DAILY MAIL', 'BBC RADIO LINCOLNSHIRE', 'STERN MAGAZINE',
                   'BLOGS.WSJ.COM', 'EL MUNDO', 'GIZMODO.COM', 'GLOBE AND MAIL', 'BUSINESS INSIDER', 'THENEXTWEB.COM',
                   'ABC', 'WWW.THEGUARDIAN.COM', 'CNN EUROPE', 'BOSTON BUSINESS JOURNAL', 'ONLINE.WSJ.COM',
                   'WWW.FOXNEWS.COM', 'GIGAOM', 'USA TODAY SPORTS WEEKLY', 'WASHINGTON POST']


# sourceTitleList = ['356', '24', '3409', '1049', '440', '1633', '2482', '993', '36482', '736', '560', '653', '458', '1017', '330', '64', '649', '75', '249', '738', '2305', '377', '20', '1044', '77', '1233', '872', '1522', '44', '98']
# sourceTitleList = list(range(-15,15))

category_list = json.load(open('allCategoriesList.json'))

def PrintSourceTitleList(sourceInfoDir):
    ttlLst = list()
    for filename in os.listdir(sourceInfoDir):
        f = open(sourceInfoDir + "/" + filename)
        s: dict = json.load(f)
        ttlLst.append(s["sourceTitle"])
        f.close()
    print(ttlLst)


def ExtractFeatures(features: list, sourceInfoDir):
    xs = list()
    for sourceFileName in os.listdir(sourceInfoDir):
        f = open(sourceInfoDir + "/" + sourceFileName)
        source = json.load(f)
        srcCoords = list()
        for feature in features:
            srcCoords.append(source[feature])
        f.close()
        xs.append(srcCoords)

    xsNP = np.array(xs)

    return xsNP


def CreateTSNE(xsNP: np.array):
    xs_embedded = TSNE(n_iter=100000, n_iter_without_progress=1000, perplexity=5).fit_transform(xsNP)

    # with open('xs_embedded from TSNE.npy', 'rb') as fl:
    #     xs_embedded = np.load(fl)

    df = pd.DataFrame(xs_embedded, index=sourceTitleList)
    df = df.rename(columns={0: "X", 1: "Y"})
    plt.figure(figsize=(10, 10))
    sns.scatterplot(data=df, x='X',y='Y')
    for i in range(df.shape[0]):
        plt.annotate(text= df.index[i], xy= (df.X[i], df.Y[i]))
    plt.show()

arr = ExtractFeatures(category_list,"SourceInfo10000")

CreateTSNE(arr)

#PrintSourceTitleList('SourceInfo10000')