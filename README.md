# LangChain

## 准备工作

#### 使用langchain前安装依赖

```PowerShell
uv add langchain
```

如果爆出错误： error: No \`pyproject.toml\` found in current directory or any parent directory

则需要初始化一下

```PowerShell
uv init
```

随后输出了这个：Initialized project \`agent-ln\`

报错得以解决。

###### LangChain支持各种不同的模型，而且提供了对应的兼容SDK，不过也都需要安装对应依赖，可以按需添加：

```PowerShell
# 集成 DeepSeek
uv add langchain-deepseek

# 集成 OpenAI
uv add langchain-openai

# 集成 Anthropic
uv add langchain-anthropic
```

