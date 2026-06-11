#!/usr/bin/env python3
"""Generate all 720 fixtures for p1344 (Angle Between Hands of a Clock, hour in [1,12], minutes in [0,59])."""
import os

def angle_clock(hour, minutes):
    h = (hour % 12) * 30 + minutes * 0.5
    m = minutes * 6
    d = abs(h - m)
    return min(d, 360 - d)

out = os.path.join(os.path.dirname(__file__), '..', 'fixtures', 'p1344')
os.makedirs(out, exist_ok=True)

idx = 0
for hour in range(1, 13):
    for minutes in range(0, 60):
        angle = angle_clock(hour, minutes)
        with open(os.path.join(out, f'{idx:04d}.in'),  'w') as f: f.write(f'{hour}\n{minutes}\n')
        with open(os.path.join(out, f'{idx:04d}.out'), 'w') as f: f.write(f'{angle:.5f}\n')
        idx += 1

print(f'Generated {idx} fixtures in fixtures/p1344/')
