import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s ')

hola=5
while hola!=15:
    logging.debug("hola isn equal to 15. hola is equal to %s"%(hola))
    hola=hola+1
