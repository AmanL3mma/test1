import re
from pathlib import Path

PASSWORD_RE = re.compile(r'''
    ^
    (?=.*[a-z])
    (?=.*[A-Z])
    (?=.*\d)
    (?=.*[_$!])
    .{8,}
    $
    ''', re.VERBOSE)

def is_valid(password: str) -> bool:
    return bool(PASSWORD_RE.match(password))

FILE = Path('passwords.txt')

with FILE.open(encoding='utf-8') as fh:
    for lineno, raw in enumerate(fh, 1):
        pw = raw.rstrip('\n')
        verdict = 'OK' if is_valid(pw) else 'INVALID'
        print(f'Line {lineno:>4}: {verdict}   ({pw})')