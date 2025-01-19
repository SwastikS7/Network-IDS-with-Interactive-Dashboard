import argparse
from network_ids.network_ids import NetworkIDS
from ids_web.app import app
from config import Config
import multiprocessing
import sys

def run_ids():
    ids = NetworkIDS()
    ids.start()


def run_web():
    # Modified web server configuration for Windows compatibility
    app.run(
        host='127.0.0.1',  # Using localhost instead of 0.0.0.0
        port=5000,
        debug=False  # Disable debug mode for multiprocessing
    )


if __name__ == "__main__":
    # Set start method for Windows
    multiprocessing.freeze_support()

    parser = argparse.ArgumentParser(description='Run Network IDS and Dashboard')
    parser.add_argument('--component', choices=['all', 'ids', 'web'],
                        default='all', help='Component to run')

    args = parser.parse_args()

    if args.component in ['all', 'ids']:
        ids_process = multiprocessing.Process(target=run_ids)
        ids_process.start()

    if args.component in ['all', 'web']:
        # Run web directly if it's the only component
        if args.component == 'web':
            run_web()
        else:
            web_process = multiprocessing.Process(target=run_web)
            web_process.start()