
def extract_subject(sentence,i):
    ga_index = sentence.find("が")

if ga_index != -1:
    subject = sentence[:ga_index].strip()
else:
    subject = "No subject found"

def extract_subject(sentence):
    wo_index = sentence.find("を")

if wo_index != -1:
    subject = sentence[:wo_index].strip()
else:
    subject = "No subject found"
    
    return subject

# test case

sentence = [
    "猫が魚を食べる",
    "彼女が花を買う",
    "子供たちが公園で遊ぶ",
    "本を読む",
    "泳ぐ",
    "日本語を勉強する" 
]

for sentence in i:
    subject = extract_subject(i)
    print("Sentence:", i)
    print("Subject:", i)
    print()  # Print an empty line for better readability

for sentence in i:
    subject = extract_subject(sentence)
    print("Sentence:", sentence)
    print("Subject:", subject)
    print()  # Print an empty line for better readability

def extract_subjects(sentences):
    subjects = []
    for sentence in i:
        ga_index = sentence.find("が")
        subject = sentence[:ga_index].strip()
        subjects.append(subject)
    return subjects

sentences = ["私（わたし）がリンゴを食べます","彼（かれ）が本を読みます", "あなたが手紙を書きます"]
subjects = extract_subjects(sentences)
print("Subjects:", subjects)

