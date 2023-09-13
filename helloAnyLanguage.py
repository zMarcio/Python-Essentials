import os
import sys
import locale
import logging

log_level = os.getenv("LOG_LEVEL", "WARNING").upper()

# nossa instancia
log = logging.Logger("helloAnyLanguage.py", logging.DEBUG)
# level
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
#formatacao
fmt = logging.Formatter(
    "%(asctime)s %(name)s %(levelname)s l:%(lineno)d f:%(filename)s: %(message)s"
)
ch.setFormatter(fmt)
#destino
log.addHandler(ch)

# print(locale.getlocale()[0])

arguments = {
    "lang":None,
    "count":None
}

for arg in sys.argv[1:]:
    try:
        key, value = arg.split("=")
    except ValueError as e:
        log.error(
            "you need to use `=`, you passed %s, try with --key=value: %s",
            arg,
            str(e)
        )
        sys.exit(1)

    key = key.lstrip("-").strip()
    value = value.strip()
    
    if key not in arguments:
        print(f"invalid options '{key}'")
        sys.exit(1)
    arguments[key] = value

current_language = arguments["lang"]

if current_language is None:
    current_language = locale.getlocale()[0]
    if current_language is None:
        current_language = input("Choose a language:  ")
msg = {
    "en_US":"Hello, World!",
    "pt_BR":"Olá, Mundo!",
    "it_IT":"Ciao, Mondo!",
    "es_ES":"Hola, Mundo!",
    "fr_FR":"Bonjour, Monde!"
}

count = int(arguments["count"]) if arguments["count"] else 1
print(msg.get(current_language, "Idioma não suportado") * count)