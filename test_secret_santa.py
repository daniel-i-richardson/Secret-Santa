from secret_santa import Secret_Santa

def test_randomization():
    from_people = ["Jim", "Brenda", "Katie", "Matt", "Evelyn", "Daniel", "Susanna", "Nathan", "Tatiana", "Patrick", "Marjorie", "Harry", "Hannah", "Ben", "Zachary"]
    test_itterations = 200
    ss = Secret_Santa()

    for i in range(test_itterations):
        secret_santa_list = ss.create_secret_santa_list(from_people)
        for giver, receiver in secret_santa_list:
            assert giver != receiver

#def test_duplicates():
