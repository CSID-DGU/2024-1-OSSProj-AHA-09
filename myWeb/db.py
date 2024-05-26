import sqlite3
import pandas as pd

dic = ['감자', '고구마', '고추', '대파', '벼', '복숭아', '사과', '양파', '옥수수', '콩', '포도']

def read_csv(csv_file, crop):
    # CSV 파일을 데이터프레임으로 읽기
    df = pd.read_csv(csv_file)
    df['crop'] = crop
    df = df.rename(columns={'지역': 'region', '년': 'year', 'prediction_label':'prediction'})
    df = df[['crop', 'year', 'region', 'prediction']]

    return df

if __name__ == '__main__':
    # CSV 파일, SQLite 파일 및 테이블 이름 설정
    df = pd.DataFrame()

    for crop in dic :
        csv_file = '../predict/predict_'+crop+'.csv'
        sqlite_file = 'db.sqlite3'
        table_name = 'map_data_prediction'

        # CSV 파일을 SQLite 데이터베이스에 삽입
        d = read_csv(csv_file, crop)
        df = pd.concat([df, d], axis=0, ignore_index=True)
    
    print(df)
    df['id'] = range(1, len(df) + 1)
    conn = sqlite3.connect(sqlite_file)
    df.to_sql(table_name, conn, if_exists='replace', index=False)

    conn.close()