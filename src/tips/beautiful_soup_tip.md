# BeautifulSoup Tips

## findAll
```python
findAll(tag, attributes, recursive, text, limit, keyword)
```
### 매개변수
- tag: `string` 또는 `list`를 넘겨줄 수 있다.
  ```python
  bsObj.findAll("h1")
  bsObj.findAll({"span", "h1", "table"})
  ```
- attributes: 속성으로 이루어진 `dictionary` 를 넘겨 줄 수 있다.
  ```python
  bsObj.findAll("h1", {"class": {"green", "red"}})
  ```
- recursive: 문서에서 얼마나 깊이 찾아 들어가고 싶은지 지정하는 값.
  - 기본 값: `True`
- text: 태그 속성이 아니라 텍스트 값이 일치하는 것을 찾을 때 사용.
  ```python
  bsObj.findAll(text="exmaple")
  ```
- limit: 찾을 태그 개수를 제한할 때 사용.
  - 페이지에 나타나는 순서대로 찾는다.
  - 그 순서가 원하는 바와 일치한다는 보장이 없으므로 주의.
- keyword: 특정 속성이 포함된 태그를 선택할 때 사용.
  ```python
  bsObj.findAll(id="id")
  ```

## find
```python
find(tag, attributes, recursive, text, keyword)
```
### 매개변수
- [findAll 메소드의 매개변수 참고](#findAll)