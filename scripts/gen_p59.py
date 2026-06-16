#!/usr/bin/env python3
"""Generate 20 fixtures for p59 (Spiral Matrix II, n in [1,20])."""
import os, json

def spiral_matrix(n):
    grid = [[0]*n for _ in range(n)]
    rl, rh, cl, ch = 0, n-1, 0, n-1
    v = 1
    while rl <= rh and cl <= ch:
        for c in range(cl, ch+1):
            grid[rl][c] = v; v += 1
        for r in range(rl+1, rh+1):
            grid[r][ch] = v; v += 1
        if rl < rh:
            for c in range(ch-1, cl-1, -1):
                grid[rh][c] = v; v += 1
        if cl < ch:
            for r in range(rh-1, rl, -1):
                grid[r][cl] = v; v += 1
        rl += 1; rh -= 1; cl += 1; ch -= 1
    return grid

OUT = os.path.join(os.path.dirname(__file__), '..', 'fixtures', 'p59')
os.makedirs(OUT, exist_ok=True)

for n in range(1, 21):
    idx = f'{n-1:02d}'
    with open(os.path.join(OUT, f'{idx}.in'),  'w') as f: f.write(f'{n}\n')
    with open(os.path.join(OUT, f'{idx}.out'), 'w') as f: f.write(json.dumps(spiral_matrix(n)) + '\n')

print('Generated 20 fixtures in fixtures/p59/')
