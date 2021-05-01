import numpy as np
from sklearn.linear_model import LinearRegression

x = np.random.randint(1, 100, (1, 6)).reshape((-1, 1))
y = np.random.randint(1, 100, (6, 1))
model = LinearRegression()
model.fit(x, y)
r_sq = model.score(x, y)
print('coefficient of determination:', r_sq)
print('intercept:', model.intercept_)
print('slope:', model.coef_)
y_before = model.predict(x)
print('predicted response:', y_before, sep='\n')
