import json
import os

# Crear directorio data si no existe
if not os.path.exists('data'):
    os.makedirs('data')

# 1. Archivo composers.json
composers = [
    {
        "name": "Claude Debussy",
        "country": "Francia",
        "style": "Impresionismo",
        "works": []  # El documento no especifica obras
    },
    {
        "name": "Maurice Ravel",
        "country": "Francia",
        "style": "Impresionismo",
        "works": []  # El documento no especifica obras
    },
    {
        "name": "Alban Berg",
        "country": "Austria",
        "style": "Expresionismo",
        "works": []  # El documento no especifica obras
    },
    {
        "name": "Arnold Schoenberg",
        "country": "Austria",
        "style": "Expresionismo",
        "works": []  # El documento no especifica obras
    },
    {
        "name": "Zoltán Kodály",
        "country": "Hungría",
        "style": "Nacionalismo",
        "works": []  # El documento no especifica obras
    },
    {
        "name": "George Gershwin",
        "country": "Estados Unidos",
        "style": "Nacionalismo",
        "works": []  # El documento no especifica obras
    },
    {
        "name": "Manuel de Falla",
        "country": "España",
        "style": "Nacionalismo",
        "works": []  # El documento no especifica obras
    },
    {
        "name": "Serguéi Prokófiev",
        "country": "Rusia",
        "style": "Nacionalismo",
        "works": []  # El documento no especifica obras
    },
    {
        "name": "Vaughan Williams",
        "country": "Reino Unido",
        "style": "Nacionalismo",
        "works": []  # El documento no especifica obras
    },
    {
        "name": "Jean Sibelius",
        "country": "Finlandia",
        "style": "Nacionalismo",
        "works": []  # El documento no especifica obras
    },
    {
        "name": "Igor Stravinsky",
        "country": "Rusia",
        "style": "Neoclasicismo",
        "works": []  # El documento no especifica obras
    },
    {
        "name": "Edward Varèse",
        "country": "Francia/Estados Unidos",
        "style": "Música Concreta",
        "works": []  # El documento no especifica obras
    },
    {
        "name": "Karheinz Stockhausen",
        "country": "Alemania",
        "style": "Música Electrónica",
        "works": []  # El documento no especifica obras
    },
    {
        "name": "John Cage",
        "country": "Estados Unidos",
        "style": "Música Aleatoria",
        "works": []  # El documento no especifica obras
    }
]

# 2. Archivo styles.json
styles = [
    {
        "name": "Impresionismo",
        "characteristics": [
            "Melodías poco definidas o fragmentadas",
            "Acordes sofisticados",
            "Uso de escalas antiguas y pentatónicas",
            "Instrumentación especial (oboè, corn anglés, arpa, metalls amb sordina...)"
        ],
        "composers": ["Claude Debussy", "Maurice Ravel"]
    },
    {
        "name": "Expresionismo",
        "characteristics": [
            "Abandono de la tonalidad",
            "Uso de disonancias",
            "Líneas melódicas con grandes saltos interválicos difíciles de entonar",
            "Técnica 'sprechgesang' (canto hablado)",
            "Tono 'histérico' e inquietante",
            "Argumentos fuertes, violentos y con conductas poco comunes"
        ],
        "composers": ["Alban Berg", "Arnold Schoenberg"]
    },
    {
        "name": "Nacionalismo",
        "characteristics": [
            "Búsqueda de identidad nacional a través de la música",
            "Inspiración en músicas autóctonas",
            "En EEUU, inspiración en el jazz"
        ],
        "composers": ["Zoltán Kodály", "George Gershwin", "Manuel de Falla", "Serguéi Prokófiev", "Vaughan Williams", "Jean Sibelius"]
    },
    {
        "name": "Neoclasicismo",
        "characteristics": [
            "Retorno a los géneros del Clasicismo (concierto, sinfonía, suite...)",
            "Alejamiento del impresionismo y expresionismo",
            "Nueva claridad en la forma, melodía y textura"
        ],
        "composers": ["Igor Stravinsky"]
    },
    {
        "name": "Música Concreta",
        "characteristics": [
            "Grabación de sonidos naturales (tren, piano, pasos...)",
            "Transformación electrónica de sonidos grabados"
        ],
        "composers": ["Edward Varèse"]
    },
    {
        "name": "Música Electrónica",
        "characteristics": [
            "Creación de sonidos propios con sintetizadores y otros medios",
            "No utiliza sonidos de la naturaleza o instrumentos preexistentes"
        ],
        "composers": ["Karheinz Stockhausen"]
    },
    {
        "name": "Música Aleatoria",
        "characteristics": [
            "Incorporación de elementos al azar en la composición",
            "No se fijan valores a las notas",
            "Las dinámicas las elige el intérprete",
            "Uso del piano preparado (concepto de John Cage)"
        ],
        "composers": ["John Cage"]
    }
]

# 3. Archivo paintings.json (el documento no especifica pinturas concretas)
paintings = [
    {
        "style": "Impresionismo",
        "paintings": []  # El documento menciona que hay que relacionarlo con la pintura pero no especifica cuáles
    },
    {
        "style": "Expresionismo",
        "paintings": []  # El documento menciona que hay que relacionarlo con la pintura pero no especifica cuáles
    }
]

# 4. Archivo relationships.json
relationships = {
    "styles_and_composers": {
        "Impresionismo": ["Claude Debussy", "Maurice Ravel"],
        "Expresionismo": ["Alban Berg", "Arnold Schoenberg"],
        "Nacionalismo": ["Zoltán Kodály", "George Gershwin", "Manuel de Falla", "Serguéi Prokófiev", "Vaughan Williams", "Jean Sibelius"],
        "Neoclasicismo": ["Igor Stravinsky"],
        "Música Concreta": ["Edward Varèse"],
        "Música Electrónica": ["Karheinz Stockhausen"],
        "Música Aleatoria": ["John Cage"]
    },
    "styles_and_characteristics": {
        "Impresionismo": ["Melodías poco definidas", "Acordes sofisticados", "Escalas antiguas y pentatónicas", "Instrumentación especial"],
        "Expresionismo": ["Abandono de la tonalidad", "Disonancias", "Grandes saltos interválicos", "Sprechgesang", "Tono histérico"],
        "Nacionalismo": ["Identidad nacional", "Músicas autóctonas", "Jazz (EEUU)"],
        "Neoclasicismo": ["Retorno a géneros clásicos", "Claridad formal", "Claridad melódica"],
        "Música de Vanguardia": ["Desligada de instrumentos tradicionales", "Notación no tradicional"]
    },
    "vanguardias": {
        "Música Concreta": ["Grabación de sonidos naturales", "Transformación electrónica"],
        "Música Electrónica": ["Creación de sonidos con sintetizadores"],
        "Música Aleatoria": ["Elementos al azar", "Piano preparado"]
    }
}

# Guardar los archivos JSON
with open('data/composers.json', 'w', encoding='utf-8') as f:
    json.dump(composers, f, ensure_ascii=False, indent=2)

with open('data/styles.json', 'w', encoding='utf-8') as f:
    json.dump(styles, f, ensure_ascii=False, indent=2)

with open('data/paintings.json', 'w', encoding='utf-8') as f:
    json.dump(paintings, f, ensure_ascii=False, indent=2)

with open('data/relationships.json', 'w', encoding='utf-8') as f:
    json.dump(relationships, f, ensure_ascii=False, indent=2)

print("Archivos JSON creados en la carpeta 'data':")
print("- composers.json")
print("- styles.json")
print("- paintings.json")
print("- relationships.json")