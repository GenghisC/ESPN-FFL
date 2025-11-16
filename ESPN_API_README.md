# ESPN Fantasy Football API Documentation

Comprehensive Swagger/OpenAPI-style documentation for the ESPN Fantasy Football API v3.

## 📚 Documentation Files

This documentation package includes:

1. **`espn_fantasy_api_docs.yaml`** - OpenAPI 3.0 specification in YAML format
2. **`API_CODE_EXAMPLES.md`** - Comprehensive Python code examples
3. **`test_espn_api.py`** - Working test script
4. **`explore_espn_api.py`** - API exploration tool

## 🚀 Quick Start

### Installation

```bash
pip install espn-api
```

### Basic Usage

```python
from espn_api.football import League

# Private League
league = League(
    league_id=987132062, 
    year=2025, 
    espn_s2='YOUR_ESPN_S2_COOKIE',
    swid='{YOUR-SWID-COOKIE}'
)

# Get standings
for team in league.standings():
    print(f"{team.team_name}: {team.wins}-{team.losses}")
```

## 📖 Viewing the Documentation

### Option 1: Swagger UI (Recommended)

Use the online Swagger Editor to view the interactive API documentation:

1. Go to https://editor.swagger.io/
2. Click **File** → **Import File**
3. Select `espn_fantasy_api_docs.yaml`
4. Explore the interactive documentation

### Option 2: VS Code (with Extension)

1. Install the **Swagger Viewer** extension in VS Code
2. Open `espn_fantasy_api_docs.yaml`
3. Right-click → **Preview Swagger**

### Option 3: ReDoc

For a cleaner reading experience:

1. Go to https://redocly.github.io/redoc/
2. Upload `espn_fantasy_api_docs.yaml`

## 🔑 Authentication

ESPN Fantasy Football API requires authentication for private leagues.

### Getting Your Credentials

1. **League ID**: Found in your league URL
   ```
   https://fantasy.espn.com/football/league?leagueId=987132062
   ```

2. **SWID & ESPN_S2 Cookies**:
   - Log into ESPN Fantasy Football
   - Open Browser DevTools (F12)
   - Go to **Application** tab → **Cookies** → `https://fantasy.espn.com`
   - Copy values for:
     - `swid` (e.g., `{93EC88D8-16BF-45A2-9323-B07B24D2BDF0}`)
     - `espn_s2` (long string, 100+ characters)

### Cookie Expiration

⚠️ **Important**: ESPN_S2 cookies expire frequently (every few days). You'll need to refresh them regularly.

## 📊 Available Endpoints

The API provides access to:

### League Information
- League settings and configuration
- Member information
- Previous seasons

### Teams
- Current standings
- Historical standings (by week)
- Team rosters
- Team statistics
- Schedule and results

### Players
- Player information and stats
- Free agents
- Player projections
- Injury status
- Ownership percentages

### Matchups & Scoring
- Weekly scoreboard
- Detailed box scores
- Player-level performance
- Projected vs actual scores

### Transactions
- Waiver wire activity
- Free agent pickups
- Trades
- Recent activity feed

### Analytics
- Power rankings
- Season leaders
- Weekly high/low scores
- Points against statistics

### Draft
- Draft picks and order
- Draft results

## 📝 Code Examples

See `API_CODE_EXAMPLES.md` for comprehensive code examples including:

- Authentication setup
- Getting league information
- Team operations
- Player searches
- Matchup analysis
- Transaction tracking
- Advanced analytics
- Error handling

## 🔍 API Exploration

Use the included `explore_espn_api.py` script to discover additional API features:

```bash
python explore_espn_api.py
```

This will output all available methods, properties, and data structures.

## 📦 Data Models

### Key Objects

#### League
- `league_id`, `year`, `current_week`
- `teams` (list of Team objects)
- `settings` (LeagueSettings object)
- `members`, `draft`, `previousSeasons`

#### Team
- `team_name`, `team_id`, `owner`
- `wins`, `losses`, `ties`
- `points_for`, `points_against`
- `standing`, `playoff_pct`
- `roster` (list of Player objects)
- `schedule`, `scores`, `outcomes`

#### Player
- `name`, `playerId`, `position`, `proTeam`
- `total_points`, `avg_points`
- `projected_total_points`, `projected_avg_points`
- `percent_owned`, `percent_started`
- `injured`, `injuryStatus`
- `stats` (detailed statistics)

#### BoxScore
- `home_team`, `away_team`
- `home_score`, `away_score`
- `home_lineup`, `away_lineup` (player stats)
- `home_projected`, `away_projected`

## 🎯 Common Use Cases

### 1. Weekly Scoreboard
```python
matchups = league.scoreboard()
for m in matchups:
    print(f"{m.away_team.team_name} vs {m.home_team.team_name}")
    print(f"{m.away_score:.2f} - {m.home_score:.2f}")
```

### 2. Top Free Agents
```python
free_agents = league.free_agents(position='RB', size=20)
for player in free_agents:
    print(f"{player.name}: {player.avg_points:.2f} PPG")
```

### 3. Power Rankings
```python
rankings = league.power_rankings()
for rank, team, score in rankings:
    print(f"{rank}. {team.team_name} ({score:.2f})")
```

### 4. Recent Transactions
```python
transactions = league.transactions()
for t in transactions:
    print(f"{t.team.team_name}: {t.type}")
```

## 🛠️ Testing Your Connection

Use the included test script to verify your credentials:

```bash
python test_espn_api.py
```

This will:
✅ Test authentication  
✅ Display league info  
✅ Show current standings  
✅ List current week matchups  

## ⚠️ Common Issues

### 403 Forbidden Error
**Cause**: Expired or invalid ESPN_S2 cookie  
**Solution**: Get a fresh cookie from your browser

### No Data Returned
**Cause**: Wrong year or league ID  
**Solution**: Verify the league ID from your URL and use current season year

### Player Not Found
**Cause**: Player name spelling or player not in system  
**Solution**: Use player ID instead of name, or check spelling

### Empty Roster
**Cause**: Not loaded for specific week  
**Solution**: Call `league.load_roster_week(week)` first

## 📚 Additional Resources

- **Official Library**: https://github.com/cwendt94/espn-api
- **ESPN API Documentation**: https://stmorse.github.io/journal/espn-fantasy-v3.html
- **Community Examples**: https://github.com/tbryan2/Pull-Matchup-Data-w-ESPN-API

## 🤝 Contributing

To extend this documentation:

1. Run `explore_espn_api.py` to discover new features
2. Add examples to `API_CODE_EXAMPLES.md`
3. Update `espn_fantasy_api_docs.yaml` with new endpoints
4. Test with `test_espn_api.py`

## 📄 License

This documentation is provided for educational purposes. ESPN Fantasy Football data is © ESPN.

---

## 📞 Support

For issues with:
- **This documentation**: Create an issue in your project
- **espn-api library**: https://github.com/cwendt94/espn-api/issues
- **ESPN API itself**: Community forums and documentation

---

**Last Updated**: November 2025  
**API Version**: v3  
**Library Version**: espn-api (latest)
