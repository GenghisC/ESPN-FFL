# ESPN Fantasy Football API - Quick Reference

## 🎯 Most Common Operations

### Setup
```python
from espn_api.football import League
league = League(league_id=ID, year=2025, espn_s2=COOKIE, swid=SWID)
```

### League Info
| Operation | Code |
|-----------|------|
| League name | `league.settings.name` |
| Current week | `league.current_week` |
| Number of teams | `len(league.teams)` |
| Refresh data | `league.refresh()` |

### Teams & Standings
| Operation | Code |
|-----------|------|
| All teams | `league.teams` |
| Current standings | `league.standings()` |
| Weekly standings | `league.standings_weekly(week=5)` |
| Team record | `team.wins`, `team.losses` |
| Team points | `team.points_for`, `team.points_against` |
| Team roster | `team.roster` |

### Matchups
| Operation | Code |
|-----------|------|
| Current scoreboard | `league.scoreboard()` |
| Week N scoreboard | `league.scoreboard(week=N)` |
| Detailed box scores | `league.box_scores()` |
| Week N box scores | `league.box_scores(week=N)` |

### Players
| Operation | Code |
|-----------|------|
| Find by name | `league.player_info(name="Player Name")` |
| Find by ID | `league.player_info(playerId=12345)` |
| Top free agents | `league.free_agents(size=50)` |
| Free agents by pos | `league.free_agents(position='QB', size=20)` |
| Player points | `player.total_points`, `player.avg_points` |
| Player projection | `player.projected_total_points` |

### Transactions
| Operation | Code |
|-----------|------|
| All transactions | `league.transactions()` |
| Waivers only | `league.transactions(types={'WAIVER'})` |
| Free agent adds | `league.transactions(types={'FREEAGENT'})` |
| Trades | `league.transactions(types={'TRADE'})` |
| Recent activity | `league.recent_activity(size=25)` |

### Analytics
| Operation | Code |
|-----------|------|
| Power rankings | `league.power_rankings()` |
| Week N rankings | `league.power_rankings(week=N)` |
| Top scorer | `league.top_scorer()` |
| Lowest scorer | `league.least_scorer()` |
| Highest week | `league.top_scored_week()` |
| Lowest week | `league.least_scored_week()` |
| Most points against | `league.most_points_against()` |

### Draft
| Operation | Code |
|-----------|------|
| All draft picks | `league.draft` |
| Pick details | `pick.team`, `pick.player`, `pick.round_num` |

## 📊 Object Properties Reference

### Team Object
```python
team.team_id              # Unique ID
team.team_name            # Team name
team.team_abbrev          # Abbreviation
team.owner                # Owner name
team.wins                 # Win count
team.losses               # Loss count
team.ties                 # Tie count
team.points_for           # Total points scored
team.points_against       # Total points allowed
team.standing             # League rank
team.playoff_pct          # Playoff probability
team.division_id          # Division ID
team.division_name        # Division name
team.roster               # List of Player objects
team.schedule             # List of opponent Teams
team.scores               # List of weekly scores
team.outcomes             # List of 'W'/'L'/'T'
team.mov                  # Margins of victory
team.streak_type          # 'WIN'/'LOSS'/'TIE'
team.streak_length        # Current streak
team.acquisitions         # Number of adds
team.drops                # Number of drops
team.trades               # Number of trades
team.waiver_rank          # Waiver priority
```

### Player Object
```python
player.playerId           # Unique player ID
player.name               # Player name
player.position           # Position (QB, RB, etc.)
player.proTeam            # NFL team (DAL, KC, etc.)
player.lineupSlot         # Current slot
player.eligibleSlots      # Available positions
player.total_points       # Season total
player.avg_points         # Points per game
player.projected_total_points    # Season projection
player.projected_avg_points      # Projected PPG
player.percent_owned      # % owned in leagues
player.percent_started    # % started
player.posRank            # Position rank
player.injured            # True/False
player.injuryStatus       # ACTIVE/OUT/QUESTIONABLE/etc
player.acquisitionType    # DRAFT/ADD/TRADE
player.onTeamId           # Current team ID
player.stats              # Detailed statistics dict
```

### BoxScore Object
```python
boxscore.home_team        # Team object
boxscore.away_team        # Team object
boxscore.home_score       # Home score
boxscore.away_score       # Away score
boxscore.home_lineup      # List of player stats
boxscore.away_lineup      # List of player stats
boxscore.home_projected   # Projected home score
boxscore.away_projected   # Projected away score
```

### Matchup Object
```python
matchup.home_team         # Team object
matchup.away_team         # Team object
matchup.home_score        # Home score
matchup.away_score        # Away score
matchup.matchup_type      # REGULAR/PLAYOFF/CHAMPIONSHIP
matchup.week              # Week number
```

### League Object
```python
league.league_id          # League ID
league.year               # Season year
league.current_week       # Current week
league.nfl_week           # NFL week
league.teams              # List of Team objects
league.settings           # Settings object
league.members            # List of member dicts
league.draft              # List of draft picks
league.previousSeasons    # List of years
```

### Settings Object
```python
settings.name             # League name
settings.size             # Number of teams
settings.playoff_team_count        # Playoff spots
settings.reg_season_count          # Regular season weeks
settings.scoring_type              # Scoring format
settings.trade_deadline            # Trade deadline week
settings.veto_votes_required       # Veto threshold
settings.playoff_seed_tie_rule     # Tiebreaker rule
```

## 🎨 Position Codes

| Code | Position |
|------|----------|
| QB | Quarterback |
| RB | Running Back |
| WR | Wide Receiver |
| TE | Tight End |
| K | Kicker |
| D/ST | Defense/Special Teams |
| FLEX | Flex Position |
| BE | Bench |
| IR | Injured Reserve |

## 📈 Injury Status Codes

| Code | Meaning |
|------|---------|
| ACTIVE | Healthy/Active |
| QUESTIONABLE | Questionable |
| DOUBTFUL | Doubtful |
| OUT | Out |
| IR | Injured Reserve |
| PUP | Physically Unable to Perform |
| SUSPENSION | Suspended |

## 🔄 Transaction Types

| Type | Description |
|------|-------------|
| WAIVER | Waiver wire claim |
| FREEAGENT | Free agent add |
| TRADE | Trade between teams |
| WAIVER_ERROR | Failed waiver claim |

## 🏆 Matchup Types

| Type | Description |
|------|-------------|
| REGULAR | Regular season game |
| PLAYOFF | Playoff game |
| CHAMPIONSHIP | Championship game |

## ⚙️ Common Filters

### Get Top Performers
```python
# Top scoring teams
sorted(league.teams, key=lambda x: x.points_for, reverse=True)[:5]

# Top players by position
qbs = [p for t in league.teams for p in t.roster if p.position == 'QB']
sorted(qbs, key=lambda x: x.total_points, reverse=True)[:10]
```

### Get Close Games
```python
matchups = league.scoreboard()
close = [m for m in matchups if abs(m.home_score - m.away_score) < 10]
```

### Get Best Available Free Agents
```python
top_fa = league.free_agents(size=50)
best = sorted(top_fa, key=lambda x: x.avg_points, reverse=True)[:20]
```

### Get Teams in Playoff Hunt
```python
playoff_teams = [t for t in league.teams if t.playoff_pct > 50]
bubble_teams = [t for t in league.teams if 10 < t.playoff_pct < 90]
```

## 🔧 Useful Helper Functions

### Win Percentage
```python
def win_pct(team):
    total_games = team.wins + team.losses + team.ties
    return (team.wins + team.ties * 0.5) / total_games if total_games > 0 else 0
```

### Points Per Game
```python
def ppg(team):
    games = team.wins + team.losses + team.ties
    return team.points_for / games if games > 0 else 0
```

### Get Starter vs Bench Points
```python
def split_starter_bench_points(lineup):
    starters = sum(p.points for p in lineup if p.slot_position != 'BE')
    bench = sum(p.points for p in lineup if p.slot_position == 'BE')
    return starters, bench
```

## 🚨 Error Codes & Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| 403 Forbidden | Expired cookie | Get fresh ESPN_S2 |
| 401 Unauthorized | Invalid credentials | Check SWID and ESPN_S2 |
| 404 Not Found | Wrong league ID or year | Verify league ID from URL |
| Empty roster | Week not loaded | Call `load_roster_week(week)` |
| Player not found | Wrong name/ID | Use exact spelling or player ID |

## 📱 Quick Tips

1. **Refresh regularly**: `league.refresh()` to get latest data
2. **Store player IDs**: More reliable than names
3. **Check current_week**: Ensures you're looking at right data
4. **Use box_scores**: Most detailed matchup information
5. **Handle injuries**: Always check `player.injured` and `player.injuryStatus`
6. **Week ranges**: 1-17 for regular season, 18+ for playoffs
7. **Cookie refresh**: Update ESPN_S2 weekly to avoid auth errors
8. **Position filters**: Save time by filtering free agents by position

## 🎯 One-Liner Examples

```python
# League leader in scoring
max(league.teams, key=lambda x: x.points_for)

# Team with worst record
min(league.teams, key=lambda x: x.wins)

# Current week winners
[m.home_team if m.home_score > m.away_score else m.away_team 
 for m in league.scoreboard()]

# All starting QBs
[p for t in league.teams for p in t.roster 
 if p.position == 'QB' and p.lineupSlot == 'QB']

# Teams on winning streak
[t for t in league.teams if t.streak_type == 'WIN' and t.streak_length >= 3]

# High scorers this week
[t for t in league.teams if t.scores[-1] > 130]

# Best available RB
max(league.free_agents(position='RB', size=20), key=lambda x: x.avg_points)
```

---

**💡 Pro Tip**: Bookmark this page for quick reference while coding!
