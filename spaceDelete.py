# 使用言語は Python です
# *Google Colablatory で作成したコードなので、以下それに応じたコメントを付与しています

# 半角スペースを消去するコード
# コード上にカーソルを置いて、「Shift + Enter」で実行できます！
# テキストボックスが表示されるので、そこに「Ctrl + V」で半角スペースを消去したいテキストを打ち込めば、実行画面の下部に実行後のテキストが表示されます！

texts = input('半角スペースを消したいテキストをペーストしてください >>> ')
text = texts.replace(' ','')
print('  ')
print('------ 以下が空白を消去したテキストです ------')
print('  ')
print(text)
