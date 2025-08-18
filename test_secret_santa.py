from main import create_secret_santa_list

def test_randomization():
    name_list = ["Jim", "Brenda", "Katie", "Matt", "Evelyn", "Daniel", "Susanna", "Nathan", "Tatiana", "Patrick", "Marjorie", "Harry", "Hannah", "Ben", "Zachary"]
    test_itterations = 200

    for i in range(test_itterations):
        secret_santa_list = create_secret_santa_list(name_list)
        for giver, receiver in secret_santa_list.items():
            assert giver != receiver
