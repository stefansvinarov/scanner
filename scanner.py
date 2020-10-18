#!/usr/bin/python3


import time, sys, shodan, nmap


###Colors###
class c:
    RESET = '\033[0m'
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

while True:
    a = str(input('Enter your API key or type \'key\' to use mine : \n'))
    if a == 'key':
        a = 'HARD-CODED KEY PLACEHOLDER' #Insert your own shodan api key here, I removed mine to avoid abuse but you can hard-code one here.
        print(c.WARNING + 'You are using Stefan\'s key! Use it with caution, please :>' + c.RESET + '\n' + 'Key: ' +  a)

    key = input('Is this your key (y/n) :' + '\n' + a + '\n')

    if key == 'n':
        print('reenter')
    elif key == 'y':
        try: 
            print(c.OKGREEN + 'Proceeding....' + '\n' + 'Enter your search: \n')
            api = shodan.Shodan(a)
            q = str(input('>>>')) #query
            result = api.search(q)
            f = open('rezultz.txt', mode='wt', encoding='utf-8')
            for i in result['matches']:
                time.sleep(0.05) #this is so we don't flood shodan with our requests, otherwise it will block us.
                f.writelines('{}'.format(i['ip_str']))
                f.write('\n')
                print('IP: {}'.format(i['ip_str']))
                print('Hostname: {}'.format(i['hostnames']))
        except Exception as e:
            print(e)
        break

        f.close()

    else:    
        print(key + ' is an invalid choice please use \'n\' or \'y\' only')

print(c.OKBLUE + '100 hosts added in your rezultz.txt file. Resolving targets\' information on ports 1-81 and 8080 using stealth syn scan....' + c.OKGREEN)
nm = nmap.PortScanner() #short for nmap scanner

try:
    f = open('rezultz.txt', mode='rt', encoding='utf-8')
    for i in f:
        j = api.host(i)
        time.sleep(0.7) #for better visibility
        print('''
        IP: {}
        Org: {}
        OS: {}
        '''.format(j['ip_str'], j.get('org', 'n/a'), j.get('os', 'n/a')))
        try:
            nm.scan(i, '1-81, 8080', '-sS')
            print(nm.csv())
        except Exception as e:
            print(e)


except Exception as e:
    print(e)
    
f.close()


