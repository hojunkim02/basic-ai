import pandas as pd

# [코드5-2] Series 생성 예제

data_series = pd.Series([1, 2, 3, 4, 5, "A", "B", "C", "가", "나", "다"])

print(data_series)
print(type(data_series))


# [코드5-3] Series에 list로 index 설정하기

data_series1 = pd.Series(
    [1, 2, 3, 4, 5, "A", "B", "C", "가", "나", "다"],
    ["a", "b", "c", "d", "e", "f", "g", "h", "i", "k", "k"],
)
print(data_series1)

data_series2 = pd.Series(
    [1, 2, 3, 4, 5, "A", "B", "C", "가", "나", "다"],
    index=["a", "b", "c", "d", "e", "f", "g", "h", "i", "k", "k"],
)
print(data_series2)


# [코드5-4] Series에 딕셔너리로 index 설정

data_series1 = pd.Series({"a": 1, "b": 2, "c": 3, "d": 4, "e": 5})
print(data_series1)
data_series2 = pd.Series({"a": 1, "b": 2, "c": 3, "c": 4, "e": 5})
print(data_series2)


# [코드5-5] 딕셔너리로 DataFrame 생성 예제

data_frame = pd.DataFrame({"A": [1, 2, 3, 4], "B": [5, 6, 7, 8]})
print(data_frame)
print(type(data_frame))


# [코드5-6] numpy.ndarray, columns 값을 따로 정해주는 생성 예제

data_frame = pd.DataFrame([[1, 5], [2, 6], [3, 7], [4, 8]], columns=["A", "B"])
print(data_frame)
print(type(data_frame))


# [코드 5-7] CSV 파일 읽어오기

data = pd.read_csv("samples/sample.csv")
print(data)
data = pd.read_excel("samples/sample.xlsx")
print(data)


# [코드5-10] set_index() 설정

data = pd.read_csv("samples/sample.csv")
data2 = data.set_index("학번", drop=False)
print(data2)

data = pd.read_csv("samples/sample.csv")
data2 = data.set_index("학번", drop=True)
print(data2)


# [코드5-11] reset_index 설정

data = pd.read_csv("samples/sample.csv")
data = data.set_index("학번", drop=True)
data2 = data.reset_index(drop=False)
print(data2)

data = pd.read_csv("samples/sample.csv")
data = data.set_index("학번", drop=True)
data2 = data.reset_index(drop=True)
print(data2)
