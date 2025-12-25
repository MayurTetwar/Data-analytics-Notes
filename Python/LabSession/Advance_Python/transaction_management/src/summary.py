
def generate_summary(transaction_generator):
    total_transactions = 0
    total_credit = 0
    total_debit = 0
    final_balance = 0

    for txn in transaction_generator:
        total_transactions += 1
        final_balance = txn["balance"]

        if txn["type"] == "CREDIT":
            total_credit += txn["amount"]
        elif txn["type"] == "DEBIT":
            total_debit += txn["amount"]

    return {
        "total_transactions": total_transactions,
        "total_credit": total_credit,
        "total_debit": total_debit,
        "final_balance": final_balance
    }
