from game_api.models import Role

initial_roles = [
  Role(
    name='Quarentine Specialist', 
    description="Prevent disease cube placements [and outbreaks] in the city you are in and all cities connected to it."
  ),
  Role(
    name='Scientist', 
    description="You need only 4 cards of the same color to do the Discover a Cure action"
  ),
  Role(
    name='Contingency Planner', 
    description="As an actuon, take any discarded Event card and store it on this card. When you play the stored Event card, remove it from the game. Limit: 1 Event card on this card at a time, which is not part of your hand."
  ),
  Role(
    name='Researcher', 
    description="You may give any 1 of your City cards when you Share Knowledge. It need not match your city. A player who Shares Knowledge with you on their turn can take any 1 of your City cards."
  ),
  Role(
    name='Operations Expert', 
    description="As an action, buold a resarch station in the city you are in [no City card needed]. Once per turn as a n action, move from a research station to any city by discarding any City card."
  ),
  Role(
    name='Medic', 
    description="Remove all cubes of one color when doing Treat Disease. Automatically remove cubes of cured disases from the city you are in [and prevent them from being placed there]."
  ),
  Role(
    name='Dispatcher', 
    description="Move another player's pawn as if it were yours. As an action, move any pawn to a city with another pawn. Git permission before moving another player's pawn."
  ),
]