import psycopg2
import csv

def get_connection():
    return psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="12345678",
        host="localhost",
        port="5432"
    )

def export_scores_to_csv(filename='top_scores.csv'):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT u.username, s.score, s.level, s.timestamp
        FROM user_score s
        JOIN users u ON s.user_id = u.id
        ORDER BY s.score DESC, s.timestamp DESC
        LIMIT 10
    """)
    rows = cursor.fetchall()
    
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Username', 'Score', 'Level', 'Timestamp'])  # заголовки
        writer.writerows(rows)
    
    cursor.close()
    conn.close()
    print(f"✅ Топ 10 игроков сохранён в файл: {filename}")

if __name__ == '__main__':
    export_scores_to_csv()
