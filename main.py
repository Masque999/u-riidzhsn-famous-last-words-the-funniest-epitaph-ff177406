LINE = "Do not stand at my grave and weep. I am not there; I am in the cloud, and the subscription renews forever."

# The entry must be exactly one line of 1-150 characters.
assert 1 <= len(LINE) <= 150, f"line is {len(LINE)} chars"
assert "\n" not in LINE

import os
assert LINE == LINE.strip(), "line must not have leading or trailing whitespace"

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)

with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)
