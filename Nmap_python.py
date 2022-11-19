#!/use/bin/python3
Import nmap

#CREATING VARIABLE SCANNERTO STORE PORTSCANNER() CLASS
scanner = nmap.PortScanner()

Print("Welcome this is namp aut. Tool")

#CREATING VARIABLE TO TAKE USER INPUT
ip_addr = input("Please enter your ip address you want to scan")
Print("the ip you enterred" , ipaddr)
type(ip_addr)

#CREATING A VAR RESPONSE THE USER GIVES WHAT SCAN THEY WANT TO RUN
resp= input("""\nplease enter the type of scan you want to run
			1)SYN ACK SCAN
			2)UDP SCAN
			3)COMPREHENSIVE SCAN""")
print("you've selected option:", resp)

If resp =='1':
	Print("Nmap version", scanner.nmap_version())
	
	#STARTS SCANNING THE IP ADDR GIVEN FROM PORT 1 TO 1024 AS IN NMAP
	scanner.scan(ip_addr, '1-1024', '-v -sS')
	
	#PRINTS THE SCANNED INFO OF OUTPUT
	Print(scanner.scaninfo())
	
	#PRINTS THE CURRENT STATE OF THE IP ADDR
	Print("Ip status" , scanner[ip_addr].state())
	
	#PRINTS THE PROTOCOL USED 
	Print(scanner[ip_addr].all_protocols())
	
	#PRINTS THE OPEN PORTS IN FORM OF KEYS
	Print("Open ports' , scanner[ip_addr]["tcp'].keys())
elif resp == '2':
	Print("Nmap version", scanner.nmap_version())
	
	#STARTS SCANNING THE IP ADDR GIVEN FROM PORT 1 TO 1024 AS IN NMAP
	scanner.scan(ip_addr, '1-1024', '-v -sU')
	
	#PRINTS THE SCANNED INFO OF OUTPUT
	Print(scanner.scaninfo())
	
	#PRINTS THE CURRENT STATE OF THE IP ADDR
	Print("Ip status" , scanner[ip_addr].state())
	
	#PRINTS THE PROTOCOL USED 
	Print(scanner[ip_addr].all_protocols())
	
	#PRINTS THE OPEN PORTS IN FORM OF KEYS
	Print("Open ports' , scanner[ip_addr]["udp'].keys())
elif resp == '3':
	Print("Nmap version", scanner.nmap_version())
	
	#STARTS SCANNING THE IP ADDR GIVEN FROM PORT 1 TO 1024 AS IN NMAP
	scanner.scan(ip_addr, '1-1024', '-v -sS -sV -sC -A -O')
	
	#PRINTS THE SCANNED INFO OF OUTPUT
	Print(scanner.scaninfo())
	
	#PRINTS THE CURRENT STATE OF THE IP ADDR
	Print("Ip status" , scanner[ip_addr].state())
	
	#PRINTS THE PROTOCOL USED 
	Print(scanner[ip_addr].all_protocols())
	
	#PRINTS THE OPEN PORTS IN FORM OF KEYS
	Print("Open ports' , scanner[ip_addr]["tcp'].keys())
else resp >= '4':
Print ("please enter a valid option")