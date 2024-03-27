def caseparse(inputLIST):
    results = []

    for inputSTR in inputLIST:
        resultDICT = {
            "Subject": None,
            "Object": None,
            "Verb": None
        }

        # 分割输入的句子
        input_words = inputSTR.split(" ")

        def extractSubject(input_words):
            for word in input_words:
                if "が" in word or "は" in word:
                    resultDICT["Subject"] = word.split("（")[0].strip("がは")

        def extract_substring_between_keywords(input_words, keyword_before, keyword_after):
            # 找到第一个关键字前的索引
            keyword_before_index = input_words.find(keyword_before)
        
            if keyword_before_index != -1:
                # 从第一个关键字后开始寻找第二个关键字的索引
                remaining_sentence = input_words[keyword_before_index + len(keyword_before):]
                keyword_after_index = remaining_sentence.find(keyword_after)
        
                if keyword_after_index != -1:
                    # 提取两个关键字之间的子串
                    substring = remaining_sentence[:keyword_after_index]
                    return substring.strip()  # 删除前后的空格
        
            return None
        
        def extractObject(input_words):
            for word in input_words:
                if "を" in word:
                    resultDICT["Object"] = word.split("を")[0]

        def extractVerb(input_words):
            for word in input_words:
                if "ます" in word:
                    resultDICT["Verb"] = word.split("ます")[0]

        # 调用提取函数
        extractSubject(input_words)
        extractObject(input_words)
        extractVerb(input_words)

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