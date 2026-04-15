"""
ML Training script with MLflow tracking and error logging.
"""

import logging
import mlflow

logging.basicConfig(filename="error_logs.txt", level=logging.ERROR)


def main():
    """Execute model training and log metrics to MLflow."""
    # Set MLflow tracking URI (uses local ./mlruns directory)
    mlflow.set_tracking_uri("file:./mlruns")
    
    # Start MLflow experiment
    mlflow.set_experiment("ML_A6_Training")
    
    try:
        with mlflow.start_run():
            print("Starting training...")
            
            # Log parameters
            mlflow.log_param("model_type", "sklearn_classifier")
            mlflow.log_param("dataset", "synthetic")
            
            # Simulate training
            accuracy = 0.95
            precision = 0.93
            recall = 0.92
            f1_score = 0.925
            
            # Log metrics to MLflow
            mlflow.log_metric("accuracy", accuracy)
            mlflow.log_metric("precision", precision)
            mlflow.log_metric("recall", recall)
            mlflow.log_metric("f1_score", f1_score)
            
            # Save training logs
            with open("training_logs.txt", "w") as f:
                f.write(f"Training Results:\n")
                f.write(f"Accuracy: {accuracy}\n")
                f.write(f"Precision: {precision}\n")
                f.write(f"Recall: {recall}\n")
                f.write(f"F1 Score: {f1_score}\n")
            
            # Log artifact
            mlflow.log_artifact("training_logs.txt")
            
            print(f"Training complete. Accuracy: {accuracy}")
            print("Metrics logged to MLflow!")
            
    except Exception as e:
        logging.error(f"Training failed: {e}")
        raise


if __name__ == "__main__":
    main()
