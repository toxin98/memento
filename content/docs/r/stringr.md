
mutate(group = str_replace(sample, "^(.*)_.*$", "\\1")) |>  # 返回最后一个下划线前的字符，如果没有下划线，返回全部

mutate(category = str_extract(variable, "\\S+")) # 返回第一个空格前的字符，如果没有空格，返回全部
