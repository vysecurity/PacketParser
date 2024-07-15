from scapy.utils import rdpcap
import argparse
from scapy.layers.inet import IP, TCP

# Usage example:
# python3 packetparser.py -i it-office.pcap -o unique.txt -oP unique-ports.txt -oI unique-ips.txt -s

date = "2024-07-15"
version = "0.1.0"
author = "@vysecurity"

def parse_cap(cap_file, output_ip_file, output_port_file, output_pair_file, silent):
    packets = rdpcap(cap_file)
    dest_pairs = []

    for packet in packets:
        if IP in packet and TCP in packet:
            dest_ip = packet[IP].dst
            dest_port = packet[TCP].dport
            dest_pairs.append((dest_ip, dest_port))

    # Write unique destination IP addresses to the output file
    if output_ip_file:
        with open(output_ip_file, 'w') as f:
            unique_ips = set(ip for ip, _ in dest_pairs)
            for ip in unique_ips:
                f.write(f"{ip}\\n")

    # Write unique TCP ports to the output file
    if output_port_file:
        with open(output_port_file, 'w') as f:
            unique_ports = set(port for _, port in dest_pairs)
            for port in unique_ports:
                f.write(f"{port}\\n")

    # Write unique IP:port pairs to the output file
    if output_pair_file:
        with open(output_pair_file, 'w') as f:
            unique_pairs = set(dest_pairs)
            for dest_ip, dest_port in unique_pairs:
                f.write(f"{dest_ip}:{dest_port}\\n")

    if not silent:
        return dest_pairs

# Create an argument parser
parser = argparse.ArgumentParser(description='Parse cap file')

# Add an argument for the input file
parser.add_argument('-i', '--input', type=str, help='Path to the cap file')

# Add arguments for the output files
parser.add_argument('-oI', '--output-ip', type=str, help='Path to the output file for unique IP addresses')
parser.add_argument('-oP', '--output-port', type=str, help='Path to the output file for unique TCP ports')
parser.add_argument('-o', '--output-pair', type=str, help='Path to the output file for unique IP:port pairs')

# Add an argument for the banner
parser.add_argument('-nb', '--nobanner', action='store_true', help='Do not display the banner')

# Add an argument for silent mode
parser.add_argument('-s', '--silent', action='store_true', help='Disable printing of the summary')

# Parse the command line arguments
args = parser.parse_args()

# Check if the banner argument is provided
if not args.nobanner:
    print("  ____       _       _   ____                          ")
    print(" |  _ \\ _ __(_)_ __ | |_|  _ \\ __ _ _ __ ___  ___ _ __ ")
    print(" | |_) | '__| | '_ \\| __| |_) / _` | '__/ __|/ _ \\ '__|")
    print(" |  __/| |  | | | | | |_|  __/ (_| | |  \\__ \\  __/ |   ")
    print(" |_|   |_|  |_|_| |_|\\__|_|   \\__,_|_|  |___/\\___|_|   ")
    print("                                                       ")
    print(f" Author: {author}")
    print(f" Version: {version}")
    print(f" Date: {date}")
    print()

# Check if the input file argument is provided
if args.input:
    cap_file = args.input
else:
    print("Please provide the path to the cap file using the -i/--input option.")
    exit(1)

# Check if the output IP file argument is provided
if args.output_ip:
    output_ip_file = args.output_ip
else:
    output_ip_file = None

# Check if the output port file argument is provided
if args.output_port:
    output_port_file = args.output_port
else:
    output_port_file = None

# Check if the output pair file argument is provided
if args.output_pair:
    output_pair_file = args.output_pair
else:
    output_pair_file = None

dest_pairs = parse_cap(cap_file, output_ip_file, output_port_file, output_pair_file, args.silent)

if not args.silent:
    for dest_ip, dest_port in dest_pairs:
        print(f"Destination IP: {dest_ip}, TCP Port: {dest_port}")

    # Calculate the summary of destination and port pairs
    summary = f"Total unique destination and port pairs: {len(set(dest_pairs))}"

    # Print the summary
    print(summary)

    # Print unique destination and port pairs
    unique_pairs = set(dest_pairs)
    for dest_ip, dest_port in unique_pairs:
        print(f"Destination IP: {dest_ip}, TCP Port: {dest_port}")
