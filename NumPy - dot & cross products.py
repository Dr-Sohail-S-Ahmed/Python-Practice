import numpy as np

features = np.array([[2000,3],      # House 1 sq.ft & bedrooms
                     [1800,2]])     # House 2 sq.ft & bedrooms
weights = np.array([150,50000])
print(np.dot(features,weights))     # total prices of both houses or dot (.) product i.e. (A . B) = (f . w) = (2000*150) + (3*50000) = 450000
# Dot Product is SCALAR + measures degree to which 2 vectors are parallel + has no direction
# dot = 0 → vectors are orthogonal (unrelated), dot > 0 → aligned, dot < 0 → opposed
# Used in linear models (linear regression, logistic regression, perceptrons, SVMs) i.e. every prediction is a dot product
# Also used in neural networks, cosine similarity (NLP, search, embeddings, attention mechanism (transformers)

m1 = np.array([1,2,3])   # Matrix 1
m2 = np.array([4,5,6])   # Matrix 2
print(np.cross(m1,m2))  # cross product or vector cross (x) product is as follows:
#                       |i j k|
# (A x B) = (m1 x m2) = |1,2,3| = |2,3|i - |1,3|j + |1,2|k = ((2*6)-(3*5))i - ((1*6)-(3*5))j + ((1*5)-(2*4))k = (12-15)i - (6-12)j + (5-8)k
#                       |4,5,6|   |5,6|    |4,6|    |4,5|                                         = (-3)i - (-6)j + (-3)k = -3i +6j -3k
# Output: [-3  6 -3]
# Cross Product is VECTOR + measures degree to which 2 vectors are perpendicular + resulting vector is perpendicular (orthogonal) to both A & B
# Used in robotics, 3D vision / SLAM, Physics-informed ML