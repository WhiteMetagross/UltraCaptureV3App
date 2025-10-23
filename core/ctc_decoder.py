"""
CTC decoding for model predictions
"""
import numpy as np
from typing import List


class CTCDecoder:
    """Decode CTC predictions from model output"""

    # BLANK_LABEL = 62 because the model has 63 output classes (0-62)
    # Index 62 is reserved for the CTC blank token
    # Index 0 is the character '0' in the charset
    BLANK_LABEL = 62
    
    @staticmethod
    def decode(predictions: np.ndarray, charset: str) -> str:
        """
        Decode CTC predictions using greedy decoding

        Args:
            predictions: Model output predictions (T, C) where T is time steps, C is charset size
            charset: Character set string

        Returns:
            Decoded text string
        """
        try:
            # Get argmax indices
            indices = np.argmax(predictions, axis=1)

            # Remove consecutive duplicates
            indices = CTCDecoder._remove_duplicates(indices)

            # Remove blank labels
            indices = indices[indices != CTCDecoder.BLANK_LABEL]

            # Convert indices to characters
            text = ''.join([charset[i] for i in indices if i < len(charset)])

            return text

        except Exception as e:
            raise ValueError(f"Error decoding predictions: {e}")
    
    @staticmethod
    def _remove_duplicates(indices: np.ndarray) -> np.ndarray:
        """Remove consecutive duplicate indices"""
        if len(indices) == 0:
            return indices
        
        mask = np.concatenate(([True], indices[1:] != indices[:-1]))
        return indices[mask]
    
    @staticmethod
    def decode_batch(predictions_batch: np.ndarray, charset: str) -> List[str]:
        """
        Decode batch of CTC predictions
        
        Args:
            predictions_batch: Batch of predictions (B, T, C)
            charset: Character set string
            
        Returns:
            List of decoded text strings
        """
        results = []
        for predictions in predictions_batch:
            text = CTCDecoder.decode(predictions, charset)
            results.append(text)
        return results

