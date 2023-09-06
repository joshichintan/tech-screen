# Prescreen Solutions

Sample solutions and what to look for for the [prescreen questions](pre-screen.md).

## Prescreen question 1 (SQL)

What to look for:
- Do they quickly understand what's being asked for?
- There are a couple ways to solve this. You should see a `COUNT` somewhere, and they can use `GROUP BY`
  with a `WHERE` or `HAVING` clause, **or** they can use a windowing function (e.g. `OVER(PARTITION BY ...`)

Here's the most obvious solution:

```sql
SELECT *
FROM students
WHERE ssn IN (
 SELECT ssn
 FROM students
 GROUP BY ssn
 HAVING COUNT(ssn) > 1
);
```

## Prescreen question 2 (Python)

They should use Python to code the answer, not a different language.

What to look for:
- It's a good sign if you tell them the problem is "fizzbuzz" and they don't even need the prompt because they already know it.
- The code should be syntactically correct. Do they declare the function with `def`? Do they indent correctly?
- The code should be logically correct.
- It's a good sign if they put the `int` type hint on the function parameter `limit`, like I have below. If they don't, ask them to.
- It should take no more than a few minutes.

Here's two of the most obvious solutions:

```python
def fizzbuzz(limit: int):
    for i in range(1, limit + 1):
        output = ""
        
        if i % 3 == 0:
            output += "fizz"
        if i % 5 == 0:
            output += "buzz"
        
        if output == "":
            output = i
            
        print(output)
```

```python
def fizzbuzz(limit: int):
    for i in range(1, limit + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)
```
