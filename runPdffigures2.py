import os
import subprocess

def pdffigure2(input_path, output_path):
    """
    Python client for pdffigure2
    """
    input_path = os.path.expanduser(input_path)
    output_path = os.path.expanduser(output_path)
    if not os.path.isdir(output_path):
        os.mkdir(output_path)
    command = ' '.join(['runMain', 'org.allenai.pdffigures2.FigureExtractorBatchCli', input_path, '-m', output_path, '-d', output_path])
    sbt_command = ' '.join(['sbt', '"' + command + '"'])
    output, error = subprocess.Popen([sbt_command],
                                      shell=True, universal_newlines=True).communicate()
    print('finish extracting %s to %s' % (input_path, output_path))

pdffigure2("/Users/cheng-shanhsieh/Downloads/testpdf", '~/Desktop/output/')