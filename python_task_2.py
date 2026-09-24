
from collections import Counter


class TransactionAnalyzer:

    def __init__(self, transactions):
        self.transactions = transactions

    # 1. Find duplicates
    def find_duplicates(self):
        frequency = Counter(self.transactions)
        duplicates = []

        for transaction, count in frequency.items():
            if count > 1:
                duplicates.append(transaction)

        return duplicates

    # 2. Find first duplicate
    def find_first_duplicate(self):
        seen = set()

        for transaction in self.transactions:
            if transaction in seen:
                return transaction

            seen.add(transaction)

        return None

    # 3. Find Top-N transactions
    def top_n(self, n):
        if n <= 0:
            return []

        sorted_transactions = sorted(self.transactions, reverse=True)

        return sorted_transactions[:n]

    # 4. Frequency analysis
    def frequency_analysis(self):
        frequency = Counter(self.transactions)

        return frequency

    # 5. Suspicious patterns
    def suspicious_patterns(self, threshold=3):
        frequency = Counter(self.transactions)
        suspicious = {}

        for transaction, count in frequency.items():
            if count >= threshold:
                suspicious[transaction] = count

        return suspicious


# Test data
transactions = [100, 200, 100, 500, 200, 300, 100, 200, 300]

analyzer = TransactionAnalyzer(transactions)

print("Duplicates:", analyzer.find_duplicates())
print("First duplicate:", analyzer.find_first_duplicate())
print("Top 3:", analyzer.top_n(3))
print("Frequency:", analyzer.frequency_analysis())
print("Suspicious patterns:", analyzer.suspicious_patterns())