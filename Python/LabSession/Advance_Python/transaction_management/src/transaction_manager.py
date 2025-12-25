import random
import logging
from src.file_context import FileHandler

class TransactionManager:
    def __init__(self, initial_balance, file_path):
        self.balance = initial_balance
        self.file_path = file_path
        self.transaction_id = 1

    def generate_transaction(self):
        transaction_type = random.choice(["CREDIT", "DEBIT"])
        
        if transaction_type == "CREDIT":
            amount = random.randint(100, 1000)
        else:
            amount = random.randint(1, max(1500, self.balance + 500))
        
        is_valid = True
        reason = None
        
        if transaction_type == "DEBIT":
            if self.balance == 0:
                is_valid = False
                reason = "Insufficient balance (balance is 0)"
            elif amount > self.balance:
                is_valid = False
                reason = f"Insufficient balance (required: {amount}, available: {self.balance})"
        
        new_balance = self.balance
        if is_valid:
            if transaction_type == "CREDIT":
                new_balance = self.balance + amount
            else:
                new_balance = self.balance - amount
        
        transaction = {
            "id": self.transaction_id,
            "type": transaction_type,
            "amount": amount,
            "balance_before": self.balance,
            "balance_after": new_balance,
            "is_valid": is_valid,
            "reason": reason
        }
        
        if is_valid:
            self.balance = new_balance
            
        self.transaction_id += 1
        return transaction

    def write_transaction(self, transaction):
        if transaction["is_valid"]:
            try:
                with FileHandler(self.file_path, "a") as file:
                    line = f"{transaction['id']},{transaction['type']},{transaction['amount']},{transaction['balance_after']}\n"
                    file.write(line)
                logging.info(
                    f"Transaction #{transaction['id']} - {transaction['type']} "
                    f"${transaction['amount']} - Balance: ${transaction['balance_after']}"
                )
            except Exception as e:
                logging.error(f"Failed to write transaction: {e}")
        else:
            logging.warning(
                f"INVALID Transaction - {transaction['type']} ${transaction['amount']} - "
                f"Rejected: {transaction['reason']} - "
                f"Balance remains: ${transaction['balance_before']}"
            )