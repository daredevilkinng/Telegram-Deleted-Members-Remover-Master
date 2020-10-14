from pyrogram import Filters, Client
from time import sleep

app = Client("DareDevilKinng", api_id=, api_hash="", phone_number="")

banner = """
   _______________          _______________
  |  ___________  |        |  ___________  |
  | |           | |        | |           | |
  | |   X   X   | |        | |           | |
  | |     -     | |        | |   0   0   | |
  | |    ___    | |        | |     -     | |
  | |   /   \   | |        | |   \___/   | |
  | |   \___/   | |        | |           | |
  | |___________| |        | |___________| |
  |_______________|        |_______________|
    ____|   |___.............._|________|_
   | ********** |            | ********** |
   | ********** |            | ********** |
    ------------              ------------
   [ Coded by : DareDevilKinng]
"""

print(banner)
counter = 1
@app.on_message(Filters.me & Filters.text)
def main(c, m):
    global counter
    if m.text == "DareDevilKinng":
        for i in app.iter_chat_members(m.chat.id):
            if i.user.is_deleted:
                ids = i.user.id
                app.kick_chat_member(m.chat.id, ids)
                print("Kicked "+str(counter))
                sleep(3)
                counter += 1
app.run()

banner1 = "[ Coded by : DareDevilKinng]"

print(banner1)
