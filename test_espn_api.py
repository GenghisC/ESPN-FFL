"""
ESPN Fantasy Football API Test Script
Tests authentication and basic data retrieval using the official espn-api library
"""

from espn_api.football import League

# Your credentials
LEAGUE_ID = 987132062
SWID = "{93EC88D8-16BF-45A2-9323-B07B24D2BDF0}"
ESPN_S2 = "AEA6hZvSYkTuYM6QQj%2FtUBM4nY3G3KKl80Wr9OvoBsJpai4Zl83UuYi8EcQwfsxdx%2Fo869Nk3LnMoqNe8zsO2GLBae0qcxcZIksr222ZYf4wkaWEyycjefgDG2YQOaGU4dsCYr2IhJw9GG3S%2B87zRlARD%2FsUkBn1wxZhLeVXOKS%2B0glNq4UZJmb6O%2BklQmmGL40h%2FCRkAQQVED42kMZwVHyRY401neT75j6YkdnY7Za09fs9lCvOGXDTNGLWFns8siB15HoXBMJQdSEmYm4QrKdh81bwQ8IK7Q9POwLO5lM%2F3jgx17ZO28H5CWTUChdNhAE%3D"

# Current NFL season (2025-2026)
YEAR = 2025

def test_league_connection():
    """Test connection to ESPN Fantasy League and display basic info"""
    try:
        print("\n" + "="*60)
        print("TESTING ESPN FANTASY FOOTBALL API CONNECTION")
        print("="*60)
        print(f"League ID: {LEAGUE_ID}")
        print(f"Year: {YEAR}")
        
        # Initialize league with authentication
        league = League(league_id=LEAGUE_ID, year=YEAR, espn_s2=ESPN_S2, swid=SWID)
        
        print("\n✓ Successfully connected to ESPN API!")
        
        # Display league info
        print("\n" + "="*60)
        print("LEAGUE INFORMATION")
        print("="*60)
        print(f"League Name: {league.settings.name}")
        print(f"Current Week: {league.current_week}")
        print(f"Number of Teams: {len(league.teams)}")
        
        # Display teams and standings
        print("\n" + "="*60)
        print("TEAM STANDINGS")
        print("="*60)
        
        # Sort teams by wins
        sorted_teams = sorted(league.teams, key=lambda x: x.wins, reverse=True)
        
        for i, team in enumerate(sorted_teams, 1):
            print(f"{i}. {team.team_name}: {team.wins}-{team.losses} ({team.points_for:.2f} PF)")
        
        # Display current week matchups
        print("\n" + "="*60)
        print(f"WEEK {league.current_week} MATCHUPS")
        print("="*60)
        
        box_scores = league.box_scores(league.current_week)
        
        for matchup in box_scores:
            if matchup.home_team and matchup.away_team:
                print(f"\n{matchup.away_team.team_name}: {matchup.away_score:.2f}")
                print(f"{matchup.home_team.team_name}: {matchup.home_score:.2f}")
                print("-" * 40)
        
        print("\n" + "="*60)
        print("✓ TEST COMPLETE - API ACCESS VERIFIED!")
        print("="*60)
        
        return True
        
    except Exception as e:
        print(f"\n✗ ERROR: {e}")
        print("\nThis could mean:")
        print("1. The ESPN_S2 cookie has expired (need to get a fresh one)")
        print("2. Invalid SWID or League ID")
        print("3. Network/API connection issue")
        return False

if __name__ == "__main__":
    test_league_connection()
