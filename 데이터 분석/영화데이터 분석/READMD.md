## Dacon 집값예측 

###  가상환경 설정하기

1. `venv` 파일 생성
2. `source venv/Scripts/activate` 로 가상환경 활성화

### 1. Pandas

#### 데이터 불러오기

```python
csv_test = pd.read_csv('경로')
```

#### 데이터 확인하기

- `head()` , `tail()` : 첫번째와 마지막 확인
- `index`, `columns`, `value` : 인덱스, 행, 데이터
- `describe()` : 데이터프레임에 대한 간단한 통계정보
- 

