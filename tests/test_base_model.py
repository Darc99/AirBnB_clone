#!/usr/bin/python3
"""

"""
import uuid
from models.base_model import BaseModel
import unittest
from datetime import datetime
import uuid


class TestBaseModel(unittest.TestCase):
    """
    
    """
    def test_base_model_id_is_string(self):
        """
        
        """
        bMod = BaseModel()
        self.assertIsInstance(bMod.id, str)

    def test_base_model_created_at_is_datetime(self):
        """
        
        """
        bMod = BaseModel()
        self.assertIsInstance(bMod.created_at, datetime)
        
    def test_base_model_updated_at_is_datetime(self):
        """
        
        """
        bMod = BaseModel()
        self.assertIsInstance(bMod.updated_at, datetime)

