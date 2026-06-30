import matplotlib.pyplot as plt

# Sample data
front = [i for i in range(5)]
side = [i for i in range(5)]
sales_volume = [
    [-0.75, -0.68, -0.62, -0.62, -0.65],
    [-0.4, -0.35, -0.32, -0.33, -0.34],
    [-0.06, -0.05, -0.02, -0.03, -0.08],
    [0.23,  0.20,  0.20,  0.14,  0.07],
    [0.42,  0.46,  0.43,  0.32,  0.17]
]

# Creating a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plotting 3D bars
for i in range(len(front)):
    for j in range(len(side)):
        ax.bar3d(i, j, 0, 0.8, 0.8, sales_volume[i][j])

ax.set_xlabel('Side')
ax.set_ylabel('Front')
ax.set_zlabel('Height')
ax.set_title('Basic 3D Bar Graph')

# Displaying the plot
plt.show()
