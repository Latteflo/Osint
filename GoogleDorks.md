# Google Dorking

Google Dorking is a technique used by hackers to find sensitive information on the web. It involves using advanced search operators to find specific information that is not easily accessible through normal search queries.

 This technique can be used to find things like passwords, usernames, email addresses, and other sensitive information that is not intended to be publicly available.

## Learning objectives

* Use google query syntax
* Formulate requests in a specific way
* Target sensitive information with google queries


## What ?

Google is the most used search engine in the world and is surely the best, even if we can reproach a lot of things to its privacy policy or to the use that the company makes of our data , in our environment, it is a quality ally, let's see why...

### Some statistics

- It has 90% of the search engine market share, the only countries where he is not a leader are, not surprisingly, Russia and China.

- There are more than 130 000 billion pages indexed by google.

- Google crawls over 20 billion pages per day.

- Google is also 80,000 queries every second or 6.9 billion per day, in short, more than 2000 billion per year.

As you can see, when it comes to information research, google becomes a very interesting database to exploit ...

Sources : [Google Trends](https://trends.google.fr/trends/?geo=BE) and [Stat Counter](https://gs.statcounter.com/)

### How to use it ?

Google uses its own syntax to search its database. This is very powerful to refine our searches, and we will work on this.

**First, some tips**

- In English : It seems obvious but you will always find more content

- Make it simple : Use only keywords, no need for long sentences.

- Use the operators : "", ., OR, AND, *, NOT, ~, ().

- Use the prefixes (advanced search operators) : site:, filetype:, cache:, and more, there are many, some are deprecated, some are more efficient than others but some combination can be very useful for a targeted search.

- Don't forget to use the image search too !

### What is dorking ?

It is precisely the set of search possibilities with Google's own syntax that allows you to make very targeted searches of websites, we talk about Google Dorking.

For example, we can find sensitive information such as emails, passwords, hidden files...
Identify authentication pages.
Search for hardware connected to the Internet (cameras, routers, printers, ...)
Check misconfigured web servers
Target web server related tools like phpmyadmin, phpinfo(), site administration...
Find vulnerabilities that allow to hack the target.

You can consult the following [page](https://www.exploit-db.com/google-hacking-database) if you want to have an overview of the possibilities ;)

## Check

Let's start with a little introduction

[![Tuto google dorking](./assets/dork.png)](https://www.youtube.com/watch?v=hrVa_dhD-iA)

## Here are some of the most commonly used Google dorks:

1. site: - Search within a specific website Example: site:example.com confidential
2. filetype: - Search for specific file types Example: filetype:pdf "employee handbook"
3. inurl: - Search for a specific word in the URL Example: inurl:admin
4. intitle: - Search for a specific word in the page title Example: intitle:"index of" passwords
5. intext: - Search for specific text within the page content Example: intext:"username" intext:"password"
6. cache: - View Google's cached version of a site Example: cache:example.com
7. ext: - Search for specific file extensions Example: ext:sql intext:password
8. - (minus sign) - Exclude certain words from search results Example: cybersecurity -courses
9. | (pipe symbol) - Search for either one term or another Example: intext:username | intext:user
10. .. (two periods) - Search within a range of numbers Example: salary $50000..$100000
11. related: - Find sites related to a given domain Example: related:github.com
12. info: - Get information about a website Example: info:example.com

These dorks can be combined to create more complex queries.

## Practices

[*] [Room Google dorking](https://tryhackme.com/room/googledorking) 
[*] [Google H DB](https://www.exploit-db.com/google-hacking-database)

Disclamer: Google dorking is not illegal, but using it to access sensitive information without permission is illegal. Always ensure you have permission before using Google dorks to search for information.
