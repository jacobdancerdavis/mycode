import psutil
import time
import socket

def get_cpu_usage():
    cpu_percent = psutil.cpu_percent()
    return cpu_percent

def get_memory_usage():
    memory_info = psutil.virtual_memory()
    return memory_info.percent

def get_disk_usage():
    disk_info = psutil.disk_usage('/')
    return disk_info.percent

def monitor_cpu(log_file=None, max_tests=5):
    print("CPU Usage (%):")
    test_count = 0
    try:
        while test_count < max_tests:
            cpu_percent = get_cpu_usage()
            print(f"CPU Usage: {cpu_percent}%")

            # Check usage thresholds and display messages
            if cpu_percent < 50:
                print("Usage good")
            elif 50 <= cpu_percent < 70:
                print("Usage moderate")
            elif 70 <= cpu_percent < 85:
                print("Usage high")
            else:
                print("Usage dangerously high. Expand or clean this item.")
            
            if log_file:
                log_file.write(f"CPU Usage: {cpu_percent}%\n")
                log_file.write(f"Usage Message: {get_usage_message(cpu_percent)}\n")

            test_count += 1
            if test_count < max_tests:
                time.sleep(1)
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")

def monitor_memory(log_file=None, max_tests=5):
    print("Memory Usage:")
    test_count = 0
    try:
        while test_count < max_tests:
            memory_percent = get_memory_usage()
            print(f"Memory Usage (%): {memory_percent}")

            # Check usage thresholds and display messages
            if memory_percent < 50:
                print("Usage good")
            elif 50 <= memory_percent < 70:
                print("Usage moderate")
            elif 70 <= memory_percent < 85:
                print("Usage high")
            else:
                print("Usage dangerously high. Expand or clean this item.")
            
            if log_file:
                log_file.write(f"Memory Usage (%): {memory_percent}\n")
                log_file.write(f"Usage Message: {get_usage_message(memory_percent)}\n")

            test_count += 1
            if test_count < max_tests:
                time.sleep(1)
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")

def monitor_disk(log_file=None, max_tests=5):
    print("Disk Usage:")
    test_count = 0
    try:
        while test_count < max_tests:
            disk_percent = get_disk_usage()
            print(f"Disk Usage (%): {disk_percent}")

            # Check usage thresholds and display messages
            if disk_percent < 50:
                print("Usage good")
            elif 50 <= disk_percent < 70:
                print("Usage moderate")
            elif 70 <= disk_percent < 85:
                print("Usage high")
            else:
                print("Usage dangerously high. Expand or clean this item.")
            
            if log_file:
                log_file.write(f"Disk Usage (%): {disk_percent}%\n")
                log_file.write(f"Usage Message: {get_usage_message(disk_percent)}\n")

            test_count += 1
            if test_count < max_tests:
                time.sleep(1)
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")

def get_usage_message(percentage):
    if percentage < 50:
        return "Usage good"
    elif 50 <= percentage < 70:
        return "Usage moderate"
    elif 70 <= percentage < 85:
        return "Usage high"
    else:
        return "Usage dangerously high. Expand or clean this item."

def monitor_open_ports(log_file=None, max_tests=5):
    print("Open Ports:")
    test_count = 0
    try:
        while test_count < max_tests:
            open_ports = []
            for port in range(1, 65536):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                result = sock.connect_ex(('localhost', port))
                if result == 0:
                    open_ports.append(port)
                sock.close()
            
            if open_ports:
                print(f"Open Ports: {', '.join(map(str, open_ports))}")
                if log_file:
                    log_file.write(f"Open Ports: {', '.join(map(str, open_ports))}\n")
            else:
                print("No active ports")
                if log_file:
                    log_file.write("No active ports\n")
            
            test_count += 1
            if test_count < max_tests:
                time.sleep(5)
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")

def monitor_processes(log_file=None, max_tests=5):
    print("Active Background Processes:")
    test_count = 0
    try:
        while test_count < max_tests:
            processes = []

            for process in psutil.process_iter(attrs=['pid', 'name', 'cpu_percent', 'memory_percent']):
                processes.append(process.info)
            
            processes = sorted(processes, key=lambda x: x['cpu_percent'], reverse=True)

            for process in processes:
                print(f"Process: {process['name']} (PID: {process['pid']})")
                print(f"   CPU Usage: {process['cpu_percent']:.2f}%")
                print(f"   Memory Usage: {process['memory_percent']:.2f}%")
                if log_file:
                    log_file.write(f"Process: {process['name']} (PID: {process['pid']})\n")
                    log_file.write(f"   CPU Usage: {process['cpu_percent']:.2f}%\n")
                    log_file.write(f"   Memory Usage: {process['memory_percent']:.2f}%\n")
            
            test_count += 1
            if test_count < max_tests:
                time.sleep(5)
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")

def main():
    port_test_count = 0  # Initialize port test count
    process_test_count = 0  # Initialize process test count

    while True:
        print("\nSelect Performance Metric to Monitor:")
        print("1. CPU Usage")
        print("2. Memory Usage")
        print("3. Disk Usage")
        print("4. Open Ports")
        print("5. Active Background Processes")
        print("6. Exit")

        choice = input("Enter your choice (1/2/3/4/5/6): ")
        
        if choice == '6':
            print("Exiting the program.")
            break  # Exit the loop and end the program
        elif choice in ['1', '2', '3', '4', '5']:
            log_choice = input("Do you want to log results to a file? (y/n): ").lower()
            log_file = None

            if log_choice == 'y':
                log_filename = input("Enter the log file name: ")
                log_file = open(log_filename, "w")

            max_tests = 5  # Maximum number of tests for CPU, Memory, and Disk

            if choice == '4' and port_test_count >= 2:
                print("Port test has already run twice. Skipping.")
                continue  # Skip if port test has already run twice

            if choice == '5' and process_test_count >= 1:
                print("Process test has already run once. Skipping.")
                continue  # Skip if process test has already run once

            try:
                if choice == '1':
                    monitor_cpu(log_file, max_tests)
                elif choice == '2':
                    monitor_memory(log_file, max_tests)
                elif choice == '3':
                    monitor_disk(log_file, max_tests)
                elif choice == '4':
                    monitor_open_ports(log_file, 2)  # Run port test only twice
                    port_test_count += 2
                elif choice == '5':
                    monitor_processes(log_file, 1)  # Run process test only once
                    process_test_count += 1
            finally:
                if log_file:
                    log_file.close()
        else:
            print("Invalid choice. Please select 1, 2, 3, 4, 5, or 6.")

if __name__ == "__main__":
    main()
