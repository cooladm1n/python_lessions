from tasks import Animal, Dog, Cat, Zoo


def test_animal_inheritance():
    dog = Dog("Buddy")
    cat = Cat("Whiskers")
    assert dog.make_sound() == "Woof!"
    assert cat.make_sound() == "Meow!"


def test_zoo():
    zoo = Zoo()
    zoo.add_animal(Dog("Rex"))
    zoo.add_animal(Cat("Fluffy"))
    sounds = zoo.make_all_sounds()
    assert "Woof!" in sounds
    assert "Meow!" in sounds


