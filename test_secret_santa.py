import re
import random
import pytest
from secret_santa import (
    Secret_Santa, 
    DuplicateNameException, 
    InsufficientNamesException
)

# ---------- Fixtueres ---------- #
@pytest.fixture
def names():
    return ["Alice", "Bob", "Charlie", "Dana"]

@pytest.fixture
def ss(names):
    # Start with a known list through the constructor string path
    return Secret_Santa("Alice, Bob, Charlie, Dana")

# ---------- initialize_class ---------- #
def init_class_from_string():
    ss = Secret_Santa("Alice, Bob, Charlie, Dana")
    assert ss.people == ["Alice", "Bob", "Charlie", "Dana"]

def init_class_from_string_cleaned():
    ss = Secret_Santa(" Alice  ,  Bob,Charlie,Dana  ")
    assert ss.people == ["Alice", "Bob", "Charlie", "Dana"]

def init_class_from_list():
    ss = Secret_Santa(["Alice", "Bob", "Charlie", "Dana"])
    assert ss.people == ["Alice", "Bob", "Charlie", "Dana"]

def init_class_from_list_cleaned():
    ss = Secret_Santa(["    Alice", "Bob", "Charlie  ", "     Dana   "])
    assert ss.people == ["Alice", "Bob", "Charlie", "Dana"]

# ---------- _string_to_list ---------- #
def test_string_to_list_basic():
    ss = Secret_Santa("")
    assert ss._string_to_list(" Alice , Bob,, Charlie, ,Dana ") == ["Alice", "Bob", "Charlie", "Dana"]

def test_string_to_list_empty_safe():
    ss = Secret_Santa("")
    assert ss._string_to_list("") == []

# ---------- validate_names ---------- #
def test_validate_names_unique_ok():
    ss = Secret_Santa("")
    assert ss.validate_names(["A", "B", "C"]) is True

def test_validate_names_duplicates_raise():
    ss = Secret_Santa("")
    with pytest.raises(DuplicateNameException):
        ss.validate_names(["A", "B", "A"])

def test_randomization():
    from_people = ["Jim", "Brenda", "Katie", "Matt", "Evelyn", "Daniel", "Susanna", "Nathan", "Tatiana", "Patrick", "Marjorie", "Harry", "Hannah", "Ben", "Zachary"]
    test_itterations = 200
    ss = Secret_Santa()

    for i in range(test_itterations):
        secret_santa_list = ss.create_secret_santa_list(from_people)
        for giver, receiver in secret_santa_list:
            assert giver != receiver

# ---------- create_secret_santa_list ---------- #
def test_create_secret_santa_requires_two():
    ss = Secret_Santa("")
    with pytest.raises(InsufficientNamesException):
        ss.create_secret_santa_list(["OnlyOne"])

def test_create_secret_santa_derangement_and_permutation(ss, names):
    # Seed RNG for determinism
    random.seed(12345)
    pairs = ss.create_secret_santa_list(names)

    # No fixed points
    assert all(giver != receiver for giver, receiver in pairs)

    # Same multiset
    givers = [g for g, _ in pairs]
    receivers = [r for _, r in pairs]
    assert sorted(givers) == sorted(names)
    assert sorted(receivers) == sorted(names)

def test_create_secret_santa_works_for_two_people():
    ss = Secret_Santa("")
    random.seed(0)
    pairs = ss.create_secret_santa_list(["A", "B"])
    assert set(pairs) in ({("A", "B"), ("B", "A")}, {("B", "A"), ("A", "B")})
    assert all(a != b for a, b in pairs)

# ---------- generate_formatted_list ----------#
def test_generate_formatted_list_format(ss):
    random.seed(999)
    out = ss.generate_formatted_list(ss.people)
    lines = out.splitlines()
    # One line per participant
    assert len(lines) == len(ss.people)
    # Each line formatted as "giver 👉 receiver"
    for line in lines:
        assert "👉" in line
        giver, receiver = [p.strip() for p in line.split("👉")]
        assert giver and receiver and giver != receiver
    # No trailing newline 
    assert not out.endswith("\n")

# ---------- append ----------#
def test_append_adds_and_validates():
    ss = Secret_Santa("Alice, Bob")
    ss.append("Charlie, Dana")
    assert ss.people == ["Alice", "Bob", "Charlie", "Dana"]

def test_append_duplicate_raises():
    ss = Secret_Santa("Alice, Bob")
    with pytest.raises(DuplicateNameException):
        ss.append("Bob, Charlie")

# ---------- __add__ ---------- #
def test_add_returns_new_instance_and_combines():
    ss = Secret_Santa("Alice, Bob")
    result = ss + "Charlie, Dana"
    # new object, correct type
    assert isinstance(result, Secret_Santa)
    assert result is not ss
    # combined values present
    assert result.people == ["Alice", "Bob", "Charlie", "Dana"]

def test_add_does_not_mutate_original():
    ss = Secret_Santa("Alice, Bob")
    _ = ss + "Charlie"
    assert ss.people == ["Alice", "Bob"] # original unchanged



# ---------- __str__ ---------- #
def test_str_shape_only_due_to_randomness(ss):
    random.seed(777)
    s = str(ss)
    # Expect 4 lines, each "name 👉 name"
    lines = s.splitlines()
    assert len(lines) == 4
    assert all(re.match(r".+\s👉\s.+", line) for line in lines)