import sys
sys.path.append(r'C:\Users\Vinot\Desktop\CoincapAPIETL\src')

import unittest
from unittest.mock import patch
import pandas as pd
from sqlalchemy import create_engine
from load_data import load_data  # Replace 'your_module' with the actual name of your module

class TestDataLoading(unittest.TestCase):
    @patch("your_module.create_engine")  # Replace 'your_module' with the actual name of your module
    def test_load_data_success(self, mock_create_engine):
        # Mock the create_engine method to avoid actually connecting to the database
        mock_engine = mock_create_engine.return_value
        mock_engine.return_value = None  # You can modify this if you want to set up a specific behavior for the engine

        # Create a sample DataFrame
        sample_data = {'column1': [1, 2, 3], 'column2': ['a', 'b', 'c']}
        df = pd.DataFrame(sample_data)

        # Call the function
        result = load_data(df)

        # Assert that the correct methods were called
        mock_create_engine.assert_called_once_with("postgresql://postgres:1221@localhost:5433/postgres")
        mock_engine.assert_called_once()
        mock_engine.return_value.to_sql.assert_called_once_with('coincap_assets', con=mock_engine.return_value, if_exists='replace', index=False)
        
        # Assert the result
        self.assertEqual(result, "Data loaded successfully to PostgreSQL.")

    @patch("your_module.create_engine")
    def test_load_data_failure(self, mock_create_engine):
        # Mock the create_engine method to raise an exception
        mock_engine = mock_create_engine.return_value
        mock_engine.return_value.to_sql.side_effect = Exception("Mocked database error")

        # Create a sample DataFrame
        sample_data = {'column1': [1, 2, 3], 'column2': ['a', 'b', 'c']}
        df = pd.DataFrame(sample_data)

        # Call the function
        result = load_data(df)

        # Assert that the correct methods were called
        mock_create_engine.assert_called_once_with("postgresql://postgres:1221@localhost:5433/postgres")
        mock_engine.assert_called_once()
        mock_engine.return_value.to_sql.assert_called_once_with('coincap_assets', con=mock_engine.return_value, if_exists='replace', index=False)

        # Assert the result
        self.assertIn("Error loading data to PostgreSQL:", result)

if __name__ == '__main__':
    unittest.main()
