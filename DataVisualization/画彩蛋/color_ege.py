# -*- coding:utf-8 -*-
# _author_='Zhang JunFeng'

import matplotlib .pyplot as plt
import numpy as np


fig = plt.figure()
ax = fig.gca(projection='3d')
x = 10 * np.outer(np.cos(u), np.sin(v))
y = 10 * np.outer(np.sin(u), np.sin(v))
z = 6 * np.outer(np.ones(np.size(u)), np.cos(v))
ax.plot_surface(x, y, z, cmap=plt.cm.get_cmap(value))

plt.plot([-15, 0, 10], [0, 0, 0], [0, 0, 0], color='indigo', linestyle='--')
plt.plot([0, 0, 0], [-15, 0, 10], [0, 0, 0], color='indigo', linestyle='--')
plt.plot([0, 0, 0], [0, 0, 0], [-10, 0, 6], color='indigo', linestyle='--')
ax.quiver(0, 0, 6, 0, 0, 5, length=1, color='indigo', linestyle='--')
ax.quiver(0, 10, 0, 0, 5, 0, length=1, color='indigo', linestyle='--')
ax.quiver(10, 0, 0, 5, 0, 0, length=1, color='indigo', linestyle='--')