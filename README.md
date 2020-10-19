# scanner
Python script querrying Shodan for different searches


This script utilizes the shodan and nmap python libraries to automate, simplify, fasten 
the searches one may be interested in.

USAGE:

Execute the script (su permissions required because of the nmap part) and enter your shodan 
API key when prompted to.

NOTE: Initially there was a hard-coded key in the script I removed it from this repo
due to obvious reasons.

Confirm your key and you will be promted to type in your search by '>>>'.
Type in whatever you are looking for and a result list will be generated.
If you are using a free key, this list will be limited to 100 entries. After the list
is composed the script will perform a basic predefined (but easily adjustable) syn 
stealth scan on several ports via nmap and show the results in real time.

Example of some of the shodan search filters:


General

    all
    asn
    city
    country
    cpe
    device
    geo
    has_ipv6
    has_screenshot
    has_ssl
    has_vuln
    hash
    hostname
    ip
    isp
    link
    net
    org
    os
    port
    postal
    product
    region
    scan
    shodan.module
    state
    version


HTTP

    http.component
    http.component_category
    http.favicon.hash
    http.html
    http.html_hash
    http.robots_hash
    http.securitytxt
    http.status
    http.title
    http.waf



SSL

    ssl
    ssl.alpn
    ssl.cert.alg
    ssl.cert.expired
    ssl.cert.extension
    ssl.cert.fingerprint
    ssl.cert.issuer.cn
    ssl.cert.pubkey.bits
    ssl.cert.pubkey.type
    ssl.cert.serial
    ssl.cert.subject.cn
    ssl.chain_count
    ssl.cipher.bits
    ssl.cipher.name
    ssl.cipher.version
    ssl.version

Full list of filters here:

NOTE: Some, like the 'vuln' one, require a payed key.
https://beta.shodan.io/search/filters
