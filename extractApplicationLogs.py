import os
import re

def parse_log_statements(file_path):
    with open(file_path, "r") as f:
        file_content = f.read()
        log_statements = re.findall(r"\.(info|warn|error)\((.*)\);", file_content)
        log_statements = [(file_path, line_number + 1, log_level, log_message) for line_number, log_statement in enumerate(log_statements) for log_level, log_message in [log_statement]]
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
            f.write(f"<tr><td>{class_name}</td><td>{line_number}</td><td>{log_level}</td><td>{log_message}</td></tr>")
        f.write("</table></body></html>")

if __name__ == "__main__":
    project_folder = "<INPUT_HERE_YOUR_SOURCE_CODE_FOLDER_PATH>"
    report_file = "report.html"
    create_report(project_folder, report_file)
