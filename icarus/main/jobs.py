import logging
from typing import AnyStr, Callable
from datetime import datetime



def kick_off(
    app_name: AnyStr,
    job_name: AnyStr,
    function: Callable,
):
    
    try:
        logging.info(f"{job_name} started at {datetime.now()}")
        function()
        logging.info(f"{job_name} finished at {datetime.now()}")

    except Exception as e:
        error_string = "Exception during " + job_name + str(e)
        logging.error(error_string)
        raise e
