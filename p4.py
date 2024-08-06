import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

def draw_objects(obj, trans, title):
    fig, ax = plt.subplots(1, 1, figsize=(5, 5))
    ax.add_patch(Polygon(obj, color='blue', alpha=0.5))

    transformed_obj = np.dot(trans, np.vstack((obj.T, np.ones(len(obj)))))
    transformed_obj = transformed_obj[:2, :].T  # Extracting the transformed points

    ax.add_patch(Polygon(transformed_obj, color='red', alpha=0.5))
    ax.set_title(title)
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.set_aspect('equal', 'box')
    ax.grid(True)
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.plot(0, 0, 'ko')  
    plt.show()

square = np.array([[0, 0], [1, 0], [1, 1], [0, 1]])
triangle = np.array([[0, 0], [1, 0], [0.5, np.sqrt(3)/2]])

scaling_matrix = np.array([[2, 0, 0], [0, 2, 0], [0, 0, 1]])  
shearing_matrix = np.array([[1, 0.5, 0], [0.5, 1, 0], [0, 0, 1]])  
translation_matrix = np.array([[1, 0, 2], [0, 1, -1], [0, 0, 1]]) 
theta = np.pi / 4 
rotation_matrix = np.array([
    [np.cos(theta), -np.sin(theta), 0],
    [np.sin(theta), np.cos(theta), 0],
    [0, 0, 1]
]) 

objects = [square, triangle]
transformations = [translation_matrix, rotation_matrix]
titles = ['Translation', 'Rotation']

for obj, trans, title in zip(objects, transformations, titles):
    draw_objects(obj, trans, title)

transformations = [scaling_matrix, shearing_matrix]
titles = ['Scaling', 'Shearing']

for obj, trans, title in zip(objects, transformations, titles):
    draw_objects(obj, trans, title)


