log_file = open("server_log.txt", "r")
lines = log_file.readlines()
error_lines = []
for line in lines:
    if "ERROR" in line:
        error_lines.append(line)
    error_file = open("errors_only.txt", "w")
    error_file.writelines(error_lines)
    error_file.close()
print("Number of errors found:", len(error_lines))
