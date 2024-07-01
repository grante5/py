import turtle
import math

def draw_polygon(vertices):
    turtle.penup()
    turtle.goto(vertices[-1])
    turtle.pendown()
    for vertex in vertices:
        turtle.goto(vertex)
    turtle.goto(vertices[0])
    turtle.hideturtle()

def translate_polygon(vertices, tx, ty):
    translated_vertices = [(vertex[0] + tx, vertex[1] + ty) for vertex in vertices]
    return translated_vertices

def shear_polygon(vertices, shx, shy):
    sheared_vertices = [(vertex[0] + shx * vertex[1], vertex[1] + shy * vertex[0]) for vertex in vertices]
    return sheared_vertices

def scale_polygon(vertices, sx, sy):
    scaled_vertices = [(vertex[0] * sx, vertex[1] * sy) for vertex in vertices]
    return scaled_vertices

def rotate_polygon(vertices, angle):
    rotated_vertices = []
    for vertex in vertices:
        x = vertex[0] * math.cos(math.radians(angle)) - vertex[1] * math.sin(math.radians(angle))
        y = vertex[0] * math.sin(math.radians(angle)) + vertex[1] * math.cos(math.radians(angle))
        rotated_vertices.append((x, y))
    return rotated_vertices

def main():
    n = int(input("Enter the number of sides in the polygon: "))
    vertices = []
    print("Enter coordinates (x, y) for each vertex:")
    for _ in range(n):
        x, y = map(int, input().split())
        vertices.append((x, y))

    tx, ty = map(float, input("Enter translation factors (tx, ty): ").split())
    translated_vertices = translate_polygon(vertices, tx, ty)

    shx, shy = map(float, input("Enter shear factors (shx, shy): ").split())
    sheared_vertices = shear_polygon(vertices, shx, shy)

    sx, sy = map(float, input("Enter scale factors (sx, sy): ").split())
    scaled_vertices = scale_polygon(vertices, sx, sy)

    angle = float(input("Enter rotation angle (in degrees): "))
    rotated_vertices = rotate_polygon(vertices, angle)

    turtle.speed(1)
    turtle.bgcolor("white")  # Set the background color to white

    turtle.color("red")
    draw_polygon(vertices)

    turtle.color("blue")
    draw_polygon(translated_vertices)

    turtle.color("green")
    draw_polygon(sheared_vertices)

    turtle.color("purple")
    draw_polygon(scaled_vertices)

    turtle.color("orange")
    draw_polygon(rotated_vertices)

    turtle.done()

if __name__ == "__main__":
    main()