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
        [InlineKeyboardButton("✨ Bot Status and More Bots ✨", url="https://t.me/StarkBots/7")],
        [InlineKeyboardButton(text="🏡 Home", callback_data="home")],
    ]
    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("✨ Bot Status and More Bots ✨", url="https://t.me/StarkBots/7")
        ],
        [
            InlineKeyboardButton("How to Use ❔", callback_data="help"),
            InlineKeyboardButton("🎪 About 🎪", callback_data="about")
        ],
        [InlineKeyboardButton("♥ More Amazing bots ♥", url="https://t.me/StarkBots")],
        [InlineKeyboardButton("🎨 Support Group 🎨", url="https://t.me/StarkBotsChat")],
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
**About This Bot** 

Bot created by @StarkBots

Source Code : [Click Here](https://github.com/StarkBotsIndustries/StickerToolsBot)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : @StarkProgrammer
    """
