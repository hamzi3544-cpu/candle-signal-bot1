#!/usr/bin/env python3
# Educational 2-minute advance candle signal calculator.
# No broker login and no automatic trading.

def signal(c):
    if len(c) < 5:
        return "WAIT"
    last = c[-1]
    prev = c[-2]
    body = last["close"] - last["open"]
    prev_body = prev["close"] - prev["open"]
    rng = max(last["high"] - last["low"], 1e-9)
    body_ratio = abs(body) / rng

    if body > 0 and prev_body > 0 and body_ratio >= 0.55:
        return "CALL"
    if body < 0 and prev_body < 0 and body_ratio >= 0.55:
        return "PUT"
    return "WAIT"

candles=[]
print("2-Minute Advance Candle Signal Bot (demo)")
print("Enter 5+ candles as: open high low close")
while True:
    try:
        s=input("Candle (O H L C), or q: ").strip()
        if s.lower()=="q":
            break
        o,h,l,cl=map(float,s.split())
        candles.append({"open":o,"high":h,"low":l,"close":cl})
        print("Next 2-minute signal:", signal(candles))
    except Exception:
        print("Invalid input. Example: 100 102 99 101")
