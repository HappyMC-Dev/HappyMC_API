# 简单的Token生成脚本
对于conf.ini选项的解释

```ini
[TokenGenerator]
length = 32
include_uppercase = True
include_lowercase = True
include_digits = True
include_symbols = True
```

这些选项定义了令牌生成器的一些参数，让你可以根据需要自定义生成的令牌。以下是每个选项的意义：

1. `length`: 定义生成的令牌的长度。在你的配置中，设置为 32，表示生成的令牌将包含 32 个字符。
2. `include_uppercase`: 一个布尔值，指示是否在生成的令牌中包含大写字母。如果设置为 `True`，则包含大写字母；如果设置为 `False`，则不包含大写字母。
3. `include_lowercase`: 一个布尔值，指示是否在生成的令牌中包含小写字母。如果设置为 `True`，则包含小写字母；如果设置为 `False`，则不包含小写字母。
4. `include_digits`: 一个布尔值，指示是否在生成的令牌中包含数字。如果设置为 `True`，则包含数字；如果设置为 `False`，则不包含数字。
5. `include_symbols`: 一个布尔值，指示是否在生成的令牌中包含符号。如果设置为 `True`，则包含符号；如果设置为 `False`，则不包含符号。在常见的情况下，符号包括标点符号和特殊字符。
这些选项允许你在生成令牌时进行灵活的定制，以满足特定的安全或应用需求。通过调整这些参数，你可以生成不同长度和包含不同字符集的令牌。