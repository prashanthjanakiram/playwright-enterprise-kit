"""Enterprise-grade logging for Playwright tests."""

import logging
import sys
from datetime import datetime

def setup_logger():
    """Configure structured logging for tests."""
    logger = logging.getLogger('playwright-kit')
    logger.setLevel(logging.INFO)
    
    # Console handler with timestamp
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter(
        '%(asctime)s | %(levelname)s | %(message)s',
        datefmt='%H:%M:%S'
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    
    return logger

# Global logger instance
logger = setup_logger()