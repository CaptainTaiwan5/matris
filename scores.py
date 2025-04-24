import os

scorefile = os.path.join(os.path.dirname(__file__), ".highscores")

def load_score():
    #-------------------------------------------------------------------------
    # 讀黨
    # 回傳最高分數，如果沒有則回傳0
    
    try:
        with open(scorefile) as file:
            # 使用sort找出最高分
            scores = sorted([int(score.strip())
                             for score in file.readlines()
                             if score.strip().isdigit()], reverse=True)
    except IOError:
        scores = []

    return scores[0] if scores else 0

def write_score(score):
    #-------------------------------------------------------------------------
    # 把分數寫入檔案
    #-------------------------------------------------------------------------
    assert str(score).isdigit()
    with open(scorefile, 'a') as file:
        file.write("{}\n".format(score))
