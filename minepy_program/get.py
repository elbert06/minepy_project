from mminepy.mminepy import *
init()
g = ArrayList(string())
while time(Enable()):
    print("plugin enabled")
while event(PlayerDeathEvent()):
    e = Event()
    player_name = e.getEntity().getName()
    while when(g.__contains__(player_name)):
        player_1 = e.getEntity()
        player_1.sendMessage("test") 
while command("check"):
    while when(not(g.__contains__("elbert"))):
        g.add("elbert")
        print("test_complete")
make(server=True,online=False,port=True)