现在不能据此删掉 Run check，也不应每天催升级。映射三列只是准备好输入，点击 Run check 才会发起核对。客服提出的“用户以为映射后会自动运行”是合理解释，尚未得到用户反馈或行为证据验证；另一类 viewer 的权限不足则已有明确原因。直接取消运行这一步会改变执行机制，还涉及谁有权触发核对，不能把它当成单纯减少点击。当前也没有证据表明付费升级能解决这两类问题，更没有足够数据判断这些做法能提高多少激活率。

对已经上传、映射却未运行的用户，先给清晰的下一动作，并说明完成后能拿到什么。下面的英文引导适用于已确认处于这一状态的用户；它是可用文案，尚未发送或写入产品。

:::writing{variant="standard" id="94184"}
Your CSV is uploaded and the three columns are mapped. Mapping prepares your data; it does not start the invoice check.

Select **Run check** to start. When the check finishes, review the differences against your source invoices, then export the result for your reconciliation work. If there are no differences, check that the result covers the records you intended to reconcile before exporting it.

If you see a permission error, ask your team's owner to authorize you to run the check. Upgrading is not the next step for this error.
:::

这一状态的恢复路径是先回到当前已映射的数据，确认三列选择正确，再由有权限的用户点击 Run check，查看实际运行结果。若页面仍保留文件与映射，就继续当前流程，不要求用户重新上传；若会话已失效或页面明确显示数据缺失，才重新上传并映射。若用户表示已经点过运行，则先核对是否正在处理或已有结果，避免把“未运行”误判成“结果入口没看见”而反复提交。若仍不能运行，客服收集卡住的步骤、界面显示和错误文本，再判断是否转入权限问题或其他运行故障；这些进一步原因目前未知。

对已经点击 Run check、明确显示权限不足且角色为 viewer 的用户，使用另一段引导。不能让用户反复重试同一个无权限动作，也不能用升级提示替代权限处理。

:::writing{variant="standard" id="94185"}
The check could not run because your current role is **viewer**. Only your team's **owner** can authorize you to run checks.

Ask your owner to authorize you to run the check for this invoice-reconciliation task. Once they confirm that authorization is in place, return to your mapped CSV and select **Run check** again. You do not need to re-upload the file if it and the column mapping are still available.

If you still see the permission error after your owner confirms authorization, stop retrying and contact support with the error text, your current role, and when the authorization was confirmed. Do not include invoice contents in the support message unless support requests them through an approved channel.

Once the check succeeds, review the result against your source invoices and export it for your reconciliation work.
:::

权限状态的责任划分是用户联系 owner，owner 核实任务需要并完成授权，用户在授权已确认后重新尝试运行，客服处理授权后仍报错的情况。没有 owner 回复时，状态保持“等待 owner 授权”，不能记成运行成功或激活；owner 不愿或无法授权时，先由其决定团队如何完成这次核对，客服不绕过权限。这里没有提供角色变更的具体界面或机制，因此不补造设置路径，也不把“授权运行”擅自解释成必须将用户升级为 owner。

首次价值以真实团队完成一次发票核对为观察单位：使用真实业务 CSV，成功运行，用户核查差异或确认没有差异的结果覆盖正确记录，随后导出一个可用于这次对账工作的结果。请完成者确认“这个导出结果可以用于你本次的发票核对吗？”并说明任何仍阻止使用的问题。运行成功、看过结果和导出都是可观察动作；若导出内容错误、缺失或用户表示无法用于工作，仍不能认定首次价值已经实现。样例文件体验、单纯上传映射或只点过按钮也不算。

可以把同一团队的这次核对按“准备完成、运行被阻、运行成功、结果经核查且可用、已导出”分别记录，关联到同一任务，避免把多次重试或多名成员重复计作多个团队激活。用户完成任务、回复需要帮助或进入等待授权状态后，就停止原来的提醒；即使将来授权发送，也应由实际卡点触发，不能默认每日催付费。是否再次在真实工作中使用，以及是否付费，是首次价值之后另行观察的结果。本次完成的是诊断与引导草稿，产品和客户状态均未实际修改。
