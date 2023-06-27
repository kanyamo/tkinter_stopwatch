import json
from constants import HIGH_SCORE_FILENAME


class HighScoreManager():
    MAX_HIGH_SCORES = 5
    FILENAME = HIGH_SCORE_FILENAME

    def __init__(self):
        self.high_scores = []

    def load(self):
        try:
            with open(self.FILENAME, "r") as f:
                self.high_scores = self.json_to_scores(f.read())
        except FileNotFoundError:
            # create a new file if the file does not exist
            with open(self.FILENAME, "w") as f:
                pass

    def save(self):
        with open(self.FILENAME, "w") as f:
            f.write(self.scores_to_json())

    def add(self, high_score: "HighScore"):
        self.high_scores.append(high_score)
        # sort the high scores by diff in ascending order
        self.high_scores.sort(key=lambda x: x.diff)

    # Consider whether to include it in the high scores, and if so, update it
    def update(self, high_score: "HighScore"):
        if len(self.high_scores) < self.MAX_HIGH_SCORES:
            self.add(high_score)
        else:
            # check if the new high score is better than the worst high score
            if high_score.diff < self.high_scores[-1].diff:
                self.high_scores[-1] = high_score
                # sort the high scores by diff in ascending order
                self.high_scores.sort(key=lambda x: x.diff)

    def scores_to_json(self):
        return json.dumps([high_score.to_dict() for high_score in self.high_scores])

    def json_to_scores(self, json_str: str):
        return [HighScore.from_dict(high_score_dict) for high_score_dict in json.loads(json_str)]

    def __str__(self):
        return "\n".join([str(high_score) for high_score in self.high_scores])


class HighScore:

    def __init__(self, name: str, diff: float):
        self.name = name
        self.diff = diff

    def to_dict(self):
        return {"name": self.name, "diff": self.diff}

    @classmethod
    def from_dict(cls, dict_: dict):
        return cls(dict_["name"], dict_["diff"])

    def __str__(self):
        return f"{self.name}: {self.diff:.2f}"
