#!/usr/bin/env python3
"""
Command-Line Calculator Utility
A simple calculator for addition and subtraction operations
"""

from abc import ABC, abstractmethod
import sys
from typing import Union


# Interface Definitions
class IInputValidator(ABC):
    """Interface for input validation"""
    @abstractmethod
    def validate_input(self, input_str: str) -> bool:
        """Validate if input is numeric"""
        pass


class ICalculatorEngine(ABC):
    """Interface for calculator operations"""
    @abstractmethod
    def add_numbers(self, num1: float, num2: float) -> float:
        """Add two numbers"""
        pass
    
    @abstractmethod
    def subtract_numbers(self, num1: float, num2: float) -> float:
        """Subtract two numbers"""
        pass


class IOutputFormatter(ABC):
    """Interface for output formatting"""
    @abstractmethod
    def format_output(self, result: float) -> str:
        """Format the result for display"""
        pass


class IErrorHandler(ABC):
    """Interface for error handling"""
    @abstractmethod
    def handle_error(self, message: str) -> str:
        """Handle and format error messages"""
        pass


# Implementation Classes
class InputValidator(IInputValidator):
    """Validates user input to ensure it's numeric"""
    
    def validate_input(self, input_str: str) -> bool:
        """
        Validate if the input string can be converted to a float
        
        Args:
            input_str (str): The input string to validate
            
        Returns:
            bool: True if input is valid numeric, False otherwise
        """
        try:
            float(input_str.strip())
            return True
        except ValueError:
            return False
    
    def parse_number(self, input_str: str) -> float:
        """
        Parse a validated input string to float
        
        Args:
            input_str (str): The input string to parse
            
        Returns:
            float: The parsed number
            
        Raises:
            ValueError: If input is not a valid number
        """
        try:
            return float(input_str.strip())
        except ValueError:
            raise ValueError(f"Invalid number format: {input_str}")


class CalculatorEngine(ICalculatorEngine):
    """Core calculator engine for mathematical operations"""
    
    def add_numbers(self, num1: float, num2: float) -> float:
        """
        Add two numbers
        
        Args:
            num1 (float): First number
            num2 (float): Second number
            
        Returns:
            float: Sum of the two numbers
        """
        return num1 + num2
    
    def subtract_numbers(self, num1: float, num2: float) -> float:
        """
        Subtract second number from first number
        
        Args:
            num1 (float): First number (minuend)
            num2 (float): Second number (subtrahend)
            
        Returns:
            float: Difference (num1 - num2)
        """
        return num1 - num2


class OutputFormatter(IOutputFormatter):
    """Formats output for display to user"""
    
    def format_output(self, result: float) -> str:
        """
        Format the calculation result for display
        
        Args:
            result (float): The calculation result
            
        Returns:
            str: Formatted result string
        """
        # Format to remove unnecessary decimal places
        if result.is_integer():
            return f"Result: {int(result)}"
        else:
            return f"Result: {result:.6g}"  # Up to 6 significant digits
    
    def format_welcome_message(self) -> str:
        """Return welcome message"""
        return """
=== Command-Line Calculator ===
Operations: Addition (+) and Subtraction (-)
Type 'quit' or 'exit' to close the application
"""
    
    def format_operation_prompt(self) -> str:
        """Return operation selection prompt"""
        return "Select operation: [1] Addition (+) [2] Subtraction (-): "


class ErrorHandler(IErrorHandler):
    """Singleton error handler for consistent error messaging"""
    
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ErrorHandler, cls).__new__(cls)
        return cls._instance
    
    def handle_error(self, message: str) -> str:
        """
        Handle and format error messages
        
        Args:
            message (str): The error message
            
        Returns:
            str: Formatted error message
        """
        return f"❌ Error: {message}"
    
    def handle_invalid_input_error(self) -> str:
        """Return formatted invalid input error"""
        return self.handle_error("Invalid input. Please enter a valid number.")
    
    def handle_invalid_operation_error(self) -> str:
        """Return formatted invalid operation error"""
        return self.handle_error("Invalid operation. Please select 1 for addition or 2 for subtraction.")


class Calculator:
    """Main Calculator CLI class"""
    
    def __init__(self):
        """Initialize calculator with all components"""
        self.validator = InputValidator()
        self.engine = CalculatorEngine()
        self.formatter = OutputFormatter()
        self.error_handler = ErrorHandler()
    
    def get_number_input(self, prompt: str) -> Union[float, None]:
        """
        Get and validate number input from user
        
        Args:
            prompt (str): The input prompt message
            
        Returns:
            Union[float, None]: The validated number or None if invalid
        """
        user_input = input(prompt).strip()
        
        # Check for exit commands
        if user_input.lower() in ['quit', 'exit', 'q']:
            return None
        
        if self.validator.validate_input(user_input):
            return self.validator.parse_number(user_input)
        else:
            print(self.error_handler.handle_invalid_input_error())
            return False  # Indicates invalid input (but not exit)
    
    def get_operation_input(self) -> Union[str, None]:
        """
        Get operation choice from user
        
        Returns:
            Union[str, None]: Operation choice or None for exit
        """
        choice = input(self.formatter.format_operation_prompt()).strip()
        
        if choice.lower() in ['quit', 'exit', 'q']:
            return None
        
        if choice in ['1', '2']:
            return choice
        else:
            print(self.error_handler.handle_invalid_operation_error())
            return False  # Indicates invalid input (but not exit)
    
    def perform_calculation(self, num1: float, num2: float, operation: str) -> float:
        """
        Perform the requested calculation
        
        Args:
            num1 (float): First number
            num2 (float): Second number
            operation (str): Operation choice ('1' for add, '2' for subtract)
            
        Returns:
            float: Calculation result
        """
        if operation == '1':
            return self.engine.add_numbers(num1, num2)
        elif operation == '2':
            return self.engine.subtract_numbers(num1, num2)
    
    def display_calculation_summary(self, num1: float, num2: float, operation: str, result: float):
        """
        Display calculation summary
        
        Args:
            num1 (float): First number
            num2 (float): Second number
            operation (str): Operation choice
            result (float): Calculation result
        """
        op_symbol = '+' if operation == '1' else '-'
        op_name = 'Addition' if operation == '1' else 'Subtraction'
        
        print(f"\n--- {op_name} ---")
        print(f"{num1} {op_symbol} {num2} = {result}")
        print(self.formatter.format_output(result))
        print("-" * 20)
    
    def run(self):
        """Main application loop"""
        print(self.formatter.format_welcome_message())
        
        while True:
            try:
                print("\n" + "=" * 30)
                
                # Get first number
                num1 = self.get_number_input("Enter the first number: ")
                if num1 is None:  # User wants to exit
                    break
                elif num1 is False:  # Invalid input, continue loop
                    continue
                
                # Get second number
                num2 = self.get_number_input("Enter the second number: ")
                if num2 is None:  # User wants to exit
                    break
                elif num2 is False:  # Invalid input, continue loop
                    continue
                
                # Get operation
                operation = self.get_operation_input()
                if operation is None:  # User wants to exit
                    break
                elif operation is False:  # Invalid input, continue loop
                    continue
                
                # Perform calculation
                result = self.perform_calculation(num1, num2, operation)
                
                # Display results
                self.display_calculation_summary(num1, num2, operation, result)
                
                # Ask if user wants to continue
                continue_choice = input("\nDo you want to perform another calculation? (y/n): ").strip().lower()
                if continue_choice in ['n', 'no', 'quit', 'exit']:
                    break
                    
            except KeyboardInterrupt:
                print("\n\nOperation cancelled by user.")
                break
            except Exception as e:
                print(self.error_handler.handle_error(f"Unexpected error: {str(e)}"))
                continue
        
        print("\nThank you for using the Command-Line Calculator! 👋")
        sys.exit(0)


def main():
    """Entry point of the application"""
    calculator = Calculator()
    calculator.run()


if __name__ == "__main__":
    main()
