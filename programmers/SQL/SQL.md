# SQL
> 프로그래머스를 풀면서 sql 문법 정리


## BASIC

- `역순 정렬`
```sql
ORDER BY ANIMAL_ID DESC;
```

- `not <값> 인 경우 찾기`
```SQL
WHERE INTAKE_CONDITION <> 'AGED';
```

- 여러 기준으로 정렬하기
```SQL
ORDER BY NAME, DATETIME DESC;
```
- 상위 N개 레코드
```SQL
SELECT * FROM ANIMAL_INS LIMIT 1;
```
- 레코드 갯수 구하기
```SQL
SELECT COUNT(*) AS count
    FROM ANIMAL_INS;
```
- 중복 제거하기
    - 방법 1
    - `DISTINCT`는 중복을 제거해준다.
    - `COUNT`는 `NULL`을 세지 않는다.
    ```SQL
    SELECT COUNT(DISTINCT(NAME)) AS count
        FROM ANIMAL_INS
    ```
    - 방법 2
    - `GROUP BY`
    - `HAVING`
    ```SQL
    SELECT COUNT(*) AS count
    FROM
        (
         SELECT NAME
         FROM ANIMAL_INS
         GROUP BY NAME
         HAVING NAME IS NOT NULL
        )AS NAME_TABLE;
    ```

- 그룹 수 구하기
```SQL
-- 코드를 입력하세요
SELECT ANIMAL_TYPE, COUNT(*) AS count
FROM ANIMAL_INS
GROUP BY ANIMAL_TYPE;
```

- `GROUP`에서 `COUNT(*)`에 대한 조건 넣기 
```SQL
SELECT NAME, COUNT(*) AS count
FROM ANIMAL_INS
GROUP BY NAME
HAVING count >=2 AND NAME IS NOT NULL
ORDER BY NAME;
```

- SELECT 변수로 `GROUP BY`하기 
```SQL
SELECT HOUR(DATETIME) AS HOUR, COUNT(*) AS COUNT
FROM ANIMAL_OUTS
GROUP BY HOUR
HAVING 9<=HOUR AND HOUR<=19;
```

- `SET @`변수 활용하기, `스칼라 서브쿼리`
```SQL
SET @hour = -1;
SELECT
    @hour :=@hour+1 AS HOUR,
    (SELECT COUNT(*) FROM ANIMAL_OUTS
    WHERE HOUR(DATETIME) = @hour) AS COUNT
FROM ANIMAL_OUTS
WHERE @hour < 23
```
- `SELECT` 안에 `SELECT`을 넣는 것을 `스칼라 서브쿼리`라고 부른다.
- `@hour`이 < 23이 되기까지 즉 24번 반복하면서 `count(*)` == `O(쿼리갯수)`만큼 반복을 돌린다.

- `IFNULL` OR `CASE WHEN` 사용하여 NULL 처리

    ```SQL
    SELECT 
        ANIMAL_TYPE,
        IFNULL(NAME,'No name') AS NAME,
        SEX_UPON_INTAKE
    FROM
        ANIMAL_INS;
    ```
    ```SQL
    SELECT 
        ANIMAL_TYPE,
        CASE
            WHEN NAME IS NOT NULL THEN NAME
            ELSE 'No name'
        END AS NAME,
        SEX_UPON_INTAKE
    FROM ANIMAL_INS
    ORDER BY ANIMAL_ID;
    ```

## `JOIN`

- `LEFT JOIN`
```SQL
SELECT A.ANIMAL_ID, A.NAME
FROM ANIMAL_OUTS A LEFT JOIN ANIMAL_INS B ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE B.ANIMAL_ID IS NULL
ORDER BY A.ANIMAL_ID;
```

- 있었는데요 없었습니다.
> https://programmers.co.kr/learn/courses/30/lessons/59043
```SQL
SELECT A.ANIMAL_ID, A.NAME
FROM ANIMAL_INS A LEFT JOIN ANIMAL_OUTS B ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE A.DATETIME > B.DATETIME
# 보호시작일보다 입양일이 빠르다는 것은 보호시작일이 더 크다는 것을 뜻한다.
ORDER BY A.DATETIME;
```

- `오랜기간 보호한 동물(1)`
> https://programmers.co.kr/learn/courses/30/lessons/59044
```SQL
SELECT A.NAME, A.DATETIME
FROM ANIMAL_INS A LEFT JOIN ANIMAL_OUTS B ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE B.ANIMAL_ID IS NULL
ORDER BY A.DATETIME
LIMIT 3;
```
- `보호소에서 중성화한 동물`
> https://programmers.co.kr/learn/courses/30/lessons/59045

```SQL
SELECT A.ANIMAL_ID, A.ANIMAL_TYPE, A.NAME
FROM ANIMAL_INS A LEFT JOIN ANIMAL_OUTS B ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE A.SEX_UPON_INTAKE LIKE 'Intact%' AND (B.SEX_UPON_OUTCOME LIKE 'Spayed%' OR B.SEX_UPON_OUTCOME LIKE 'Neutered%')
ORDER BY A.ANIMAL_ID;
```

- `오랜 기간 보호한 동물(2)`
> https://programmers.co.kr/learn/courses/30/lessons/59411
```SQL
SELECT A.ANIMAL_ID, A.NAME
FROM ANIMAL_INS A LEFT JOIN ANIMAL_OUTS B ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE B.DATETIME IS NOT NULL
ORDER BY B.DATETIME - A.DATETIME DESC
LIMIT 2;
```