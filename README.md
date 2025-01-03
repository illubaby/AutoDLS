
Step :
To change the private DNS settings in BlueStacks to block ad:

adb -s emulator-5554 shell settings put global private_dns_mode hostname
adb -s emulator-5554 shell settings put global private_dns_specifier dns.adguard.com
adb -s emulator-5554 shell settings put global private_dns_mode off




```mermaid
stateDiagram-v2
    [*] --> LiveEvents
    LiveEvents --> LiveMatch : is_LiveEvents
    LiveMatch --> LiveEvents : is_concede, is_opponent_out

