import pandas as pd

# [코드5-13] 데이터 columns 확인

data = pd.read_csv("samples/sample.csv")
data_columns = data.columns
print(data_columns)
columns_len = len(data_columns)
print("데이터의 columns 크기는", columns_len)


# [코드 5-15] column 데이터 선택

data = pd.read_csv("sample.csv")
data_1 = data["창사코"]
data_2 = data.창사코
data_3 = data[["창사코", "대기소"]]
print(data_1)
print(data_2)
print(data_3)


# [코드 5-16] row 데이터 선택

data = pd.read_csv("sample.csv")
data_1 = data[0:5]
print(data_1)


# [코드5-19] at, iat으로데이터선택

data = pd.read_csv("sample.csv")
data_1 = data.loc[0, ["대기소"]]
data_2 = data.iloc[2, [1]]
data_3 = data.at[0, "대기소"]
data_4 = data.iat[2, 1]
print(data_1)
print(data_2)
print(data_3)
print(data_4)


# [코드5-20] 조건을 이용한 데이터 선택

data = pd.read_csv("sample.csv")
data_1 = data[data["대기소"] >= 80]
print(data_1)
data_2 = data[(data["대기소"] >= 60) & (data["창사코"] >= 90)]
print(data_2)


# [코드5-21] 필터를 이용한 데이터 선택

data = pd.read_csv("sample.csv")
data_1 = data["대기소"].isin([60, 93])
print(data_1)
data_2 = data[data["대기소"].isin([60, 93])]
print(data_2)
data_3 = data[data.isin([60, 98])]
print(data_3)


# [코드 5-26] 여러 개의 행과 열 값 변경하기

data = pd.read_csv("sample.csv")
print(data.loc[0:3, ["대기소", "AI활용"]])
data.loc[0:3, ["대기소", "AI활용"]] = [[10, 10], [20, 20], [30, 30], [40, 40]]
print(data.loc[0:3, ["대기소", "AI활용"]])


# [코드5-27] drop()으로 값 삭제하기

data = pd.read_csv("sample.csv")
data_1 = data.drop(2)
data_2 = data.drop([5, 7])
data_3 = data.drop("대기소", axis=1)
data_4 = data.drop(["창사코", "대기소"], axis=1)
print(data_1)
print(data_2)
print(data_3)
print(data_4)


# [코드 5-32] 지정한 값 다른 데이터로 변경

data = pd.read_csv("sample.csv")
data = data.replace(100, 0)
print(data)


# [코드5-33] 함수를 사용한 값 변경
def func(row):
    if row > 90:
        return "A"
    elif row > 80:
        return "B"
    else:
        return "C"


data = pd.read_csv("sample.csv")
data["성적"] = data["대기소"].apply(func)
print(data)


# [코드5-34] insert()로 데이터 입력

data = pd.read_csv("sample.csv")
column_name = "새과목"
column_value = (
    [57, 54, 53, 80, 84, 88, 79, 64, 75, 65, 84, 90, 72, 95, 100, 94, 85, 63, 57, 95],
)
data.insert(1, column_name, column_value)
print(data)
