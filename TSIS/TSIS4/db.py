import psycopg2

def get_db_connection():
    return psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="        ",
        host="localhost"
    )

def get_or_create_player(username):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO players (username) VALUES (%s) ON CONFLICT (username) DO NOTHING", (username,))
    cur.execute("SELECT id FROM players WHERE username = %s", (username,))
    player_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return player_id

def save_game_session(player_id, score, level):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO game_sessions (player_id, score, level_reached) VALUES (%s, %s, %s)", 
                (player_id, score, level))
    conn.commit()
    cur.close()
    conn.close()

def get_top_10():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT p.username, gs.score, gs.level_reached, gs.played_at 
        FROM game_sessions gs 
        JOIN players p ON gs.player_id = p.id 
        ORDER BY gs.score DESC LIMIT 10
    """)
    res = cur.fetchall()
    cur.close()
    conn.close()
    return res

def get_personal_best(player_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT MAX(score) FROM game_sessions WHERE player_id = %s", (player_id,))
    res = cur.fetchone()[0]
    cur.close()
    conn.close()
    return res if res else 0