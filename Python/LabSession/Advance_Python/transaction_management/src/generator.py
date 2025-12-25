import logging
from src.file_context import FileHandler

def transaction_reader(file_path):
    try:
        with FileHandler(file_path, "r") as file:  
            for line in file:
                try:
                    parts = line.strip().split(",")

                    if len(parts) != 4:
                        raise ValueError("Invalid record format")

                    transaction = {
                        "id": int(parts[0]),
                        "type": parts[1],
                        "amount": int(parts[2]),
                        "balance": int(parts[3])
                    }

                    yield transaction

                except Exception as e:
                    logging.error(f"Skipping invalid record: {line.strip()} | Error: {e}")

    except FileNotFoundError:
        logging.error(f"Transaction file not found: {file_path}")