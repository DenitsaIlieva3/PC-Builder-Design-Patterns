# PC Builder – Design Patterns

## Overview

PC Builder is a Python console application that allows users to create computer configurations, customize them by adding hardware components, calculate the final price and performance, and manage component prices.

The project demonstrates the practical implementation of several object-oriented design patterns, including **Facade, Decorator, and Observer**.

## Features

- Create predefined computer configurations:
  - Office PC
  - Gaming PC
  - Server PC
- Customize computers by adding hardware components:
  - RAM
  - SSD
  - GPU
- Calculate the total configuration price.
- Calculate the total performance score.
- Display the complete computer configuration.
- Update component prices.
- Track price changes through a price history observer.
- Prevent adding the same component multiple times.
- Validate user input and handle errors.

## Design Patterns

### Facade

The `PCBuilderFacade` provides a simplified interface for interacting with the system. It manages the creation of computers, component selection, configuration calculations, and price management.

### Decorator

The Decorator pattern allows hardware components to be dynamically added to an existing computer configuration without modifying the original computer classes.

### Observer

The Observer pattern is used to monitor component price changes. When a component's price is updated, the `PriceHistoryObserver` receives a notification and records the change.

## Technologies

- Python 3.11
- Object-Oriented Programming
- Visual Studio Code
- Git
- GitHub

## Project Structure

```text
PC_Builder/
│
├── configurations/
│   └── base_configurations.py
│
├── decorators/
│   ├── computer_decorator.py
│   ├── ram_decorator.py
│   ├── ssd_decorator.py
│   └── gpu_decorator.py
│
├── documentation/
│   ├── Documentation_PC_Builder.pdf
│   └── UML.png
│
├── facade/
│   └── pc_builder_facade.py
│
├── models/
│   ├── computer.py
│   └── component.py
│
├── observer/
│   ├── observer.py
│   ├── subject.py
│   ├── price_catalog.py
│   └── price_history_observer.py
│
├── main.py
└── .gitignore
```

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/DenitsaIlieva3/PC-Builder-Design-Patterns.git
```

2. Navigate to the project directory:

```bash
cd PC-Builder-Design-Patterns
```

3. Run the application:

```bash
python main.py
```

## Example

The application allows the user to select a base computer configuration and add components.

For example:

```text
Base configuration: Gaming PC
Base price: 1200.00 EUR
Base performance: 85 points

Added components:
- Kingston Fury 32GB RAM
- Samsung 990 PRO 1TB SSD
- NVIDIA RTX 4070

Final price: 1830.00 EUR
Final performance: 150 points
```

## Documentation

The `documentation` folder contains:

- Project documentation
- UML class diagram

## Author

**Denitsa Ilieva**

GitHub: [DenitsaIlieva3](https://github.com/DenitsaIlieva3)