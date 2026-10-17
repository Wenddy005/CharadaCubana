from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.core.clipboard import Clipboard
import random


VERSION = "1.0.0"
TARJETA_DONACION = "9205-9598-7818-1842"

CHARADA = {
    1: "Caballo", 2: "Mariposa", 3: "Marinero", 4: "Gato", 5: "Monja",
    6: "Perro", 7: "Cocina", 8: "Muerto", 9: "Bebé", 10: "Elefante",
    11: "Gallina", 12: "Pescado", 13: "Carnicero", 14: "Cochino",
    15: "Pavo Real", 16: "León", 17: "Cabra", 18: "Cerdo", 19: "Ratón",
    20: "Conejo", 21: "Vaca", 22: "Serpiente", 23: "Tigre", 24: "Venado",
    25: "Lagartija", 26: "Mono", 27: "Burro", 28: "Toro", 29: "Mula",
    30: "Araña", 31: "Cangrejo", 32: "Pavo", 33: "Paloma", 34: "Águila",
    35: "Gaviota", 36: "Faisán", 37: "Loro", 38: "Guacamayo",
    39: "Tortuga", 40: "Ballena", 41: "Tiburón", 42: "Delfín",
    43: "Rana", 44: "Sapo", 45: "Culebra", 46: "Puercoespín",
    47: "Zorro", 48: "Lobo", 49: "Oso", 50: "Chivo",
    51: "Buey", 52: "Yegua", 53: "Potrillo", 54: "Perra",
    55: "Gata", 56: "Leona", 57: "Tigresa", 58: "Coneja",
    59: "Cabra montés", 60: "Oveja", 61: "Carnero", 62: "Cordero",
    63: "Camello", 64: "Jirafa", 65: "Cebra", 66: "Hipopótamo",
    67: "Rinoceronte", 68: "Cocodrilo", 69: "Iguana", 70: "Camaleón",
    71: "Pavo real blanco", 72: "Flamenco", 73: "Cisne", 74: "Pato",
    75: "Ganso", 76: "Águila real", 77: "Halcón", 78: "Búho",
    79: "Cuervo", 80: "Murciélago", 81: "Abeja", 82: "Hormiga",
    83: "Mariposa negra", 84: "Escorpión", 85: "Ciempiés",
    86: "Alacrán", 87: "Cucaracha", 88: "Mosca", 89: "Mosquito",
    90: "Grillo", 91: "Saltamontes", 92: "Mantis", 93: "Libélula",
    94: "Caracol", 95: "Estrella de mar", 96: "Pulpo",
    97: "Calamar", 98: "Medusa", 99: "Sirena", 100: "Dragón"
}


# ============================
# PANTALLA DEL MENÚ PRINCIPAL
# ============================
class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)

        titulo = Label(
            text="LA CHARADA CUBANA",
            font_size='32sp',
            bold=True,
            color=(1, 0.8, 0.2, 1),
            size_hint=(1, 0.25)
        )
        layout.add_widget(titulo)

        subtitulo = Label(
            text="Versión " + VERSION,
            font_size='16sp',
            color=(0.7, 0.7, 0.7, 1),
            size_hint=(1, 0.1)
        )
        layout.add_widget(subtitulo)

        layout.add_widget(Label(text="", size_hint=(1, 0.1)))

        btn_jugar = Button(
            text="JUGAR",
            font_size='22sp',
            bold=True,
            background_color=(0.2, 0.7, 0.3, 1),
            size_hint=(1, 0.15)
        )
        # Usamos una función normal en lugar de lambda para evitar errores
        btn_jugar.bind(on_press=self.ir_al_juego)
        layout.add_widget(btn_jugar)

        btn_donar = Button(
            text="DONAR",
            font_size='22sp',
            bold=True,
            background_color=(0.8, 0.5, 0.1, 1),
            size_hint=(1, 0.15)
        )
        btn_donar.bind(on_press=self.mostrar_donacion)
        layout.add_widget(btn_donar)

        btn_salir = Button(
            text="SALIR",
            font_size='22sp',
            bold=True,
            background_color=(0.7, 0.2, 0.2, 1),
            size_hint=(1, 0.15)
        )
        btn_salir.bind(on_press=self.salir_app)
        layout.add_widget(btn_salir)

        layout.add_widget(Label(text="", size_hint=(1, 0.1)))

        creditos = Label(
            text="Hecho con cariño para la comunidad cubana",
            font_size='12sp',
            color=(0.6, 0.6, 0.6, 1),
            size_hint=(1, 0.1)
        )
        layout.add_widget(creditos)

        self.add_widget(layout)

    # Funciones para los botones
    def ir_al_juego(self, instance):
        self.manager.current = 'juego'

    def salir_app(self, instance):
        App.get_running_app().stop()

    def mostrar_donacion(self, *args):
        content = BoxLayout(orientation='vertical', padding=15, spacing=15)

        content.add_widget(Label(
            text="¿Deseas apoyar el desarrollo?",
            font_size='16sp',
            color=(1, 1, 1, 1)
        ))

        content.add_widget(Label(
            text="Número de tarjeta para donar:",
            font_size='14sp',
            color=(0.8, 0.8, 0.8, 1)
        ))

        tarjeta_label = Label(
            text=TARJETA_DONACION,
            font_size='20sp',
            bold=True,
            color=(1, 0.8, 0.2, 1)
        )
        content.add_widget(tarjeta_label)

        btn_copiar = Button(
            text="COPIAR NÚMERO",
            font_size='16sp',
            background_color=(0.2, 0.5, 0.8, 1),
            size_hint=(1, 0.4)
        )

        def copiar(*a):
            Clipboard.copy(TARJETA_DONACION)
            btn_copiar.text = "¡COPIADO!"
            btn_copiar.background_color = (0.2, 0.8, 0.3, 1)

        btn_copiar.bind(on_press=copiar)
        content.add_widget(btn_copiar)

        btn_cerrar = Button(
            text="CERRAR",
            font_size='16sp',
            background_color=(0.6, 0.2, 0.2, 1),
            size_hint=(1, 0.3)
        )
        content.add_widget(btn_cerrar)

        popup = Popup(
            title="Donación",
            content=content,
            size_hint=(0.85, 0.55),
            title_size='20sp'
        )
        btn_cerrar.bind(on_press=popup.dismiss)
        popup.open()


# ============================
# PANTALLA DEL JUEGO
# ============================
class JuegoScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        barra = BoxLayout(orientation='horizontal', size_hint=(1, 0.08), spacing=5)

        btn_volver = Button(
            text="← Menú",
            font_size='14sp',
            background_color=(0.3, 0.3, 0.5, 1),
            size_hint=(0.3, 1)
        )
        btn_volver.bind(on_press=self.volver_menu)
        barra.add_widget(btn_volver)

        version_label = Label(
            text="v" + VERSION,
            font_size='12sp',
            color=(0.6, 0.6, 0.6, 1),
            size_hint=(0.7, 1)
        )
        barra.add_widget(version_label)
        layout.add_widget(barra)

        self.titulo = Label(
            text="LA CHARADA CUBANA",
            font_size='24sp',
            bold=True,
            color=(1, 0.8, 0.2, 1),
            size_hint=(1, 0.1)
        )
        layout.add_widget(self.titulo)

        self.instruccion = Label(
            text="Adivina qué figura corresponde al número",
            font_size='14sp',
            color=(1, 1, 1, 1),
            size_hint=(1, 0.08)
        )
        layout.add_widget(self.instruccion)

        self.numero_label = Label(
            text="",
            font_size='60sp',
            bold=True,
            color=(0.3, 0.9, 1, 1),
            size_hint=(1, 0.18)
        )
        layout.add_widget(self.numero_label)

        scroll = ScrollView(size_hint=(1, 0.42))
        self.opciones_grid = GridLayout(
            cols=2,
            spacing=8,
            padding=8,
            size_hint_y=None
        )
        self.opciones_grid.bind(minimum_height=self.opciones_grid.setter('height'))
        scroll.add_widget(self.opciones_grid)
        layout.add_widget(scroll)

        self.puntaje = 0
        self.puntaje_label = Label(
            text="Puntos: 0",
            font_size='18sp',
            bold=True,
            color=(0.4, 1, 0.4, 1),
            size_hint=(1, 0.07)
        )
        layout.add_widget(self.puntaje_label)

        self.boton_siguiente = Button(
            text="Siguiente",
            font_size='18sp',
            bold=True,
            background_color=(0.2, 0.7, 0.3, 1),
            size_hint=(1, 0.1),
            disabled=True
        )
        self.boton_siguiente.bind(on_press=self.nueva_pregunta)
        layout.add_widget(self.boton_siguiente)

        self.add_widget(layout)

        self.numero_actual = None
        self.ultimo_numero = None
        self.nueva_pregunta()

    def volver_menu(self, *args):
        self.manager.current = 'menu'

    def nueva_pregunta(self, *args):
        self.opciones_grid.clear_widgets()

        while True:
            self.numero_actual = random.randint(1, 100)
            if self.numero_actual != self.ultimo_numero:
                break
        self.ultimo_numero = self.numero_actual

        respuesta_correcta = CHARADA[self.numero_actual]

        opciones_falsas = set()
        intentos = 0
        while len(opciones_falsas) < 3 and intentos < 200:
            num_falso = random.randint(1, 100)
            if num_falso != self.numero_actual:
                opciones_falsas.add(CHARADA[num_falso])
            intentos += 1

        opciones = list(opciones_falsas) + [respuesta_correcta]
        random.shuffle(opciones)

        self.numero_label.text = "#" + str(self.numero_actual)
        self.instruccion.text = "¿Qué figura corresponde a este número?"
        self.boton_siguiente.disabled = True

        for opcion in opciones:
            btn = Button(
                text=opcion,
                font_size='16sp',
                bold=True,
                background_color=(0.25, 0.4, 0.7, 1),
                size_hint_y=None,
                height=70
            )
            btn.bind(on_press=lambda b, o=opcion: self.verificar_respuesta(b, o))
            self.opciones_grid.add_widget(btn)

    def verificar_respuesta(self, boton, opcion_elegida):
        respuesta_correcta = CHARADA[self.numero_actual]

        for child in self.opciones_grid.children:
            child.disabled = True
            if child.text == respuesta_correcta:
                child.background_color = (0.2, 0.8, 0.3, 1)
            elif child.text == opcion_elegida and opcion_elegida != respuesta_correcta:
                child.background_color = (0.8, 0.2, 0.2, 1)

        if opcion_elegida == respuesta_correcta:
            self.puntaje += 10
            mensaje = "El " + str(self.numero_actual) + " es " + respuesta_correcta + "\n+10 puntos"
            self.mostrar_popup("¡CORRECTO!", mensaje, True)
        else:
            mensaje = "El " + str(self.numero_actual) + " es " + respuesta_correcta
            self.mostrar_popup("INCORRECTO", mensaje, False)

        self.puntaje_label.text = "Puntos: " + str(self.puntaje)
        self.boton_siguiente.disabled = False

    def mostrar_popup(self, titulo, mensaje, exito):
        color_bg = (0.15, 0.5, 0.2, 1) if exito else (0.5, 0.15, 0.15, 1)
        content = BoxLayout(orientation='vertical', padding=10, spacing=10)
        content.add_widget(Label(text=mensaje, font_size='16sp', color=(1, 1, 1, 1)))
        cerrar = Button(
            text="OK",
            size_hint=(1, 0.5),
            font_size='16sp',
            background_color=color_bg
        )
        content.add_widget(cerrar)

        popup = Popup(
            title=titulo,
            content=content,
            size_hint=(0.8, 0.4),
            title_size='18sp'
        )
        cerrar.bind(on_press=popup.dismiss)
        popup.open()


# ============================
# APLICACIÓN PRINCIPAL
# ============================
class CharadaApp(App):
    def build(self):
        self.title = "Charada Cubana v" + VERSION
        Window.clearcolor = (0.1, 0.1, 0.15, 1)

        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(JuegoScreen(name='juego'))
        return sm


if __name__ == "__main__":
    CharadaApp().run()
