#!/usr/bin/python3
'''Script to parse and analyze HTTP request logs.'''
import re


def extract_input(input_line):
    '''Extract specific parts from a line of an HTTP request log.'''
    # Define regex patterns to capture IP, date, request, status code, and file size
    patterns = (
        r'\s*(?P<ip>\S+)\s*',  # Capture IP address
        r'\s*\[(?P<date>\d+-\d+-\d+ \d+:\d+:\d+\.\d+)\]',  # Capture date and time
        r'\s*"(?P<request>[^"]*)"\s*',  # Capture request details
        r'\s*(?P<status_code>\S+)',  # Capture status code
        r'\s*(?P<file_size>\d+)'  # Capture file size
    )
    
    # Dictionary to store extracted status code and file size
    info = {
        'status_code': 0,
        'file_size': 0,
    }

    # Construct the log format regex by combining all patterns
    log_format = '{}\\-{}{}{}{}\\s*'.format(*patterns)
    
    # Try to match the input line to the log format
    match = re.fullmatch(log_format, input_line)
    if match:
        # Extract status code and file size if matched
        info['status_code'] = match.group('status_code')
        info['file_size'] = int(match.group('file_size'))
    
    return info


def print_statistics(total_file_size, status_codes_stats):
    '''Output the total file size and the number of occurrences of each status code.'''
    print(f'File size: {total_file_size}', flush=True)
    
    # Print each status code with its occurrence count
    for code, count in sorted(status_codes_stats.items()):
        if count > 0:
            print(f'{code}: {count}', flush=True)


def update_metrics(line, total_file_size, status_codes_stats):
    '''Update the metrics using data from the log line.

    Args:
        line (str): A single line of log data.

    Returns:
        int: The updated total file size.
    '''
    # Extract the necessary log info from the line
    line_info = extract_input(line)
    status_code = line_info.get('status_code', '0')
    
    # Update the status code count if it exists in the dictionary
    if status_code in status_codes_stats:
        status_codes_stats[status_code] += 1
    
    # Return the new total file size
    return total_file_size + line_info['file_size']


def run():
    '''Main function to process log input and output statistics.'''
    line_count = 0
    total_file_size = 0
    # Initialize status code count tracking
    status_codes_stats = {code: 0 for code in ['200', '301', '400', '401', '403', '404', '405', '500']}

    try:
        while True:
            line = input()  # Read each line of input
            total_file_size = update_metrics(line, total_file_size, status_codes_stats)
            line_count += 1
            
            # Every 10 lines, print the current statistics
            if line_count % 10 == 0:
                print_statistics(total_file_size, status_codes_stats)
    
    except (KeyboardInterrupt, EOFError):
        # Print final statistics when the script is interrupted or ends
        print_statistics(total_file_size, status_codes_stats)


if __name__ == '__main__':
    run()

