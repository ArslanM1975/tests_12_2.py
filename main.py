import unittest

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name

class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1

        while self.participants:
            for participant in self.participants.copy():
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers

class TournamentTest(unittest.TestCase):
    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_usain = Runner("Усэйн", speed=10)
        self.runner_andrei = Runner("Андрей", speed=9)
        self.runner_nik = Runner("Ник", speed=3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            print(result)
        print()

    def test_race_usain_nik(self):
        tournament = Tournament(90, self.runner_usain, self.runner_nik)
        results = tournament.start()

        # Печатаем результаты для отладки
        print("Результаты забега Усэйн и Ник: ", {k: str(v) for k, v in results.items()})

        self.all_results[max(results.keys())] = results
        self.assertEqual(str(results[1]), "Усэйн")

    def test_race_andrei_nik(self):
        tournament = Tournament(90, self.runner_andrei, self.runner_nik)
        results = tournament.start()

        # Печатаем результаты для отладки
        print("Результаты забега Андрей и Ник: ", {k: str(v) for k, v in results.items()})

        self.all_results[max(results.keys())] = results
        self.assertEqual(str(results[1]), "Андрей")

    def test_race_usain_andrei_nik(self):
        tournament = Tournament(90, self.runner_usain, self.runner_andrei, self.runner_nik)
        results = tournament.start()

        # Печатаем результаты для отладки
        print("Результаты забега Усэйн, Андрей и Ник: ", {k: str(v) for k, v in results.items()})

        self.all_results[max(results.keys())] = results
        self.assertEqual(str(results[1]), "Усэйн")  # Ожидаем, что Усэйн финиширует первым

if __name__ == '__main__':
    unittest.main()
