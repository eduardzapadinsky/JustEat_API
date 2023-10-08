# Just Eat API Client

This Python script provides a client for interacting with the Just Eat API to retrieve restaurant information by postal
code in the UK.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/just-eat-api-client.git
   ```

2. Navigate to the project directory:

   ```bash
   cd just-eat-api-client
   ```

3. Create and activate a virtual environment (optional but recommended):

   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate

   # On macOS and Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

4. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

To use this script, run it from the command line with a valid postal code as an argument:

```bash
python just_eat_client.py EC4
```

Replace `EC4` with the postal code you want to search for. The script will fetch and display a list of restaurants in
the specified area, including their names, ratings, and cuisines.

## Error Handling

The script handles various error scenarios, including invalid postal codes and API request failures. It displays error
messages without terminating the program.
