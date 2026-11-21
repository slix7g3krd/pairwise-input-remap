import pytest
import math
from gameplay import input_remap as mod

CASES = [
    ("device", 'm.device("abc") == "dev:abc"'),
    ("bind", 'm.bind("attack") == "attack"'),
    ("conflict", 'm.conflict("a", "a") is True'),
    ("pick", 'm.pick(100, 200) == 200'),
    ("hold", 'm.hold(0.5) == 0.5'),
    ("priority", 'm.priority(("ctrl", "a")) == 2'),
    ("deadzone", 'm.deadzone(0.1, 0.2) == 0'),
    ("persist", 'm.persist({"a": 1}) == {"a": 1}'),
    ("glyph", 'm.glyph("jump") == "icon:jump"'),
    ("clear", 'm.clear([1]) == []'),
    ("remap", 'm.remap("a", "b") == "b"'),
    ("clamp", 'm.clamp_dz(2) == 1'),
    ("pressed", 'm.pressed(0.6) is True'),
    ("count", 'm.count([1, 2]) == 2'),
    ("key", 'm.key("attack") == "a:attack"')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx, "math": math})
