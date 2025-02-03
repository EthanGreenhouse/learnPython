# Python Learning 1
# Ethan Greenhouse 2/2/2025

class PacketGen:
    def __init__(self):
        self.Packet_t = 0 

    def generate_packet(self, pid, dst, src, data):
        # Convert data to a binary string
        binary_data = ''.join(format(ord(char), '08b') for char in data)
        
        # If the data is empty set parity bit = 1
        if not binary_data:
            parity_bit = '1'
        else:
            # Compute the parity bit (0 if the number of '1's in binary_data is even, 1 if odd)
            parity_bit = '0' if binary_data.count('1') % 2 == 0 else '1'

        # Create the packet tuple
        packet = (pid, dst, src, data, parity_bit)

        self.Packet_t = packet
        return packet


class PacketRecv:
    def __init__(self, packet_t):
        self.pktid = packet_t[0]        # Packet ID
        self.dst = packet_t[1]          # Destination
        self.src = packet_t[2]          # Source
        self.data = packet_t[3]         # Message
        self.rcvd_parity = packet_t[4]  # Received parity bit
        self.ParityValid = -1           # Sets ParityValid to unvalid
    
    # Calculates the parity bit for the given data and compares it with the received parity.
    # If they match, sets ParityValid to True. Otherwise sets it to False.
    def check_parity(self, data, rcvd_parity):
        # Convert the data to a binary string
        binary_data = ''.join(format(ord(char), '08b') for char in data)

        # Calculate the parity bit: 0 if even number of '1's, 1 if odd number of '1's
        computed_parity = '0' if binary_data.count('1') % 2 == 0 else '1'

        # Compare the computed parity with the received parity and set ParityValid
        if computed_parity == rcvd_parity:
            self.ParityValid = True
        else:
            self.ParityValid = False
    
    # Return all packet details
    def parsed_packet(self):
        return "Packet Number " + str(self.pktid) + " with a message " + str(self.data) + \
            " is received from node " + str(self.src) + ". Parity Check returns " + str(self.ParityValid)

# Sums integers from 0 to given number
def problem_one(integer_to_sum_to):
    # Check if input is an integer
    if not isinstance(integer_to_sum_to, int):
        return None

    # Check if number if positive
    if (integer_to_sum_to > 0):
        return sum(range(integer_to_sum_to + 1))
    
    return None

# Concatenates two lists and removes duplicates
def problem_two(left_list, right_list):
    concatenated = left_list + right_list
    sorted = []
    
	# Check if inputs are lists
    if not isinstance(left_list, list) or not isinstance(right_list, list):
        return None
    
    # Check that every item left list is an integer
    for i in left_list:
        if not isinstance(i, int):
            return None

    # Check that every item right list is an integer
    for i in right_list:
        if not isinstance(i, int):
            return None
    
    # Go through each number in concatenated list
    for i in concatenated:
        # If number is not in sorted list, add it
        if i not in sorted:
            sorted.append(i)
            
    return sorted

# Reads a .csv file and returns a list of arrays of the given 2D array
def problem_three(filename):
    # Check if input is a string
    if not isinstance(filename, str):
        return None
    
    # Open the file with .csv added
    with open(filename + ".csv", 'r') as file:
        result = []
            
        # Read each line from the file
        for line in file:
            # Remove whitespace and split by comma, then convert each value to integer and add as a new row
            row = [int(x.strip()) for x in line.split(',')]
            result.append(row)
            
        return result

# Converts hexadecimal to ascii
def problem_four(hex_string):
    # Check if hex_string is a string
    if not isinstance(hex_string, str):
        return None
    
    # Check if hex_string has an even length
    if len(hex_string) % 2 != 0:
        return None
    
    # Check if string only contains valid hexadecimal characters
    if not all(c in '0123456789abcdefABCDEF' for c in hex_string):
        return None
        
    # Convert hex to bytes and then to ASCII string
    # bytes.fromhex() will convert pairs of hex digits to bytes
    # decode('ascii') will convert those bytes to an ASCII string
    return bytes.fromhex(hex_string).decode('ascii')

# Doubles last value in each row of a 2D array
def problem_five(list_of_lists):  
    # Check if input is a 2D array
    if not isinstance(list_of_lists, list): 
        return None
    
    for row in list_of_lists:
        # Check if each row is a list
        if not isinstance(row, list):
            return None
        
        # Check if list is empty
        if len(row) == 0:
            return None

    result = []
        
    for row in list_of_lists:
        # Check if row has more than 1 element
        if len(row) == 0:
            return None
               
        # Create new row and double the last element
        new_row = row[:-1] + [row[-1] * 2]
        result.append(new_row)  
    
    return result

# Lists unique domain names and extensions given a list of strings
def problem_six(list_of_email_addresses):
    # Check if the input is a list
    if not isinstance(list_of_email_addresses, list):
        return None

    unique_domains = set()

    for email in list_of_email_addresses:
        # Ensure the email is a string
        if not isinstance(email, str):
            return None

        # Check for a single '@' in the email
        if email.count('@') == 1:
            # Split the email into local part and domain part
            local, domain = email.split('@')

            # Check if domain has a '.' and valid structure
            if '.' in domain:
                # Split the domain from the last dot into domain_name and extension
                domain_name, extension = domain.rsplit('.', 1)

                # Check that domain name and extension only contain letters
                if domain_name.isalpha() and extension.isalpha():
                    unique_domains.add(domain)

    return sorted(unique_domains)

# Create a packet with multiple data fields and adds a parity bit
def problem_seven(pid, dst, src, data):
    pktGen = PacketGen()
    return pktGen.generate_packet(pid, dst, src, data)

# Process packet created in problem 7 and verify if the parity bit matches the calculated parity bit
def problem_eight(packet_t):
    # Check if packet_t is a tuple with 5 elements
    if not isinstance(packet_t, tuple) or len(packet_t) != 5:
        return None

    # Create an instance of PacketRecv with inputted packet
    pkt = PacketRecv(packet_t)

    # Call check_parity to verify if the received parity is correct
    pkt.check_parity(pkt.data, pkt.rcvd_parity)

    return pkt.parsed_packet()

# Test functions
if __name__ == '__main__':
    print("Problem 1")
    print(problem_one(6))																		# Expect: 21
    print(problem_one(10))																		# Expect: 55
    print(problem_one(-1))																		# Expect: None
    print(problem_one("Test"))																	# Expect: None
    
    print("\n Problem 2")
    print(problem_two([1, 2, 3], [2, 3, 4]))													# Expect: [1, 2, 3, 4]
    print(problem_two([1],[2]))																	# Expect: [1, 2]
    print(problem_two([], []))																	# Expect: []
    print(problem_two([1, 2, 3], [2, 3, "Test"]))												# Expect: None

    print("\n Problem 3")
    print(problem_three("MyData"))																# Expect: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(problem_three(0))																		# Expect: None
    
    print("\n Problem 4")
    print(problem_four("48656c6c6f20576f726c6421"))												# Expect: Hello World!
    print(problem_four("48656c6c6f20576f726c642"))												# Expect: None
    print(problem_four("ZZZZZZ"))																# Expect: None
    print(problem_four(0))																		# Expect: None
    
    print("\n Problem 5")
    print(problem_five([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))										# Expect: [[1, 2, 6], [4, 5, 12], [7, 8, 18]]
    print(problem_five("Test"))																	# Expect: None
    print(problem_five([[1, 2, 3], [4, 5, 6], []]))												# Expect: None
    print(problem_five([[1, 2, 3], [4, 5, 6], "Test"]))											# Expect: None
    
    print("\n Problem 6")
    print(problem_six(['cats@gmail.com', 'Hello World!', 'dogs@gmail.com', 'cows@yahoo.com']))	# Expect: ['gmail.com', 'mail.org', 'yahoo.com']
    print(problem_six(['test1@@test1.com', 'test2.com', 'test3@com']))							# Expect: []
    print(problem_six(['test1@invalid.', 'test2@valid.com', 'test3@invalid.com.2']))  			# Expect: ['valid.com']
    print(problem_six("Test"))																	# Expect: None
    
    print("\n Problem 7")
    print(problem_seven('2', '10', '5', 'Hi'))													# Expect: ('2', '10', '5', 'Hi', '0')
    print(problem_seven('9', '7', '3', 'Testing'))												# Expect: ('9', '7', '3', 'Testing', '0')
    print(problem_seven('', '', '', ''))  														# Expect: ('', '', '', '', '1')
    print(problem_seven(1, 2, 3, 'Test'))  														# Expect: None

    
    print("\n Problem 8")
    packet = ('2', '10', '5', 'Hi', '0')
    print(problem_eight(packet))																# Expect: Packet Number 2 with a message Hi is received from node 5. Parity Check returns True			
    packet = ('6', '2', '3', 'Testing', '1')
    print(problem_eight(packet))																# Expect: Packet Number 6 with a message Testing is received from node 3. Parity Check returns False
    print(problem_eight(('2', '10', '5', 'Hi')))  												# Expect: None
    print(problem_eight("Test"))  																# Expect: None
