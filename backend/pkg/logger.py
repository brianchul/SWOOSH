import logging
from pylogrus import PyLogrus, TextFormatter, CL_BLDYLW

def get_logger():
    logging.setLoggerClass(PyLogrus)

    logger = logging.getLogger(__name__)  # type: PyLogrus
    logger.setLevel(logging.DEBUG)

    formatter = TextFormatter(datefmt='Z', colorize=True)
    # formatter.override_level_names({'CRITICAL': 'CRIT', 'ERROR': 'ERRO', 'WARNING': 'WARN', 'DEBUG': 'DEBU'})
    # formatter.override_colors({'prefix': CL_BLDYLW})

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    return logger