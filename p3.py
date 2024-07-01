import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def draw_object(vertices, ax, color):
    ax.plot_trisurf(vertices[:, 0], vertices[:, 1], vertices[:, 2], color=color)

def translate_object(vertices, tx, ty, tz):
    translation_matrix = np.array([[1, 0, 0, tx],
                                  [0, 1, 0, ty],
                                  [0, 0, 1, tz],
                                  [0, 0, 0, 1]])
    translated_vertices = np.dot(vertices, translation_matrix.T)
    return translated_vertices

def shear_object(vertices, shxy, shxz, shyx, shyz, shzx, shzy):
    shear_matrix = np.array([[1, shxy, shxz, 0],
                             [shyx, 1, shyz, 0],
                             [shzx, shzy, 1, 0],
                             [0, 0, 0, 1]])
    sheared_vertices = np.dot(vertices, shear_matrix.T)
    return sheared_vertices

def scale_object(vertices, sx, sy, sz):
    scale_matrix = np.array([[sx, 0, 0, 0],
                             [0, sy, 0, 0],
                             [0, 0, sz, 0],
                             [0, 0, 0, 1]])
    scaled_vertices = np.dot(vertices, scale_matrix.T)
    return scaled_vertices

def rotate_object(vertices, angle_x, angle_y, angle_z):
    rotation_matrix_x = np.array([[1, 0, 0, 0],
                                  [0, np.cos(angle_x), -np.sin(angle_x), 0],
                                  [0, np.sin(angle_x), np.cos(angle_x), 0],
                                  [0, 0, 0, 1]])

    rotation_matrix_y = np.array([[np.cos(angle_y), 0, np.sin(angle_y), 0],
                                  [0, 1, 0, 0],
                                  [-np.sin(angle_y), 0, np.cos(angle_y), 0],
                                  [0, 0, 0, 1]])

    rotation_matrix_z = np.array([[np.cos(angle_z), -np.sin(angle_z), 0, 0],
                                  [np.sin(angle_z), np.cos(angle_z), 0, 0],
                                  [0, 0, 1, 0],
                                  [0, 0, 0, 1]])

    rotation_matrix = np.dot(rotation_matrix_x, np.dot(rotation_matrix_y, rotation_matrix_z))
    rotated_vertices = np.dot(vertices, rotation_matrix.T)
    return rotated_vertices

def main():
    vertices = np.array([[0, 0, 0, 1],
                         [1, 0, 0, 1],
                         [1, 1, 0, 1],
                         [0, 1, 0, 1]])

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Original object (blue)
    draw_object(vertices, ax, 'blue')

    # Translation (red)
    translated_vertices = translate_object(vertices, 1, 1, 1)
    draw_object(translated_vertices, ax, 'red')

    # Shear (green)
    sheared_vertices = shear_object(vertices, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5)
    draw_object(sheared_vertices, ax, 'green')

    # Scale (purple)
    scaled_vertices = scale_object(vertices, 1.5, 1.5, 1.5)
    draw_object(scaled_vertices, ax, 'purple')

    # Rotation (orange)
    rotated_vertices = rotate_object(vertices, np.pi / 4, np.pi / 4, np.pi / 4)
    draw_object(rotated_vertices, ax, 'orange')

    plt.show()

if __name__ == "__main__":
    main()