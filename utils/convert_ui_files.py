import os
import glob

def convert(in_dir=''):
    #os.popen('rm -rf *.pyc')
    if in_dir == '':
        in_dir = os.path.dirname(os.path.realpath(__file__))

    print 'search in: ', in_dir
    uiFiles =  glob.glob('{0}/*.ui'.format(in_dir))
    for uiFile in uiFiles:
        print 'ui file to convert', os.path.basename(uiFile)
        uiFilewOPath = os.path.basename(uiFile)
        nameWOext =  os.path.splitext(os.path.basename(uiFile))
        pyFile = '{0}.py'.format(nameWOext[0])
        try:
            os.popen('pyside-uic -o "{0}" "{1}"'.format(os.path.join(in_dir,pyFile),uiFile))
            print 'created py File', pyFile
        except:
            print "Failed"


if __name__ == "__main__":
    convert()