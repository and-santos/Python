"""
# Animações
No cerne do manim está a animação. Geralmente, você pode adicionar uma animação à sua cena
chamando o método play()
De forma simples, animações são prodecimentos que interpolam entre dois mobjects.
Por exemplo, FadeIn(square) começa com uma versão transparente de 'square', e termina com
uma versão totalmente opaca, interpolando entre eles aumentando gradualmente a opacidade.
'FadeOut' funciona de maneira oposta.
Como outro exemplo, 'Rotate' começa com um mobject atribuído como argumento, e termina
com o mesmo objeto porém rotacionado por uma certa quantidade, desta vez interpolando
o ângulo de 'mobject' ao invés da opacidade


# Animando métodos
Qualquer propriedade de um 'mobject' que pode ser modificada pode ser animada. De fato,
qualquer método que modifique uma propriedade de 'mobject' pode ser usada como uma
animação, através do uso de ApplyMethod

# Tempo de execução da animação
Por padrão, qualquer animação atribuida à play() dura exatamente 1 segundo. Use o argumento
run_time para controlar a duração
"""
from manim import *


class SomeAnimations(Scene):
    def construct(self):
        square = Square()
        self.add(square)

        # Some animations display mobjects,...
        self.play(FadeIn(square))

        # ... some move or rotate mobjects around...
        self.play(Rotate(square, PI/4))

        # some animations remove mobjects from the screen
        self.play(FadeOut(square))

        self.wait(1)


class ApplyMethodExample(Scene):
    def construct(self):
        square = Square().set_fill(RED, opacity=1.0)
        self.add(square)

        # animate the change of color
        self.play(ApplyMethod(square.set_fill, WHITE))
        self.wait(1)

        # animate the change of position
        self.play(ApplyMethod(square.shift, UP))
        self.wait(1)

class RunTime(Scene):
    def construct(self):
        square = Square()
        self.add(square)
        self.play(ApplyMethod(square.shift, UP), run_time=3)
        self.wait(1)
