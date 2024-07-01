import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def draw_3d_objects(objects, transformations, titles):
    fig = plt.figure(figsize=(15, 5))

    for i, (obj, trans, title) in enumerate(zip(objects, transformations, titles)):
        ax = fig.add_subplot(1, len(objects), i + 1, projection='3d')
        ax.set_title(title)

        ax.add_collection3d(Poly3DCollection([obj], color='blue', alpha=0.5))

        transformed_obj = np.dot(trans, np.vstack((obj.T, np.ones(len(obj)))))[:3, :]
        ax.add_collection3d(Poly3DCollection([transformed_obj.T], color='red', alpha=0.5))

        ax.set_xlim([-5, 5])
        ax.set_ylim([-5, 5])
        ax.set_zlim([-5, 5])
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.grid(True)
        ax.scatter(0, 0, 0, color='black', s=50)

    plt.tight_layout()
    plt.show()

def main():
    cube = np.array([[0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0], [0, 0, 1], [1, 0, 1], [1, 1, 1], [0, 1, 1]])
    pyramid = np.array([[0.5, 0.5, 0], [0, 1, 0], [1, 1, 0], [0.25, 0.75, 1], [0.75, 0.75, 1], [0.5, 0.5, 2]])

    scaling_matrix = np.array([[2, 0, 0, 0],
                               [0, 2, 0, 0],
                               [0, 0, 2, 0],
                               [0, 0, 0, 1]])

    shearing_matrix = np.array([[1, 0.5, 0, 0],
                                [0.5, 1, 0, 0],
                                [0, 0, 1, 0],
                                [0, 0, 0, 1]])

    translation_matrix = np.array([[1, 0, 0, 2],
                                   [0, 1, 0, -1],
                                   [0, 0, 1, 1],
                                   [0, 0, 0, 1]])

    theta = np.pi / 4
    rotation_matrix = np.array([[np.cos(theta), -np.sin(theta), 0, 0],
                                [np.sin(theta), np.cos(theta), 0, 0],
                                [0, 0, 1, 0],
                                [0, 0, 0, 1]])

    objects = [cube, pyramid]
    transformations = [translation_matrix, rotation_matrix]
    titles = ['Translation', 'Rotation']
    draw_3d_objects(objects, transformations, titles)

    transformations = [scaling_matrix, shearing_matrix]
    titles = ['Scaling', 'Shearing']
    draw_3d_objects(objects, transformations, titles)

if __name__ == "__main__":
    main()
