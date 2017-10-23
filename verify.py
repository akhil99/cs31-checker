import os
import sys
import yaml
from subprocess import call
import os.path as path
import shutil


def checkFiles(folder, files):
    noErrors = True
    # Get a list of extra or missing files
    missingFiles = []
    extraFiles = os.listdir(folder)
    for file in files:
        try:
            extraFiles.remove(file)
        except ValueError:
            missingFiles.append(file)


    print('\nFile Check | Checking Directory ' + folder)

    if len(missingFiles) > 0:
        print('File Check |X| Missing files: ' + ', '.join(missingFiles))
        noErrors = False
    else:
        print('File Check | No Missing files!')

    if len(extraFiles) > 0:
        print('File Check |X| ERR: Extra files present: ' + ', '.join(extraFiles))
        noErrors = False
    else:
        print('File Check | No Extraneous files present!')

    return noErrors

def compileFile(infile, outfile, compiler):
    result = call([compiler, infile, '-o', outfile])
    return (result == 0)

def compileAll(indir, outdir, compileList):
    noError = True;
    if not os.path.isdir(outdir):
        call(['mkdir', outdir])
    for d in compileList:
        name = path.splitext(d)[0]
        result = compileFile(path.join(indir, d), path.join(outdir, name), compiler)
        if result:
            print("Compiling | " + d + " succeeded!")
        else:
            print("Compiling | " + d + " failed!")
            noError = False;
    return noError;

def testOutput(dataMap, testDir, tempFileName):
    for test in dataMap['tests']:
        templateText = dataMap['template']
        testFile = testDir + '/' + test['file']

        for index, result in enumerate(test['out']):
            templateID = '~' + str(index)
            templateText = templateText.replace(templateID, result)

        file = open(tempFileName, 'w')
        file.write(templateText)
        file.close()

        print('Runtime Test | Testing input: ' + test['in'])
        call(['./testfile.sh', 'tempfile', testFile, test['in']])

    call(['rm', tempFileName])

# Check to ensure we have 1 argument
if len(sys.argv) < 2:
    print('missing arguments!')
    sys.exit()

dataMap = {}
# Read YAML file for data
with open(sys.argv[1]) as f:
    dataMap = yaml.safe_load(f)

directory = dataMap['dir']
fileList = dataMap['files']
compileList = dataMap['compile']
compiler = dataMap['compiler']

if not checkFiles(directory, fileList):
    sys.exit(1)
if not compileAll(directory, 'bin', compileList):
    sys.exit(1)

testOutput(dataMap, 'bin', 'tempfile')

if len(sys.argv) >= 3:
    zipName = sys.argv[2]
    shutil.make_archive(zipName, 'zip', directory)
