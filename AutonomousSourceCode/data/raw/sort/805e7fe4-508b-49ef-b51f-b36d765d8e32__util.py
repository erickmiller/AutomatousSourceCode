from tempfile import NamedTemporaryFile
import subprocess

def report_diff(correct_report_path, test_report_path):
    #Sort the correct report
    sorted_correct = NamedTemporaryFile()
    presort_correct = open(correct_report_path)
    for line in sorted(presort_correct):
        sorted_correct.file.write(line)
    sorted_correct.file.flush()
    
    #Sort the test report
    sorted_test = NamedTemporaryFile()
    presort_test = open(test_report_path)
    for line in sorted(presort_test):
        sorted_test.file.write(line)
    sorted_test.file.flush()
    
    result = subprocess.Popen(["diff", "-b", sorted_correct.name, sorted_test.name],
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    result.wait()
    return "".join(result.stdout)