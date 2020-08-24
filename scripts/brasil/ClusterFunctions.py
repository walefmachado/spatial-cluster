# para agrupamento - K-médias
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.spatial.distance import pdist
from scipy.cluster.hierarchy import cut_tree
from sklearn.cluster import KMeans
%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
# número de recursão
#import sys
# print(sys.getrecursionlimit())
#sys.setrecursionlimit(4000)

class ClusterFunctions:
    from scipy.cluster.hierarchy import dendrogram, linkage
    from scipy.spatial.distance import pdist
    from scipy.cluster.hierarchy import cut_tree
    from sklearn.cluster import KMeans
    %matplotlib inline
    import matplotlib.pyplot as plt
    import numpy as np
    def __init__(self):
        self.X = X
    def Dendrograma(self, X):
    # subselecionar variáveis
    # X = dados_cluster.drop(['nome_mun', 'geometry'], axis=1)
    # transformar em matriz (necessário para gerar o gráfico)
        XX = X.values
        # mudar o tipo dos dados
        XX = np.asarray(XX, dtype=float)
        n = XX.shape[0]
        p = XX.shape[1]
        # vetor de médias
        Xb = np.mean(XX, axis=0)
        # matriz de covariâncias
        S = np.cov(XX.T)
        # matriz de somas de quadrados e produtos
        W = (n - 1) * S

        Z = linkage(X, method='ward')

        max_d = 0
        grupos = cut_tree(Z, height=max_d)

        # Dendrograma 
        fig, ax = plt.subplots(figsize=(15, 7))
        ax = dendrogram(
            Z,
            truncate_mode='lastp',  # mostrar apenas os p últimos grupos formados
            p=5,  # quantos passos mostrar
            show_leaf_counts=True,  # mostrar quantas observações há em cada grupo entre parênteses
            leaf_rotation=90., # rotação
            leaf_font_size=10., # tamanho da fonte
            labels=dados.index, # rótulos do eixo x
            show_contracted=True,  # to get a distribution impression in truncated branches,
            above_threshold_color='black',
            color_threshold=0.1, # para que todas as linhas sejam da mesma cor
            # color_threshold=max_d, # para que os grupos fiquem com cores diferentes
        )
        plt.axhline(y=max_d, c='grey', lw=1, linestyle='dashed')
        plt.xlabel('município')
        plt.ylabel('distância');
        return ax

#Z = linkage(X, method='ward')

## definir a distância de corte baseando no dendrograma
#max_d = 2e8
# grupos = cut_tree(Z, height=max_d)

