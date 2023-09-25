import pandas as pd
import hashlib

def calculate_hash(row):
    # Concatenate the values of 'Column1' and 'Column2' as a string
    concatenated_values = str(row['Chapter'])

    # Encode the concatenated string to bytes
    concatenated_bytes = concatenated_values.encode('utf-8')

    # Calculate the SHA-256 hash
    hash_value = hashlib.md5(concatenated_bytes).hexdigest()

    return hash_value

df = pd.read_excel('./DB/init.xlsx')
df['hash'] = df.apply(calculate_hash, axis=1)
df.to_csv('./DB/hash.csv')
print(df)
print(df.info())
print(df.describe())