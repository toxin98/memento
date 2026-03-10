write_xlsx(
  x = df,
  path = "result.xlsx",
  format_headers = FALSE
)

`format_headers`默认是TRUE，会把列名加粗和居中，按个人喜好来，我喜欢FALSE

导出后看一下效果，中文用户可能会发现所有的字体都是宋体，我不喜欢这样，这和系统有关，开发者的回答在[这里](https://github.com/ropensci/writexl/issues/74#issuecomment-1958443174)，我也找到里解决方案：选项>语言>Office 创作语言和校对, 把英语设为首选
