class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        builder = []

        for i in range(len(S) - 1, -1, -1):
            if S[i] == '-':
                continue
            if len(builder) % (K + 1) == K:
                builder.append('-')
            builder.append(S[i].upper())

        return ''.join(builder[::-1])
