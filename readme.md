# 阴阳师脚本文件
## 常见错误与警告
- `libpng warning: iCCP: cHRM chunk does not match sRGB`
> 这种情况是由于我们使用了QQ拼音输入法的情况。把输入法切换走就行
>
> 出现场景通常都是结束程序时才出现的，而且一般是warning级，一般不用管。可能有的依赖库对这个信号是error级而非warning级，因此切换输入法即可
- `error: (-215:Assertion failed) !_src.empty() in function 'cv::cvtColor'`
> 这是因为你配置的config.py中的路径有中文
>
> 因为opencv-python库是不识别中文路径的，因此请将路径改成中文的

