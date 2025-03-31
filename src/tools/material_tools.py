"""
Tool implementations for SimpleReActFramework.
"""
import os
import traceback
import pandas as pd
from matminer.featurizers.composition import ElementProperty
from catboost import CatBoostClassifier
from pymatgen.core.composition import Composition
from typing import List, Dict, Any, Optional

from src.utils.helpers import sanitize_path, safe_composition_conversion, ensure_directory_exists
from src.utils.logger import setup_logger

logger = setup_logger("material_analysis.tools.material_tools")

class MaterialTools:
    """Tools for material analysis operations."""
    
    def __init__(self):
        """Initialize tools with empty state."""
        self.data = None
        self.df_magpie = None
        self.X = None
        self.rule_match_materials = None
    
    def read_data(self, file_path: str) -> str:
        """
        Read material expression data
        
        Args:
            file_path: Data file path
            
        Returns:
            Operation result message
        """
        file_path = sanitize_path(file_path)
        logger.info(f"Reading data file: {file_path}")
        
        try:
            if not os.path.exists(file_path):
                error_msg = f"File does not exist: {file_path}"
                logger.error(error_msg)
                return error_msg
                
            self.data = pd.read_csv(file_path)
            # Convert composition column
            self.data['composition'] = self.data['Substance'].apply(
                lambda x: safe_composition_conversion(x)
            )
            # Use magpie feature extractor
            ep_featurizer = ElementProperty.from_preset('magpie')
            self.df_magpie = ep_featurizer.featurize_dataframe(self.data, col_id='composition')
            self.X = self.df_magpie.drop(['Substance', 'composition'], axis=1)
            
            logger.info(f"Successfully read material expressions, shape: {self.data.shape}")
            return f"Successfully read material expressions, total {len(self.data)} records"
        except Exception as e:
            error_msg = f"Failed to read data: {str(e)}"
            logger.error(f"{error_msg}\n{traceback.format_exc()}")
            return error_msg
        
    def model_predict(self, model_path: str) -> str:
        """
        Predict material properties
        
        Args:
            model_path: Model file path
            
        Returns:
            Operation result message
        """
        model_path = sanitize_path(model_path)
        logger.info(f"Using model for prediction: {model_path}")
        
        try:
            if self.data is None or self.X is None:
                error_msg = "Please read data first"
                logger.error(error_msg)
                return error_msg
                
            if not os.path.exists(model_path):
                error_msg = f"Model file does not exist: {model_path}"
                logger.error(error_msg)
                return error_msg
                
            loaded_model = CatBoostClassifier()
            loaded_model.load_model(model_path)
            y_pred = loaded_model.predict_proba(self.X)[:,1]
            self.data['pred'] = y_pred
            self.data = self.data.sort_values(by=['pred'], ascending=False)
            
            logger.info("Model prediction completed")
            return "Model prediction completed successfully"
        except Exception as e:
            error_msg = f"Model prediction failed: {str(e)}"
            logger.error(f"{error_msg}\n{traceback.format_exc()}")
            return error_msg
        
    def rule_match(self, rule_elements: str) -> str:
        """
        Match materials containing specific elements
        
        Args:
            rule_elements: A comma-separated list of element symbols, e.g., 'Fe,Co,Ni'
            
        Returns:
            Operation result message
        """
        logger.info(f"Performing rule matching: {rule_elements}")
        try:
            if self.data is None:
                error_msg = "Please read data first"
                logger.error(error_msg)
                return error_msg
                
            rule_elements = [element.strip() for element in rule_elements.split(',')]
            
            def contains_element(comp):
                if not isinstance(comp, Composition):
                    return False
                
                elements = comp.elements
                
                for element in elements:
                    if element.symbol in rule_elements:
                        return True
                
                return False

            self.data['rule_match'] = self.data['composition'].apply(contains_element)
            self.rule_match_materials = self.data[self.data['rule_match'] == True]
            
            match_count = len(self.rule_match_materials)
            logger.info(f"Rule matching completed, found {match_count} matching materials")
            return f"Rule matching completed successfully, found {match_count} materials containing specified elements"
        except Exception as e:
            error_msg = f"Rule matching failed: {str(e)}"
            logger.error(f"{error_msg}\n{traceback.format_exc()}")
            return error_msg
    
    def save_result(self, save_path: str) -> str:
        """
        Save matched materials to a CSV file
        
        Args:
            save_path: File path to save the result
            
        Returns:
            Operation result message
        """
        save_path = sanitize_path(save_path)
        logger.info(f"Saving results to: {save_path}")
        
        try:
            if self.rule_match_materials is None:
                error_msg = "Please perform rule matching first"
                logger.error(error_msg)
                return error_msg
                
            # Ensure directory exists
            ensure_directory_exists(save_path)
            
            self.rule_match_materials.to_csv(save_path, index=False)
            
            logger.info(f"Results saved to {save_path}")
            return f"Results successfully saved to {save_path}, total {len(self.rule_match_materials)} records"
        except Exception as e:
            error_msg = f"Failed to save results: {str(e)}"
            logger.error(f"{error_msg}\n{traceback.format_exc()}")
            return error_msg 