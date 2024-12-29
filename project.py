from art import converter_art
import os
import argparse


def main():
    """Main loop of the converter program."""
    parser = argparse.ArgumentParser(description="Unit Conversion Tool")
    # Adding all command line argument options
    add_conversion_arguments(parser)

    # Parse arguments
    args = parser.parse_args()

    # Main loop to handle user input and conversions
    should_restart = True
    while should_restart:
        print(converter_art)

        if not parse_command_line_args(args):
            prompt_for_conversion()
        else:
            handle_command_line_conversion(args)

        should_restart = prompt_restart(args, parser)


def add_conversion_arguments(parser):
    """Adds the conversion options to the parser with clear descriptions."""
    conversion_flags = [
        ("len", "Lengths/Distance-Converter: Convert between various length and distance units such as cm to inches,"
                " km to miles, etc."),
        ("mass", "Mass/Weight-Converter: Convert between various mass and weight units such as kg to lb,"
                 " oz to g, etc."),
        ("vol", "Volume-Converter: Convert between various volume units such as liters to gallons,"
                " mL to fluid ounces, etc."),
        ("temp", "Temperature-Converter: Convert between temperature units such as Celsius to Fahrenheit,"
                 " Kelvin to Celsius, etc."),
        ("area", "Area-Converter: Convert between areas such as square meters to square feet, acres to "
                 "square meters, etc."),
        ("speed", "Speed/Velocity-Converter: Convert between speed units such as mph to km/h, km/h to mph, etc."),
        ("time", "Time-Converter: Convert between time units such as hours to minutes, days to hours, etc."),
        ("energy", "Energy-Converter: Convert between energy units such as joules to calories, kWh to joules, etc."),
        ("power", "Power-Converter: Convert between power units such as watts to horsepower, kW to watts, etc."),
        ("currency", "Currency-Converter: Convert between various currencies such as USD to EUR, GBP to USD, etc."),
    ]

    for flag, description in conversion_flags:
        parser.add_argument(
            f"-{flag}",
            help=description,  # Detailed description added
            type=float,
            metavar=f"<value>",  # Suggests the user should input a value after the flag
        )


def parse_command_line_args(args):
    """Parses the command line arguments and returns True if valid arguments are found."""
    for flag, value in vars(args).items():
        if value is not None:
            for conv_type, (_, _, conv_flag) in CONVERTER_TYPES.items():
                if flag == conv_flag:
                    return value, conv_type
    return False


def prompt_for_conversion():
    """Prompts the user for a conversion type if no command-line args were passed."""
    print("What do you want to convert:\n"
          "1. Lengths/Distance\n"
          "2. Weight/Mass\n"
          "3. Volume\n"
          "4. Temperature\n"
          "5. Area\n"
          "6. Speed/Velocity\n"
          "7. Time\n"
          "8. Energy\n"
          "9. Power\n"
          "10. Currency\n")

    conv_type = input_conversion_choice()
    print(f"\nWelcome to the {CONVERTER_TYPES[conv_type][0]}-Converter")

    value = get_conversion_value()
    result = perform_conversion(value, conv_type)
    display_conversion(value, result)


def input_conversion_choice():
    """Gets a valid conversion type from the user."""
    while True:
        try:
            conv_type = int(input("Choose a number: ").strip())
            if conv_type in CONVERTER_TYPES:
                return conv_type
        except ValueError:
            print("Input should be a number!")


def get_conversion_value():
    """Gets the number to be converted from the user."""
    while True:
        try:
            return float(input("Input your number: "))
        except ValueError:
            print("Please enter a valid number!")


def perform_conversion(value, conv_type):
    """Performs the conversion and returns the results."""
    if conv_type in CONVERTER_TYPES:
        _, conv_func, _ = CONVERTER_TYPES[conv_type]
        return conv_func(value)
    print(f"No conversion function implemented for {CONVERTER_TYPES[conv_type][0]}")
    return []


def display_conversion(value, result):
    """Displays the conversion results."""
    for r in result:
        initial, converted = r[0].split(" to ")
        print(f"{value} {initial:<10} =\t{r[1]:.2f} {converted}")


def handle_command_line_conversion(args):
    """Handles conversion when command-line arguments are passed."""
    value, conv_id = parse_command_line_args(args)
    print(f"Welcome to the {CONVERTER_TYPES[conv_id][0]}-Converter\n")
    result = perform_conversion(value, conv_id)
    display_conversion(value, result)


def prompt_restart(args, parser):
    """Prompts the user to restart the conversion process."""
    again = input("\nWant to restart the Converter Y/N? ").strip().lower()
    if again == "y":
        reset_args(args)  # Reset args when restarting
        os.system('cls')  # Clear terminal screen
        return True
    return False


def reset_args(args):
    """Resets the command line arguments."""
    for flag in vars(args):
        setattr(args, flag, None)


def len_convert(n):
    result = [
        ("cm to in", n * 0.393701),
        ("in to cm", n * 2.54),
        ("ft to m", n * 0.3048),
        ("m to ft", n * 3.28084),
        ("mi to km", n * 1.60934),
        ("km to mi", n * 0.621371),
        ("yd to m", n * 0.9144),
        ("m to yd", n * 1.09361),
        ("mm to in", n * 0.0393701),
        ("in to mm", n * 25.4),
        ("mm to cm", n / 10),
        ("cm to mm", n * 10)
    ]
    return result


def mass_convert(n):
    result = [
        ("kg to lb", n * 2.20462),
        ("lb to kg", n / 2.20462),
        ("oz to g", n * 28.3495),
        ("g to oz", n / 28.3495),
        ("t to kg", n * 907.184),
        ("kg to t", n / 907.184)
    ]
    return result


def vol_convert(n):
    result = [
        ("L to gal", n * 0.264172),
        ("gal to L", n / 0.264172),
        ("mL to fl oz", n * 0.033814),
        ("fl oz to mL", n / 0.033814),
        ("cups to mL", n * 237),
        ("mL to cups", n / 237),
        ("m³ to L", n * 1000),
        ("L to m³", n / 1000)
    ]
    return result


def temp_convert(n):
    result = [
        ("°C to °F", (n * 9/5) + 32),
        ("°F to °C", (n - 32) * 5/9),
        ("°C to K", n + 273.15),
        ("K to °C", n - 273.15),
        ("°F to K", (n - 32) * 5/9 + 273.15),
        ("K to °F", (n - 273.15) * 9/5 + 32)
    ]
    return result


def area_convert(n):
    result = [
        ("m² to ft²", n * 10.7639),
        ("ft² to m²", n / 10.7639),
        ("ac to m²", n * 4046.86),
        ("m² to ac", n / 4046.86),
        ("mi² to km²", n * 2.58999),
        ("km² to mi²", n / 2.58999)
    ]
    return result


def speed_convert(n):
    result = [
        ("mph to km/h", n * 1.60934),
        ("km/h to mph", n / 1.60934),
        ("kn to mph", n * 1.15078),
        ("kn to km/h", n * 1.852),
        ("mph to kn", n / 1.15078),
        ("km/h to kn", n / 1.852)
    ]
    return result


def time_convert(n):
    result = [
        ("s to min", n / 60),
        ("min to s", n * 60),
        ("h to min", n * 60),
        ("min to h", n / 60),
        ("days to h", n * 24),
        ("h to days", n / 24),
        ("weeks to days", n * 7),
        ("days to weeks", n / 7),
        ("months to days", n * 30),  # Approximate, as months vary
        ("days to months", n / 30),  # Approximate
    ]
    return result


def energy_convert(n):
    result = [
        ("J to cal", n * 0.239006),
        ("cal to J", n / 0.239006),
        ("kW/h to J", n * 3.6e6),
        ("J to kW/h", n / 3.6e6),
        ("kW/h to cal", n * 860420.65),
        ("cal to kW/h", n / 860420.65)
    ]
    return result


def power_convert(n):
    result = [
        ("W to hp", n / 745.7),
        ("hp to W", n * 745.7),
        ("W to kW", n / 1000),
        ("kW to W", n * 1000),
        ("kW to hp", n * 1.34102),
        ("hp to kW", n / 1.34102)
    ]
    return result


def currency_convert(n):
    result = [
        ("USD to EUR", n * 0.92),  # Example, exchange rates fluctuate
        ("EUR to USD", n / 0.92),
        ("GBP to USD", n * 1.26),
        ("USD to GBP", n / 1.26),
        ("JPY to USD", n * 0.0068),
        ("USD to JPY", n / 0.0068),
        ("CAD to USD", n * 0.74),
        ("USD to CAD", n / 0.74),
        ("AUD to USD", n * 0.65),
        ("USD to AUD", n / 0.65)
    ]
    return result


if __name__ == "__main__":
    CONVERTER_TYPES = {
        1: ["Lengths/Distance", len_convert, "len"],
        2: ["Weight/Mass", mass_convert, "mass"],
        3: ["Volume", vol_convert, "vol"],
        4: ["Temperature", temp_convert, "temp"],
        5: ["Area", area_convert, "area"],
        6: ["Speed/Velocity", speed_convert, "speed"],
        7: ["Time", time_convert, "time"],
        8: ["Energy", energy_convert, "energy"],
        9: ["Power", power_convert, "power"],
        10: ["Currency", currency_convert, "currency"]
    }
    main()
