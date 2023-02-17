class Name:
    """Name for pokemon."""

    def __init__(
        self,
        english: str,
        japanese: str,
        chinese: str,
        french: str
    ) -> None:
        self.english  = english 
        self.japanese = japanese
        self.chinese = chinese
        self.french = french


class Base:
    """Base stats for pokemon."""

    def __init__(
        self,
        hp: int,
        attack: int,
        defense: int,
        sp_attack: int,
        sp_defense: int,
        speed: int
    ) -> None:
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.sp_attack = sp_attack
        self.sp_defense = sp_defense
        self.speed = speed
        

class Pokemon:
    """My pokemon class."""

    def __init__(
        self,
        id: int,
        name: Name,
        type: list[str],
        base: Base
    ) -> None:
        self.id = id
        self.name = name
        self.type = type
        self.base = base
