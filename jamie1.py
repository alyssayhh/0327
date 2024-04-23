with open(file = "untitled-1.py", mode="r", encoding="utf-8") as f
inputList = f.readlines()
def caseparse(inputLIST):
    results = []

    for inputSTR in inputLIST:
        resultDICT = {
            "Subject": None,
            "Object": [],
            "Verb": []
        }

        # 分割输入的句子
        input_words = inputSTR.split(" ")

        def extractSubject(input_words):
            for i, word in enumerate(input_words):
                if "が" in word or "は" in word:
                    resultDICT["Subject"] = word.split("（")[0].strip("がは")
                    return i  # Return the index where subject was found

        def extractObject(input_words, start_index):
            for i, word in enumerate(input_words[start_index:], start=start_index):
                if "を" in word:
                    resultDICT["Object"] = word.split("を")[0]
                    return i  # Return the index where object was found

        def extractVerbs(input_words, start_index):
            for word in input_words[start_index:]:
                if "ます" in word:
                    resultDICT["Verb"].append(word.split("ます")[0])

        # 调用提取函数
        subject_index = extractSubject(input_words)
        if subject_index is not None:
            object_index = extractObject(input_words, subject_index + 1)
            extractVerbs(input_words, object_index + 1 if object_index is not None else subject_index + 1)

        results.append(resultDICT)

    return results

inputSTR = """私（わたし）がリンゴを食べます。
彼（かれ）が本を読みます。
私（わたし）が友達を見ます。
彼女（かのじょ）が花を買います。
私（わたし）が犬を飼います。
田中さんが車を運転します。
あなたが手紙を書きます。
先生が生徒に教えます。
子供がお菓子を食べます。
あなたが問題を解決します。
友達がプレゼントを持ってきます。
彼が日本語を話します。
先生が質問に答えます。
私が夕食を作ります。
彼女がピアノを弾きます。
あなたが助けを求めます。
子供が遊びます。 
先生が新しい言葉を教えます。
私がお茶を飲みます。
彼がボールを投げます。"""

inputLIST = inputSTR.split('\n')
resultDICT = caseparse(inputLIST)
for result in resultDICT:
    print(result)
