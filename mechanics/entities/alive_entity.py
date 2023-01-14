from lib.utils import clamp


# TODO: change name, update methods (are they needed here?)
class Health:
    def __init__(self, max_health):
        self.max_health = max_health
        self.current_health = max_health

    def damage(self, amount) -> None:
        self.current_health = clamp(
            self.current_health - amount,
            lower_limit=0,
            upper_limit=self.max_health,
        )

    def heal(self, amount) -> None:
        self.current_health = clamp(
            self.current_health + amount,
            lower_limit=0,
            upper_limit=self.max_health,
        )

    @property
    def is_alive(self) -> bool:
        return self.current_health > 0
