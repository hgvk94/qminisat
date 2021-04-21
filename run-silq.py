from subprocess import Popen, PIPE
import re
fp = '(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?'
regex = re.compile('[+-]?\([+-]?(%s)[+-](%s)i\)·\|(\d+)⟩' %(fp, fp), re.UNICODE)
process = Popen(["silq", "main.slq", "--run"], stdout=PIPE)
(output, err) = process.communicate()
exit_code = process.wait()
f = open("op.txt", "wb")
for line in output.splitlines():
    l = line.decode("utf-8")
    match = regex.search(l)
    if match:
        # print(match.group(0))
        real = float(match.group(1))
        img = float(match.group(2))
        state = match.group(3)
        content =str(round((real**2 + img**2)*100)) + "," + str(state) + "\n"; 
        f.write(content.encode('ascii'))
f.close()


# "/────────
# QUANTUM STATE
#  (0.353553+0i)·|0⟩₀
# +(0.353553+0i)·|1⟩₀
# +(0.353553+0i)·|2⟩₀
# +(0.353553+0i)·|3⟩₀
# +(0.353553+0i)·|4⟩₀
# +(0.353553+0i)·|5⟩₀
# +(0.353553+0i)·|6⟩₀
# +(0.353553+0i)·|7⟩₀

# VARIABLES
# cand ↦ ref(0)
# f ↦ ⟨is_bad_clause(const a: uint[3])qfree{
#     cdb := vector[!ℕ[]](160,array[!ℕ](1,1)): !ℤ[]^160;
#     lrnt := vector[!ℕ[]](6,array[!ℕ](1,1)): !ℤ[]^6;
#     lrnt[0] ← [154,089];
#     lrnt[1] ← [041,080];
#     lrnt[2] ← [010,083,095];
#     lrnt[3] ← [121,080,092];
#     lrnt[4] ← [072,165,151];
#     lrnt[5] ← [051,17,099];
#     sz := a < 6;
#     c0 := (a = 0 && lrnt[0].length > 4);
#     c1 := (a = 1 && lrnt[1].length > 4);
#     c2 := (a = 2 && lrnt[2].length > 4);
#     c3 := (a = 3 && lrnt[3].length > 4);
#     c4 := (a = 4 && lrnt[4].length > 4);
#     c5 := (a = 5 && lrnt[5].length > 4);
#     cnstr := sz && (c0 || c1 || c2 || c3 || c4 || c5);
#     return cnstr;
# }⟩
# k ↦ 1
# nIterations ↦ 2

# `frame ↦ {}
# `outer ↦ {n ↦ 3}
# ────────/
# "
