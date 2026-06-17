# 发布前脱敏检查清单

每次向公开仓库新增或更新内容前，必须完成以下检查：

## 一、禁止公开

- [ ] API Key / Token / Cookie / 私钥 / 证书 / OAuth refresh token
- [ ] 真实姓名、手机号、私人邮箱、住址、身份证等个人信息
- [ ] 公司名、客户名、供应商名、内部项目名、合同或报价信息
- [ ] 内部域名、内网 IP、生产环境地址、数据库连接串
- [ ] 真实本机路径，例如 `/Users/<真实用户名>/...`
- [ ] 未经授权的公司源码、日志、截图、需求文档、接口文档

## 二、推荐替换

| 原始类型 | 公开写法 |
|---|---|
| 本机绝对路径 | `~/workspace/project/...` 或 `/path/to/project/...` |
| 真实邮箱 | `user@example.com` |
| 真实组织名 | `<ORG_NAME>` |
| Token / Key | `<TOKEN>` / `<API_KEY>` |
| 内部域名 | `internal.example.com` |
| 内网 IP | `10.0.0.1` / `192.168.0.1` 示例网段 |

## 三、发布命令建议

```bash
python3 tools/sensitive_scan.py .
git diff --cached
```

扫描只是辅助，最终仍以人工复核为准。
