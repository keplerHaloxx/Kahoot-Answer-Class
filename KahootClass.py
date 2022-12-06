from urllib.request import urlopen
from json import load

class Kahoot:
    def __init__(self, uuid):
        self.uuid = uuid
        self.data = load(urlopen(f"https://play.kahoot.it/rest/kahoots/{uuid}"))

    def get_quiz_details(self):
        return {
            "uuid": self.data["uuid"],
            "creator_username": self.data["creator_username"],
            "title": self.data["title"],
            "description": self.data["description"],
            "cover": self.data["cover"]}

    def get_questions(self):
        return self.data["questions"]

    def get_question_names(self):
        questions = []
        for i in range(self.get_quiz_length()):
            if self.get_question_details(i)["type"] == "content":
                questions.append(self.get_question_details(i)["title"])
            else:
                questions.append(self.get_question_details(i)["question"])
        return questions

    def get_quiz_length(self):
        return len(self.data["questions"])

    def get_question_details(self, question):
        if self.data["questions"][question]["type"] == "content":
            data = {
                "type": "content",
                "title": self.data["questions"][question]["title"],
                "description": self.data["questions"][question]["description"]
            }
        else:
            data = {
                "type": self.data["questions"][question]["type"],
                "question": str(self.data["questions"][question]["question"]).replace('"', '\\"').replace("<p>", "").replace("</p>", "").replace("<strong>", "").replace("</strong>", "").replace("<br/>", "\n").replace("</span>", "").replace("</mo>", "").replace("</mrow>", "").replace("<mn>", "").replace("</mn>", "").replace("</annotation>", "").replace("</semantics>", "").replace("</math>", "").replace("<span>", "").replace("<math>", "").replace("<semantics>", "").replace("<mrow>", "").replace("<mo>", "").replace("<msup>", "").replace("<mi>", "").replace("</mi>", "").replace("</msup>", ""),
                "choices": self.data["questions"][question]["choices"],
                "amount_of_answers": len(self.data["questions"][question]["choices"]),
                "amount_of_correct_answers": 0}

            for i in range(len(self.data["questions"][question]["choices"])):
                if self.data["questions"][question]["choices"][i]["correct"]:
                    data["amount_of_correct_answers"] += 1

        if "layout" in self.data["questions"][question]:
            data["layout"] = self.data["questions"][question]["layout"]
        else:
            data["layout"] = None

        if "image" in self.data["questions"][question]:
            data["image"] = self.data["questions"][question]["image"]
        else:
            data["image"] = None

        if "pointsMultiplier" in self.data["questions"][question]:
            data["pointsMultiplier"] = self.data["questions"][question]["pointsMultiplier"]
        else:
            data["pointsMultiplier"] = None

        if "time" in self.data["questions"][question]:
            data["time"] = self.data["questions"][question]["time"]
        else:
            data["time"] = None

        return data

    def get_answer(self, question):
        answers = []
        if self.get_question_details(question)["type"] == "content":
            answers = None

        elif self.get_question_details(question)["type"] == "jumble":
            for i in self.get_question_details(question)["choices"]:
                answers.append(i["answer"])

        else:
            for i in self.get_question_details(question)["choices"]:
                if i["correct"]:
                    answers.append(i["answer"])
            if len(answers) == 0:
                answers = None
        return answers
