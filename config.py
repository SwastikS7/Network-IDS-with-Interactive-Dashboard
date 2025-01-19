import os

class Config:
    # Base directory setup
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    # Network paths and directories
    LOG_DIR = os.path.join(BASE_DIR, 'network_ids', 'logs')
    LOG_PATH = os.path.join(LOG_DIR, 'ids_logs.log')
    DATABASE_PATH = os.path.join(BASE_DIR, 'ids_web', 'ids_alerts.db')

    # Web server configuration
    HOST = '0.0.0.0'
    PORT = 5000
    DEBUG = True

    # IDS configuration
    INTERFACE = "Wi-Fi"
    PORT_SCAN_THRESHOLD = 10
    TIME_WINDOW = 60
    MAX_HISTORY = 1000

    # Create necessary directories
    @classmethod
    def create_directories(cls):
        os.makedirs(cls.LOG_DIR, exist_ok=True)


# Create required directories when config is imported
Config.create_directories()