"""LC 127 Word Ladder (HARD) — Pattern: BFS on implicit graph (wildcard buckets).
https://leetcode.com/problems/word-ladder/
Return number of WORDS in shortest transformation sequence, 0 if impossible."""
from collections import defaultdict, deque


def ladder_length(begin: str, end: str, word_list: list[str]) -> int:
    words = set(word_list)
    if end not in words:
        return 0
    buckets = defaultdict(list)                 # "h*t" -> [hot, hit]
    for w in words | {begin}:
        for i in range(len(w)):
            buckets[w[:i] + "*" + w[i + 1:]].append(w)
    q, seen = deque([(begin, 1)]), {begin}
    while q:
        w, d = q.popleft()
        if w == end:
            return d
        for i in range(len(w)):
            key = w[:i] + "*" + w[i + 1:]
            for nxt in buckets[key]:
                if nxt not in seen:
                    seen.add(nxt); q.append((nxt, d + 1))
            buckets[key] = []                   # bucket fully explored
    return 0
