from logging import handlers
import os
import logging

log_level = os.getenv("LOG_LEVEL", "WARNING").upper()

# nossa instancia
log = logging.Logger("logs.py", logging.DEBUG)
# level
# ch = logging.StreamHandler()
# ch.setLevel(logging.DEBUG)
fh = handlers.RotatingFileHandler(
    "meuLog.log",
    maxBytes=10**6,
    backupCount=10
)
fh.setLevel(log_level)
#formatacao
fmt = logging.Formatter(
    "%(asctime)s %(name)s %(levelname)s l:%(lineno)d f:%(filename)s: %(message)s"
)
# ch.setFormatter(fmt)
fh.setFormatter(fmt)
#destino
# log.addHandler(ch)
log.addHandler(fh)


log.debug("mensagem pro dev, qe, sysadmin")
log.info("mensagem geral para usuario")
log.warning("aviso que nao causa erro")
log.error("erro que afeta uma unica execucao")
log.critical("erro geral ex: banco de dados sumiu")

try:
    1/0
except ZeroDivisionError as e:
    log.error("[ERRO] Deu erro %s", str(e))