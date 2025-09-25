#!/usr/bin/env python3
"""
Unit Tests for Command-Line Calculator Utility
Comprehensive test suite covering all components
"""

import pytest
import sys
from io import StringIO
from unittest.mock import patch, MagicMock
import os

# Add the parent directory to the path to import the main module
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from calculator_main import (
    InputValidator,
    CalculatorEngine,
    OutputFormatter,
    ErrorHandler,
    Calculator
)


class TestInputValidator:
    """Test cases for InputValidator class"""
    
    def setup_method(self):
        """Setup test instance"""
        self.validator = InputValidator()
    
    def test_validate_valid_integer(self):
        """Test validation of valid integer input"""
        assert self.validator.validate_input("42") is True
        assert self.validator.validate_input("0") is True
        assert self.validator.validate_input("-42") is True
    
    def test_validate_valid_float(self):
        """Test validation of valid float input"""
        assert self.validator.validate_input("42.5") is True
        assert self.validator.validate_input("0.0") is True
        assert self.validator.validate_input("-42.5") is True
        assert self.validator.validate_input("3.14159") is True
    
    def test_validate_valid_input_with_whitespace(self):
        """Test validation with whitespace"""
        assert self.validator.validate_input("  42  ") is True
        assert self.validator.validate_input("\t42.5\n") is True
    
    def test_validate_invalid_input(self):
        """Test validation of invalid input"""
        assert self.validator.validate_input("abc") is False
        assert self.validator.validate_input("12abc") is False
        assert self.validator.validate_input("") is False
        assert self.validator.validate_input("   ") is False
        assert self.validator.validate_input("12.34.56") is False
    
    def test_parse_number_valid(self):
        """Test parsing valid numbers"""
        assert self.validator.parse_number("42") == 42.0
        assert self.validator.parse_number("42.5") == 42.5
        assert self.validator.parse_number("-42") == -42.0
        assert self.validator.parse_number("  42.5  ") == 42.5
    
    def test_parse_number_invalid(self):
        """Test parsing invalid numbers raises ValueError"""
        with pytest.raises(ValueError):
            self.validator.parse_number("abc")
        with pytest.raises(ValueError):
            self.validator.parse_number("12abc")


class TestCalculatorEngine:
    """Test cases for CalculatorEngine class"""
    
    def setup_method(self):
        """Setup test instance"""
        self.engine = CalculatorEngine()
    
    def test_add_numbers_positive(self):
        """Test addition with positive numbers"""
        assert self.engine.add_numbers(5, 3) == 8
        assert self.engine.add_numbers(0, 0) == 0
        assert self.engine.add_numbers(10.5, 2.5) == 13.0
    
    def test_add_numbers_negative(self):
        """Test addition with negative numbers"""
        assert self.engine.add_numbers(-5, -3) == -8
        assert self.engine.add_numbers(-5, 3) == -2
        assert self.engine.add_numbers(5, -3) == 2
    
    def test_add_numbers_float(self):
        """Test addition with floating point numbers"""
        assert self.engine.add_numbers(1.5, 2.5) == 4.0
        assert self.engine.add_numbers(3.14, 2.86) == pytest.approx(6.0)
    
    def test_subtract_numbers_positive(self):
        """Test subtraction with positive numbers"""
        assert self.engine.subtract_numbers(5, 3) == 2
        assert self.engine.subtract_numbers(10, 10) == 0
        assert self.engine.subtract_numbers(10.5, 2.5) == 8.0
    
    def test_subtract_numbers_negative(self):
        """Test subtraction with negative numbers"""
        assert self.engine.subtract_numbers(-5, -3) == -2
        assert self.engine.subtract_numbers(-5, 3) == -8
        assert self.engine.subtract_numbers(5, -3) == 8
    
    def test_subtract_numbers_float(self):
        """Test subtraction with floating point numbers"""
        assert self.engine.subtract_numbers(5.5, 2.5) == 3.0
        assert self.engine.subtract_numbers(3.14, 1.14) == pytest.approx(2.0)


class TestOutputFormatter:
    """Test cases for OutputFormatter class"""
    
    def setup_method(self):
        """Setup test instance"""
        self.formatter = OutputFormatter()
    
    def test_format_output_integer(self):
        """Test formatting integer results"""
        assert self.formatter.format_output(42.0) == "Result: 42"
        assert self.formatter.format_output(-42.0) == "Result: -42"
        assert self.formatter.format_output(0.0) == "Result: 0"
    
    def test_format_output_float(self):
        """Test formatting float results"""
        assert self.formatter.format_output(42.5) == "Result: 42.5"
        assert self.formatter.format_output(-42.5) == "Result: -42.5"
        assert self.formatter.format_output(3.14159) == "Result: 3.14159"
    
    def test_format_output_precision(self):
        """Test formatting with precision limits"""
        assert self.formatter.format_output(3.14159265359) == "Result: 3.14159"
        assert self.formatter.format_output(1000000.0) == "Result: 1000000"
    
    def test_format_welcome_message(self):
        """Test welcome message formatting"""
        message = self.formatter.format_welcome_message()
        assert "Command-Line Calculator" in message
        assert "Addition" in message
        assert "Subtraction" in message
        assert "quit" in message or "exit" in message
    
    def test_format_operation_prompt(self):
        """Test operation prompt formatting"""
        prompt = self.formatter.format_operation_prompt()
        assert "1" in prompt
        assert "2" in prompt
        assert "Addition" in prompt or "+" in prompt
        assert "Subtraction" in prompt or "-" in prompt


class TestErrorHandler:
    """Test cases for ErrorHandler class (Singleton)"""
    
    def test_singleton_pattern(self):
        """Test that ErrorHandler implements singleton pattern"""
        handler1 = ErrorHandler()
        handler2 = ErrorHandler()
        assert handler1 is handler2
    
    def test_handle_error(self):
        """Test generic error handling"""
        handler = ErrorHandler()
        error_msg = handler.handle_error("Test error message")
        assert "Error:" in error_msg
        assert "Test error message" in error_msg
    
    def test_handle_invalid_input_error(self):
        """Test invalid input error handling"""
        handler = ErrorHandler()
        error_msg = handler.handle_invalid_input_error()
        assert "Error:" in error_msg
        assert "Invalid input" in error_msg
    
    def test_handle_invalid_operation_error(self):
        """Test invalid operation error handling"""
        handler = ErrorHandler()
        error_msg = handler.handle_invalid_operation_error()
        assert "Error:" in error_msg
        assert "Invalid operation" in error_msg


class TestCalculator:
    """Test cases for main Calculator class"""
    
    def setup_method(self):
        """Setup test instance"""
        self.calculator = Calculator()
    
    def test_calculator_initialization(self):
        """Test calculator components are initialized"""
        assert self.calculator.validator is not None
        assert self.calculator.engine is not None
        assert self.calculator.formatter is not None
        assert self.calculator.error_handler is not None
    
    def test_get_number_input_valid(self):
        """Test getting valid number input"""
        with patch('builtins.input', return_value='42'):
            result = self.calculator.get_number_input("Enter number: ")
            assert result == 42.0
    
    def test_get_number_input_invalid(self):
        """Test getting invalid number input"""
        with patch('builtins.input', return_value='abc'):
            with patch('builtins.print'):  # Mock print to avoid output during tests
                result = self.calculator.get_number_input("Enter number: ")
                assert result is False
    
    def test_get_number_input_exit(self):
        """Test exit commands in number input"""
        with patch('builtins.input', return_value='quit'):
            result = self.calculator.get_number_input("Enter number: ")
            assert result is None
        
        with patch('builtins.input', return_value='exit'):
            result = self.calculator.get_number_input("Enter number: ")
            assert result is None
    
    def test_get_operation_input_valid(self):
        """Test getting valid operation input"""
        with patch('builtins.input', return_value='1'):
            result = self.calculator.get_operation_input()
            assert result == '1'
        
        with patch('builtins.input', return_value='2'):
            result = self.calculator.get_operation_input()
            assert result == '2'
    
    def test_get_operation_input_invalid(self):
        """Test getting invalid operation input"""
        with patch('builtins.input', return_value='3'):
            with patch('builtins.print'):  # Mock print to avoid output during tests
                result = self.calculator.get_operation_input()
                assert result is False
    
    def test_get_operation_input_exit(self):
        """Test exit commands in operation input"""
        with patch('builtins.input', return_value='quit'):
            result = self.calculator.get_operation_input()
            assert result is None
    
    def test_perform_calculation_addition(self):
        """Test perform calculation for addition"""
        result = self.calculator.perform_calculation(5, 3, '1')
        assert result == 8
    
    def test_perform_calculation_subtraction(self):
        """Test perform calculation for subtraction"""
        result = self.calculator.perform_calculation(5, 3, '2')
        assert result == 2
    
    @patch('builtins.print')
    def test_display_calculation_summary(self, mock_print):
        """Test display calculation summary"""
        self.calculator.display_calculation_summary(5, 3, '1', 8)
        # Check that print was called (summary was displayed)
        assert mock_print.called
    
    @patch('builtins.input')
    @patch('builtins.print')
    @patch('sys.exit')
    def test_run_single_calculation(self, mock_exit, mock_print, mock_input):
        """Test running a single calculation"""
        # Simulate user inputs: first number, second number, operation, no continue
        mock_input.side_effect = ['5', '3', '1', 'n']
        
        self.calculator.run()
        
        # Verify that sys.exit was called
        mock_exit.assert_called_once_with(0)
    
    @patch('builtins.input')
    @patch('builtins.print')
    @patch('sys.exit')
    def test_run_exit_on_first_number(self, mock_exit, mock_print, mock_input):
        """Test exiting during first number input"""
        mock_input.return_value = 'quit'
        
        self.calculator.run()
        
        mock_exit.assert_called_once_with(0)
    
    @patch('builtins.input')
    @patch('builtins.print')
    @patch('sys.exit')
    def test_run_keyboard_interrupt(self, mock_exit, mock_print, mock_input):
        """Test handling keyboard interrupt"""
        mock_input.side_effect = KeyboardInterrupt()
        
        self.calculator.run()
        
        mock_exit.assert_called_once_with(0)


class TestIntegration:
    """Integration tests for the complete calculator system"""
    
    @patch('builtins.input')
    @patch('builtins.print')
    @patch('sys.exit')
    def test_complete_addition_workflow(self, mock_exit, mock_print, mock_input):
        """Test complete workflow for addition"""
        mock_input.side_effect = ['10', '5', '1', 'n']  # 10 + 5, don't continue
        
        calculator = Calculator()
        calculator.run()
        
        # Verify the calculation was performed and system exited
        mock_exit.assert_called_once_with(0)
    
    @patch('builtins.input')
    @patch('builtins.print')
    @patch('sys.exit')
    def test_complete_subtraction_workflow(self, mock_exit, mock_print, mock_input):
        """Test complete workflow for subtraction"""
        mock_input.side_effect = ['10', '3', '2', 'n']  # 10 - 3, don't continue
        
        calculator = Calculator()
        calculator.run()
        
        # Verify the calculation was performed and system exited
        mock_exit.assert_called_once_with(0)
    
    @patch('builtins.input')
    @patch('builtins.print')
    @patch('sys.exit')
    def test_error_recovery_workflow(self, mock_exit, mock_print, mock_input):
        """Test error recovery and continuation"""
        mock_input.side_effect = [
            'abc',  # Invalid first number
            '10',   # Valid first number
            'xyz',  # Invalid second number
            '5',    # Valid second number
            '1',    # Addition operation
            'n'     # Don't continue
        ]
        
        calculator = Calculator()
        calculator.run()
        
        # Verify the system recovered from errors and completed
        mock_exit.assert_called_once_with(0)


if __name__ == "__main__":
    # Run tests with pytest
    pytest.main([__file__, "-v"])
