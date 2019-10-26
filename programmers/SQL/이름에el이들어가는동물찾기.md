# 이름에 el이 들어가는 동물 찾기

```sql
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE
    NAME LIKE '%el%' AND
    ANIMAL_TYPE = 'Dog'
ORDER BY NAME;
```

- `LIKE '%el%'`