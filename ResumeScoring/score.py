import WrongDetector
import ListTest

if __name__ == '__main__':
    with open("Resume.txt", "r", encoding='utf-8') as f:
        text = f.read()  # 读取文件
    detector = WrongDetector.WrongGrammarDetector(text)
    tester = ListTest.ListTester(text)
    Score = 50 - detector.getWrongNum() + tester.getListTest()
    if Score < 0:
        Score = 0
    if Score > 100:
        Score = 100
    print(Score)