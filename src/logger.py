import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Set default logging level to INFO
DEFAULT_LOG_LEVEL = logging.INFO

# Get the logging level from environment variable if set
log_level = os.getenv('LOG_LEVEL', 'INFO').upper()

print(log_level)

# Configure logging level
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=getattr(logging, log_level, DEFAULT_LOG_LEVEL),
)

logger = logging.getLogger()
logger.setLevel(getattr(logging, log_level, DEFAULT_LOG_LEVEL))