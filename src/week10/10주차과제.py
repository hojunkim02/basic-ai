import pandas as pd

# [코드 5-37] describe()

data = pd.read_csv("sample.csv")
data_describe = data.describe()
print(data_describe)


# [코드5-38] 데이터의 행과 열 바꾸기

data = pd.read_csv("sample.csv")
data_T = data.T
data_t = data.transpose()
print(data_T)
print(data_t)


# [코드 5-39] sort_index()로 정렬하기

data = pd.read_csv("sample.csv")
sort_index1 = data.sort_index(axis=0, ascending=False)
print(sort_index1)
sort_index2 = data.sort_index(axis=1, ascending=True)
print(sort_index2)


# [코드 5-40] sort_value()로 정렬하기

data = pd.read_csv("sample.csv")
data_sort1 = data.sort_values(axis=0, by="대기소", ascending=True)
print(data_sort1)
data_sort2 = data.sort_values(axis=1, by=2, ascending=True)
print(data_sort2)


# [코드5-46] rank()
data = pd.read_csv("sample.csv")
data_rank = data.rank(
    axis=0, method="min", ascending=False, numeric_only=True, na_option="top"
)
print(data_rank)


# [활동5-1]<그림5.5>의샘플데이터를가공해보자.
# 1. 가장 오른쪽에 총합, 평균열을 추가하고 각 학생의 총합, 평균값을 입력한다.
# 2. 총합을 기준으로 순위를 결정한다.
# 3. 순위를 기준으로 1등부터 오름차순으로 나열한다.
# 4. 평균을 기준으로 90 이상은 A, 80 이상은 B, 나머지는 C인 등급을 학점열에 추가한다.
