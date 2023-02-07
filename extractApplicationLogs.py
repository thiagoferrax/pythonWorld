import os
import re

def parse_log_statements(file_path):
    log_statements = []
    with open(file_path, "r") as f:
        for line_number, line in enumerate(f):
            match = re.search(r"\.(info|warn|error)\((.*)\);", line)
            if match:
                log_level, log_message = match.groups()
                log_statements.append((file_path, line_number + 1, log_level, log_message))
    return log_statements

def create_report(project_folder, report_file):
    log_statements = []
    for root, dirs, files in os.walk(project_folder):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            if file_path.endswith(".java"):
                log_statements.extend(parse_log_statements(file_path))
    
    with open(report_file, "w") as f:
        f.write("<html><head><title>Log Statement Report</title></head><body>")
        f.write("<h1>Log Statement Report</h1>")
        f.write("<table border='1'><tr><th>Class</th><th>Line</th><th>Level</th><th>Message</th></tr>")
        for class_name, line_number, log_level, log_message in log_statements:
            class_name = os.path.splitext(os.path.basename(class_name))[0]
            f.write(f"<tr><td>{class_name}</td><td>{line_number}</td><td>{log_level}</td><td>{log_message}</td></tr>")
        f.write("</table></body></html>")

if __name__ == "__main__":
    project_folder = "<your project folder here>"
    report_file = "report.html"
    create_report(project_folder, report_file)
