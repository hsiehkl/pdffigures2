# Step1: Download PDFFigures 2.0
Download the whole project from GitHub repository directly. https://github.com/allenai/pdffigures2

# Step2: Download sbt for running Scala
Download it form the official website. https://www.scala-sbt.org/download.html

# Step3: Run PDFFigures 2.0 with python
Add a python file in the folder. Use following code to give sbt command, assign input path (where your pdfs are) and output path(where you want to store the result).

`import os
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

pdffigure2("/your folder path", '/output path')`

# Step4: Edit Java code (if applicable)
If you get the error, "value EXIT_ON_CLOSE is not a member of object javax.swing.JFrame", when running the code above, then go to VisualLogger.scala file and change `frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)` to `frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE)`. Run the code again, it should solve the problem. See more on: https://github.com/scala/bug/issues/10596