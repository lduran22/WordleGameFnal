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

        self.definiciones = {"abeja": "Insecto volador que se encuentra en colmenas y produce miel.",
    "agua": "Sustancia líquida incolora, inodora e insípida que es esencial para la vida.",
    "aire": "Mezcla de gases que rodea la Tierra y permite la respiración de los seres vivos.",
    "aldea": "Población pequeña o asentamiento rural.",
    "alfil": "Pieza de ajedrez que se mueve en diagonal.",
    "almir": "Forma coloquial de referirse a un almirante, un rango naval.",
    "altar": "Estructura elevada en un lugar de culto religioso donde se realizan ofrendas o rituales.",
    "altura": "Medida vertical de un objeto o distancia desde la base hasta la cima.",
    "amigo": "Persona con la que se tiene una relación cercana y de afecto.",
    "ancho": "Medida horizontal o distancia de un lado a otro.",
    "ancla": "Objeto pesado que se arroja al agua para mantener una embarcación en su lugar.",
    "angel": "Ser celestial en diversas tradiciones religiosas y mitológicas.",
    "animo": "Estado de ánimo, energía o voluntad para hacer algo.",
    "antes": "En un momento anterior al presente o a un punto específico en el tiempo.",
    "apoyo": "Ayuda o respaldo brindado a alguien o algo.",
    "arbol": "Planta de tallo leñoso que tiene hojas y raíces.",
    "arena": "Partículas de roca pequeñas que se encuentran en playas y desiertos.",
    "aroma": "Olor agradable o fragancia que desprende algo.",
    "atlas": "Libro de mapas o colección de mapas geográficos.",
    "atomo": "La unidad básica de la materia, compuesta por núcleo y electrones.",
    "aviso": "Comunicación que alerta o informa sobre algo.",
    "banda": "Grupo de personas unidas por un propósito común, o una tira de tela.",
    "barco": "Embarcación utilizada para navegar en el agua.",
    "bello": "Hermoso o atractivo a la vista.",
    "besar": "Mostrar afecto o amor al presionar los labios contra algo o alguien.",
    "bicho": "Término informal que se usa para referirse a un insecto o criatura pequeña.",
    "bieno": "Término informal que se utiliza en algunos lugares como sinónimo de 'bueno'.",
    "bordo": "Lado de una embarcación o vehículo.",
    "bravo": "Valiente o furioso.",
    "breve": "De corta duración o conciso.",
    "cable": "Conductor eléctrico que transmite señales o energía.",
    "caida": "Acción de caer desde una altura.",
    "caoba": "Madera preciosa de color rojizo.",
    "causa": "Motivo o razón detrás de un evento o situación.",
    "cayos": "Islotes de coral o acumulaciones de rocas en aguas poco profundas.",
    "chico": "Término coloquial para referirse a un niño o joven.",
    "choza": "Vivienda pequeña y rústica, a menudo de materiales simples.",
    "cielo": "La bóveda celeste o espacio sobre la Tierra donde se ven las estrellas y las nubes.",
    "cima": "El punto más alto de una montaña o colina.",
    "circo": "Lugar donde se realizan espectáculos con payasos, acróbatas y animales.",
    "clave": "Información o detalle importante que es fundamental para entender algo.",
    "clavo": "Perno metálico afilado que se utiliza para sujetar objetos juntos.",
    "clima": "Patrón de condiciones atmosféricas en una región durante un período de tiempo.",
    "colin": "Nombre propio de origen latino que significa 'victorioso' o 'triunfador'.",
    "colza": "Planta de la familia de la mostaza, cuyas semillas se utilizan para producir aceite.",
    "coral": "Pequeños animales marinos que secretan un esqueleto calcáreo, o la estructura que forman.",
    "corte": "Acción de cortar algo con una herramienta afilada.",
    "crema": "Sustancia suave o espesa, a menudo utilizada en la cocina o para el cuidado de la piel.",
    "cruel": "Que disfruta infligiendo dolor o sufrimiento a otros.",
    "cubos": "Forma plural de 'cubo', un poliedro con seis caras cuadradas.",
    "cuerpo": "El conjunto de órganos, tejidos y sistemas que forman un organismo.",
    "cuento": "Narración breve que cuenta una historia o relata un evento.",
    "culto": "Grupo de personas que siguen una creencia religiosa o sistema de pensamiento específico.",
    "dardo": "Proyectil puntiagudo lanzado con una fuerza a un blanco.",
    "decir": "Expresar pensamientos, ideas o información a través del habla.",
    "desde": "Indica el punto de partida en tiempo o espacio.",
    "dieta": "Patrón de alimentación y consumo de alimentos de una persona.",
    "divan": "Mueble en forma de sofá con respaldo y brazos, usado para descansar o recibir visitas.",
    "doble": "Que tiene dos veces la cantidad o tamaño de algo.",
    "dosis": "Cantidad específica de un medicamento o sustancia que se debe tomar.",
    "droga": "Sustancia química que puede tener efectos psicoactivos o medicinales.",
    "dulce": "Sabor agradable que se percibe en alimentos ricos en azúcar.",
    "dunas": "Montículos de arena que se forman en áreas desérticas o costas.",
    "durar": "Permanecer en existencia o continuar durante un período de tiempo.",
    "echar": "Arrojar o lanzar algo con fuerza.",
    "elegir": "Tomar una decisión entre diferentes opciones o alternativas.",
    "enano": "Persona o ser de pequeña estatura.",
    "enero": "Primer mes del año en el calendario gregoriano.",
    "envio": "Acción de enviar algo a través de un medio de transporte o comunicación.",
    "epoca": "Período de tiempo o era histórica.",
    "equipo": "Grupo de personas o elementos que trabajan juntos para lograr un objetivo común.",
    "error": "Mistake o acción incorrecta que conduce a un resultado no deseado.",
    "etapa": "Período de tiempo o fase en el desarrollo de algo.",
    "extra": "Más allá de lo usual o necesario, en cantidad adicional.",
    "falar": "Término coloquial para referirse a hablar o conversar.",
    "falta": "Ausencia o carencia de algo.",
    "faros": "Luces de señalización en lugares peligrosos o en la navegación marítima.",
    "fauces": "Parte interna de la boca, incluyendo la garganta y la tráquea.",
    "fazos": "Término coloquial para referirse a los fazos o cigarros.",
    "feudo": "Territorio o posesión bajo el control de un señor feudal.",
    "final": "Última parte o conclusión de algo.",
    "firma": "Nombre escrito de una persona como aprobación o autenticación.",
    "flaco": "Que tiene poco peso o grasa corporal, delgado.",
    "flota": "Conjunto de vehículos o embarcaciones que se desplazan juntos.",
    "fluir": "Moverse suavemente y sin interrupciones, como un líquido.",
    "fotos": "Imágenes o fotografías.",
    "frase": "Grupo de palabras que forman una unidad de significado.",
    "fuego": "Proceso de combustión que produce calor y luz.",
    "fujos": "Término coloquial para referirse a los flujos o corrientes de agua.",
    "fuosa": "Término coloquial para referirse a una persona que se encuentra en estado de ebriedad o borrachera.",
    "gafas": "Objeto que se usa para proteger los ojos de la luz solar o para corregir la visión.",
    "globo": "Objeto inflable generalmente lleno de aire o gas y que puede elevarse en el aire.",
    "granar": "Término coloquial para referirse a la acción de llover granizo.",
    "gusan": "Forma coloquial para referirse a un gusano o larva.",
    "haber": "Verbo auxiliar que se utiliza para formar los tiempos compuestos en español.",
    "hecho": "Acción realizada o evento ocurrido en el pasado.",
    "helio": "Elemento químico con el símbolo He y número atómico 2, es un gas incoloro e inodoro.",
    "heron": "Ave zancuda que se encuentra en hábitats acuáticos.",
    "hiena": "Mamífero carnívoro de la familia Hyaenidae.",
    "humor": "Estado de ánimo o disposición emocional.",
    "humus": "Materia orgánica descompuesta que mejora la calidad del suelo.",
    "idear": "Concebir o crear una idea o plan.",
    "idiar": "Forma coloquial para referirse al acto de hablar o comunicarse en un idioma.",
    "ileso": "Que no ha sufrido daño ni lesiones.",
    "impar": "Número que no es divisible por 2.",
    "inicio": "Principio o comienzo de algo.",
    "irano": "Pertenece o se relaciona con Irán, un país de Asia Occidental.",
    "islas": "Extensiones de tierra rodeadas de agua en un entorno natural.",
    "jabon": "Producto de limpieza sólido o líquido que se utiliza para lavar y limpiar.",
    "japaz": "Término coloquial para referirse al país Japón.",
    "juego": "Actividad recreativa o deportiva que implica competencia y entretenimiento.",
    "jugos": "Líquidos naturales extraídos de frutas u otros alimentos.",
    "jurar": "Prometer solemnemente o hacer una declaración bajo juramento.",
    "labio": "Parte carnosa que rodea la boca.",
    "lacio": "Cabello que es liso y sin rizos.",
    "largo": "Que tiene una longitud mayor de lo normal.",
    "latir": "Movimiento rítmico de contracción y expansión del corazón.",
    "lazos": "Ataduras o nudos que unen cosas o personas.",
    "legal": "Relacionado con la ley o lo permitido por la normativa.",
    "legio": "Término coloquial que puede referirse a la legión o a un grupo grande de personas.",
    "lente": "Objeto óptico utilizado para enfocar la luz y producir imágenes.",
    "leyes": "Reglas o normas establecidas por la autoridad para regular la conducta.",
    "ligar": "Conectar o unir cosas o personas.",
    "limbo": "Estado de incertidumbre o indefinición.",
    "limon": "Fruta cítrica de forma redonda o ovalada.",
    "lindo": "Que es bonito o atractivo a la vista.",
    "lleno": "Que está completamente ocupado o lleno de algo.",
    "lleva": "Tercera persona del singular del verbo 'llevar' en presente, indica una acción actual.",
    "local": "Relacionado con un lugar específico o cercano.",
    "lomos": "Parte de la espalda que se encuentra entre los hombros y la cintura.",
    "lujos": "Bienes o comodidades costosas y no esenciales.",
    "lunar": "Marca o mancha en la piel de forma redonda o irregular.",
    "macho": "Se refiere al sexo masculino de una especie.",
    "macos": "Término coloquial para referirse a los macos o machos, en plural.",
    "madre": "Persona que da a luz a un hijo o hija.",
    "malta": "País insular en el mar Mediterráneo.",
    "manga": "Parte de la ropa que cubre el brazo desde el hombro hasta la muñeca.",
    "manos": "Extremidades superiores del cuerpo humano.",
    "marca": "Símbolo o signo que identifica un producto o empresa.",
    "mares": "Plural de 'mar', se refiere a grandes masas de agua salada.",
    "maria": "Nombre propio de una persona o lugar.",
    "marin": "Pertenece o se relaciona con la marina o el mar.",
    "mayas": "Civilización precolombina de América Central.",
    "medio": "Parte intermedia de algo, en el centro.",
    "mesas": "Muebles con una superficie plana, generalmente con patas, que se utilizan para poner objetos o comer.",
    "mina": "Excavación subterránea para extraer minerales o recursos.",
    "minos": "Término coloquial para referirse a los minos o hombres, en plural.",
    "mujer": "Persona de sexo femenino.",
    "mundo": "El planeta Tierra y todo lo que contiene, incluyendo la vida y la civilización.",
    "murio": "Forma conjugada del verbo 'morir' en tercera persona del singular del pretérito perfecto simple.",
    "noria": "Mecanismo que se utiliza para elevar agua desde un pozo o río.",
    "norte": "Uno de los cuatro puntos cardinales, en dirección al Polo Norte.",
    "nota": "Registro escrito o gráfico que contiene información o mensajes.",
    "nudos": "Lazos o apreturas hechos en una cuerda o hilo.",
    "nuevo": "Que es reciente o está en sus primeras etapas.",
    "nulos": "Plural de 'nulo', que significa que carece de valor o efecto legal.",
    "nunca": "En ningún momento o en ninguna ocasión.",
    "ocelo": "Etapa del desarrollo de los insectos, caracterizada por la muda de la piel.",
    "ocena": "Variante de 'oceán' que se utiliza en algunas regiones.",
    "ondas": "Movimientos periódicos de una superficie, como las ondas en el agua.",
    "optas": "Forma conjugada del verbo 'optar' en segunda persona del singular del presente de indicativo.",
    "ordas": "Término coloquial que puede referirse a multitudes o grupos grandes de personas.",
    "orden": "Instrucción o mandato para hacer algo de manera organizada.",
    "orgia": "Reunión desenfrenada y caótica de personas, a menudo con excesos y descontrol.",
    "ovino": "Pertenece o se relaciona con las ovejas o el ganado ovino.",
    "oxido": "Compuesto químico formado por oxígeno y otro elemento, a menudo asociado con la corrosión.",
    "ozono": "Molécula formada por tres átomos de oxígeno, que se encuentra en la atmósfera terrestre.",
    "papas": "Plural de 'papa', que se refiere a las patatas o papas, tubérculos comestibles.",
    "papel": "Material delgado hecho de pulpa de madera, a menudo utilizado para escribir o envolver objetos.",
    "parar": "Detenerse o interrumpir una acción o movimiento.",
    "paris": "Capital de Francia y una de las ciudades más conocidas del mundo.",
    "parra": "Planta trepadora que produce uvas.",
    "pasto": "Hierba que se utiliza como alimento para el ganado.",
    "pasta": "Masa de harina y agua utilizada para hacer pan, pasta u otros alimentos.",
    "patas": "Extremidades de un animal que le permiten moverse.",
    "pedir": "Hacer una solicitud o demanda a alguien.",
    "pedro": "Nombre propio de una persona.",
    "pelos": "Fibras que cubren la piel de los mamíferos, incluyendo los humanos.",
    "pense": "Forma conjugada del verbo 'pensar' en primera persona del singular del pretérito perfecto simple.",
    "peras": "Frutas de la peral.",
    "peres": "Forma conjugada del verbo 'perar', que se usa en algunas regiones.",
    "pesar": "Sentir tristeza o pesar por algo.",
    "petas": "Forma conjugada del verbo 'petar', que se usa en algunas regiones como sinónimo de explotar.",
    "pezar": "Pesar algo o calcular su peso.",
    "piano": "Instrumento musical de teclado que produce sonidos mediante cuerdas percutidas.",
    "picas": "Forma conjugada del verbo 'picar' en segunda persona del singular del presente de indicativo.",
    "pides": "Forma conjugada del verbo 'pedir' en segunda persona del singular del presente de indicativo.",
    "piedra": "Fragmento de roca o mineral.",
    "pijos": "Término coloquial que puede referirse a piojos o personas de clase alta.",
    "pilar": "Columna o soporte vertical que sostiene una estructura.",
    "pique": "Competencia o rivalidad entre dos personas o grupos.",
    "pirca": "Muro de piedra construido sin mortero, utilizado en algunas regiones de América del Sur.",
    "pleno": "En su totalidad o con todas las partes presentes.",
    "plomo": "Elemento químico con el símbolo Pb y número atómico 82, de color gris azulado.",
    "pluma": "Objeto que se utiliza para escribir, generalmente con tinta líquida.",
    "pollo": "Ave de corral que se cría para la alimentación.",
    "polar": "Relacionado con los polos de la Tierra o la polaridad magnética.",
    "poros": "Pequeñas aberturas en la piel u otras superficies.",
    "primer": "Que ocurre en primer lugar o antes que otros.",
    "pulso": "Latido rítmico del corazón.",
    "queja": "Expresión de insatisfacción o disgusto con algo o alguien."}

        self.palabra_oculta = self.generar_palabra_oculta()
        self.intentos_restantes = 6
        self.historial_intentos = []
        self.partida_terminada = False


    def generar_palabra_oculta(self):
        palabras_posibles = ["abeja", "agua", "aire", "aldea", "alfil", "almir", "altar", "altura", "amigo", "ancho",
    "ancla", "angel", "animo", "antes", "apoyo", "arbol", "arena", "aroma", "atlas", "atomo",
    "aviso", "banda", "barco", "bello", "besar", "bicho", "bieno", "besar", "bicho",
    "bordo", "bravo", "breve", "cable", "caida", "caoba", "causa", "cayos", "chico",
    "choza", "cielo", "cima", "circo", "clave", "clavo", "clima", "colin", "colza", "coral",
    "corte", "crema", "cruel", "cubos", "cuerpo", "cuento", "culto",  "dardo",
    "decir", "desde", "dieta", "divan", "doble", "dosis", "droga",
    "dulce", "dunas", "durar", "echar", "elegir", "enano", "enero",
     "envio", "epoca", "equipo", "error", "etapa", "extra", "falar",
    "falta", "falta", "faros", "fauces", "fazos", "feudo", "final",
    "firma", "flaco", "flota", "fluir", "fotos", "frase", "fuego", "fujos", "fuosa",
    "gafas", "globo", "granar", "gusan", "haber",  "hecho", "helio", "heron", "hiena",
    "humor", "humus", "idear", "idiar",  "ileso",  "impar", "inicio",
    "irano", "islas", "jabon", "japaz", "juego", "jugos", "jurar",
     "labio", "lacio", "largo", "latir", "lazos", "legal", "legio", "lente",
    "leyes", "ligar", "limbo", "limon", "lindo", "lleno", "lleva", "local", "lomos", "lujos",
    "lunar", "lunar", "macho", "macos", "madre", "malta", "manga", "manos", "marca",
     "mares", "maria", "marin",  "mayas", "medio",  "mesas",
     "mina", "minos", "mujer", "mundo", "murio",
    "noria", "norte", "nota",  "nudos", "nueva", "nueva", "nueva", "nuevo", "nulos",
    "nunca", "ocelo", "ocena",   "ondas", "optas", "ordas",
    "orden", "orgia", "ovino", "oxido", "ozono",  "papas", "papel", "parar", "paris",
    "parra", "pasta", "pasta", "pasta",   "pasto", "pasta", "patas", "pedir",
    "pedro", "pelos", "pense", "peras", "peres", "pesar", "petas", "pezar", "piano", "picas",
    "pides", "piedra", "pijos", "pilar",  "pique", "pirca", "pleno", "plomo",
    "pluma", "pollo", "polar", "poros", "primer", "pulso", "queja"]
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
