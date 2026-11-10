from datetime import date, timedelta
start = date(2026,11,8)
for n in range(1,122):
    d = start + timedelta(days=7*(n-1))
    kind = "TEST" if n <= 96 and n % 4 == 0 else ("P3" if n >= 100 else "LESSON")
    print(f"{n:3d} {d.isoformat()} {kind}")
