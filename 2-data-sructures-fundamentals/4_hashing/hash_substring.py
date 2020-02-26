class RabinKarp:
    def __init__(self):
        self._multiplier = 263
        self._prime = 1000000007
        self.occurrences = []

    def _hash_func(self, s, l, r):
        ans = 0
        for i in range(r, l - 1, -1):
            ans = (ans * self._multiplier + ord(s[i])) % self._prime
            
        return ans

    def get_occurrences(self, pattern, text):
        
        positions = []
        hashPattern = self._hash_func(pattern, 0, len(pattern) - 1)
        hashText = self._hash_func(text, len(text) - len(pattern), len(text) - 1)

        if hashText == hashPattern:
            positions.append(len(text) - len(pattern))

        multiplierPowP = 1
        for i in range(len(pattern)):
            multiplierPowP = (multiplierPowP * self._multiplier)  % self._prime

        for i in range(len(text) - len(pattern) - 1, -1, -1):
            hashText = (hashText * self._multiplier + (ord(text[i]) - multiplierPowP * ord(text[i + len(pattern)]))) % self._prime
            if hashText == hashPattern:
                positions.append(i)

        results = []
        for i in range(len(positions) - 1, -1, -1):
            if pattern == text[positions[i]:positions[i] + len(pattern)]:
                results.append(positions[i])

        return results

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences_naive(pattern, text):
    return [
        i 
        for i in range(len(text) - len(pattern) + 1) 
        if text[i:i + len(pattern)] == pattern
    ]

if __name__ == '__main__':

    rabinKarp = RabinKarp()
    print_occurrences(rabinKarp.get_occurrences(*read_input()))