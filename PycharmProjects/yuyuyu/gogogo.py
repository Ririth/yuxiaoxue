# -*- coding: utf-8 -*- 
# @Time : 2021/4/26 上午11:31 
# @Author : yuxiaoxue
# @File : gogogo.py

import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

logger.info("Start print log")
logger.debug("Do something")
logger.warning("Something maybe fail.")

logger.info("Finish")
