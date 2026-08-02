import logging
import os
from datetime import datetime


# Create logs folder if it doesn't exist
os.makedirs("logs", exist_ok=True)

# Generate a unique log file name
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
log_file = f"logs/test_{timestamp}.log"

# Configure logging
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

# Create logger
logger = logging.getLogger(__name__)