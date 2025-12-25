import logging
from src.transaction_manager import TransactionManager
from src.generator import transaction_reader
from src.summary import generate_summary

logging.basicConfig(
    filename="transaction_management/logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main():
    file_path = "transaction_management/data/transactions.csv"

    manager = TransactionManager(initial_balance=1000, file_path=file_path)

    valid_count = 0
    invalid_count = 0
    
    print("\n----- Generating Transactions -----")
    for i in range(20):  
        transaction = manager.generate_transaction()
        manager.write_transaction(transaction)
        
        if transaction["is_valid"]:
            valid_count += 1
            print(f"✓ Transaction #{transaction['id']}: {transaction['type']} ${transaction['amount']}")
        else:
            invalid_count += 1
            print(f"✗ Invalid #{transaction['id']}, {transaction['type']}: ${transaction['amount']} - {transaction['reason']}")
    
    print(f"\nValid Transactions: {valid_count}")
    print(f"Invalid Transactions: {invalid_count}")

    transactions = transaction_reader(file_path)
    summary = generate_summary(transactions)

    print("\n----- Transaction Summary -----")
    print(f"Total Transactions : {summary['total_transactions']}")
    print(f"Total Credit       : {summary['total_credit']}")
    print(f"Total Debit        : {summary['total_debit']}")
    print(f"Final Balance      : {summary['final_balance']}")
    print("\nCheck 'logs/app.log' for detailed transaction log including invalid transactions.")

if __name__ == "__main__":
    main()