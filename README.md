# 海外销售转化与客户增长 · Global Sales & Retention

把感兴趣的用户推进到真实购买，再帮助客户获得价值、留下来并合理扩展。适合处理试用不转化、企业销售卡单、上手困难、续费风险和客户增购。

这是海外增长技能包的第四个独立 Skill，名称为 `global-sales-retention`。可单独使用，支持产品自助购买、销售协助与企业销售。它会根据当前阻碍给出可执行的跟进稿、演示与试点方案、交付交接或客户挽回动作，不要求先建设完整 CRM。

## 安装和第一次使用

将本仓库的 `skills/global-sales-retention` 完整复制到支持 Agent Skills 的客户端。例如 Codex：

```bash
git clone https://github.com/NextVariable/global-sales-retention-skill.git
cd global-sales-retention-skill
mkdir -p ~/.agents/skills
cp -R skills/global-sales-retention ~/.agents/skills/
```

已有同名技能时先核对版本，再决定是否替换。重新加载客户端后调用 `$global-sales-retention`。

```text
使用 $global-sales-retention。我们为设计团队做云端评审工具，年付每席 120 美元。
一家公司有 8 名用户，其中 3 人完成了第一次客户评审，采购尚未加入，
负责人想试 30 人但要求私有部署；我们目前只支持云版，每周能投入 6 小时支持。
请根据这些情况和附上的沟通记录，判断下一步该推进什么，
写出一次需求确认会议提纲和会后跟进邮件草稿，明确不能承诺的内容。
```

提供产品、当前客户或用户状态、已有沟通/使用/付款记录，以及价格与支持能力即可。缺少信息时先完成能做的部分，只询问会影响当前决定的问题。客户资料保存在自己的项目目录中，不放进公开仓库或安装目录。

## 能帮你完成什么

| 当前问题 | 交付内容 |
|---|---|
| 有兴趣，但不知道是否值得跟进 | 资格判断、购买角色与下一项客户行动 |
| Demo、试点或采购迟迟不推进 | 按买方任务设计的演示、成功条件、阻碍与跟进稿 |
| 报价、定制和交付边界不清 | 可讨论的商业选项、范围与验收条件、交接说明 |
| 注册多、上手少、付费少 | 首次价值路径、流失位置、相应引导与销售协助条件 |
| 客户减少使用或临近续费 | 原因诊断、恢复价值的动作、续费与扩展条件 |

能使用当前客户端已有的 CRM、邮件和文件工具。实际发送消息、更新 CRM、调整订阅或商业条件，需要用户对该动作有明确授权；只写好草稿时会明确说明未发送，工具失败时不会宣称执行成功。无需专用服务或密钥，缺少工具仍可产出完整的交接材料。

## 分工与边界

第一部分决定市场和优先客户，第二部分制作定位与增长内容，第三部分把客户带来，本部分推进购买与客户价值，第五部分设计实验并解释结果。这里可根据实际销售反馈提出市场或内容问题，但不重新接管整个增长计划。其他四个 Skill 都不是运行依赖。

主要面向软件、数字产品和订阅服务；实体产品按实际交付、设备激活和复购周期调整。不会用统一转化率判断所有产品，也不会把登录、口头答应、签约或开票直接当作留存、成交回款或增长验证。

方法结构见 [设计说明](docs/design.md)，实际试用结果与验证范围见 [验证说明](validation/README.md)。运行 `python3 scripts/validate.py` 检查安装结构与记录一致性。模拟任务可以检查判断和交付质量，不能证明实际销售额或留存提升。

## English

An independent Agent Skill for moving qualified interest toward purchase, helping customers reach value, and managing retention and expansion. It supports self-service, sales-assisted and enterprise motions, with task-specific guidance for discovery, demos, pilots, commercial handoff, activation and renewal. Instructions are written in Chinese; customer-facing assets follow the requested audience language. Invoke `$global-sales-retention` after installing the complete skill directory. External actions require explicit authorization and verifiable results.

## License

[MIT](LICENSE). Keep bundled license and notice files when redistributing.
