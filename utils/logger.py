from loguru import logger
import os, sys


if os.path.exists("logs"):
    os.makedirs("logs")


logger.remove() #Remove default logger
logger.add(sys.stdout, level="INFO", format="<green>{time}</green> <level>{message}</level>")
logger.add("logs/multi_agent_system.log", rotation="1 MB", retention="10 days", level="DEBUG", format="{time} {level} {message}")
