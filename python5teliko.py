import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
def cosineSimilarity(x, y):
    cos = cosine_similarity(x.reshape(1,-1),y.reshape(1,-1))
    cos=str(cos)
    if len(cos)<7:
        return cos[2]
    elif cos[2]=="-":
        return cos[2:9]
    else:
        return cos[2:8]
a=np.array([9.32, -8.3, 0.2])
b=np.array([-5.3, 8.2, 7])
cosdist=cosineSimilarity(a,b)
print(cosdist)


def cosineSimilarity(x, y):
    cos = cosine_similarity(x.reshape(1,-1),y.reshape(1,-1))
    cos=str(cos)
    if len(cos)<7:
        return cos[2]
    elif cos[2]=="-":
        return cos[2:9]
    else:
        return cos[2:8]
a=np.array([6.5, 1.3, 0.3, 16, 2.4, -5.2, 2, -6, -6.3])
b=np.array([0.5, -1, -7.3, -7, -9.4, 8.2, -9, 6, 6.3])
cosdist=cosineSimilarity(a,b)
print(cosdist)


def cosineSimilarity(x, y):
    cos = cosine_similarity(x.reshape(1,-1),y.reshape(1,-1))
    cos=str(cos)
    if len(cos)<7:
        return cos[2]
    elif cos[2]=="-":
        return cos[2:9]
    else:
        return cos[2:8]
a=np.array([-0.5, 1, 7.3, 7, 9.4, -8.2])
b=np.array([1.25, 9.02, -7.3, -7, 15, 12.3])
cosdist=cosineSimilarity(a,b)
print(cosdist)


def cosineSimilarity(x, y):
    cos = cosine_similarity(x.reshape(1,-1),y.reshape(1,-1))
    cos=str(cos)
    if len(cos)<7:
        return cos[2]
    elif cos[2]=="-":
        return cos[2:9]
    else:
        return cos[2:8]
a=np.array([2, 8, 5.2])
b=np.array([2, 8, 5.2])
cosdist=cosineSimilarity(a,b)
print(cosdist)

