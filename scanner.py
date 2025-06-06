import scapy.all as scapy
import optparse

def get_argument():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest="target", help="Target IP / IP range.")
    (options, arguments) = parser.parse_args()
    if not options.target:
        parser.error("[-] Please specify a target, use --help for more info.")
    return options

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    clients_list = []
    for element in answered_list:
        client = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(client)

    return clients_list

def print_result(results_list):
    print("IP Address\t\tMAC Address")
    print("-----------------------------------------")
    for client in results_list:
        print(f"{client['ip']}\t\t{client['mac']}")

options = get_argument()
scan_result = scan(options.target)
print_result(scan_result)
