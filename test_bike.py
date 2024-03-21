import pytest
import sqlite3
from Bike001 import BikeRental

# Fixture to create an instance of BikeRental for each test
@pytest.fixture
def bike_rental_instance():
    return BikeRental(100)

# Test case for create method
def test_create(bike_rental_instance, monkeypatch):
    # Mocking user input
    mock_input_values = iter(["John Doe", "5"])
    def mock_input(prompt):
        return next(mock_input_values)

    monkeypatch.setattr('builtins.input', mock_input)

    # Calling create method
    bike_rental_instance.Create()

    # Asserting expected database state after create
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM bikes WHERE name = 'John Doe'")
    result = cur.fetchone()
    cur.close()
    conn.close()

    assert result is not None
    assert result[1] == "John Doe"
    assert result[2] == 5

# Test case for display method
def test_display(bike_rental_instance, capsys):
    # Calling display method
    bike_rental_instance.display()

    # Capturing stdout to check printed output
    captured = capsys.readouterr()
    assert "John Doe" in captured.out  # Assuming John Doe with 5 bikes is in the output

# Test case for ReturnBike method
def test_return_bike(bike_rental_instance, monkeypatch, capsys):
    # Mocking user input
    mock_input_values = iter(["123"])  # Assuming valid ID for testing
    def mock_input(prompt):
        return next(mock_input_values)

    monkeypatch.setattr('builtins.input', mock_input)

    # Calling ReturnBike method
    bike_rental_instance.ReturnBike()

    # Capturing stdout to check printed output
    captured = capsys.readouterr()
    assert "ID number not found" in captured.out  # Assuming ID 123 does not exist in the database initially

# Test case for update method
def test_update(bike_rental_instance, monkeypatch):
    # Mocking user input
    mock_input_values = iter(["123", "Jane Doe", "8"])  # Assuming valid ID for testing
    def mock_input(prompt):
        return next(mock_input_values)

    monkeypatch.setattr('builtins.input', mock_input)

    # Calling update method
    bike_rental_instance.update()

    # Asserting expected database state after update
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM bikes WHERE name = 'Jane Doe'")
    result = cur.fetchone()
    cur.close()
    conn.close()

    assert result is not None
    assert result[1] == "Jane Doe"
    assert result[2] == 8

# Test case for Delete method
def test_delete(bike_rental_instance, monkeypatch):
    # Mocking user input
    mock_input_values = iter(["123"])  # Assuming valid ID for testing
    def mock_input(prompt):
        return next(mock_input_values)

    monkeypatch.setattr('builtins.input', mock_input)

    # Calling Delete method
    bike_rental_instance.Delete()

    # Asserting expected database state after delete
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM bikes WHERE ID_number = 123")
    result = cur.fetchone()
    cur.close()
    conn.close()

    assert result is None

# Test case for Quit method
def test_quit(bike_rental_instance, capsys, monkeypatch):
    # Mocking user input
    mock_input_values = iter(["6"])  # Assuming Quit option is chosen
    def mock_input(prompt):
        return next(mock_input_values)

    monkeypatch.setattr('builtins.input', mock_input)

    # Calling Quit method
    with pytest.raises(SystemExit):
        bike_rental_instance.Quit()

    # Capturing stdout to check printed output
    captured = capsys.readouterr()
    assert captured.out == ""  # Assuming Quit method does not print anything

# Test case for invalid input handling in Create method
def test_create_invalid_input_handling(bike_rental_instance, capsys, monkeypatch):
    # Mocking user input with invalid NumofBike
    mock_input_values = iter(["John Doe", "invalid"])
    def mock_input(prompt):
        return next(mock_input_values)

    monkeypatch.setattr('builtins.input', mock_input)

    # Calling create method with invalid input
    bike_rental_instance.Create()

    # Capturing stdout to check printed output
    captured = capsys.readouterr()
    assert "Error converting NumofBike to integer" in captured.out

# Test case for invalid ID number handling in ReturnBike method
def test_return_bike_invalid_id(bike_rental_instance, capsys, monkeypatch):
    # Mocking user input with invalid ID
    mock_input_values = iter(["invalid"])
    def mock_input(prompt):
        return next(mock_input_values)

    monkeypatch.setattr('builtins.input', mock_input)

    # Calling ReturnBike method with invalid ID
    bike_rental_instance.ReturnBike()

    # Capturing stdout to check printed output
    captured = capsys.readouterr()
    assert "INVALID ID NUMBER" in captured.out

# Test case for invalid ID number handling in update method
def test_update_invalid_id(bike_rental_instance, capsys, monkeypatch):
    # Mocking user input with invalid ID
    mock_input_values = iter(["invalid", "Jane Doe", "8"])
    def mock_input(prompt):
        return next(mock_input_values)

    monkeypatch.setattr('builtins.input', mock_input)

    # Calling update method with invalid ID
    bike_rental_instance.update()

    # Capturing stdout to check printed output
    captured = capsys.readouterr()
    assert "INVALID ID NUMBER" in captured.out

# Test case for invalid ID number handling in Delete method
def test_delete_invalid_id(bike_rental_instance, capsys, monkeypatch):
    # Mocking user input with invalid ID
    mock_input_values = iter(["invalid"])
    def mock_input(prompt):
        return next(mock_input_values)

    monkeypatch.setattr('builtins.input', mock_input)

    # Calling Delete method with invalid ID
    bike_rental_instance.Delete()

    # Capturing stdout to check printed output
    captured = capsys.readouterr()
    assert "INVALID ID NUMBER" in captured.out
