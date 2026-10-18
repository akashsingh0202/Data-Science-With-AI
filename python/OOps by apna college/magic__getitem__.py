class Team:
    def __init__(self, members):
        self.members = members

    def __getitem__(self, index):
        return self.members[index]

team = Team(["Aman", "Ravi", "Neha"])

print(team[0])
print(team[1])