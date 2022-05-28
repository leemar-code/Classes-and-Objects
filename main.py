class Student:
    # [assignment] Skeleton class. Add your code here
    # comment
    # comment
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score
    def change_name(self, name):
        return str(self.name)
    def change_age(self, age):
        return int(self.age)
    def add_track(self, tracks):
        return list(self.tracks)
    def get_score(self, score):
        return float(self.score)
Bob = Student(name="folasayo", age=18, tracks=["Html", "CSS"], score=89.9)
Bob.name = str("Atser")
Bob.age = 100
Bob.tracks = list(["software development", "Web development"])
Bob.score = float(99)
print(Bob.name)
print(Bob.age)
print(Bob.tracks)
print(Bob.score)