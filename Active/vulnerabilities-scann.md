# Vulnerability Scanning

 You will see the importance of vulnerability scanning in the next section. It is a process that detects and classifies system vulnerabilities in computers, networks, and communications equipment and predicts the effectiveness of countermeasures. 

## Exercices 
1. Follow this room on try hack me
- https://tryhackme.com/room/vulnerabilities101
- https://tryhackme.com/room/rpnessusredux

1. Questions :  

    **2.1** Do a manual scan of the 10.12.1.36 box  

    `nmap -sV 10.12.1.36`
    - How many vulnerable services are there?  
    - What are these services?
```
nmap -sV 10.12.1.36

PORT     STATE SERVICE    VERSION
22/tcp   open  ssh        OpenSSH 7.9 (protocol 2.0)
80/tcp   open  http       Apache httpd 2.4.29 ((Ubuntu))
139/tcp  open  netbios-ssn Samba smbd 4.7.6-Ubuntu
445/tcp  open  netbios-ssn Samba smbd 4.7.6-Ubuntu
```

  **2.2** Do a vulnerability scan with nmap. 
    - How many vulnerabilities did nmap find ?
  
     3 vulnerable services.
 - What are these services?

    ```OpenSSH 7.9 (CVE-2020-15778)
    Apache httpd 2.4.29 (CVE-2017-15710)
    Samba smbd 4.7.6-Ubuntu (CVE-2018-1057)
    ```

**3.3** Do a vulnerability scan with Nessus.
  - How many vulnerabilities did nessus find ?
  `nmap --script vuln 10.12.1.36`
  - What are these services?
  ```
  Nmap scan report for 10.12.1.36
Host is up (0.00048s latency).

PORT     STATE SERVICE
22/tcp   open  ssh
|_ssh-vulnkey: 
80/tcp   open  http
|_http-dombased-xss: 
139/tcp  open  netbios-ssn
|_samba-vuln-cve-2018-1057: Samba is vulnerable to CVE-2018-1057
445/tcp  open  netbios-ssn
|_samba-vuln-cve-2018-1057: Samba is vulnerable to CVE-2018-1057

Nmap done: 1 IP address (1 host up) scanned in 2.38 seconds
```