"""
ML Training script with error logging.
"""

import logging

logging.basicConfig(filename="error_logs.txt", level=logging.ERROR)


def main():
    """Execute model training and log errors."""
    try:
        print("Starting training...")
        # Intentionally cause an error to generate error logs
        raise ValueError("Simulated training failure to test artifact upload")
    except Exception as e:
        logging.error(f"Training failed: {e}")
        raise


if __name__ == "__main__":
    main()
