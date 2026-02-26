# 計算機プログラム（Google Colab用）

print("=== シンプル計算機 ===")
print()

# ユーザーに数字を入力してもらう
num1 = float(input("最初の数字を入力してください: "))
operator = input("演算子を入力してください (+, -, *, /): ")
num2 = float(input("2番目の数字を入力してください: "))

# 演算子に応じて計算を実行
if operator == "+":
    result = num1 + num2
    print(f"\n{num1} + {num2} = {result}")
elif operator == "-":
    result = num1 - num2
    print(f"\n{num1} - {num2} = {result}")
elif operator == "*":
    result = num1 * num2
    print(f"\n{num1} × {num2} = {result}")
elif operator == "/":
    # ゼロで割らないようにチェック
    if num2 == 0:
        print("\nエラー：ゼロで割ることはできません")
    else:
        result = num1 / num2
        print(f"\n{num1} ÷ {num2} = {result}")
else:
    print("\nエラー：無効な演算子です")
