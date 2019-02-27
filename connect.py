import network
def con():
    sta=network.WLAN(network.STA_IF)
    ap=netwrk.WLAN(network.AP_IF)
    ap.active(False)
    sta.connect('Artemis','password')
    print(sta.config())
