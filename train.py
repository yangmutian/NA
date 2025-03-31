"""
Main training script for material properties prediction model.
"""
import os
import argparse
from src.models.trainer import ModelTrainer
from src.data.processor import DataProcessor
from src.utils.logger import setup_logger
from src.utils.helpers import ensure_directory_exists
from config.settings import TRAINING_CONFIG

logger = setup_logger("material_analysis.train")

def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description='Train a material property prediction model')
    
    parser.add_argument('--data-path', type=str, default=TRAINING_CONFIG['DATA_PATH'],
                        help=f'Path to the training data CSV file (default: {TRAINING_CONFIG["DATA_PATH"]})')
    parser.add_argument('--model-output', type=str, default=TRAINING_CONFIG['MODEL_OUTPUT_PATH'],
                        help=f'Path to save the trained model (default: {TRAINING_CONFIG["MODEL_OUTPUT_PATH"]})')
    parser.add_argument('--test-size', type=float, default=TRAINING_CONFIG['TEST_SIZE'],
                        help=f'Proportion of the dataset to include in the test split (default: {TRAINING_CONFIG["TEST_SIZE"]})')
    parser.add_argument('--random-state', type=int, default=TRAINING_CONFIG['RANDOM_STATE'],
                        help=f'Random state for reproducibility (default: {TRAINING_CONFIG["RANDOM_STATE"]})')
    
    return parser.parse_args()

def main():
    """Main function to train the model."""
    logger.info("Starting model training process")
    
    # Parse arguments
    args = parse_arguments()
    
    # Verify that training data exists
    if not os.path.exists(args.data_path):
        logger.error(f"Training data file not found: {args.data_path}")
        print(f"Error: Training data file not found: {args.data_path}")
        return
    
    logger.info(f"Training with data from: {args.data_path}")
    
    # Initialize data processor
    data_processor = DataProcessor()
    
    try:
        # Load and process data
        logger.info("Loading and processing training data")
        X_train, X_test, y_train, y_test = data_processor.load_and_split_data(
            args.data_path, 
            target_column='label',
            test_size=args.test_size,
            random_state=args.random_state
        )
        
        # Initialize model trainer
        trainer = ModelTrainer(random_state=args.random_state)
        
        # Train model
        logger.info("Training model")
        trainer.train(X_train, y_train)
        
        # We still evaluate the model but don't display metrics
        trainer.evaluate(X_test, y_test, log_metrics=False)
        
        # Save model
        model_path = args.model_output
        ensure_directory_exists(model_path)
        trainer.save_model(model_path)
        logger.info(f"Model saved to: {model_path}")
        print(f"Model successfully trained and saved to: {model_path}")
        
        logger.info("Training process completed successfully")
        
    except Exception as e:
        logger.error(f"Error during training: {str(e)}")
        print(f"Error during training: {str(e)}")
        import traceback
        logger.error(traceback.format_exc())

if __name__ == "__main__":
    main()
