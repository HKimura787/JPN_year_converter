# JPN_year_converter

和暦・西暦を変換するためのPythonモジュールです。

## 使い方

### クラスの宣言 
```
> cvtetr = JPN_year_converter()
```

### 和暦➡西暦
```
> cvter.warekiYear2ADYear('令和4年')
```

出力
```
2022
```

和暦のパラメータには

- R4
- r4
- 令和４年
- 令和4年度
- れいわ4
- ﾚｲﾜ4年度

などの様式で指定できます。

# 西暦➡和暦
```
> cvter.ADYear2warekiYear(2022)
```

出力
```
R4
```

変数`kanji`を`TRUE`にすると日本語が返されます。
```
> cvter.ADYear2warekiYear(2022, kanji = TRUE)
```

出力
```
令和4年度
```
