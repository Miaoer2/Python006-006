# -*- coding: utf-8 -*-
from datetime import datetime
import logging
import os


def set_logging(file_name):
    logging.basicConfig(level = logging.INFO,
                        filename = file_name,
                        datefmt = "%Y-%m-%d %H:%M:%S",
                        format = "%(asctime)s  %(name)s  %(levelname)s  "
                                 "%(pathname)s:%(lineno)d  %(message)s")


def get_cur_datetime(fmt="%Y-%m-%d %H:%M:%S"):
    return datetime.now().strftime(fmt)


def create_if_not_exist(path):
    if os.path.exists(path):
        return
    try:
        os.makedirs(path)
    except Exception as e:
        logging.error("mkdir {} error, {}".format(path, e))


def logging_cur_time():
    logging.info(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


if __name__ == "__main__":
    log_dir = os.path.join("log", "python-{}".format(get_cur_datetime("%Y-%m-%d")))
    create_if_not_exist(log_dir)
    set_logging(os.path.join(log_dir, "week01.log"))
    logging_cur_time()


