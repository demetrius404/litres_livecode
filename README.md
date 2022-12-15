```text
# without regexp

"ab[cd]e" > "abcde"
"[ab]" > ab
"a2[b3[cd]]" > "abcdcdcdbcdcdcd"
```

## pip 
`pip install -r requirements.txt`

## pre-commit hook
`pre-commit install`

## linter 
`flake8`

## test 
`pytest ./src`