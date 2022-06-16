from clouglog import CloudLog

logger = CloudLog("serviceAccountKey.json", "nube")
logger2 = CloudLog("serviceAccountKey.json", "nube")

logger.success()
logger2.error("puntero nulo")
