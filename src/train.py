import logging

logging.basicConfig(filename="error_logs.txt", level=logging.ERROR)


def main():
    """Execute model training."""
    try:
        print("Starting training...")
        # Intentionally cause an error to generate artifacts
        raise ValueError("Simulated training failure for artifact testing")
    except Exception as e:
        logging.error(f"Training failed: {e}")
        raise


if __name__ == "__main__":
    main()
