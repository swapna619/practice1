import sys

def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python temperature.py <celsius>")
    else:
        celsius = float(sys.argv[1])
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"Temperature in Fahrenheit: {fahrenheit}")
