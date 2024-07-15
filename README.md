# PacketParser

<img alt="Image" src="https://static.wixstatic.com/media/a7a5b4_7202bbbf2eac46f0b6ee4ba1f0b5bc56~mv2.jpg/v1/fill/w_308,h_231,fp_0.50_0.50,q_90,enc_auto/a7a5b4_7202bbbf2eac46f0b6ee4ba1f0b5bc56~mv2.jpg">

> **A cap/pcap packet parser to make life easier when performing stealth/passive reconnaissance.**

To use PacketParser, follow these steps:

1. Clone the repository:
    ```
    git clone https://github.com/vysec/PacketParser.git
    ```

2. Navigate to the project directory:
    ```
    cd PacketParser
    ```

3. Install the required dependencies:
    ```
    pip install -r requirements.txt
    ```

4. Run the packet parser:
    ```
    python3 packetparser.py -i it-office.pcap -o unique.txt -oP unique-ports.txt -oI unique-ips.txt -s
    ```

For more information and usage examples, please refer to the [PacketParser documentation](https://github.com/vysec/PacketParser).

