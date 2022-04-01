from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hello! {}
<b>This is A Sticker to Image & Image to Sticker Function Bot.</b>
Send Multiple images or stickers and it will work the same

Made with ❤ By @TheTeleRoid.
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("👤 Master", url="https://t.me/TheTeleRoid")],
        [InlineKeyboardButton(text="🏡 Home", callback_data="home")],
    ]
    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("Want to Buys Bots ", url="https://t.me/PayForBotz")
        ],
        [
            InlineKeyboardButton("♻ Help", callback_data="help"),
            InlineKeyboardButton("👤 About", callback_data="about")
        ],
        [InlineKeyboardButton("⭕ Updates Channel ⭕", url="https://t.me/TeleRoidGroup")],
        [InlineKeyboardButton("😇 Support Group ", url="https://t.me/TeleRoid14")],
    ]

    # Help Message
    HELP = """
There is nothing hard to use this:-
Just Follow Given Below.....! 
-> Send Sticker to get Image. 
-> Send Image to get Sticker. 
You can send any amount of images or stickers or both together at Once.
    """

    # About Message
    ABOUT = """
**Know About This Bot** 

📢 Updates : [Channel](https://t.me/TeleRoidGroup) 

😇 Support : [Group](https://t.me/TeleRoid14) 

🐱 Source Code : [Click Here](https://github.com/StarkBotsIndustries/StickerToolsBot)

🌐 Framework : [Pyrogram](docs.pyrogram.org)

🈶 Language : [Python](www.python.org)

👮 Developer : @TheTeleRoidGroup

⚡ Powered By : @MoviesFlixers_DL
    """
