# AI Daily Workflows

这里记录我在日常工作和学习中沉淀的 AI 使用流程、协作方法和安全边界。

## 内容索引

- [Handoff 日常操作流程](docs/2026-06-17-handoff-daily-workflow.md)：用于长窗口压缩、跨窗口接续、Claude/Codex/Agent 协同时的上下文交接。
- [双端审核实现指南（脱敏版）](docs/dual-review-implementation-guide.md)：如何用主端自检 + 对端审核 + 主端反验收，构建受控的 AI 审核闭环。

## 公开发布原则

本仓库是公开分享仓库。任何新增内容在提交或上传前必须先脱敏：

- 不上传真实姓名、手机号、邮箱、住址、身份证、公司/客户名称等个人或组织信息。
- 不上传 API Key、Token、Cookie、证书、私钥、数据库连接串、支付信息等密钥材料。
- 不上传真实内部域名、内网 IP、生产环境地址、真实仓库路径、真实用户目录。
- 不上传公司、客户、第三方 SDK 的非公开文档、源码、日志或截图。
- 示例路径统一使用 `~/workspace/...`、`/path/to/...` 等占位符。
- 示例账号统一使用 `user@example.com`、`<TOKEN>`、`<ORG_NAME>` 等占位符。

## 发布前检查

建议每次发布前至少执行：

```bash
python3 tools/sensitive_scan.py .
```

扫描通过不代表绝对安全；公开发布前仍需要人工复核。

## License

文档默认按 [CC BY 4.0](LICENSE) 分享，允许转载和改编，但请保留署名。
