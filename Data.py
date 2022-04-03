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
        [InlineKeyboardButton("⭕ Updates Channel ⭕", url="https://t.me/TeleRoidGroup"),
         InlineKeyboardButton("😇 Support Group ", url="https://t.me/TeleRoid14")],
        [
            InlineKeyboardButton("🔐 Close", callback_data="close")
        ],
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
╭────[🔅Stickers Info🔅]───⍟
│
├<b>📢 Channel : <a href='https://t.me/TeleRoidGroup'>Bots Channel</a></b>
│
├<b>👥 Version : <a href='https://t.me/joinchat/t1ko_FOJxhFiOThl'>0.9.2 beta</a></b>
│
├<b>💢 Source : <a href='https://github.com/PredatorHackerzZ'>Click Here</a></b>
│
├<b>🌐 Server : <a href='https://heroku.com'>Heroku</a></b>
│
├<b>📕 Library : <a href='https://github.com/pyrogram'>Pyrogram 1.2.8</a></b>
│
├<b>㊙ Language: <a href='https://www.python.org'>Python 3.9.4</a></b>
│
├<b>👨‍💻 Developer : <a href='https://t.me/PredatorHackerZ'>Pred∆tor</a></b>
│
├<b>🚸 Powered By : <a href='https://t.me/Moviesflixers_DL'>HindiWebNetwork</a></b>
│
╰──────[Thanks 😊]───⍟

    """
