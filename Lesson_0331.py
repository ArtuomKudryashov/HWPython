log_file = "all.log"
warning_logfile = "warnings.log"

warnings = []
with open(log_file, "r") as file:
    for line in file.readlines():
        if "WARNING" in line:
            with open(warning_logfile, "a") as warnings_file:
                    warnings_file.write(line)
