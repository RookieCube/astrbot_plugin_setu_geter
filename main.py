from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.api import logger
import astrbot.api.message_components as Comp
@register("setu_getter", "RookieCube", "简单色图插件", "1.0.2")
class Setu(Star):
    def __init__(self, context: Context):
        super().__init__(context)
    async def initialize(self):
        """可选择实现异步的插件初始化方法，当实例化该插件类之后会自动调用该方法。"""
    @filter.command("setu")
    def setu(self, event: AstrMessageEvent, a: str, b: int, c: str):
        chain = [
            Comp.At(qq=event.get_sender_id()), # At 消息发送者
            Comp.Image.fromURL(f"https://image.anosu.top/pixiv/direct?keyword={a}&r18={b}&size={c}"), # 从 URL 发送图片
        ]
        yield event.chain_result(chain)
    async def terminate(self):
        """可选择实现异步的插件销毁方法，当插件被卸载/停用时会调用。"""
