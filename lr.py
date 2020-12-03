from sklearn.linear_model import LogisticRegression
import numpy as np
from sklearn.cluster import KMeans
import plotly.graph_objects as go

n = 50
x = np.random.randint(0, 100, n)
y = np.random.randint(0, 100, n)
z = np.random.randint(0, 100, n)

points = [([x[i], y[i], z[i]]) for i in range(n)]
clusters = KMeans(n_clusters=2).fit(points).labels_
colors = ['red' if l == 0 else 'blue' for l in clusters]

clf = LogisticRegression()
clf.fit(points, clusters)
w = clf.coef_[0]
temp = np.linspace(0, 100, 100)
xx, yx = np.meshgrid(temp, temp)
zz = -(clf.intercept_[0] + w[0] * xx + w[1] * yx) / w[2]

figure = go.Figure()
figure.add_trace(go.Scatter3d(x=x, y=y, z=z, mode='markers', marker=dict(color=colors)))
figure.add_trace(go.Surface(x=xx, y=yx, z=zz))
figure.show()
