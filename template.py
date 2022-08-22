import os


dirs = [ os.path.join('data','raw'),
os.path.join('data','processed'),
'notebooks',
'saved_models','src','data_given']

for i in dirs:
    os.makedirs(i, exist_ok=True)
    with open(os.path.join(i,".gitkeep"),'w') as f:
        pass

file_ = [
    'dvc.yaml', 'params.yaml', '.gitignore', os.path.join('src', '__init__.py')]

for ii in file_:
    with open(ii,'w') as f:

        pass
