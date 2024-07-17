# Shodan

## Learning objectives

* Understand how the Shodan search engine works
* Identify vulnerable connected devices
* Evaluate security and configuration features of connected tools

![Shodan](https://miro.medium.com/max/489/1*ujI2MhP8M7nlzUZ1ci-d8w.jpeg)
## What ?

* Shodan, surely the fastest solution to identify IP, server types, locations...
It's a search engine for Internet-connected devices. Traditional web search engines are great for finding websites, but they become inefficient for listing all connected devices, such as surveillance cameras, ICS, printers, fridges, in short, everything related to IOT in general.

* Unlike a classic search engine, Shodan does not give the content, but just the information that the devices disclose, such as their names, locations, ip, port used and more... All this information is collected a banner that centralizes all the metadata of the device.

* Another point to note is that Shodan is not limited to the web, it covers the whole internet...

## How it works ?

A video is better than a long speech, or not, so we'll do both.

There are several ways to use Shodan :

- The first, the simplest, is to use the web interface available, you can find several very simple tutorials like [this](https://www.youtube.com/watch?v=i7PIyCq_VU4) to understand how it works but nothing complicated, you can already use it without any problem, you can of course consult the getting started to better understand and discover the interface. ([Shodan help center](https://help.shodan.io/))

- The second way is to use the CLI, this is the one we will discover together.

- And the third way is to use directly the shodan api to manipulate it through a script, we will come back to this way later ;)

NB : 2 tips

* For the 3 methods, don't forget to create an account, you will still be limited unless you take the money out, like every time...

* Even if it's a dedicated search engine, it's still a search engine and so it also works with keywords, don't forget to consult the documentation to use them ([Basic Query](https://help.shodan.io/the-basics/search-query-fundamentals))

## CLI

Before we get into the nitty-gritty, we'll go over all of your account setup and installation, then we'll start with some basic searches ([CLI Shodan doc](https://cli.shodan.io/))

### Register

- Shodan register : [link](https://account.shodan.io/register)

- Insert your username, password and email address : 

![Shodan register](./assets/shodanRegister.png)
- Don't forget to check your email to activate your account

### Installation

- Just copy the following command line :

```BASH
pip3 install -U --user shodan
```

### Api // To be modified no longer free

- To finish the installation of your account correctly and use the available commands (free) you will have to get your API Key.

- [Link](https://account.shodan.io/) to your API Key, make a copy of this one : 

![](./assets/shodanAPI.png)

- After that, if we follow the doc, you can insert the following command :

```BASH
shodan init YOUR_API_KEY
```

![](./assets/success.png)

- This key will not allow you to use all searches on Shodan and some features will only be available with a premium subscription, like *radar*, *stream*..., but let's see what we can do.

### Search

- Ok, first (and not the last...) : 

```BASH
shodan -h
```

- Let's run a basic search

```BASH
shodan search YOUR REQUEST
```

- [TLDR](https://en.wikipedia.org/wiki/Wikipedia:Too_long;_didn%27t_read)... well, let's tidy up a bit, try this :

```BASH
shodan search --fields org YOUR REQUEST
```

- It's better, we will be able to sort the results according to what we are interested in and managing the fields, we have just left the field "org" but we can manage the banner in a more interesting way by adding several fields ([Spec](https://datapedia.shodan.io/)), and you will be able to sort with the more crisp information :

```BASH
shodan search --fields ip_str,port,org YOUR REQUEST
```

- And that's enough, be careful though, filters for a search are not available in the CLI with the free version...

### Download : 

- Ok, to download the results, we will just proceed like this :

```BASH
shodan download --limit 10 check YOUR REQUEST
```

NB : here, we limit the results to 10, -1 if you want all possible results

- Once it's done we'll just parse the results with the same fields :

```BASH
shodan parse --fields ip_str,port,org check.json.gz
```

#### Advanced Search Techniques

1. **Using Filters:**
   - **Hostname:** `hostname:"example.com"` to find devices related to a specific hostname.
   - **Operating System:** `os:"Windows XP"` to find devices running a particular OS.
   - **Network Range:** `net:"192.168.1.0/24"` to search within a specific IP range.

2. **Combining Filters:**
   - Combine multiple filters to refine your search. For example:
     - `apache city:"San Francisco" port:8080` to find Apache servers in San Francisco running on port 8080.
     - `nginx country:"DE" product:"Apache Tomcat/Coyote JSP engine"` to find Nginx servers in Germany running Apache Tomcat.

3. **Special Searches:**
   - **Default Passwords:** `"default password"` to find devices using factory default credentials, which can be a significant security risk.
   - **Vulnerable Devices:** `"vulnerable"` to find devices known to have vulnerabilities.

#### Command-Line Interface (CLI)

1. **Installation:**
   - Install Shodan CLI using `pip install shodan`.
   - Initialize with your API key using `shodan init <API_KEY>`.

2. **Basic Commands:**
   - `shodan search <query>`: Perform a search query.
   - `shodan host <IP>`: Get detailed information about a specific IP address.
   - `shodan count <query>`: Get the total number of results for a query.
   - `shodan download <filename> <query>`: Download search results for offline analysis.

3. **Advanced CLI Usage:**
   - **Scan Submission:** `shodan scan submit <IP>` to request Shodan to crawl an IP or netblock.
   - **Export Data:** Use the `shodan download` command to save your search results in various formats for further analysis.

#### Practical Examples

1. **Finding Vulnerable SMB Services:**
   - Query: `port:445 Authentication: "disabled" country:"CA" "Documents"` to find potentially vulnerable SMB shares in Canada.

2. **Identifying Open RDP Ports:**
   - Query: `ip:"<IP>" "\x03\x00\x00\x0b\x06\xd0\x00\x00\x124\x00" has_screenshot:true` to find open RDP ports and gather additional information.

## Practice

- Type : Solo
- Duration : 2 days
- Prerequisites: Python + Shodan api
- Link : [Simplon form]()


Ok, If we didn't talk about the API and it's voluntary, we'll ask you to create a script that will be able to reproduce a search like in the CLI tutorial and all this with Python...

Your script must :

* Get an input from the terminal
* Run a search on this input
* Identify if a vulnerability is present
* Download the first 10 results in a json file
* Refine the results by keeping only the ip, port, organization and hostnames
* Display the results

## Resources

- [Shodan complete guide](./assets/shodan.pdf)
- [Shodan help center](https://help.shodan.io/)
- [Banner Spec](https://datapedia.shodan.io/)
- [Shodan filters](https://www.shodan.io/search/filters)
- [Shodan for dev](https://developer.shodan.io/)
- [Shodan-Python](https://shodan.readthedocs.io/en/latest/index.html)
