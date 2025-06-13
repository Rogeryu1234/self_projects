import requests
from collections import deque
import time

ASHBY_ID = "ef1e6360-f367-4ce5-8680-15cf6102e843"
API_BASE = "https://jobbo-api.n1.xyz/api"
HEADERS = {'Content-Type': 'application/json'}

def get_board(level):
    url = f"{API_BASE}/game/{ASHBY_ID}/board?level={level}"
    res = requests.get(url, headers=HEADERS)
    res.raise_for_status()
    return res.json()

def submit_moves(moves):
    url = f"{API_BASE}/game/{ASHBY_ID}/submit"
    res = requests.post(url, headers=HEADERS, json={"moves": moves})
    res.raise_for_status()
    return res.json()

def get_coords(board, symbol):
    for y, row in enumerate(board):
        for x, cell in enumerate(row):
            if cell == symbol:
                return (x, y)
    return None

def bfs(board, start, goal, walls):
    directions = {
        "up": (0, -1), "down": (0, 1),
        "left": (-1, 0), "right": (1, 0)
    }
    rows, cols = len(board), len(board[0])
    queue = deque([(start, [])])
    visited = set([start])
    
    while queue:
        (x, y), path = queue.popleft()
        if (x, y) == goal:
            return path
        for move, (dx, dy) in directions.items():
            nx, ny = x + dx, y + dy
            if (0 <= nx < cols and 0 <= ny < rows and 
                (nx, ny) not in visited and (nx, ny) not in walls):
                visited.add((nx, ny))
                queue.append(((nx, ny), path + [move]))
    return []



def solve_game():
    level = 1
    while True:
        data = get_board(level)
        board = data['board']
        start = get_coords(board, 'P')
        goal = get_coords(board, 'A')
        wall_coords = set((w['x'], w['y']) for w in data.get('walls', []))

        print(f"Level {level} | Start: {start} → Goal: {goal}")
        print(f"Walls: {len(wall_coords)}")

        moves = bfs(board, start, goal, wall_coords)
        print(f"Planned moves ({len(moves)}): {moves}")

        if not moves:
            print(f"❌ No path found on level {level}!")
            break

        try:
            result = submit_moves(moves)
        except requests.exceptions.HTTPError as err:
            print("❌ Submission failed:", err)
            print("Full response text:", err.response.text)
            break

        if result.get("gameCompleted"):
            print(f"🎉 Game Complete! Total Moves: {result['gameState']['totalMoves']}")
            break

        level = result["gameState"]["level"]


if __name__ == "__main__":
    solve_game()
