#!/usr/bin/env python3
"""Iteration 266: exact transpose-class reduction of polarized null-soft B3."""
import json

legs = ("s", "a", "b")
terms = []
terms.append({"family":"Q0A3Q0","label":"Q0 A3[s,a,b] Q0","transpose":"self","vanishes":False})

for x in legs:
    yz = tuple(y for y in legs if y != x)
    left = f"Q1[{x}] A2[{yz[0]},{yz[1]}] Q0"
    right = f"Q0 A2[{yz[0]},{yz[1]}] Q1[{x}]"
    terms += [
        {"family":"Q1A2","label":left,"transpose":right,"vanishes":False},
        {"family":"Q1A2","label":right,"transpose":left,"vanishes":False},
    ]

for y in legs:
    pair = tuple(x for x in legs if x != y)
    left = f"Q2[{pair[0]},{pair[1]}] A1[{y}] Q0"
    right = f"Q0 A1[{y}] Q2[{pair[0]},{pair[1]}]"
    vanish = (y == "s")
    terms += [
        {"family":"Q2A1","label":left,"transpose":right,"vanishes":vanish},
        {"family":"Q2A1","label":right,"transpose":left,"vanishes":vanish},
    ]

for y in legs:
    outside = [x for x in legs if x != y]
    left = f"Q1[{outside[0]}] A1[{y}] Q1[{outside[1]}]"
    right = f"Q1[{outside[1]}] A1[{y}] Q1[{outside[0]}]"
    vanish = (y == "s")
    terms += [
        {"family":"Q1A1Q1","label":left,"transpose":right,"vanishes":vanish},
        {"family":"Q1A1Q1","label":right,"transpose":left,"vanishes":vanish},
    ]

survivors = [t for t in terms if not t["vanishes"]]
labels = {t["label"] for t in survivors}
visited=set(); classes=[]
for t in survivors:
    if t["label"] in visited:
        continue
    if t["transpose"] == "self":
        members=[t["label"]]
    else:
        assert t["transpose"] in labels
        members=[t["label"],t["transpose"]]
    visited.update(members)
    classes.append({"representative":members[0],"members":members,"size":len(members)})

assert len(terms) == 19
assert sum(t["vanishes"] for t in terms) == 4
assert len(survivors) == 15
assert len(classes) == 8
assert sorted(len(c["members"]) for c in classes) == [1,2,2,2,2,2,2,2]

result={
  "iteration":266,
  "assumptions":["A1[s]=0","Qn^T=Qn","An^T=An","Q2[x,y]=Q2[y,x]","A2[x,y]=A2[y,x]"],
  "raw_polarized_terms":19,
  "nullsoft_vanishing_terms":4,
  "nullsoft_surviving_terms":15,
  "independent_transpose_classes":8,
  "class_sizes":[len(c["members"]) for c in classes],
  "classes":classes,
  "reconstruction":"B3 = Q0 A3 Q0 + sum_over_7_nonself_representatives (X + X^T)",
  "status":["PASS_EXACT_NULLSOFT_B3_TRANSPOSE_CLASS_REDUCTION_15_TO_8","NO_DOUBLE_EVALUATION_OF_TRANSPOSE_PAIRED_B3_TERMS"]
}
print(json.dumps(result,indent=2,sort_keys=True))
