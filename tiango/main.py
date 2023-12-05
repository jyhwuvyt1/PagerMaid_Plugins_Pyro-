from pyrogram import Client
from pagermaid.listener import listener
from pagermaid.utils import Message, client, edit_delete


@listener(command="tiango", description="舔狗日记")
async def tiango(_: Client, message: Message):
    for _ in range(5):
        req = await client.get("https://cloud.qqshabi.cn/api/tiangou/api.php")
        if req.status_code == 200:
            return await message.edit(req.text)
    await edit_delete(message, "出错了呜呜呜 ~ 试了好多好多次都无法访问到 API 服务器 。")
