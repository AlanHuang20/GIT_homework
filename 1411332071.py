def calculate_bmi():
    try:
        # 取得使用者輸入
        height_cm = float(input("請輸入您的身高（公分）："))
        weight = float(input("請輸入您的體重（公斤）："))

        # 將身高公分轉換為公尺
        height_m = height_cm / 100.0

        # 計算 BMI：體重(kg) / 身高(m)的平方
        bmi = weight / (height_m ** 2)

        # 顯示結果，取到小數點後兩位
        print(f"\n您的 BMI 值為：{bmi:.2f}")

        # 簡單的體位判斷 (依據台灣國健署標準)
        if bmi < 18.5:
            print("狀態：體重過輕")
        elif bmi < 24:
            print("狀態：健康體位")
        elif bmi < 27:
            print("狀態：過重")
        else:
            print("狀態：肥胖")
            
    except ValueError:
        print("輸入錯誤，請輸入有效的數字！")

if __name__ == "__main__":
    calculate_bmi()