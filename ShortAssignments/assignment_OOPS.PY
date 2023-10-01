# Problem Statement:
# You are going to write a program that models a fantasy sports league. You can pick the
# sport. You should have classes that represent: the entire league, a team, and a player.
# You should store appropriate information about each of these entities and you should –
# at minimum – have methods that provide Create and Read functionality.
class League():
    def __init__(self, league_name, league_budget=100000):
        self.league_name = league_name
        self.number_of_teams = 20
        self.league_budget = league_budget
        self.teams = []

    def __str__(self) -> str:
        return f"{self.league_name}"

    def add_team(self, team):
        if isinstance(team, Team):
            self.teams.append(team)
            print(f"{team} succesfully added!")
        else:
            print(f"{team} is not League, Hence addition failed!")

    def remove_team(self, team_to_remove):
        if isinstance(team_to_remove, Team):
            if team_to_remove in self.teams:
                try:
                    self.teams.remove(team_to_remove)
                    print(
                        f"{team_to_remove.team_name} is removed from {self.league_name}. Remove Success!")
                except ValueError:
                    print(
                        f"{team_to_remove.team_name} is not present in {self.league_name}. Remove failed!")
        else:
            print("Team cannot be removed since it's not of Team type.")

    def display_all_teams(self):
        if len(self.teams) != 0:
            print(
                f"---------- Teams in {self.league_name}  - Manager ----------")
            for team in self.teams:
                print(f"{team.team_name} - {team.team_manager}")
        else:
            print("No players to display!")


class Team(League):

    def __init__(self, league_name, team_name, team_manager):
        super().__init__(league_name)
        self.team_name = team_name
        self.team_manager = team_manager
        self.team_players = []

    def __str__(self) -> str:
        return f"{self.team_name}"

    def add_player(self, player):
        if isinstance(player, Player):
            self.team_players.append(player)
            print(f"{player.player_name} succesfully added!!")
        else:
            print(f"{player} is not Player, Hence addition failed!")

    def update_team_manager(self, team_manager_to_update):
        if (self.team_manager and type(team_manager_to_update) == str):
            self.team_manager = team_manager_to_update
            print("Team Manager updated!")
        else:
            print("Connot update Team Manager.")

    def remove_player(self, player_to_remove):
        if isinstance(player_to_remove, Player):
            if player_to_remove in self.team_players:
                try:
                    self.team_players.remove(player_to_remove)
                    print(
                        f"{player_to_remove.player_name} is removed from {self.team_name}. Remove Success!")
                except ValueError:
                    print(
                        f"{player_to_remove.player_name} is not present in {self.team_name}. Remove failed!")
        else:
            print("Player cannot be removed since it's not of Player type.")

    def display_all_players(self):
        if len(self.team_players) != 0:
            print(
                f"---------- Players of {self.team_name} Football Club ----------")
            for player in self.team_players:
                print(f"PlayerName: {player.player_name.upper()}")
                print(f"Age: {player.age}")
                print(f"Position: {player.position}")
                print(f"Jersey: {player.jersey_number}")
                print(f"Weekly wage: ${player.weekly_wage}")
        else:
            print("No players to display!")


class Player(Team):

    def __init__(self, league_name, team_name, team_manager, player_name, position, age, jersey_number, weekly_wage):
        super().__init__(league_name, team_name, team_manager)
        self.player_name = player_name
        self.position = position
        self.age = age
        self.jersey_number = jersey_number
        self._weekly_wage = weekly_wage

    def __str__(self) -> str:
        return f"Hola! I'm {self.player_name}, I am a {self.position} and I play for {self.team_name} in {self.league_name}."

    @property
    def weekly_wage(self):
        return self._weekly_wage

    @weekly_wage.setter
    def weekly_wage(self, new_wage):
        if (new_wage > 0 and (type(new_wage) == int or type(new_wage) == float)):
            self._weekly_wage = new_wage
        else:
            print("Wage update failed! Please enter appropriate wage.")


# creating league
premier_league = League("Premier League", 1000000)
# creating teams
mancity = Team("Premier League", "Manchester City", "Pep Gurodiola")
liverpool = Team("Premier League", "Liverpool", "Roy Hudson")
spurs = Team("Premier League", "Tottenham", "Maricio Potttechino")
# adding teams to league
premier_league.add_team(liverpool)
premier_league.add_team(mancity)
premier_league.add_team(spurs)
# update team manager
liverpool.update_team_manager("Jurgen Klopp")
# creating players
gundagon = Player("Premier League", "Manchester City",
                  "Pep Guardiola", "Ilkay Gundagon", "Midfielder", 30, 8, 39000)
haland = Player("Premier League", "Manchester City",
                "Pep Guardiola", "Erling Haaland", "Striker", 23, 9, 50000)
kdb = Player("Premier League", "Manchester City", "Pep Guardiola",
             "Kevin De Bruyne", "Midfielder", 29, 17, 55000)
salah = Player("Premier League", "Liverpool", "Jurgen Klopp",
               "Mohammed Salah", "Forward", 29, 11, 45000)
nunez = Player("Premier League", "Liverpool", "Jurgen Klopp",
               "Darwin Nunez", "Forward", 24, 7, 30000)
son = Player("Premier League", "Tottenham", "Maricio Potttechino",
             "Son heung Min", "Forward", 27, 7, 42000)
# change player wage
print(f"{nunez.player_name} Wage:{nunez.weekly_wage}")
nunez.weekly_wage = 35000
print(f"Updated {nunez.player_name} Wage:{nunez.weekly_wage}")
# adding players to teams
liverpool.add_player(nunez)
liverpool.add_player(salah)
mancity.add_player(kdb)
mancity.add_player(haland)
mancity.add_player(gundagon)
spurs.add_player(son)
# displaying players of teams
mancity.display_all_players()
liverpool.display_all_players()
spurs.display_all_players()
# displaying all teams of league
premier_league.display_all_teams()
print("----------------------------")
# remove player from team
mancity.remove_player(gundagon)
mancity.display_all_players()
# remove team from league
premier_league.remove_team(spurs)
print("----------------------------")
premier_league.display_all_teams()
