import numpy as np
import matplotlib.pyplot as plt

x = np.array([2022,2023,2024,2025,2026])
y1 = np.array([23,33,45,29,36])
y2 = np.array([12,22,34,19,26])
y3 = np.array([17,27,39,24,31])

line_style = dict(
    marker = '2',
    ms = 10,
    markerfacecolor = 'cyan',
    markeredgecolor = 'blue',
    markeredgewidth = 4,
)

plt.plot(x,y1, color = '#A52F2F', **line_style)
plt.plot(x,y2, color = '#6C3761', **line_style)
plt.plot(x,y3, color = "#2600FFC5", **line_style)

plt.show()