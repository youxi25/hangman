#hangman
#作成所要時間：約２時間半...

def hangman():
    """当ててもらうwordを決める"""
    import random
    wordlist = ["anteater", "cow", "horse", "wolf", "hippopotamaus",
                "kangaroo", "giraffe", "bear", "rhinoceros",
                "deer", "zebra", "elephant", "reindeer", "tiger",
                "tapir", "baboon", "leopard", "sheep", "pig",
                "lion", "donkey", "goat", "badger", "raccoon",
                "armadillo", "weasel", "dog", "rappit",
                "platypus", "fox", "koala", "bat", "monkey",
                "marten", "sloth", "cat", "mouse", "hedgehog",
                "mole", "porcupine", "dormouse", "squirrel"
                ]
    word = random.choice(wordlist)
    """何回間違えたかのパラメーター"""
    wrong_guesses = 0
    """ステージ"""
    stages = ["",
              " +----+    ",
              " |    |    ",
              " |    °    ",
              " |         ",
              " |         ",
              " |         ",
              " |________ ",
              "/_処_刑_台_\\"
              ]
    body = [" |    O    ", #stagesの4行目と入れ替える
            " |    |    ", #stagesの5行目と入れ替える
            " |   /|    ", #stagesの5行目と入れ替える
            " |   /|\   ", #stagesの5行目と入れ替える
            " |   /     ", #stagesの6行目と入れ替える
            " |   / \   ", #stagesの6行目と入れ替える
            " |    O  < I AM DEAD ☠"]
    """当てないといけない文字"""
    remaining_letters = list(word)
    """文字表示"""
    letter_board = ["__"] * len(word)
    """入力済みの文字一覧"""
    already_guess = []
    """勝つための条件のための設定"""
    win = False
    """ユーザーへの表示"""
    print("\n".join(stages),
          "\n\nHANGMANへようこそ！\n単語を当てて救出だ！\n",
          " ".join(letter_board)
          )
    """間違った回数がbodyの数より少ない場合＝まだ負けてないとき"""
    while wrong_guesses < len(body):
        already_guess = list(dict.fromkeys(already_guess))
        print("\n現在入力済みの文字：{}".format(already_guess))
        guess = input("１文字予想してね！ヒントは動物：")
        already_guess.append(guess)
        if guess in remaining_letters:
            character_index = remaining_letters.index(guess)
            letter_board[character_index] = guess
            remaining_letters[character_index] = "$" #同じ文字が２個以上あった場合用
        else:
            wrong_guesses += 1
            if wrong_guesses <= 1:
                stages[3] = body[0]
            elif wrong_guesses <= 4:
                stages[4] = body[wrong_guesses - 1]
            elif wrong_guesses <= 6:
                stages[5] = body[wrong_guesses - 1]
            else:
                stages[3] = body[wrong_guesses -1]
        print(" ".join(letter_board),
              "\n",
              "\n".join(stages)
              )
        if "__" not in letter_board:
            print("あなたの勝ちです！正解は：",
                  " ".join(letter_board)
                  )
            win = True
            break
    if not win:
            print("あなたの負けです！正解は{}".format(word))

hangman()
    
