# Python Math Calculator

A production-ready command-line calculator utility for basic math operations (addition and subtraction) built using Software Development Life Cycle (SDLC) best practices.

## 🚀 Features

- **Simple Command-Line Interface**: Easy-to-use interactive calculator
- **Basic Math Operations**: Addition and subtraction of two numbers
- **Input Validation**: Comprehensive validation to ensure numeric inputs
- **Error Handling**: Graceful error handling with informative messages
- **Production Ready**: Built with SDLC best practices, comprehensive testing, and clean architecture
- **Extensible Design**: Object-oriented architecture allows easy addition of new operations

## 📋 Requirements

- Python 3.7 or higher
- pytest (for running tests)

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/shyamnarayan2001/python-math-calculator-1.git
cd python-math-calculator-1
```

2. Install dependencies (optional, for testing):
```bash
pip install -r requirements.txt
```

## 🎮 Usage

### Running the Calculator

```bash
python calculator_main.py
```

### Example Session

```
=== Command-Line Calculator ===
Operations: Addition (+) and Subtraction (-)
Type 'quit' or 'exit' to close the application

==============================
Enter the first number: 15
Enter the second number: 7
Select operation: [1] Addition (+) [2] Subtraction (-): 1

--- Addition ---
15.0 + 7.0 = 22.0
Result: 22
--------------------

Do you want to perform another calculation? (y/n): n

Thank you for using the Command-Line Calculator! 👋
```

## 🧪 Testing

Run the comprehensive test suite:

```bash
# Run all tests
python -m pytest test_calculator.py -v

# Run tests with coverage
python -m pytest test_calculator.py --cov=calculator_main --cov-report=html

# Run specific test class
python -m pytest test_calculator.py::TestCalculatorEngine -v
```

## 🏗️ Architecture

The calculator follows a clean, object-oriented architecture with clear separation of concerns:

### Core Components

- **CLI Module**: Manages user interactions and displays prompts
- **Input Validator**: Validates user inputs and handles input errors
- **Calculator Engine**: Contains methods for addition and subtraction
- **Error Handler**: Generates error messages for invalid inputs (Singleton pattern)
- **Output Formatter**: Formats the output for user readability

### Design Patterns Used

- **Singleton Pattern**: ErrorHandler ensures consistent error messaging
- **Strategy Pattern**: CalculatorEngine allows easy addition of new operations
- **Interface Segregation**: Clear interface definitions for each component

## 📁 Project Structure

```
python-math-calculator-1/
├── calculator_main.py      # Main application file
├── test_calculator.py      # Comprehensive test suite
├── requirements.txt        # Python dependencies
├── README.md              # Project documentation
├── .gitignore            # Git ignore rules
└── LICENSE               # MIT License
```

## 🎯 Key Features

### Input Validation
- Validates numeric inputs (integers and floats)
- Handles whitespace and formatting
- Provides clear error messages for invalid inputs

### Error Handling
- Graceful handling of invalid inputs
- User-friendly error messages
- Keyboard interrupt handling
- Robust exception management

### User Experience
- Clear prompts and instructions
- Multiple exit options (`quit`, `exit`, `q`)
- Calculation summaries with operation details
- Continue/exit options after each calculation

## 📊 Test Coverage

The project includes comprehensive unit tests covering:

- ✅ Input validation (valid/invalid inputs, edge cases)
- ✅ Calculator operations (addition, subtraction, floating-point precision)
- ✅ Output formatting (integers, floats, precision handling)
- ✅ Error handling (singleton pattern, error messages)
- ✅ Main calculator workflow (user interactions, exit conditions)
- ✅ Integration tests (complete calculation workflows)
- ✅ Edge cases and error recovery

## 🔄 SDLC Process

This project was developed following a complete Software Development Life Cycle:

1. **Requirements Analysis**: Generated comprehensive Business Requirements Document (BRD)
2. **System Design**: Created High-Level Design (HLD) and Low-Level Design (LLD)
3. **Implementation**: Developed production-ready code following design specifications
4. **Testing**: Comprehensive unit and integration test suite
5. **Documentation**: Complete project documentation and usage guides

## 🚦 Getting Started

1. **Quick Start**: Run `python calculator_main.py` to start calculating immediately
2. **Development**: Check the test suite with `python -m pytest test_calculator.py -v`
3. **Extend**: Add new operations by extending the `CalculatorEngine` class

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-operation`)
3. Make your changes and add tests
4. Run the test suite to ensure everything passes
5. Commit your changes (`git commit -am 'Add new operation'`)
6. Push to the branch (`git push origin feature/new-operation`)
7. Create a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ✨ Acknowledgments

- Built using SDLC Agent for comprehensive requirements and design documentation
- Follows Python best practices and PEP 8 style guidelines
- Implements production-ready error handling and user experience patterns

## 📞 Support

If you encounter any issues or have questions:

1. Check the existing issues on GitHub
2. Create a new issue with detailed description
3. Include steps to reproduce any bugs

---

**Made with ❤️ using SDLC best practices**