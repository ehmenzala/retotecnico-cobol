from pathlib import Path
import pandas as pd
import os

# CSV File information
BASE_DIR = Path(os.getcwd())
input_file = 'bank-transactions.csv'
input_path = BASE_DIR / 'data' / input_file

transactions_df = pd.read_csv(input_path, sep=';', encoding='latin1')

transactions = transactions_df.to_dict(orient='records')

credit_sum = 0
debit_sum = 0
greatest_transaction = None

for transaction in transactions:
  current_amount = transaction['amount']
  if greatest_transaction:
    if current_amount > greatest_transaction['amount']:
      greatest_transaction = transaction
  else:
    greatest_transaction = transaction

  if (transaction['type'] == 'Débito'):
    debit_sum += transaction['amount']
  elif (transaction['type'] == 'Crédito'):
    credit_sum += transaction['amount']

balance = debit_sum - credit_sum

print('Reporte de Transacciones')
print('---------------------------------------------')
print(f'Suma de débitos: {debit_sum}')
print(f'Suma de créditos: {credit_sum}')
print(f'Balance: {balance}')
print(f'Transacción de Mayor Monto: ID {greatest_transaction['id']} - {greatest_transaction['amount']}')