class RabinKarp:
    def __init__(self):
        self._multiplier = 263
        self._prime = 1000000007
        self.occurrences = []

    def _hash_func(self, s, l, r):
        ans = 0
        for i in range(l, r):
            ans = (ans * self._multiplier + ord(s[i])) % self._prime
            
        return ans

    def areEqual(self, text, pattern, position):
        if position + len(pattern) > len(text):
            return False

        for i in range(position, len(pattern)):
            if text[i] != pattern[i]:
                return False
        return True

    def get_occurrences(self, pattern, text):
        
        positions = []
        hashPattern = self._hash_func(pattern, 0, len(pattern))
        hashText = self._hash_func(text, 0, len(pattern))
        if hashText == hashPattern:
            positions.append(0)

        multiplierPowP_1 = 1
        for i in range(len(pattern) - 1):
            multiplierPowP_1 = (multiplierPowP_1 * self._multiplier) % self._prime

        for i in range(1, len(text) - len(pattern) + 1):
            hashText = ((hashText - ord(text[i - 1])) // self._multiplier + multiplierPowP_1 * ord(text[i + len(pattern) - 1])) % self._prime

            if hashText == hashPattern:
                positions.append(i)

        results = []
        for i in range(len(positions)):
            if self.areEqual(text, pattern, positions[i]):
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


