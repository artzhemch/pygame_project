class Level:
    """Класс уровня"""
    def __init__(self, black_prob: float, spawn_time: int, duration: int):
        """black_prob: вероятность появления черного самолёта
        spawn_time: интервал появления самолётов
        duration: продолжительность уровня"""
        self.black_prob = black_prob
        self.spawn_time = spawn_time
        self.duration = duration

    def load(self) -> tuple[float, int, int]:
        return self.black_prob, self.spawn_time, self.duration


level1 = Level(0, 10, 60)
level2 = Level(0.3, 8, 70)