"""
Helper utility functions for material analysis framework.
"""
import os
from typing import Any, Optional
from pymatgen.core.composition import Composition

def sanitize_path(path: str) -> str:
    """
    Clean path string by removing newlines and backticks.
    
    Args:
        path: Raw path string
        
    Returns:
        Sanitized path string
    """
    return path.strip().replace('\n', '').replace('`', '')

def safe_composition_conversion(x: Any) -> Optional[Composition]:
    """
    Safely convert a string to a Composition object.
    
    Args:
        x: Input to convert to Composition
        
    Returns:
        Composition object or None if conversion fails
    """
    if not isinstance(x, str):
        return None
    try:
        return Composition(x)
    except Exception:
        return None

def ensure_directory_exists(file_path: str) -> None:
    """
    Ensure the directory for a file path exists.
    
    Args:
        file_path: Path to the file
    """
    directory = os.path.dirname(os.path.abspath(file_path))
    os.makedirs(directory, exist_ok=True) 