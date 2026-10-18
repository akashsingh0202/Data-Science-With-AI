class Team:
    def __init__(self, members):
        self.members = members

    def __contains__(self, name):
        return name in self.members

team = Team(["Aman", "Ravi", "Neha"])

print("Ravi" in team)
print("Akash" in team)