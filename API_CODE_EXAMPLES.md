# ESPN Fantasy Football API - Code Examples
# Based on espn-api Python library

## Table of Contents
1. [Authentication & Setup](#authentication--setup)
2. [League Information](#league-information)
3. [Team Operations](#team-operations)
4. [Player Operations](#player-operations)
5. [Matchup & Scoring](#matchup--scoring)
6. [Transactions](#transactions)
7. [Analytics & Rankings](#analytics--rankings)
8. [Advanced Queries](#advanced-queries)

---

## Authentication & Setup

### Initialize League (Private League)
```python
from espn_api.football import League

league_id = 987132062
year = 2025
espn_s2 = 'YOUR_ESPN_S2_COOKIE'
swid = '{YOUR-SWID-COOKIE}'

league = League(league_id=league_id, year=year, espn_s2=espn_s2, swid=swid)
```

### Initialize League (Public League)
```python
from espn_api.football import League

league_id = 987132062
year = 2025

league = League(league_id=league_id, year=year)
```

### Refresh League Data
```python
# Get latest data without creating new instance
league.refresh()
```

---

## League Information

### Basic League Info
```python
# League name
print(f"League: {league.settings.name}")

# Current week
print(f"Current Week: {league.current_week}")

# Number of teams
print(f"Teams: {len(league.teams)}")

# Playoff settings
print(f"Playoff Teams: {league.settings.playoff_team_count}")
print(f"Regular Season Weeks: {league.settings.reg_season_count}")

# Scoring type
print(f"Scoring: {league.settings.scoring_type}")
```

### League Members
```python
# Get all league members
for member in league.members:
    print(f"Member: {member['firstName']} {member['lastName']}")
    print(f"  ID: {member['id']}")
```

### League Settings
```python
settings = league.settings

print(f"Trade Deadline: Week {settings.trade_deadline}")
print(f"Veto Votes Required: {settings.veto_votes_required}")
print(f"Playoff Seed Tiebreaker: {settings.playoff_seed_tie_rule}")
```

---

## Team Operations

### Get All Teams
```python
# List all teams
for team in league.teams:
    print(f"{team.team_name}: {team.wins}-{team.losses}")
```

### Get Standings (Current)
```python
# Get current standings
standings = league.standings()

for i, team in enumerate(standings, 1):
    print(f"{i}. {team.team_name}")
    print(f"   Record: {team.wins}-{team.losses}")
    print(f"   Points For: {team.points_for:.2f}")
    print(f"   Points Against: {team.points_against:.2f}")
```

### Get Standings (Specific Week)
```python
# Get standings as of week 5
week_5_standings = league.standings_weekly(week=5)

for i, team in enumerate(week_5_standings, 1):
    print(f"{i}. {team.team_name}: {team.wins}-{team.losses}")
```

### Team Details
```python
team = league.teams[0]

# Basic info
print(f"Team Name: {team.team_name}")
print(f"Owner: {team.owner}")
print(f"Division: {team.division_name}")
print(f"Logo: {team.logo_url}")

# Record
print(f"Record: {team.wins}-{team.losses}-{team.ties}")
print(f"Standing: {team.standing}")
print(f"Playoff %: {team.playoff_pct}%")

# Scoring
print(f"Points For: {team.points_for}")
print(f"Points Against: {team.points_against}")

# Streak
print(f"Current Streak: {team.streak_length} {team.streak_type}")

# Transactions
print(f"Acquisitions: {team.acquisitions}")
print(f"Drops: {team.drops}")
print(f"Trades: {team.trades}")
print(f"Waiver Rank: {team.waiver_rank}")

# Weekly scores
for i, score in enumerate(team.scores, 1):
    print(f"Week {i}: {score:.2f} ({team.outcomes[i-1]})")
```

### Team Roster
```python
team = league.teams[0]

print(f"\n{team.team_name} Roster:")
for player in team.roster:
    status = "INJURED" if player.injured else "ACTIVE"
    print(f"{player.name} ({player.position}) - {player.proTeam}")
    print(f"  Slot: {player.lineupSlot}")
    print(f"  Points: {player.total_points:.2f}")
    print(f"  Status: {status}")
```

### Load Roster for Specific Week
```python
# Load roster for week 5
league.load_roster_week(week=5)

team = league.teams[0]
print(f"Week 5 Roster for {team.team_name}:")
for player in team.roster:
    print(f"{player.name}: {player.lineupSlot}")
```

---

## Player Operations

### Search for Player by Name
```python
# Find specific player
player = league.player_info(name="Patrick Mahomes")

if player:
    print(f"Name: {player.name}")
    print(f"Position: {player.position}")
    print(f"Team: {player.proTeam}")
    print(f"Total Points: {player.total_points}")
    print(f"Avg Points: {player.avg_points}")
    print(f"Projected Points: {player.projected_total_points}")
```

### Get Player by ID
```python
# Single player
player = league.player_info(playerId=4241389)

# Multiple players
players = league.player_info(playerId=[4241389, 3116406, 2977644])
for player in players:
    print(f"{player.name}: {player.total_points} pts")
```

### Free Agents
```python
# Get top 50 free agents
free_agents = league.free_agents(size=50)

for player in free_agents:
    print(f"{player.name} ({player.position}) - {player.proTeam}")
    print(f"  Owned: {player.percent_owned}%")
    print(f"  Started: {player.percent_started}%")
    print(f"  Avg Points: {player.avg_points:.2f}")
```

### Free Agents by Position
```python
# Get available QBs
available_qbs = league.free_agents(position='QB', size=20)

for qb in available_qbs:
    print(f"{qb.name} - {qb.proTeam}")
    print(f"  Avg: {qb.avg_points:.2f}, Projected: {qb.projected_avg_points:.2f}")
```

### Free Agents for Specific Week
```python
# Get free agents as of week 5
week_5_fa = league.free_agents(week=5, size=30)
```

### Player Statistics
```python
player = league.player_info(name="CeeDee Lamb")

# Season stats
print(f"Total Points: {player.total_points}")
print(f"Average Points: {player.avg_points}")
print(f"Position Rank: {player.posRank}")

# Weekly stats (if available)
for week, stats in player.stats.items():
    if isinstance(week, int):
        print(f"Week {week}: {stats}")

# Injury status
print(f"Injured: {player.injured}")
print(f"Injury Status: {player.injuryStatus}")

# Ownership
print(f"Owned: {player.percent_owned}%")
print(f"Started: {player.percent_started}%")
```

---

## Matchup & Scoring

### Current Week Scoreboard
```python
# Get current matchups
matchups = league.scoreboard()

for matchup in matchups:
    print(f"{matchup.away_team.team_name} ({matchup.away_score:.2f})")
    print(f"  vs")
    print(f"{matchup.home_team.team_name} ({matchup.home_score:.2f})")
    print("-" * 40)
```

### Specific Week Scoreboard
```python
# Get week 5 scoreboard
week_5_matchups = league.scoreboard(week=5)

for matchup in week_5_matchups:
    winner = matchup.home_team if matchup.home_score > matchup.away_score else matchup.away_team
    print(f"Winner: {winner.team_name}")
```

### Detailed Box Scores
```python
# Get detailed box scores with player stats
box_scores = league.box_scores()

for matchup in box_scores:
    print(f"\n{matchup.away_team.team_name} vs {matchup.home_team.team_name}")
    print(f"Score: {matchup.away_score:.2f} - {matchup.home_score:.2f}")
    
    # Away team lineup
    print(f"\n{matchup.away_team.team_name} Lineup:")
    for player in matchup.away_lineup:
        print(f"  {player.name} ({player.slot_position}): {player.points:.2f}")
    
    # Home team lineup
    print(f"\n{matchup.home_team.team_name} Lineup:")
    for player in matchup.home_lineup:
        print(f"  {player.name} ({player.slot_position}): {player.points:.2f}")
```

### Box Scores for Specific Week
```python
# Week 8 box scores
week_8_boxes = league.box_scores(week=8)
```

### Team Schedule
```python
team = league.teams[0]

print(f"{team.team_name} Schedule:")
for i, opponent in enumerate(team.schedule, 1):
    outcome = team.outcomes[i-1] if i <= len(team.outcomes) else "N/A"
    score = team.scores[i-1] if i <= len(team.scores) else 0
    print(f"Week {i}: vs {opponent.team_name} - {outcome} ({score:.2f})")
```

---

## Transactions

### Recent Transactions
```python
# Get recent transactions
transactions = league.transactions()

for transaction in transactions:
    print(f"Type: {transaction.type}")
    print(f"Date: {transaction.date}")
    print(f"Team: {transaction.team.team_name}")
    
    if transaction.players_added:
        print(f"Added: {', '.join([p.name for p in transaction.players_added])}")
    
    if transaction.players_dropped:
        print(f"Dropped: {', '.join([p.name for p in transaction.players_dropped])}")
    
    if hasattr(transaction, 'bid_amount') and transaction.bid_amount:
        print(f"Bid: ${transaction.bid_amount}")
    
    print("-" * 40)
```

### Filter Transactions by Type
```python
# Only waiver transactions
waiver_transactions = league.transactions(types={'WAIVER'})

# Only free agent adds
fa_transactions = league.transactions(types={'FREEAGENT'})

# Only trades
trades = league.transactions(types={'TRADE'})
```

### Transactions for Specific Week
```python
# Week 5 transactions
week_5_transactions = league.transactions(scoring_period=5)
```

### Recent Activity Feed
```python
# Get last 25 activities
activities = league.recent_activity(size=25)

for activity in activities:
    print(f"{activity.date}: {activity.action}")
    print(f"  Team: {activity.team.team_name}")
    if activity.player:
        print(f"  Player: {activity.player.name}")
```

### Message Board
```python
# Get league messages
messages = league.message_board()

for message in messages:
    print(f"{message['date']}: {message['text']}")
```

---

## Analytics & Rankings

### Power Rankings
```python
# Current power rankings
rankings = league.power_rankings()

for rank in rankings:
    print(f"{rank[0]}. {rank[1].team_name}")
    print(f"   Power Score: {rank[2]:.2f}")
```

### Power Rankings for Specific Week
```python
# Week 8 power rankings
week_8_rankings = league.power_rankings(week=8)
```

### Season Top Scorer
```python
top_scorer = league.top_scorer()
print(f"Season Top Scorer: {top_scorer.team_name}")
print(f"Total Points: {top_scorer.points_for:.2f}")
```

### Season Lowest Scorer
```python
lowest_scorer = league.least_scorer()
print(f"Season Lowest Scorer: {lowest_scorer.team_name}")
print(f"Total Points: {lowest_scorer.points_for:.2f}")
```

### Highest Scoring Week
```python
team, week = league.top_scored_week()
score = team.scores[week-1]
print(f"Highest Scoring Week: {team.team_name}")
print(f"Week {week}: {score:.2f} points")
```

### Lowest Scoring Week
```python
team, week = league.least_scored_week()
score = team.scores[week-1]
print(f"Lowest Scoring Week: {team.team_name}")
print(f"Week {week}: {score:.2f} points")
```

### Most Points Against
```python
unlucky_team = league.most_points_against()
print(f"Most Points Against: {unlucky_team.team_name}")
print(f"Points Against: {unlucky_team.points_against:.2f}")
```

---

## Advanced Queries

### Draft Information
```python
# Get all draft picks
draft_picks = league.draft

for pick in draft_picks:
    print(f"Round {pick.round_num}, Pick {pick.round_pick} (#{pick.overall_pick})")
    print(f"  Team: {pick.team.team_name}")
    print(f"  Player: {pick.player.name} ({pick.player.position})")
```

### Team-Specific Draft Picks
```python
team = league.teams[0]
team_picks = [pick for pick in league.draft if pick.team.team_id == team.team_id]

print(f"{team.team_name} Draft Picks:")
for pick in team_picks:
    print(f"Round {pick.round_num}: {pick.player.name}")
```

### Head-to-Head Record
```python
def get_h2h_record(team1, team2):
    """Get head-to-head record between two teams"""
    wins = 0
    losses = 0
    
    for i, opponent in enumerate(team1.schedule):
        if opponent.team_id == team2.team_id:
            if team1.outcomes[i] == 'W':
                wins += 1
            elif team1.outcomes[i] == 'L':
                losses += 1
    
    return wins, losses

team_a = league.teams[0]
team_b = league.teams[1]
wins, losses = get_h2h_record(team_a, team_b)
print(f"{team_a.team_name} vs {team_b.team_name}: {wins}-{losses}")
```

### Playoff Scenarios
```python
# Teams ordered by playoff probability
teams_by_playoff_pct = sorted(league.teams, key=lambda x: x.playoff_pct, reverse=True)

print("Playoff Probabilities:")
for team in teams_by_playoff_pct:
    print(f"{team.team_name}: {team.playoff_pct:.1f}%")
```

### Best/Worst Weekly Performances
```python
# Find best single-week performance for each team
for team in league.teams:
    if team.scores:
        best_week_score = max(team.scores)
        best_week = team.scores.index(best_week_score) + 1
        print(f"{team.team_name} - Best: Week {best_week} ({best_week_score:.2f})")
```

### Points Left on Bench
```python
def calculate_bench_points(box_score):
    """Calculate total points left on bench"""
    bench_points = 0
    
    for player in box_score.home_lineup:
        if player.slot_position == 'BE':  # Bench
            bench_points += player.points
    
    return bench_points

box_scores = league.box_scores()
for matchup in box_scores:
    home_bench = calculate_bench_points(matchup)
    print(f"{matchup.home_team.team_name}: {home_bench:.2f} pts on bench")
```

### Optimal Lineup Analysis
```python
def get_optimal_score(lineup):
    """
    Calculate what the optimal score would have been
    This is simplified - real implementation would need position constraints
    """
    # Get all non-bench players sorted by points
    active_players = [p for p in lineup if p.slot_position != 'BE']
    bench_players = [p for p in lineup if p.slot_position == 'BE']
    
    actual_score = sum(p.points for p in active_players)
    
    # Simple check: highest bench player vs lowest starter
    if bench_players and active_players:
        best_bench = max(bench_players, key=lambda x: x.points)
        worst_starter = min(active_players, key=lambda x: x.points)
        
        if best_bench.points > worst_starter.points:
            optimal_score = actual_score - worst_starter.points + best_bench.points
            return actual_score, optimal_score
    
    return actual_score, actual_score

# Check current week
box_scores = league.box_scores()
for matchup in box_scores:
    actual, optimal = get_optimal_score(matchup.home_lineup)
    if optimal > actual:
        print(f"{matchup.home_team.team_name} left {optimal - actual:.2f} pts on bench")
```

### Consistency Metrics
```python
import statistics

for team in league.teams:
    if len(team.scores) > 0:
        avg_score = statistics.mean(team.scores)
        std_dev = statistics.stdev(team.scores) if len(team.scores) > 1 else 0
        
        print(f"{team.team_name}:")
        print(f"  Avg: {avg_score:.2f}")
        print(f"  Std Dev: {std_dev:.2f}")
        print(f"  Consistency: {'High' if std_dev < 15 else 'Low'}")
```

### Strength of Schedule
```python
def calculate_strength_of_schedule(team):
    """Calculate average opponent record"""
    total_opp_wins = 0
    total_opp_games = 0
    
    for opponent in team.schedule:
        total_opp_wins += opponent.wins
        total_opp_games += (opponent.wins + opponent.losses)
    
    if total_opp_games > 0:
        return total_opp_wins / total_opp_games
    return 0

for team in league.teams:
    sos = calculate_strength_of_schedule(team)
    print(f"{team.team_name} - SOS: {sos:.3f}")
```

---

## Error Handling

### Handling Expired Cookies
```python
try:
    league = League(league_id=league_id, year=year, espn_s2=espn_s2, swid=swid)
    print("Connected successfully!")
except Exception as e:
    print(f"Error: {e}")
    print("Your ESPN_S2 cookie may have expired. Get a fresh one from your browser.")
```

### Safe Player Lookups
```python
def safe_player_lookup(league, player_name):
    """Safely lookup a player"""
    try:
        player = league.player_info(name=player_name)
        if player:
            return player
        else:
            print(f"Player '{player_name}' not found")
            return None
    except Exception as e:
        print(f"Error looking up player: {e}")
        return None

player = safe_player_lookup(league, "Patrick Mahomes")
```

---

## Tips & Best Practices

1. **Refresh Data**: Call `league.refresh()` to get latest data without creating new instance
2. **Week Numbers**: Week 1 is first week of NFL season, typically starts around Week 1 of September
3. **Current Season**: Only current season supports live data (box_scores, free_agents)
4. **Historical Data**: Use same League class with different `year` parameter
5. **Rate Limiting**: ESPN may rate limit excessive requests - add delays for bulk operations
6. **Cookie Expiration**: ESPN_S2 cookies expire frequently - plan to refresh weekly
7. **Player IDs**: Store player IDs for consistent lookups across weeks/seasons
8. **Roster Loading**: Use `load_roster_week(week)` to see historical rosters
9. **Box Scores**: Most detailed data source - includes player-level stats
10. **Transactions**: Check transaction types to filter correctly
