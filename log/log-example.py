import logging

# logging.warning("a message warning")
# logging.info("a message info")
# logging.error("default log_level is warning")
#
# logging.basicConfig(filename="./python-log.log", filemode='w',level=logging.INFO)  #写文件，filemode:w 表示覆盖
# logging.info("log info")

# logging.warning("%s log message %s", "log", "warning")
# logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s', level=logging.DEBUG,datefmt='%m/%d/%Y %I:%M:%S %p')
# logging.debug("message")

logger = logging.getLogger("example-log")
logger.setLevel(logging.DEBUG)

stout = logging.StreamHandler()
stout.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s',datefmt='%m/%d/%Y %I:%M:%S %p')

stout.setFormatter(formatter)
logger.addHandler(stout)

logger.debug("hello")
logger.info('world')