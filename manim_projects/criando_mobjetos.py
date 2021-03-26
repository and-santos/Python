"""
 Geralmente todo código de um script manim deve estar dentro de um método construct()
 de uma classe Scene. Este é o principal meio de exibir um mobject na tela quando
 não está sendo animado. Para remover um objeto da tela, utilizamos o método
 remove() da "Scene" em questão.
"""
from manim import *


class CreatingMobjects(Scene):
    def construct(self):
        circle = Circle()
        self.add(circle)
        self.wait(1)
        self.remove(circle)
        self.wait(1)
