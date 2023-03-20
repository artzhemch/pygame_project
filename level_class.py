import os


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

    def __repr__(self):
        return f'Level({self.black_prob}, {self.spawn_time}, {self.duration})'


def read_levels_from_file(filename) -> dict:
    with open(os.path.join('levels', filename)) as file:
        lines = list(map(lambda x: x.strip().split(', '), file.readlines()))
    levels = []
    for prob, spawn_time, duration in lines:
        levels.append(Level(float(prob), int(spawn_time), int(duration)))
    return dict(enumerate(levels, start=1))


levels = read_levels_from_file('levels.txt')
