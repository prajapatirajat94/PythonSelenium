import logging


def test_loggingDemo():
    logger = logging.getLogger(__name__)

    # To create logging file
    filehandler = logging.FileHandler("logfile.log")
    logger.addHandler(filehandler)  # filehandler object

    # create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    filehandler.setFormatter(formatter)


    # We can set level here if you want to see perticular logs
    logger.setLevel(logging.INFO)

    logger.debug("write your logs")
    logger.info("write your logs")
    logger.warning("write your logs")
    logger.error("write your logs")
    logger.critical("write your log")
    return logger



