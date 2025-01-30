Sure! Below is a Python program for the `waste-tracker` project. This program simulates a simple command-line interface application that helps manage and analyze household waste patterns. It includes features to add waste entries, view statistics, and provides suggestions for minimizing waste.

```python
import json
import os

class WasteTracker:
    def __init__(self, filename='waste_data.json'):
        self.filename = filename
        self.data = {}
        self.load_data()

    def load_data(self):
        """Load existing waste data from a file."""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as file:
                    self.data = json.load(file)
            except (IOError, json.JSONDecodeError):
                print("Error loading data. Starting with empty data.")
                self.data = {}

    def save_data(self):
        """Save current waste data to a file."""
        try:
            with open(self.filename, 'w') as file:
                json.dump(self.data, file)
        except IOError:
            print("Error saving data. Please try again.")

    def add_waste_entry(self):
        """Add a new waste entry."""
        try:
            category = input("Enter waste category (e.g., Plastic, Food): ").strip()
            amount = float(input("Enter amount of waste (in kg): ").strip())

            if category not in self.data:
                self.data[category] = 0.0
            self.data[category] += amount

            self.save_data()
            print(f"Added {amount} kg of {category} waste.")
        except ValueError:
            print("Invalid input for amount. Please enter a numeric value.")

    def view_stats(self):
        """View statistics of waste."""
        total_waste = sum(self.data.values())
        if total_waste == 0:
            print("No data available.")
            return

        print("\nWaste Statistics:")
        for category, amount in self.data.items():
            percentage = (amount / total_waste) * 100
            print(f"{category}: {amount:.2f} kg ({percentage:.2f}%)")

    def suggest_reductions(self):
        """Provide suggestions to reduce waste."""
        if not self.data:
            print("No data available to provide suggestions.")
            return

        print("\nSuggestions to Reduce Waste:")
        for category in self.data:
            print(f"- Consider reducing the use of {category.lower()} items by opting for alternatives.")

    def run(self):
        """Run the waste tracker program."""
        while True:
            print("\nWaste Tracker Menu")
            print("1. Add Waste Entry")
            print("2. View Statistics")
            print("3. Get Reduction Suggestions")
            print("4. Exit")

            try:
                choice = int(input("Choose an option: ").strip())
            except ValueError:
                print("Invalid choice. Please enter a number between 1 and 4.")
                continue

            if choice == 1:
                self.add_waste_entry()
            elif choice == 2:
                self.view_stats()
            elif choice == 3:
                self.suggest_reductions()
            elif choice == 4:
                print("Exiting Waste Tracker. Goodbye!")
                break
            else:
                print("Invalid choice. Please choose a valid menu option.")

if __name__ == "__main__":
    tracker = WasteTracker()
    tracker.run()
```

### Key Features:
- **Persistent Data Storage**: The program saves waste data to a file (`waste_data.json`) and retrieves it upon startup.
- **Add Waste Entries**: Users can input different categories of waste along with their quantities.
- **View Statistics**: A summary of the different types of waste by percentage.
- **Suggestions**: Provides suggestions to minimize waste based on existing data.
- **Error Handling**: Includes basic error handling for file I/O and user inputs.

This basic application can be expanded further with more sophisticated analysis, integration with external databases, user authentication, and a graphical user interface for a better user experience if needed.