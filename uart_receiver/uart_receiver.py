import board
import busio
import time

UART_TX = board.IO6
UART_RX = board.IO7

PERIOD = 600 # 10 minutes
MAX_HISTORY = 500

counter = 0
history_mac = {}
# history_mac[mac] = (time.time(), channel, rssi)

def gc_history_mac():
    global history_mac
    for mac in list(history_mac.keys()):
        if time.time() - history_mac[mac][0] > PERIOD:
            del history_mac[mac]

def handle_mac(channel, rssi, mac):
    global history_mac, counter
    
    if mac in history_mac:
        last_time = history_mac[mac][0]
        if time.time() - last_time > PERIOD:
            counter += 1
            print("[%d]"%time.time(), "Counter:", counter, mac, rssi, last_time)
    else:
        counter += 1
        print("[%d]"%time.time(), "Counter:", counter, mac, rssi)
    
    history_mac[mac] = (time.time(), channel, rssi)
    
    if len(history_mac) > MAX_HISTORY:
        gc_history_mac()

def handle_uart_data(data):
    try:
        data = data.decode()
    except:
        return
    
    for item in data.split('\r\n'):
        if item:
            try:
                channel, rssi, mac = item.split('\t')
                channel = int(channel)
                rssi = int(rssi)
                if len(mac) != 17:
                    raise ValueError("Invalid MAC address")
                handle_mac(channel, rssi, mac)
            except:
                continue
            
def save_report(counter):
    pass

def main():
    uart = busio.UART(UART_TX, UART_RX, baudrate=115200)
    last_print_time = 0
    last_clear_t = time.time()

    while True:
        if uart.in_waiting > 0:
            data = uart.read(uart.in_waiting)
            if data:
                handle_uart_data(data)
        
        if time.time() - last_clear_t > PERIOD:
            global counter
            save_report(counter)
            counter = 0
            last_clear_t = time.time()
        
        if time.time() - last_print_time > 1:
            last_print_time = time.time()

if __name__ == "__main__":
    main()
