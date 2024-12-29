# Converter Program
#### Video Demo:  

https://youtu.be/smv0Pqr9xyc

#### Description:

The Converter Program is designed as the final project for CS50P and serves as a robust, user-friendly tool for performing a wide variety of unit conversions. This Python-based, command-line tool supports conversions in ten categories: lengths, weights, volumes, temperatures, areas, speeds, times, energies, powers, and currencies.

With its flexible interface, the program allows users to perform conversions seamlessly using either command-line arguments for quick results or an interactive mode for a guided, step-by-step experience. Its lightweight design ensures accessibility and ease of use on any platform with Python installed, making it an excellent resource for both casual users and professionals needing precise, reliable conversions.

---
## Features

- **Comprehensive Conversion Options**: The program supports conversions across 10 categories:
  - Lengths/Distances (e.g., cm to inches, km to miles)
  - Mass/Weight (e.g., kg to pounds, ounces to grams)
  - Volume (e.g., liters to gallons, mL to fluid ounces)
  - Temperature (e.g., Celsius to Fahrenheit, Kelvin to Celsius)
  - Area (e.g., square meters to square feet, acres to square meters)
  - Speed/Velocity (e.g., mph to km/h, knots to mph)
  - Time (e.g., hours to minutes, days to weeks)
  - Energy (e.g., joules to calories, kWh to joules)
  - Power (e.g., watts to horsepower, kW to watts)
  - Currency (e.g., USD to EUR, GBP to USD)

- **Interactive Mode**: The program can prompt users step-by-step to select a conversion type, input values, and view results interactively.

- **Command-Line Arguments**: Allows users to quickly perform conversions directly from the terminal by specifying conversion flags and values.

- **Robust Error Handling**: Handles invalid inputs gracefully, including negative numbers where appropriate, and provides clear feedback to users.

- **Customizable Restart Option**: Users can choose to restart the program for multiple conversions without exiting.

## Installation

To use the Converter Program, you need Python installed on your machine. It also requires the `pytest` library for running tests.

1. **Clone the repository**:
   ```bash
   git clone <repository_url>
   cd converter_program
   ```

2. **Install dependencies**:
   Ensure `pytest` is installed by running:
   ```bash
   pip install -r requirements.txt
   ```
   The `requirements.txt` file includes only `pytest` for testing purposes.

## Usage

The Converter Program can be run in two modes: **interactive mode** and **command-line mode**.

### Interactive Mode

Run the program without any arguments to enter the interactive mode:
```bash
python converter.py
```
In this mode, the program will:
1. Display a menu of conversion categories.
2. Prompt you to select a category.
3. Ask for the value to be converted.
4. Perform the conversion and display the results.
5. Offer the option to restart for additional conversions.

### Command-Line Mode

You can use flags to perform quick conversions directly from the terminal. Each conversion category has its own flag, followed by the value to convert. For example:
```bash
python converter.py -len 10
```
This converts 10 centimeters to other length units. Flags for each category include:
- `-len`: Length/Distance
- `-mass`: Mass/Weight
- `-vol`: Volume
- `-temp`: Temperature
- `-area`: Area
- `-speed`: Speed/Velocity
- `-time`: Time
- `-energy`: Energy
- `-power`: Power
- `-currency`: Currency

### Example

Convert 5 kilograms to pounds and other weight units:
```bash
python converter.py -mass 5
```
Expected output:
```
Welcome to the Weight/Mass-Converter
5 kg to lb      =    11.02 lb
5 lb to kg      =    2.27 kg
...
```

## Testing

The program includes unit tests for all conversion functions. To run the tests, execute:
```bash
pytest
```
This validates the correctness of all conversion calculations, including edge cases like zero and negative inputs.

## File Structure

- **`converter.py`**: Main program file containing the conversion logic and interactive/command-line interfaces.
- **`test_project.py`**: Contains unit tests for all conversion functions using `pytest`.
- **`art.py`**: Contains ASCII art.
- **`requirements.txt`**: Lists required dependencies (e.g., `pytest`).
- **`README.md`**: Documentation file (this file).

## Supported Conversions

### Length/Distance
- Centimeters to Inches
- Kilometers to Miles
- Yards to Meters
- And more...

### Mass/Weight
- Kilograms to Pounds
- Ounces to Grams
- Tons to Kilograms
- And more...

### Temperature
- Celsius to Fahrenheit
- Kelvin to Celsius
- Fahrenheit to Kelvin
- And more...

### Others
Each category includes comprehensive units for conversions. Refer to the source code for a complete list.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve the program.

## License

This project is licensed under the MIT License. See `LICENSE` for details.

## Contact
For questions or suggestions, please contact:
- Email: eikehanel@gmail.com
- GitHub: https://github.com/EikeHanel

Happy converting!
