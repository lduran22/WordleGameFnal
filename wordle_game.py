import random

class Retroalimentacion:
    def __init__(self, palabra_oculta):
        self.palabra_oculta = palabra_oculta
        self.correctas_posicion = 0
        self.correctas_incorrectas_posicion = 0
        self.incorrectas = 0

    def calcular_retroalimentacion(self, palabra):
        for i in range(5):
            if palabra[i] == self.palabra_oculta[i]:
                self.correctas_posicion += 1
            elif palabra[i] in self.palabra_oculta:
                self.correctas_incorrectas_posicion += 1
            else:
                self.incorrectas += 1

class WordleGame:
    def __init__(self):
        self.palabra_oculta = self.generar_palabra_oculta()
        self.intentos_restantes = 6
        self.historial_intentos = []
        self.partida_terminada = False


    def generar_palabra_oculta(self):
        palabras_posibles = ["abeja", "agua", "aire", "aldea", "alfil", "almir", "altar", "altura", "amigo", "ancho",
    "ancla", "angel", "animo", "antes", "apoyo", "arbol", "arena", "aroma", "atlas", "atomo",
    "aviso", "banda", "barco", "bello", "besar", "bicho", "bieno", "besar", "bicho", "bieno",
    "bordo", "bravo", "breve", "brill", "cable", "caida", "caoba", "causa", "cayos", "chico",
    "choza", "cielo", "cima", "circo", "clave", "clavo", "clima", "colin", "colza", "coral",
    "coron", "corte", "crema", "cruel", "cubos", "cuerpo", "cuento", "culto", "darlo", "dardo",
    "decir", "demon", "demon", "derro", "desde", "dieta", "divan", "doble", "dosis", "droga",
    "dulce", "dunas", "durar", "dying", "echar", "elegir", "elevo", "empez", "enano", "enero",
    "enter", "enver", "envio", "epoca", "equipo", "error", "espan", "etapa", "extra", "falar",
    "falta", "falta", "falto", "famos", "faros", "fauces", "fazos", "feudo", "fiest", "final",
    "firma", "flaco", "flota", "fluir", "fotos", "frase", "fuego", "fujos", "fuosa", "fuota",
    "gafas", "globo", "granar", "gusan", "haber", "hallo", "hecho", "helio", "heron", "hiena",
    "humor", "humus", "idear", "idiar", "idiot", "iguaz", "ileso", "image", "impar", "inicio",
    "irano", "islas", "islen", "issus", "jabon", "japaz", "juego", "jugos", "jurar", "kanes",
    "kendo", "kotza", "labio", "lacio", "largo", "latir", "lazos", "legal", "legio", "lente",
    "leyes", "ligar", "limbo", "limon", "lindo", "lleno", "lleva", "local", "lomos", "lujos",
    "lunar", "lunch", "lunar", "macho", "macos", "madre", "malta", "manga", "manos", "marca",
    "march", "mares", "maria", "marin", "maron", "mayas", "medio", "mendo", "mesas", "mexia",
    "mezco", "miaro", "milos", "mina", "minos", "mujer", "mundo", "murio", "naran", "ninos",
    "noria", "norte", "nota", "notan", "nudos", "nueva", "nueva", "nueva", "nuevo", "nulos",
    "nunca", "objet", "ocelo", "ocena", "ofens", "ofert", "ofren", "ondas", "optas", "ordas",
    "orden", "orgia", "ovino", "oxido", "ozono", "pagan", "papas", "papel", "parar", "paris",
    "parra", "pasta", "pasta", "pasta", "paste", "pasta", "pasto", "pasta", "patas", "pedir",
    "pedro", "pelos", "pense", "peras", "peres", "pesar", "petas", "pezar", "piano", "picas",
    "pides", "piedra", "piens", "pijos", "pilar", "pinas", "pique", "pirca", "pleno", "plomo",
    "pluma", "pollo", "polar", "poros", "preni", "primi", "primer", "pulso", "puopa", "queja"]
        self.palabra_oculta = random.choice(palabras_posibles)
        return self.palabra_oculta

    def realizar_intento(self, palabra):
        if not self.partida_terminada:
            self.intentos_restantes -= 1
            retroalimentacion = Retroalimentacion(self.palabra_oculta)
            retroalimentacion.calcular_retroalimentacion(palabra)
            self.historial_intentos.append((palabra, retroalimentacion))
            self.actualizar_estado_partida(retroalimentacion)

    def actualizar_estado_partida(self, retroalimentacion):
        if retroalimentacion.correctas_posicion == 5 or self.intentos_restantes == 0:
            self.partida_terminada = True

    def verificar_victoria(self):
        return self.partida_terminada and self.historial_intentos[-1][1].correctas_posicion == 5

    def verificar_derrota(self):
        return self.partida_terminada and self.intentos_restantes == 0

    def iniciar_nueva_partida(self):
        self.generar_palabra_oculta()
        self.intentos_restantes = 6
        self.historial_intentos = []
        self.partida_terminada = False
