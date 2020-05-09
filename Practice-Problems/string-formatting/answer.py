def print_formatted(number):
    width = len(bin(number)[2:])
    
    for i in range(1, number+1):
        dec_output = str(i).rjust(width, ' ')
        oct_output = oct(i)[2:].rjust(width, ' ')
        hex_output = hex(i)[2:].upper().rjust(width, ' ')
        bin_output = bin(i)[2:].rjust(width, ' ')

        print(dec_output,oct_output,hex_output,bin_output)

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
