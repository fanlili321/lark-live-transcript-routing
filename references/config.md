# 固定配置

## 飞书对象

| 对象 | 名称 | ID / Token |
|---|---|---|
| 来源群 | 226课程群 | `oc_ad278b7a15d31ab7a5ced19569769db8` |
| 来源人 | 王磊 | `ou_db3bad6668c5f077ee4f449758c7c3b1` |
| 知会人（动态，不是固定某人，见下方"知会对象"） | 当前执行本 skill 的人 | 用 `lark-cli whoami` + `contact +get-user --user-ids me` 现取 |
| 目标群（2026-08-08 起限定用途重新启用，见下方"复核通过后回填与群通知"） | 内容小分队 | `oc_d49775cef6a606b893cdec743875be02` |
| 通知机器人（仍未使用，群消息目前走当前执行者的 user 身份发送，不是走这个 bot） | 直播物料小助手 | profile `live-poster-bot` / app `cli_a94b5144b1381cb3` |
| 复核通过后固定艾特对象 | 范丽丽 | `ou_2bd618ee347cc81fe4f1832ef1f35c91` |
| 负责人（历史信息，2026-08-07 起排期表回填当作整体流程步骤已停用，不再使用；2026-08-08 起该文档改为窄用途重新启用，见下方） | 许雪梅 | `ou_30e864b8b202e6f43a493445fc7b7674` |
| 负责人（同上，历史信息） | 高一茹 | `ou_b5df7b45a85040d85bfb917665f1dc67` |
| 螺丝钉团队 | 可编辑权限团队 |  |
| 归档父文件夹 | 直播文字稿归档 | `fldcnOHFCzQqD7knn8pBv8Fqy0A` |
| 排期与流程文档（2026-08-08 起限定用途重新启用，见下方） | 直播课文字稿+课程资料整理 标准化流程（全流程） | `GHijdOBkDoyUnqxZBuPctqOPnAb` |
| 高净值PPT共享文件夹 | 高净值客户直播PPT（按第N期编号） | `fldcnFMmJZrDXZnmo8jVcekNSec` |
| PPT共享文件夹 | 第N期-标题 格式的直播PPT文件夹 | `fldcn82dxPE6sznG1xWP2OvcLvc` |
| 对外演讲PPT共享文件夹 | 钉大对外演讲/线下活动PPT（按日期+标题命名，不是"第N期-"格式） | `DU88fYBMblNlNmdah5lcHpl8nAc` |

父文件夹 URL：`https://epndqwwg0a.feishu.cn/drive/folder/fldcnOHFCzQqD7knn8pBv8Fqy0A`

排期文档 URL（历史信息，已停用）：`https://epndqwwg0a.feishu.cn/docx/GHijdOBkDoyUnqxZBuPctqOPnAb`

高净值PPT共享文件夹 URL：https://epndqwwg0a.feishu.cn/drive/folder/fldcnFMmJZrDXZnmo8jVcekNSec
PPT共享文件夹 URL：`https://epndqwwg0a.feishu.cn/drive/folder/fldcn82dxPE6sznG1xWP2OvcLvc`
对外演讲PPT共享文件夹 URL：`https://epndqwwg0a.feishu.cn/drive/folder/DU88fYBMblNlNmdah5lcHpl8nAc`（2026-08-07 用 `drive +search --query "对外演讲" --doc-types folder` 找到，标题"02-03公募-钉大对外演讲PPT"，内部子文件夹形如"20260714 如何站在客户视角，做好买方财富管理"——如果实际不是这一个，需要用户重新确认更正）

### 知会对象（2026-08-07 起改为动态）

这个 skill 会被不止一个人使用。私聊知会的对象不再固定写死为某个人，而是**谁在用，就通知谁**：

1. 先 `lark-cli whoami` 确认当前生效的登录身份。
2. 再用 `lark-cli contact +get-user --user-ids me`（或等效的"查自己"方式）拿到这个身份对应的 open_id。
3. 用这个 open_id 作为本次私聊知会的目标，不要复用之前会话里记下的某个具体人的 open_id（比如不要因为历史记录里出现过"范丽丽"就默认还是发给她）。

整理规则来源（知识库）：`https://epndqwwg0a.feishu.cn/wiki/BqGHwjDa2iciA8krDwVcRePVns4`（docx token `CpWPdz9ilob1jrxiKd2cfBuYntf`），完整规则固化在 `references/organize-rules.md`，本 skill 直接读该文件，不必每次都重新拉取知识库原文。

## 识别与命名

- 王磊发送的妙记标题为**非正式标题**（如"红利类指数基金投资方法分析""A系列指数投资知识及相关问题讲解"），不可直接用于归档命名。
- 示例：妙记标题"红利类指数基金投资方法分析" → 正式标题"红利指数涨起来了，还能投吗？"（从海报备份中读取）。
- **正式标题来源**（按优先级）：
  1. **PPT共享文件夹**：普通期数 `fldcn82dxPE6sznG1xWP2OvcLvc`（`第{期数}期-标题` 格式）；高净值 `fldcnFMmJZrDXZnmo8jVcekNSec`（同样按第N期编号）；对外演讲/线下活动 `DU88fYBMblNlNmdah5lcHpl8nAc`（`{日期} {标题}` 格式，按日期或关键词搜，不按期数搜）
  2. 飞书大纲文档的标题
  3. 本地海报备份（`live-poster-{期数}-backup-*` 中的 `{期数}期-直播物料-备份.md`，仅普通期数适用）

**2026-08-07 起不再有 `_原文` 中间态，三种类型的文档创建时就直接用最终标题，不需要整理完成后再改名去后缀。**

### 归档文件夹命名 + 文档标题命名（按类型）

| 类型 | 归档文件夹命名 | 文档标题命名 | 示例 |
|---|---|---|---|
| 普通期数 | `<期数> <正式标题>` | `<正式标题>｜螺丝钉专属直播课第<期数>期` | 文件夹 `466 A500、A50指数，该怎么投资？`；文档 `A500、A50指数，该怎么投资？｜螺丝钉专属直播课第466期` |
| 高净值客户专享直播 | `YYYYMMDD 第{N}期 <正式标题>（高净值客户尊享直播）` | `第{N}期-{标题}（高净值客户专享直播课）` | 文件夹 `20260806 第23期 牛市中后期，私募FOF是如何止盈的？（高净值客户尊享直播）`；文档 `第23期-牛市中后期，私募FOF是如何止盈的？（高净值客户专享直播课）` |
| 对外演讲/线下活动 | 与文档标题**完全相同**（folder 和 docx 同名） | `<正式标题>｜<场次说明>`，场次说明按场景选：<br>· 线下活动：`YYYYMMDD <场次类型>线下活动` 或 `YYYYMMDD <场次类型>活动（<机构/说明>）`<br>· 外部平台/机构演讲：`<平台或机构名> YYYY年M月D日` | `红利指数基金，该如何投资？｜20260530大众场活动（中信出版社读者见面会）`；`当下市场，如何做好资产配置｜20260530高净值线下活动`；`红利指数基金，该如何投资？｜吴晓波频道 2026年4月15日` |

对外演讲/线下活动这一行的规则是 2026-08-07 从归档父文件夹里已有的 3 个真实历史案例总结出来的（`VdZbfbc0VlddifdRbPIclb5Yn7b`、`X2JyfksNPlhj71dIqOwcLsFPnac`、`KUzSfmyV9lR3cwdtsTjc1Ulrnbh`），"场次类型"常见取值有大众场/高净值/出版社等，"机构/说明"是主办方或活动性质的简短说明；历史命名本身不完全统一（偶尔用"——"分隔机构名），不强求和历史每个字都一致，抓住"标题在前、场次时间信息在后，用｜分隔"这个主干即可。

## 文档内容处理

- 转写逐字稿生成的文档，**必须删除开头的关键词（Keywords）段落**，从首条发言人+时间戳段开始。
- 转写脚本默认会把妙记开头的关键词行写入文档，需要在 `block_insert_after` 阶段跳过该 block，或在追加完成后用 `block_delete` 删除对应 block_id。
- 转写前从逐字稿中去除 `YYYY-MM-DD HH:MM:SS CST|...` 的时间头行、`Keywords:` 行及其后跟随的关键词行。

## 状态门禁

`detected -> archived -> organized -> reported`

- `archived` 前禁止引用不存在的文档链接。
- `organized`：AI 文字整理 + PPT 配图 + 自查全部完成才能进入此状态（2026-08-07 起不再用 `_原文` 后缀作为判断标记，文档创建时就是最终标题；整理是否完成靠实际检查内容和图片，不是靠看标题）。
- `reported`：私聊知会当前执行者发出即完成，不等待对方回复，不再进入排期表回填或群通知环节（分别于 2026-08-07 / 2026-08-06 停用，见 `SKILL.md` 变更记录）。
- 以 `source_token` 为主幂等键，`message_id`（私聊知会消息）为审计键。

## 完成知会文案（私聊当前执行者，单向，不等待回复）

```text
直播文字稿已整理完成：
期数/主题：{issue} {title}
文件夹：{folder_url}
文字稿（已整理）：{doc_url}
{如有目录组件未加/整理疑问点，在此列出}
```

## 复核通过后的排期表回填与群通知文案（2026-08-08 起启用，触发条件见 SKILL.md"复核反馈处理"第8、9步）

只在"文档因为反馈被修改过，且用户已经明确确认没问题"之后触发，跟下面"整理刚完成"的私聊知会是两回事——初次整理完成不做这两步。

**排期与流程文档回填**：`GHijdOBkDoyUnqxZBuPctqOPnAb`，操作方式见 SKILL.md"复核反馈处理"第9步（`block_replace` 该期"链接"列的空 `<p>` 为 `<cite>` 引用）。

**群通知文案**（发到"内容小分队"群 `oc_d49775cef6a606b893cdec743875be02`，固定艾特范丽丽 `ou_2bd618ee347cc81fe4f1832ef1f35c91`，不用动态知会对象）：

```text
<at user_id="ou_2bd618ee347cc81fe4f1832ef1f35c91">范丽丽</at>，这期直播文字稿已根据反馈修改完成，可以复核：
{issue} {title}
{doc_url}
```

## 排期表回填文案 / 群通知文案（历史记录，均已停用，如恢复见 SKILL.md 变更记录）

排期表回填于 2026-08-07 停用；群通知于 2026-08-06 停用。若以后需要恢复，原来的知会文案是：

```text
直播文字稿已整理完成并回填排期表：
期数/主题：{issue} {title}
负责人：{assignee}
文件夹：{folder_url}
文字稿（已整理）：{doc_url}
排期表：已回填，负责人 {assignee}，截止 {deadline_or_排期为准}
{如有目录组件未加/整理疑问点，在此列出}
```

原来的群通知文案：

```text
<at user_id="{assignee_open_id}">{assignee}</at>，这期直播文字稿已整理完成：
{issue} {title}
{doc_url}
截止时间：{deadline_or_排期为准}
```
