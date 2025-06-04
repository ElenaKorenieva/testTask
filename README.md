# Geometry Calculator

## Overview

This is a simple geometry calculator program that reads data about various 2D geometrical shapes from standard input or a file, calculates their perimeter and area, and writes the results to standard output. The results are also saved in a file named `results.txt`.

## Supported Shapes
- Square
- Rectangle
- Circle
- Triangle

## Input Format
Each line of input represents a shape with its defining properties. Supported formats:

```
Square TopRight <x> <y> Side <length>
Rectangle TopRight <x1> <y1> BottomLeft <x2> <y2>
Circle Center <x> <y> Radius <r>
Triangle Point1 <x1> <y1> Point2 <x2> <y2> Point3 <x3> <y3>
```

## Sample Input
```
Square TopRight 1 1 Side 2
Circle Center 0 0 Radius 3
Rectangle TopRight 4 5 BottomLeft 1 1
Triangle Point1 0 0 Point2 4 0 Point3 0 3
```

## Sample Output
```
Square Perimeter 8 Area 4
Circle Perimeter 18 Area 28
Rectangle Perimeter 14 Area 12
Triangle Perimeter 12 Area 6
```

## How to Run

You can run the program using standard input or by providing an input file.

### Option 1: Using Manual Input
```sh
python main.py
```
Follow the prompt to enter shape data line-by-line. Type `END` to finish.

### Option 2: Using a File
Place input in a file, for sake of saving time and testing purposes file `shapes.txt` was created, and provide its name when prompted:
```sh
python main.py
```
Enter `shapes.txt` when asked for filename.

## Output
- Results are printed to the terminal.
- Results are also saved to `results.txt`.

## Requirements
- Python 3.x

## Implementation Notes
- The script uses an abstract base class `Figure` and subclasses for each shape.
- Uses the factory pattern to instantiate shapes from input strings.
- Handles invalid lines gracefully with error messages.

## License
This project is provided under the MIT License.
