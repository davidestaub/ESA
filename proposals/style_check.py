"""Style statistics for ESA sections, compared with Ben Moseley's DPhil thesis.

Usage: python3 proposals/style_check.py sections/03_benchmark.tex [more .tex files]
Prints sentence-length and word-habit statistics per 1000 words, with the
targets from proposals/STYLE_RULES_20261006.md.
"""
import re, sys, statistics as st

BANNED = ['delve', 'leverage', 'pivotal', 'landscape', 'notably', 'crucially', 'it is worth',
          'underscore', 'highlights the importance', 'plays a key role', 'seamless', 'in essence',
          'moreover', 'additionally', 'frozen', 'registered', 'sealed', 'genuine', 'gate',
          'firewall', 'pre-registered', 'admissible', 'authoritative', 'byte for byte',
          'certificate', ' not just', "isn't", "it's", 'this matters']
INTERNAL = ['V45', 'R7', 'sp0022', 'sp0025', 'MVI', 'Track A', 'Track B', 'dga_00', 'E13b', 'LOW', 'HIGH']

def detex(path):
    t = open(path).read()
    t = re.sub(r'(?m)^\s*%.*$', '', t)
    t = re.sub(r'(?<!\\)%.*', '', t)
    t = re.sub(r'\\begin\{(equation|align|figure|table)\*?\}.*?\\end\{\1\*?\}', ' ', t, flags=re.S)
    t = re.sub(r'\$[^$]*\$', 'X', t)
    t = re.sub(r'\\(cite[pt]?|citealp|ref|eqref|label)\{[^}]*\}', '', t)
    t = re.sub(r'\\[a-zA-Z]+\*?(\[[^\]]*\])?\{([^}]*)\}', r'\2', t)
    t = re.sub(r'\\[a-zA-Z]+', '', t)
    t = re.sub(r'[{}~]', ' ', t)
    return re.sub(r'\s+', ' ', t)

def sentences(t):
    t = re.sub(r'\b(e\.g|i\.e|et al|Fig|Eq|Sec|cf|vs|approx)\.', r'\1<DOT>', t)
    s = re.split(r'(?<=[.!?])\s+(?=[A-Z])', t)
    return [x.replace('<DOT>', '.') for x in s if len(x.split()) >= 3]

def report(path):
    t = detex(path); low = t.lower(); n = len(t.split()); S = sentences(t)
    L = sorted(len(s.split()) for s in S)
    k = lambda c: 1000 * c / n
    rows = [
        ('median sentence length (words)', st.median(L), '18-24'),
        ('share of sentences > 35 words', f'{sum(x > 35 for x in L) / len(L):.0%}', '<= 20%'),
        ('share of sentences < 10 words', f'{sum(x < 10 for x in L) / len(L):.0%}', '8-20%'),
        ('commas per 1000 words', f'{k(t.count(",")):.0f}', '<= 60'),
        ('semicolons per 1000 words', f'{k(t.count(";")):.1f}', '<= 1.5'),
        ('colons per 1000 words', f'{k(t.count(":")):.1f}', '<= 2'),
        ('"which" per 1000 words', f'{k(len(re.findall(r"\bwhich\b", low))):.1f}', '<= 6'),
        ('"for example" per 1000 words', f'{k(low.count("for example")):.1f}', '>= 1'),
        ('"I"/"my" per 1000 words', f'{k(len(re.findall(r"\b(I|my)\b", t))):.1f}', '4-8'),
        ('"we"/"our" per 1000 words', f'{k(len(re.findall(r"\b(we|our|us)\b", low))):.1f}', '0'),
        ('em dashes', t.count('—') + t.count('---'), '0'),
    ]
    print(f'\n{path}: {n} words, {len(S)} sentences')
    for name, val, tgt in rows:
        print(f'  {name:34s} {str(val):>6s}   target {tgt}')
    hits = [w for w in BANNED if re.search(r'(?<![a-z])' + re.escape(w.strip()) + r'(?![a-z])', low)]
    hits += [w for w in INTERNAL if re.search(r'\b' + re.escape(w) + r'\b', t)]
    for w, limit in [('rather than', 0.3), ('in other words', 0.3)]:
        if 1000 * low.count(w) / n > limit + 1e-9 and low.count(w) > 1: hits.append(f'{w} (x{low.count(w)}, judgment)')
    print('  banned or internal words found:', ', '.join(hits) if hits else 'none')
    # repeated sentences or repeated 8-word openings (catches duplicated fragments)
    from collections import Counter
    starts = Counter(' '.join(x.split()[:8]).lower() for x in S if len(x.split()) >= 8)
    dups = [k for k, v in starts.items() if v > 1]
    print('  repeated sentence openings:', '; '.join(dups) if dups else 'none')

for p in sys.argv[1:]:
    report(p)
