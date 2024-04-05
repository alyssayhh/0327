
def extract_subject(sentence):
    ga_index = sentence.find("が")

    if ga_index != -1:
        subject = sentence[:ga_index].strip()
    else:
        subject = "No subject found"
    
    return subject

# test case

orign_sentence = """"私（わたし）がリンゴを食べます。
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
彼がボールを投げます。 """


for i in orign_sentence.split("\n"):
    print(extract_subject(i),"\n")



