class Programmer:
    def __init__(self, name: str, language: str, skills: int):
        self.name = name
        self.language = language
        self.skills = skills

    def watch_course(self, course_name, language, skills_earned):
        result = f"{self.name} does not know {language}"
        if self.language == language:
            self.skills += skills_earned
            result = f"{self.name} watched {course_name}"
        return result

    def change_language(self, new_language, skills_needed):
        result = f"{self.name} needs {skills_needed - self.skills} more skills"
        if skills_needed <= self.skills:
            if self.language != new_language:
                result = f"{self.name} switched from {self.language} to {new_language}"
                self.language = new_language
            else:
                result = f"{self.name} already knows {new_language}"
        return result


# programmer = Programmer('John', 'Java', 50)
# print(programmer.watch_course('Python Masterclass', 'Python', 84))
# print(programmer.change_language('Java', 30))
# print(programmer.change_language('Python', 100))
# print(programmer.watch_course('Java: zero to hero', 'Java', 84))
# print(programmer.change_language('Python', 100))
# print(programmer.watch_course('Python Masterclass', 'Python', 84))

'''
John does not know Python
John already knows Java
John needs 50 more skills
John watched Java: zero to hero
John switched from Java to Python
John watched Python Masterclass
'''