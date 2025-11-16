"""
ESPN Fantasy Football API Explorer
Discovers and documents all available API endpoints and data structures
"""

from espn_api.football import League
import inspect
import json

# Your credentials
LEAGUE_ID = 987132062
SWID = "{93EC88D8-16BF-45A2-9323-B07B24D2BDF0}"
ESPN_S2 = "AEA6hZvSYkTuYM6QQj%2FtUBM4nY3G3KKl80Wr9OvoBsJpai4Zl83UuYi8EcQwfsxdx%2Fo869Nk3LnMoqNe8zsO2GLBae0qcxcZIksr222ZYf4wkaWEyycjefgDG2YQOaGU4dsCYr2IhJw9GG3S%2B87zRlARD%2FsUkBn1wxZhLeVXOKS%2B0glNq4UZJmb6O%2BklQmmGL40h%2FCRkAQQVED42kMZwVHyRY401neT75j6YkdnY7Za09fs9lCvOGXDTNGLWFns8siB15HoXBMJQdSEmYm4QrKdh81bwQ8IK7Q9POwLO5lM%2F3jgx17ZO28H5CWTUChdNhAE%3D"
YEAR = 2025

def explore_league_object():
    """Explore the League object and its methods"""
    print("="*80)
    print("ESPN FANTASY FOOTBALL API - LEAGUE OBJECT EXPLORATION")
    print("="*80)
    
    league = League(league_id=LEAGUE_ID, year=YEAR, espn_s2=ESPN_S2, swid=SWID)
    
    print("\n" + "="*80)
    print("LEAGUE CLASS METHODS")
    print("="*80)
    
    methods = [method for method in dir(league) if not method.startswith('_')]
    for method in sorted(methods):
        attr = getattr(league, method)
        if callable(attr):
            try:
                sig = inspect.signature(attr)
                print(f"\n{method}{sig}")
                if attr.__doc__:
                    print(f"  Description: {attr.__doc__.strip()}")
            except:
                print(f"\n{method}()")
    
    print("\n" + "="*80)
    print("LEAGUE PROPERTIES/ATTRIBUTES")
    print("="*80)
    
    for attr in sorted(methods):
        obj = getattr(league, attr)
        if not callable(obj):
            print(f"\n{attr}: {type(obj).__name__}")
            if isinstance(obj, (str, int, float, bool)):
                print(f"  Value: {obj}")
            elif isinstance(obj, list) and len(obj) > 0:
                print(f"  Length: {len(obj)}")
                print(f"  Item Type: {type(obj[0]).__name__}")

def explore_team_object():
    """Explore Team object structure"""
    print("\n" + "="*80)
    print("TEAM OBJECT STRUCTURE")
    print("="*80)
    
    league = League(league_id=LEAGUE_ID, year=YEAR, espn_s2=ESPN_S2, swid=SWID)
    
    if league.teams:
        team = league.teams[0]
        print(f"\nExploring: {team.team_name}")
        
        attrs = [attr for attr in dir(team) if not attr.startswith('_')]
        for attr in sorted(attrs):
            obj = getattr(team, attr)
            if not callable(obj):
                print(f"\n{attr}: {type(obj).__name__}")
                if isinstance(obj, (str, int, float, bool)):
                    print(f"  Value: {obj}")
                elif isinstance(obj, list) and len(obj) > 0:
                    print(f"  Length: {len(obj)}, Item Type: {type(obj[0]).__name__}")

def explore_player_object():
    """Explore Player object structure"""
    print("\n" + "="*80)
    print("PLAYER OBJECT STRUCTURE")
    print("="*80)
    
    league = League(league_id=LEAGUE_ID, year=YEAR, espn_s2=ESPN_S2, swid=SWID)
    
    if league.teams and league.teams[0].roster:
        player = league.teams[0].roster[0]
        print(f"\nExploring: {player.name}")
        
        attrs = [attr for attr in dir(player) if not attr.startswith('_')]
        for attr in sorted(attrs):
            obj = getattr(player, attr)
            if not callable(obj):
                print(f"\n{attr}: {type(obj).__name__}")
                if isinstance(obj, (str, int, float, bool)):
                    print(f"  Value: {obj}")
                elif isinstance(obj, dict):
                    print(f"  Keys: {list(obj.keys())[:5]}")

def explore_boxscore_object():
    """Explore BoxScore object structure"""
    print("\n" + "="*80)
    print("BOXSCORE OBJECT STRUCTURE")
    print("="*80)
    
    league = League(league_id=LEAGUE_ID, year=YEAR, espn_s2=ESPN_S2, swid=SWID)
    
    box_scores = league.box_scores(league.current_week)
    if box_scores:
        matchup = box_scores[0]
        print(f"\nExploring matchup: {matchup.away_team.team_name} vs {matchup.home_team.team_name}")
        
        attrs = [attr for attr in dir(matchup) if not attr.startswith('_')]
        for attr in sorted(attrs):
            obj = getattr(matchup, attr)
            if not callable(obj):
                print(f"\n{attr}: {type(obj).__name__}")
                if isinstance(obj, (str, int, float, bool)):
                    print(f"  Value: {obj}")

def explore_settings_object():
    """Explore Settings object structure"""
    print("\n" + "="*80)
    print("SETTINGS OBJECT STRUCTURE")
    print("="*80)
    
    league = League(league_id=LEAGUE_ID, year=YEAR, espn_s2=ESPN_S2, swid=SWID)
    settings = league.settings
    
    attrs = [attr for attr in dir(settings) if not attr.startswith('_')]
    for attr in sorted(attrs):
        obj = getattr(settings, attr)
        if not callable(obj):
            print(f"\n{attr}: {type(obj).__name__}")
            if isinstance(obj, (str, int, float, bool)):
                print(f"  Value: {obj}")
            elif isinstance(obj, dict):
                print(f"  Keys: {list(obj.keys())[:10]}")

if __name__ == "__main__":
    explore_league_object()
    explore_team_object()
    explore_player_object()
    explore_boxscore_object()
    explore_settings_object()
    
    print("\n" + "="*80)
    print("EXPLORATION COMPLETE")
    print("="*80)
