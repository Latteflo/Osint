# Shodan Guide for OSINT

## Learning Objectives

By the end of this guide, you should be able to:

1. Understand how the Shodan search engine works.
2. Identify vulnerable connected devices.
3. Evaluate security and configuration features of connected tools.

![Shodan](https://miro.medium.com/max/489/1*ujI2MhP8M7nlzUZ1ci-d8w.jpeg)

## What is Shodan?

Shodan is a search engine specifically designed for Internet-connected devices. While traditional web search engines excel at finding websites, Shodan excels at identifying various connected devices such as surveillance cameras, industrial control systems (ICS), printers, refrigerators, and other IoT devices. Unlike classic search engines, Shodan does not retrieve content but instead gathers information that devices disclose, such as names, locations, IP addresses, ports used, and more. This information is collected in a banner that centralizes all the metadata of the device. Moreover, Shodan's reach extends beyond the web, covering the entire internet.

## How Does Shodan Work?

### Using Shodan

There are several ways to use Shodan:

1. **Web Interface**: The simplest method is using the Shodan web interface. Numerous tutorials, such as [this one](https://www.youtube.com/watch?v=i7PIyCq_VU4), can help you understand how it works. You can also consult the [Shodan help center](https://help.shodan.io/) for a more detailed understanding.

2. **Command-Line Interface (CLI)**: This method provides more flexibility and power for advanced users. We will explore this method in detail below.

3. **Shodan API**: For programmatic access, you can use the Shodan API to manipulate data through scripts. We will revisit this method later.

**Important Tips:**
- For all methods, you need to create an account. Usage will be limited unless you opt for a paid plan.
- Shodan operates with keywords similar to traditional search engines. Consult the documentation for effective usage of keywords ([Basic Query](https://help.shodan.io/the-basics/search-query-fundamentals)).

### Shodan CLI

#### Account Setup and Installation

1. Install Shodan CLI using pip:
   ```bash
   pip install shodan
   ```

2. Initialize Shodan with your API key:
   ```bash
   shodan init <API_KEY>
   ```

#### Basic Commands

- `shodan search <query>`: Perform a search query.
- `shodan host <IP>`: Get detailed information about a specific IP address.
- `shodan count <query>`: Get the total number of results for a query.
- `shodan download <filename> <query>`: Download search results for offline analysis.

#### Advanced CLI Usage

- **Scan Submission**: Request Shodan to crawl an IP or netblock:
  ```bash
  shodan scan submit <IP>
  ```
- **Export Data**: Save your search results in various formats for further analysis using the `shodan download` command.

#### Advanced Search Techniques

1. **Using Filters**:
   - **Hostname**: `hostname:"example.com"` to find devices related to a specific hostname.
   - **Operating System**: `os:"Windows XP"` to find devices running a particular OS.
   - **Network Range**: `net:"192.168.1.0/24"` to search within a specific IP range.

2. **Combining Filters**:
   - Combine multiple filters to refine your search. For example:
     - `apache city:"San Francisco" port:8080` to find Apache servers in San Francisco running on port 8080.
     - `nginx country:"DE" product:"Apache Tomcat/Coyote JSP engine"` to find Nginx servers in Germany running Apache Tomcat.

3. **Special Searches**:
   - **Default Passwords**: `"default password"` to find devices using factory default credentials, which can be a significant security risk.
   - **Vulnerable Devices**: `"vulnerable"` to find devices known to have vulnerabilities.

### Practical Examples

1. **Finding Vulnerable SMB Services**:
   - Query: `port:445 Authentication: "disabled" country:"CA" "Documents"` to find potentially vulnerable SMB shares in Canada.

2. **Identifying Open RDP Ports**:
   - Query: `ip:"<IP>" "\x03\x00\x00\x0b\x06\xd0\x00\x00\x124\x00" has_screenshot:true` to find open RDP ports and gather additional information.

3. **Discovering Unsecured Webcams**:
   - Query: `webcam country:"US" city:"New York"` to find unsecured webcams in New York.

 - Query: `webcam country:"US" city:"New York"` to find unsecured webcams in New York.

  | **Category**               | **Description**                                      | **Query**                                                      |
|----------------------------|------------------------------------------------------|----------------------------------------------------------------|
| **General Device Searches**| Find all HTTP services                               | `port:80`                                                      |
|                            | Find all FTP services                                | `port:21`                                                      |
|                            | Find all SSH services                                | `port:22`                                                      |
|                            | Find all Telnet services                             | `port:23`                                                      |
|                            | Find all RDP services                                | `port:3389`                                                    |
| **Operating Systems**      | Find devices running Windows XP                      | `os:"Windows XP"`                                              |
|                            | Find Apache servers                                  | `product:"Apache httpd"`                                       |
|                            | Find devices running a specific version of nginx     | `product:"nginx" version:"1.17.6"`                             |
|                            | Find MySQL databases                                 | `product:"MySQL"`                                              |
| **Location-Based Searches**| Find devices in a specific city                      | `city:"San Francisco"`                                         |
|                            | Find devices in a specific country                   | `country:"US"`                                                 |
|                            | Find devices within a specific network range         | `net:"192.168.1.0/24"`                                         |
| **Vulnerabilities**        | Find devices with default passwords                  | `"default password"`                                           |
|                            | Find vulnerable devices                              | `"vulnerable"`                                                 |
|                            | Find devices with Heartbleed vulnerability           | `vuln:CVE-2014-0160`                                           |
|                            | Find devices with SMBv1 enabled                      | `"SMBv1"`                                                      |
| **Specific Services**      | Find Elasticsearch servers                           | `product:"Elasticsearch"`                                      |
|                            | Find MongoDB databases                               | `product:"MongoDB"`                                            |
|                            | Find Jenkins servers                                 | `product:"Jenkins"`                                            |
|                            | Find Redis servers                                   | `product:"Redis"`                                              |
| **Industrial Control**     | Find Siemens S7 PLCs                                 | `product:"Siemens S7"`                                         |
|                            | Find BACnet devices (building automation)            | `port:47808`                                                   |
|                            | Find Modbus devices                                  | `port:502`                                                     |
| **IoT Devices**            | Find webcams                                         | `"webcamXP" or "webcam 7"`                                     |
|                            | Find printers                                        | `"HP JetDirect"`                                               |
|                            | Find smart TVs                                       | `"Smart TV"`                                                   |
| **Combining Filters**      | Find Apache servers in Germany                       | `product:"Apache" country:"DE"`                                |
|                            | Find devices in the UK running nginx                 | `product:"nginx" country:"GB"`                                 |
|                            | Find open FTP services in a specific network range   | `port:21 net:"192.168.1.0/24"`                                 |
|                            | Find devices running a specific application in a city| `product:"MySQL" city:"New York"`                              |


## Practice Exercise

### Objective

Create a Python script to interact with Shodan using the API.

### Requirements

1. The script should prompt for an input from the terminal.
2. Run a search on this input.
3. Identify if a vulnerability is present.
4. Download the first 10 results in a JSON file.
5. Refine the results by keeping only the IP, port, organization, and hostnames.
6. Display the results.

Solution: [Shodan-Python-Script](/shodan_script/shodan_search.py)

## Resources

- [Shodan complete guide](./assets/shodan.pdf)
- [Shodan help center](https://help.shodan.io/)
- [Banner Spec](https://datapedia.shodan.io/)
- [Shodan filters](https://www.shodan.io/search/filters)
- [Shodan for dev](https://developer.shodan.io/)
- [Shodan-Python](https://shodan.readthedocs.io/en/latest/index.html)

