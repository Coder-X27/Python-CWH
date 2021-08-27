import os
def detector(file):
    with open(file,'r') as f:
        filecontent=f.read()
    if 'binod' in filecontent.lower():
        print(f"Binod is here in file {file}")

if __name__ == '__main__':
    for i in os.listdir():
        if i.endswith('py'):
            detector(i)