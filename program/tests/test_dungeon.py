from program.dungeon_run import Player

player = Player()
def test_hero_choice(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: next(iter("1")))
    assert player.hero_choice() == "Knight"

def test_name_your_hero(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: next(iter("Ggg")))
    assert player.name_your_hero("Wizard") == {'Name': 'Ggg', 'Character': 'Wizard', 'Treasure': 0}

def test_check_name():
    assert player.check_name("Bruno") is True
    assert player.check_name("Nina") is False

