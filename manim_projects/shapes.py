"""
 Por padrão, mobjetos são colocados no centro das coordenadas, na origem, quando são criados.
 Também é dado a eles cores padrão Além disso, a cena "Shapes" posiciona os mobjects usando o
 método shift(). O quadrado é deslocado uma unidade na direção "UP" da origem, enquanto o
 círculo e o triângulo são deslocados uma unidade para a esquerda e direita, respectivamente.
"""

from manim import *


class Shapes(Scene):
    def construct(self):
        circle = Circle()
        triangle = Triangle()
        square = Square()

        circle.shift(LEFT)
        square.shift(UP)
        triangle.shift(RIGHT)

        self.add(circle, square, triangle)
        self.wait(1)
