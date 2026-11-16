from kivy.app import App
from kivy.uix.button import Button
from kivy.animation import Animation
from kivy.core.window import Window

Window.clearcolor = (0.12, 0.15, 0.22, 1)


class BotonAnimado(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.text = "Click para animar!"
        self.font_size = "18sp"
        self.size_hint = (None, None)
        self.size = (220, 60)
        self.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        self.background_normal = ''
        self.background_color = (0.2, 0.7, 0.4, 1)

        # bandera y evento de click
        self.animando = False
        self.bind(on_press=self.ejecutar_animacion)

    def ejecutar_animacion(self, instance):
        if self.animando:
            return

        self.animando = True
        self.text = "¡Animando!"

        # 1. PARTE 1
        parte_1 = Animation(
            size=(300, 80),
            background_color=(0.9, 0.3, 0.5, 1),
            duration=2.0
        )

        # 2. PARTE 2 (retorna a su estado original)
        parte_2 = Animation(
            size=(220, 60),
            background_color=(0.2, 0.7, 0.4, 1),
            duration=2.0
        )

        animacion = parte_1 + parte_2

        animacion.bind(on_complete=self.restaurar_boton)

        animacion.start(self)

    def restaurar_boton(self, animation, widget):
        self.text = "Click para animar!"
        self.animando = False


class MyApp(App):
    def build(self):
        return BotonAnimado()


if __name__ == '__main__':
    MyApp().run()
